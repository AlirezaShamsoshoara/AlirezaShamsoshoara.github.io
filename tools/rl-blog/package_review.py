#!/usr/bin/env python3
"""Package a standalone preview as one self-contained, unpublished review HTML."""
import argparse
import base64
import html
from html.parser import HTMLParser
import json
import mimetypes
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

import sass

from article_source import outside_checkout, repository_root


TAG = re.compile(r'<[a-zA-Z][^>]*>')
SCRIPT = re.compile(r'<script\b[^>]*>.*?</script\s*>', re.I | re.S)
IMPORT = re.compile(r'''^[ \t]*import\s+(?:(?P<bindings>.*?)\s+from\s+)?['"](?P<source>[^'"]+)['"]\s*;?''', re.M | re.S)
REEXPORT = re.compile(r'''^[ \t]*export\s+(?P<names>\{[^}]*\}|\*(?:\s+as\s+\w+)?)\s+from\s+['"](?P<source>[^'"]+)['"]\s*;?''', re.M)
EXPORT_LIST = re.compile(r'^[ \t]*export\s*\{([^}]*)\}\s*;?', re.M)
EXPORT_DECL = re.compile(r'^[ \t]*export\s+(?P<kind>const|let|var|(?:async\s+)?function\s*\*?|class)\s+(?P<name>[\w$]+)', re.M)
CSS_URL = re.compile(r'''url\(\s*(['"]?)(.*?)\1\s*\)''', re.I)
CSS_IMPORT = re.compile(r'''@import\s+(?:url\(\s*(['"]?)(.*?)\1\s*\)|(['"])(.*?)\3)\s*([^;]*);''', re.I)
ASSET_LITERAL = re.compile(r'''(['"])(/[^'"\s<>]*assets/[^'"\s<>]+)\1''')


class TagReader(HTMLParser):
    def handle_starttag(self, tag, attrs):
        self.tag, self.attrs = tag, dict(attrs)
    handle_startendtag = handle_starttag


def read_tag(source):
    reader = TagReader(convert_charrefs=True)
    reader.feed(source)
    return reader.tag, reader.attrs


def write_tag(tag, attrs, closed=False):
    values = ''.join(' ' + key + ('' if value is None else '="' + html.escape(value, quote=True) + '"') for key, value in attrs.items())
    return '<' + tag + values + ('/>' if closed else '>')


def aliases(source):
    result = []
    for item in source.strip().strip('{}').split(','):
        item = item.strip()
        if not item:
            continue
        parts = re.split(r'\s+as\s+', item)
        if len(parts) > 2 or any(not re.fullmatch(r'[\w$]+', part) for part in parts):
            raise ValueError('Unsupported module binding: ' + item)
        result.append((parts[0], parts[-1]))
    return result


def module_variables(source):
    """Track module-scope variable declarations through later export aliases."""
    literals = re.compile(r'''//[^\n]*|/\*.*?\*/|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|`(?:\\.|[^`\\])*`''', re.S)
    def mask(match):
        text = match.group()
        if text.startswith(('//', '/*')):
            return ''.join('\n' if char == '\n' else ' ' for char in text)
        # Keep a literal token, but hide its internal commas, braces and newlines.
        return '0' + ' ' * (len(text) - 1)
    code = literals.sub(mask, source)
    levels, depth = [], [0, 0, 0]
    for char in code:
        levels.append(tuple(depth))
        if char in '{([':
            depth['{(['.index(char)] += 1
        elif char in '})]':
            depth['})]'.index(char)] -= 1
    variables = {}
    for match in re.finditer(r'\b(?P<export>export\s+)?(?P<kind>const|let|var)\s+', code):
        if levels[match.start()] != (0, 0, 0):
            continue
        start = match.end()
        parts = []
        for position in range(start, len(code)):
            if levels[position] == (0, 0, 0) and code[position] in ',;\n':
                part = code[start:position]
                if code[position] == '\n':
                    before, after = part.rstrip(), code[position + 1:].lstrip()
                    continuation = ',=.+-*/%?:|&^<>'
                    if not before.strip() or before[-1:] in continuation or (after and after[0] in continuation + '(['):
                        continue
                parts.append(part); start = position + 1
                if code[position] != ',':
                    break
        else:
            parts.append(code[start:])
        for part in parts:
            pattern = part.split('=', 1)[0].strip()
            if re.fullmatch(r'[A-Za-z_$][\w$]*', pattern):
                names = [pattern]
            elif pattern.startswith(('{', '[')):
                if match.group('export'):
                    raise ValueError('Destructured export declarations need a served site')
                # A conservative superset includes bindings in destructuring patterns.
                names = re.findall(r'[A-Za-z_$][\w$]*', pattern)
            else:
                continue
            for name in names:
                if name not in variables or not pattern.startswith(('{', '[')):
                    variables[name] = (match.group('kind'), bool(match.group('export')))
    declarations = re.compile(r'^[ \t]*(?:export\s+(?:default\s+)?)?(?P<kind>(?:async\s+)?function\b\s*\*?|class\b)\s*(?P<name>[A-Za-z_$][\w$]*)', re.M)
    for match in declarations.finditer(code):
        if levels[match.start()] == (0, 0, 0):
            variables.setdefault(match.group('name'), (match.group('kind'), False))
    return variables


class Packager:
    def __init__(self, preview):
        self.preview = preview.resolve()
        provenance = self.preview / 'review-provenance.json'
        self.provenance = json.loads(provenance.read_text()) if provenance.is_file() else {}
        self.base = str(self.provenance.get('baseurl') or '').rstrip('/')
        self.modules = {}
        self.active = set()
        self.module_code = []
        self.uris = {}

    def resolve(self, reference, parent=None):
        parsed = urlsplit(html.unescape(reference))
        if parsed.scheme or parsed.netloc:
            raise ValueError('A self-contained review cannot load an external asset: ' + reference)
        path = unquote(parsed.path)
        if not path:
            raise ValueError('Empty local asset reference')
        if path.startswith('/'):
            if self.base and path.startswith(self.base + '/'):
                path = path[len(self.base):]
            result = self.preview / path.lstrip('/')
        else:
            result = (parent or self.preview / 'index.html').parent / path
        result = result.resolve()
        result.relative_to(self.preview)
        if not result.is_file():
            raise FileNotFoundError(reference)
        return result

    def uri(self, reference, parent=None):
        if reference.startswith(('data:', '#')):
            return reference
        path = self.resolve(reference, parent)
        if path not in self.uris:
            mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
            self.uris[path] = 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode('ascii')
        fragment = urlsplit(reference).fragment
        return self.uris[path] + ('#' + fragment if fragment else '')

    def css(self, reference, chain=()):
        path = self.resolve(reference, chain[-1] if chain else None)
        if path in chain:
            raise ValueError('Cyclic CSS import')
        source = path.read_text(encoding='utf-8')
        def import_css(match):
            child = match.group(2) or match.group(4)
            nested = self.css(child, (*chain, path))
            condition = match.group(5).strip()
            return '@media ' + condition + '{' + nested + '}' if condition else nested
        source = CSS_IMPORT.sub(import_css, source)
        source = CSS_URL.sub(lambda match: 'url("' + self.uri(match.group(2), path) + '")', source)
        if re.search(r'@import\b', source):
            raise ValueError('Unresolved CSS import')
        return sass.compile(string=source, output_style='compressed')

    def module(self, path, inline_source=None):
        if path in self.modules:
            return self.modules[path]
        if path in self.active:
            raise ValueError('Cyclic ES module imports are not supported in a review bundle')
        self.active.add(path)
        source = path.read_text(encoding='utf-8') if inline_source is None else inline_source
        syntax = subprocess.run(['node', '--input-type=module', '--check'], input=source, text=True, capture_output=True)
        if syntax.returncode:
            raise ValueError('Original module syntax failed: ' + syntax.stderr)
        if re.search(r'\bimport\s*(?:\(|\.)', source):
            raise ValueError('Dynamic import and import.meta need a served site, not a review bundle')
        variables = module_variables(source)
        exports = {name: name for name, (_kind, direct) in variables.items() if direct}
        mutable = {name for name, (kind, direct) in variables.items() if direct and kind in ('let', 'var')}
        bindings = []
        def dependency(reference):
            if not reference.startswith(('.', '/')):
                raise ValueError('Only static local module imports can be bundled: ' + reference)
            return self.module(self.resolve(reference, path))
        def import_module(match):
            module_id, names, changing = dependency(match.group('source'))
            requested = (match.group('bindings') or '').strip()
            target = '__rl_modules[' + json.dumps(module_id) + ']'
            if not requested:
                return ''
            if requested.startswith('{'):
                pairs = aliases(requested)
                for original, local in pairs:
                    if original not in names:
                        raise ValueError('Unknown imported name: ' + original)
                    if original in changing:
                        raise ValueError('Live mutable imports need a served site: ' + original)
                    bindings.append('const ' + local + ' = ' + target + '[' + json.dumps(original) + '];')
                    variables[local] = ('import', False)
            elif requested.startswith('*'):
                match_namespace = re.fullmatch(r'\*\s+as\s+([\w$]+)', requested)
                if not match_namespace:
                    raise ValueError('Invalid namespace import')
                bindings.append('const ' + match_namespace.group(1) + ' = ' + target + ';')
                variables[match_namespace.group(1)] = ('import', False)
            else:
                first, separator, rest = requested.partition(',')
                if not re.fullmatch(r'[\w$]+', first.strip()) or 'default' not in names:
                    raise ValueError('Invalid default import')
                if 'default' in changing:
                    raise ValueError('Live mutable imports need a served site: default')
                bindings.append('const ' + first.strip() + ' = ' + target + '.default;')
                variables[first.strip()] = ('import', False)
                if separator:
                    synthetic = type('Binding', (), {'group': lambda _self, key: rest.strip() if key == 'bindings' else match.group('source')})()
                    import_module(synthetic)
            return ''
        source = IMPORT.sub(import_module, source)
        def reexport(match):
            module_id, names, changing = dependency(match.group('source'))
            target = '__rl_modules[' + json.dumps(module_id) + ']'
            requested = match.group('names')
            if requested.startswith('* as '):
                exports[requested.split()[-1]] = target
            elif requested == '*':
                exports.update({name: target + '[' + json.dumps(name) + ']' for name in names if name != 'default'})
                mutable.update(changing)
            else:
                for original, exported in aliases(requested):
                    if original not in names:
                        raise ValueError('Unknown re-exported name: ' + original)
                    exports[exported] = target + '[' + json.dumps(original) + ']'
                    if original in changing:
                        mutable.add(exported)
            return ''
        source = REEXPORT.sub(reexport, source)
        def export_list(match):
            for original, exported in aliases(match.group(1)):
                if original not in variables:
                    raise ValueError('Unclassified export alias needs a served site: ' + original)
                exports[exported] = original
                if variables[original][0] in ('let', 'var'):
                    mutable.add(exported)
            return ''
        source = EXPORT_LIST.sub(export_list, source)
        def export_declaration(match):
            kind, name = match.group('kind'), match.group('name')
            exports[name] = name
            if kind in ('let', 'var'):
                mutable.add(name)
            return kind + ' ' + name
        source = EXPORT_DECL.sub(export_declaration, source)
        default_declaration = re.search(r'^[ \t]*export\s+default\s+((?:async\s+)?function\b\s*\*?|class\b)\s*([A-Za-z_$][\w$]*)', source, re.M)
        if default_declaration and default_declaration.group(2) != 'extends':
            # A named default declaration also creates a binding for its own module.
            source = source[:default_declaration.start()] + default_declaration.group(1) + ' ' + default_declaration.group(2) + source[default_declaration.end():]
            exports['default'] = default_declaration.group(2)
        elif re.search(r'^[ \t]*export\s+default\b', source, re.M):
            source = re.sub(r'^[ \t]*export\s+default\s+', 'const __rl_default_export = ', source, count=1, flags=re.M)
            exports['default'] = '__rl_default_export'
        if re.search(r'^[ \t]*(?:import|export)\b', source, re.M):
            raise ValueError('Unresolved ES module syntax')
        module_id = 'm' + str(len(self.module_code))
        getters = ','.join(json.dumps(name) + ':{enumerable:true,get:()=>(' + value + ')}' for name, value in exports.items())
        code = '__rl_modules[' + json.dumps(module_id) + '] = (() => {\n' + '\n'.join(bindings) + '\n' + source + '\nreturn Object.defineProperties({}, {' + getters + '});\n})();'
        self.module_code.append(code)
        result = module_id, set(exports), mutable
        self.modules[path] = result
        self.active.remove(path)
        return result

    def inline_tags(self, document):
        def replace(match):
            original = match.group(0)
            tag, attrs = read_tag(original)
            changed = False
            for key, value in list(attrs.items()):
                if not value:
                    continue
                is_asset = urlsplit(value).path.lstrip('/').startswith('assets/') or '/assets/' in value
                is_media = tag in ('img', 'source', 'video', 'audio', 'track', 'image', 'input') and key in ('src', 'poster', 'href', 'xlink:href')
                if key == 'srcset' and tag in ('img', 'source'):
                    choices = []
                    if value.startswith('data:'):
                        continue
                    for item in value.split(','):
                        parts = item.strip().split()
                        if not parts:
                            raise ValueError('Empty srcset candidate')
                        choices.append(' '.join([self.uri(parts[0]), *parts[1:]]))
                    attrs[key] = ', '.join(choices); changed = True
                elif (key in ('href', 'src', 'poster', 'xlink:href') or key.startswith('data-')) and (is_asset or is_media):
                    attrs[key] = self.uri(value); changed = True
                    if tag == 'a' and key == 'href' and 'download' not in attrs:
                        attrs['download'] = Path(urlsplit(value).path).name
                elif tag == 'a' and key == 'href' and value.startswith('/') and not value.startswith('//') and self.provenance.get('site_url'):
                    attrs[key] = self.provenance['site_url'] + value; changed = True
                elif key == 'style' and 'url(' in value:
                    attrs[key] = CSS_URL.sub(lambda item: 'url("' + self.uri(item.group(2)) + '")', value); changed = True
            return write_tag(tag, attrs, original.endswith('/>')) if changed else original
        return TAG.sub(replace, document)

    def document(self):
        document = (self.preview / 'index.html').read_text(encoding='utf-8')
        def stylesheet(match):
            original = match.group(0)
            tag, attrs = read_tag(original)
            if tag == 'link' and 'stylesheet' in (attrs.get('rel') or '').split():
                if not attrs.get('href'):
                    raise ValueError('Stylesheet has no href')
                media = attrs.get('media')
                css = self.css(attrs['href'])
                return '<style' + (' media="' + html.escape(media, quote=True) + '"' if media else '') + '>' + css + '</style>'
            return original
        document = TAG.sub(stylesheet, document)
        marker = '<!-- rl-review-modules -->'
        inserted = False
        def script(match):
            nonlocal inserted
            original = match.group(0)
            tag, attrs = read_tag(original.split('>', 1)[0] + '>')
            source = original.split('>', 1)[1].rsplit('</', 1)[0]
            if attrs.get('type') == 'module':
                path = self.resolve(attrs['src']) if attrs.get('src') else self.preview / ('inline-' + str(len(self.module_code)) + '.mjs')
                self.module(path, None if attrs.get('src') else source)
                if not inserted:
                    inserted = True
                    return marker
                return ''
            if attrs.get('src'):
                source = self.resolve(attrs['src']).read_text(encoding='utf-8')
                attrs.pop('src')
                return write_tag(tag, attrs) + source.replace('</script', '<\\/script') + '</script>'
            return original
        document = SCRIPT.sub(script, document)
        if inserted:
            code = 'const __rl_modules = Object.create(null);\n' + '\n'.join(self.module_code)
            syntax = subprocess.run(['node', '--input-type=module', '--check'], input=code, text=True, capture_output=True)
            if syntax.returncode:
                raise ValueError('Bundled module syntax failed: ' + syntax.stderr)
            document = document.replace(marker, '<script type="module">\n' + code.replace('</script', '<\\/script') + '\n</script>')
        document = self.inline_tags(document)
        document = ASSET_LITERAL.sub(lambda match: match.group(1) + self.uri(match.group(2)) + match.group(1), document)
        if re.search(r'(?<![\w:./-])/(?:[^\s/]+/)*assets/', document):
            raise ValueError('Some local assets remain unresolved')
        if re.search(r'url\(\s*[\'"]?(?!data:|#)[^\s)\'"]', document, re.I):
            raise ValueError('Some CSS media remain unresolved')
        return document


def package(preview: Path, out: Path, root: Path | None = None):
    preview = preview.resolve()
    out = outside_checkout(root or repository_root(), out)
    if out == preview or preview in out.parents:
        raise ValueError('Package output must be outside the preview directory')
    packager = Packager(preview)
    document = packager.document()
    size = len(document.encode('utf-8'))
    if size >= 50 * 1024 * 1024:
        raise ValueError('The self-contained review exceeds the 50 MiB limit')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(document, encoding='utf-8')
    print(out, size)
    return {'bytes': size, 'modules': len(packager.module_code), 'local_media': len(packager.uris)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=repository_root())
    parser.add_argument('--preview', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    package(args.preview, args.out, args.root)


if __name__ == '__main__':
    main()
