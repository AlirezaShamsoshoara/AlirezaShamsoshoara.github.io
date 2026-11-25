#!/usr/bin/env python3
"""Check syntax and static highlighting of code excerpts in any RL article."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import textwrap

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
import yaml

from article_source import expand_includes, load_post, repository_root


FENCES = re.compile(r'^(?P<fence>`{3,}|~{3,})(?P<language>[^\n]*)\n(?P<source>.*?)^(?P=fence)[ \t]*$', re.M | re.S)


def check(root: Path, post: Path):
    root = root.resolve()
    post, _page, body = load_post(root, post)
    body, _includes = expand_includes(root, body)
    results = []
    for match in FENCES.finditer(body):
        language = match.group('language').strip().split()[0] if match.group('language').strip() else 'text'
        source = match.group('source')
        syntax = 'not applicable'
        if language in ('python', 'py'):
            wrapped = 'def __article_excerpt__():\n' + textwrap.indent(source or 'pass\n', '    ')
            compile(wrapped, '<article excerpt>', 'exec')
            syntax = 'passed as a function body'
        elif language in ('bash', 'sh', 'shell'):
            subprocess.run(['bash', '-n'], input=source, text=True, check=True, capture_output=True)
            syntax = 'passed without executing commands'
        elif language in ('yaml', 'yml'):
            yaml.safe_load(source)
            syntax = 'passed'
        elif language in ('javascript', 'js'):
            subprocess.run(['node', '--input-type=module', '--check'], input=source, text=True, check=True, capture_output=True)
            syntax = 'passed without executing code'
        lexer = get_lexer_by_name(language)
        rendered = highlight(source, lexer, HtmlFormatter())
        if language not in ('text', 'plaintext', 'console') and source.strip() and '<span class=' not in rendered:
            raise ValueError('Expected highlighted tokens for ' + language)
        results.append({'language': language, 'lines': len(source.splitlines()), 'syntax': syntax, 'highlighting': 'passed'})
    report = {
        'post': str(post.relative_to(root)), 'code_blocks': len(results),
        'syntax_checks': sum(row['syntax'] != 'not applicable' for row in results),
        'highlighting_checks': len(results), 'snippet_checks': results,
        'note': 'Syntax and highlighting only. Excerpts are not executed or claimed to be standalone programs.',
    }
    print(json.dumps(report, indent=2))
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=repository_root())
    parser.add_argument('--post', type=Path, required=True)
    args = parser.parse_args(argv)
    check(args.root, args.post)


if __name__ == '__main__':
    main()
