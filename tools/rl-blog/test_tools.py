"""Regression tests for parameterized article tools, using only scratch fixtures."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import re
import subprocess
import tempfile
import unittest

import yaml

from article_source import expand_includes, render_liquid, split_front_matter
from build_review_preview import build
from check_article_code import check as check_code
from check_post import check as check_post
from package_review import package


class ArticleToolsTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix='rl-blog-tools-')
        self.addCleanup(self.scratch.cleanup)
        self.base = Path(self.scratch.name)
        self.root = self.base / 'source'
        self.preview = self.base / 'preview'
        self.output = self.base / 'review.html'
        repository = Path(__file__).resolve().parents[2]
        self.layout = (repository / '_layouts/rl-article.html').read_text()
        self.write('_layouts/rl-article.html', self.layout)
        self.write('_config.yml', yaml.safe_dump({'title': 'Example', 'url': 'https://example.test', 'baseurl': '', 'author': {'name': 'Reader'}}))
        self.write('_data/blog_series.yml', yaml.safe_dump([{'id': 'rl-from-zero', 'url': '/blog/rl-from-zero/', 'subscribe_url': 'https://example.test/subscribe', 'medium_url': 'https://example.test/series'}]))
        self.write('assets/css/main.scss', '---\n---\nbody { margin: 0; }\n')
        (self.root / '_sass').mkdir()
        self.write('assets/css/rl/article.css', (repository / 'assets/css/rl/article.css').read_text())
        self.write('assets/css/rl/example.css', '.example { color: #2356a8; }\n')
        self.write('assets/js/rl/example.mjs', 'export const VALUE = 7;\n')
        self.write('assets/media/rl/example/hero.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420"><rect width="1200" height="420" fill="white"/></svg>')
        self.write('_includes/rl/outer.html', '<section id="example-figure">{% include rl/inner.html %}</section>')
        self.write('_includes/rl/inner.html', '<p id="example-caption">A real include.</p>')
        self.page = {
            'title': 'An example update', 'layout': 'rl-article',
            'permalink': '/blog/rl-from-zero/example/', 'series': 'rl-from-zero', 'series_part': 3,
            'categories': ['interesting-blogs'], 'tags': ['rl-from-zero'],
            'hero_image': '/assets/media/rl/example/hero.svg', 'hero_alt': 'An example diagram',
            'published': False, 'sitemap': False,
            'stylesheets': ['/assets/css/rl/example.css'], 'scripts': ['/assets/js/rl/example.mjs'],
        }
        self.body = 'An example article.\n\n{% include rl/outer.html %}\n\n```python\nreturn value * 2\n```\n\n```bash\nprintf hello\n```\n'
        self.post = Path('_drafts/example.md')
        self.save_post()

    def write(self, path, text):
        path = self.root / path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def save_post(self):
        return self.write(self.post, '---\n' + yaml.safe_dump(self.page, sort_keys=False) + '---\n' + self.body)

    def build_preview(self):
        self.save_post()
        with redirect_stdout(io.StringIO()):
            return build(self.root, self.post, self.preview)

    def check_source(self, state='draft'):
        self.save_post()
        with redirect_stdout(io.StringIO()):
            return check_post(self.root, self.post, state)

    def package_preview(self):
        with redirect_stdout(io.StringIO()):
            return package(self.preview, self.output)

    def test_empty_front_matter_for_theme_sass(self):
        matter, body = split_front_matter('---\n---\nbody {}')
        self.assertEqual(matter, {})
        self.assertEqual(body, 'body {}')

    def test_nested_includes_are_all_inlined(self):
        expanded, sources = expand_includes(self.root, self.body)
        self.assertNotIn('{% include', expanded)
        self.assertIn('example-caption', expanded)
        self.assertEqual(len(sources), 2)

    def test_missing_include_fails(self):
        self.body += '\n{% include rl/missing.html %}'
        with self.assertRaises(FileNotFoundError):
            self.build_preview()

    def test_include_cycle_fails(self):
        self.write('_includes/rl/inner.html', '{% include rl/outer.html %}')
        with self.assertRaises(ValueError):
            self.build_preview()

    def test_include_traversal_fails(self):
        self.body = '{% include rl/../../outside.html %}'
        with self.assertRaises(ValueError):
            self.build_preview()

    def test_minimal_layout_omits_empty_optional_elements(self):
        _, layout = split_front_matter(self.layout)
        rendered = render_liquid(layout, {'title': 'Minimal', 'series_part': 3}, {'author': {}, 'data': {'blog_series': []}}, content='<p>Body</p>')
        for marker in ('rlql-lede', 'rlql-byline', 'rlql-jump-links', 'rlql-title-figure', 'rel="prev"', 'rel="next"', '<script'):
            self.assertNotIn(marker, rendered)
        self.assertIn('Part 3 of RL From Zero', rendered)
        self.assertNotRegex(rendered, r'<(?:p|span|strong|nav)[^>]*>\s*</')
        self.assertNotIn('{{', rendered)
        self.assertNotIn('{%', rendered)

    def test_all_article_fields_render_and_jump_stays_fragment(self):
        self.page.update({'series_label': 'Example part', 'lede': 'A lede & a detail.', 'read_time_text': 'Short read', 'footer_part_label': 'The example part', 'next_teaser': 'Next: another example.', 'jump_links': [{'href': '#example-figure', 'label': 'See the figure'}], 'previous_part': {'url': '/blog/rl-from-zero/earlier/', 'title': 'Earlier'}, 'next_part': {'url': '/blog/rl-from-zero/later/', 'title': 'Later'}})
        self.build_preview()
        rendered = (self.preview / 'index.html').read_text()
        for text in ('Example part', 'A lede &amp; a detail.', 'Short read', 'The example part', 'Next: another example.', 'href="#example-figure"', 'rel="prev"', 'rel="next"'):
            self.assertIn(text, rendered)
        self.assertNotIn('/#example-figure', rendered)
        self.assertNotIn('{{', rendered)
        self.assertNotIn('{%', rendered)

    def test_preview_copies_post_assets_and_uses_its_permalink(self):
        destination = self.build_preview()
        self.assertEqual(destination, self.preview / 'blog/rl-from-zero/example/index.html')
        for path in ('assets/css/rl/article.css', 'assets/css/rl/example.css', 'assets/js/rl/example.mjs', 'assets/media/rl/example/hero.svg'):
            self.assertTrue((self.preview / path).is_file())
        provenance = json.loads((self.preview / 'review-provenance.json').read_text())
        self.assertEqual(provenance['post'], str(self.post))
        self.assertEqual(len(provenance['includes']), 2)

    def test_preview_output_inside_checkout_fails(self):
        with self.assertRaises(ValueError):
            build(self.root, self.post, self.root / 'review')

    def test_permalink_traversal_fails(self):
        self.page['permalink'] = '/../../outside/'
        with self.assertRaises(ValueError):
            self.build_preview()

    def test_draft_state_and_unique_ids_pass(self):
        report = self.check_source()
        self.assertEqual(report['state'], 'draft')
        self.assertEqual(report['unique_ids'], 4)
        self.assertEqual(report['checks_passed'], 9)

    def test_wrong_state_fails(self):
        with self.assertRaises(ValueError):
            self.check_source('published')
        self.page['published'] = True
        with self.assertRaises(ValueError):
            self.check_source()

    def test_published_state_and_filename_date(self):
        repository = Path(__file__).resolve().parents[2]
        reference = next((repository / '_posts').glob('*-q-learning-one-update-at-a-time.md'))
        stamp = reference.name[:10]
        self.post = Path('_posts') / (stamp + '-example.md')
        self.page.pop('published'); self.page.pop('sitemap')
        self.page['date'] = stamp
        self.assertEqual(self.check_source('published')['state'], 'published')
        self.page['date'] = 'invalid'
        with self.assertRaises(ValueError):
            self.check_source('published')

    def test_missing_hero_fails(self):
        self.page['hero_image'] = '/assets/media/rl/example/missing.svg'
        with self.assertRaises(FileNotFoundError):
            self.check_source()

    def test_duplicate_include_ids_fail(self):
        self.body += '\n{% include rl/outer.html %}'
        with self.assertRaises(ValueError):
            self.check_source()

    def test_missing_jump_target_fails(self):
        self.page['jump_links'] = [{'href': '#missing', 'label': 'Missing'}]
        with self.assertRaises(ValueError):
            self.check_source()

    def test_series_and_optional_field_validation(self):
        self.page['series_part'] = 0
        with self.assertRaises(ValueError):
            self.check_source()
        self.page['series_part'] = 3
        self.page['scripts'] = 'not a list'
        with self.assertRaises(ValueError):
            self.check_source()

    def test_source_hygiene_detects_dash_and_local_path(self):
        self.body += '\n' + chr(0x2014)
        with self.assertRaises(ValueError):
            self.check_source()
        self.body = 'A path: ' + '/' + 'tmp/example/file.py'
        with self.assertRaises(ValueError):
            self.check_source()

    def test_code_checks_are_parameterized(self):
        with redirect_stdout(io.StringIO()):
            report = check_code(self.root, self.post)
        self.assertEqual(report['code_blocks'], 2)
        self.assertEqual(report['syntax_checks'], 2)

    def test_invalid_python_excerpt_fails(self):
        self.body = '```python\nreturn (\n```\n'
        self.save_post()
        with self.assertRaises(SyntaxError):
            check_code(self.root, self.post)

    def test_package_inlines_all_css_modules_and_media(self):
        self.build_preview()
        report = self.package_preview()
        document = self.output.read_text()
        self.assertEqual(report['modules'], 1)
        self.assertIn('data:image/svg+xml;base64,', document)
        self.assertNotIn('/assets/', document)
        self.assertNotIn('src=', document.split('<script type="module">')[1].split('</script>')[0])
        self.assertNotIn('<link rel="stylesheet"', document)
        self.assertLess(report['bytes'], 50 * 1024 * 1024)

    def test_module_dependency_order_scope_aliases_and_single_execution(self):
        self.write('assets/js/rl/model.mjs', 'const state = 4;\nexport const VALUE = state;\nexport function double(value) { return value * 2; }\nexport default function bump(value) { return value + VALUE; }\n')
        self.write('assets/js/rl/side.mjs', 'globalThis.sideCount = (globalThis.sideCount || 0) + 1;\n')
        self.write('assets/js/rl/example.mjs', "import bump, {\n VALUE as signal, double\n} from './model.mjs';\nimport * as model from './model.mjs';\nimport './side.mjs';\nimport './side.mjs';\nconst state = 3;\nglobalThis.exampleResult = [bump(state), double(signal), model.VALUE, globalThis.sideCount];\n")
        self.build_preview()
        report = self.package_preview()
        document = self.output.read_text()
        code = re.search(r'<script type="module">\s*(.*?)</script>', document, re.S).group(1)
        result = subprocess.run(['node', '--input-type=module', '-e', code + '\nconsole.log(JSON.stringify(globalThis.exampleResult));'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), [7, 8, 4, 1])
        self.assertEqual(report['modules'], 3)

    def test_named_default_function_retains_its_local_binding(self):
        self.write('assets/js/rl/model.mjs', 'export default function helper(value) { return value + 1; }\nexport function invoke(value) { return helper(value); }\n')
        self.write('assets/js/rl/example.mjs', "import helper, {invoke} from './model.mjs';\nglobalThis.result = [helper(3), invoke(3)];\n")
        self.build_preview(); self.package_preview()
        code = re.search(r'<script type="module">\s*(.*?)</script>', self.output.read_text(), re.S).group(1)
        result = subprocess.run(['node', '--input-type=module', '-e', code + '\nconsole.log(JSON.stringify(globalThis.result));'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), [4, 4])

    def test_named_default_class_retains_its_local_binding(self):
        self.write('assets/js/rl/model.mjs', 'export default class Helper { static value = 4; }\nexport function invoke() { return Helper.value; }\n')
        self.write('assets/js/rl/example.mjs', "import Helper, {invoke} from './model.mjs';\nglobalThis.result = [Helper.value, invoke()];\n")
        self.build_preview(); self.package_preview()
        code = re.search(r'<script type="module">\s*(.*?)</script>', self.output.read_text(), re.S).group(1)
        result = subprocess.run(['node', '--input-type=module', '-e', code + '\nconsole.log(JSON.stringify(globalThis.result));'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), [4, 4])

    def test_mutable_export_aliases_are_rejected_for_named_imports(self):
        for kind in ('let', 'var'):
            with self.subTest(kind=kind):
                self.write('assets/js/rl/model.mjs', f'  {kind} count = 0;\nexport {{ count as total }};\nexport function increment() {{ count += 1; }}\n')
                self.write('assets/js/rl/example.mjs', "import {total, increment} from './model.mjs';\nincrement();\nglobalThis.result = total;\n")
                self.build_preview()
                with self.assertRaisesRegex(ValueError, 'Live mutable imports'):
                    self.package_preview()

    def test_multiline_mutable_declarations_are_rejected_for_named_imports(self):
        for kind in ('let', 'var'):
            for initializer in ('0,\n    count = 0;', '\n    0,\n    count = 0;', '1\n    + 2,\n    count = 0;'):
                with self.subTest(kind=kind, initializer=initializer):
                    self.write('assets/js/rl/model.mjs', f'{kind} spare = {initializer}\nexport {{ count as total }};\nexport function increment() {{ count += 1; }}\n')
                    self.write('assets/js/rl/example.mjs', "import {total, increment} from './model.mjs';\nincrement();\nglobalThis.result = total;\n")
                    self.build_preview()
                    with self.assertRaisesRegex(ValueError, 'Live mutable imports'):
                        self.package_preview()

    def test_multiline_exported_constants_are_all_available(self):
        self.write('assets/js/rl/model.mjs', 'export const FIRST =\n    1,\n    SECOND = 2;\n')
        self.write('assets/js/rl/example.mjs', "import {FIRST, SECOND} from './model.mjs';\nglobalThis.result = FIRST + SECOND;\n")
        self.build_preview(); self.package_preview()
        code = re.search(r'<script type="module">\s*(.*?)</script>', self.output.read_text(), re.S).group(1)
        result = subprocess.run(['node', '--input-type=module', '-e', code + '\nconsole.log(JSON.stringify(globalThis.result));'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), 3)

    def test_mutable_default_alias_import_is_rejected(self):
        self.write('assets/js/rl/model.mjs', 'let count = 0;\nexport { count as default };\n')
        self.write('assets/js/rl/example.mjs', "import count from './model.mjs';\nglobalThis.result = count;\n")
        self.build_preview()
        with self.assertRaisesRegex(ValueError, 'Live mutable imports'):
            self.package_preview()

    def test_imported_export_alias_is_classified(self):
        self.write('assets/js/rl/model.mjs', 'export const VALUE = 4;\n')
        self.write('assets/js/rl/facade.mjs', "import {VALUE} from './model.mjs';\nexport { VALUE };\n")
        self.write('assets/js/rl/example.mjs', "import {VALUE} from './facade.mjs';\nglobalThis.result = VALUE;\n")
        self.build_preview(); self.package_preview()
        code = re.search(r'<script type="module">\s*(.*?)</script>', self.output.read_text(), re.S).group(1)
        result = subprocess.run(['node', '--input-type=module', '-e', code + '\nconsole.log(JSON.stringify(globalThis.result));'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), 4)

    def test_unclassified_export_alias_fails_closed(self):
        self.write('assets/js/rl/example.mjs', 'const local = 1; function helper() { return local; }\nexport { helper };\n')
        self.build_preview()
        with self.assertRaisesRegex(ValueError, 'Unclassified export alias'):
            self.package_preview()

    def test_mutable_alias_namespace_import_stays_live(self):
        self.write('assets/js/rl/model.mjs', 'let count = 0;\nexport { count as total };\nexport function increment() { count += 1; }\n')
        self.write('assets/js/rl/example.mjs', "import * as model from './model.mjs';\nmodel.increment();\nglobalThis.result = model.total;\n")
        self.build_preview(); self.package_preview()
        code = re.search(r'<script type="module">\s*(.*?)</script>', self.output.read_text(), re.S).group(1)
        result = subprocess.run(['node', '--input-type=module', '-e', code + '\nconsole.log(JSON.stringify(globalThis.result));'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), 1)

    def test_nested_mutable_shadow_does_not_mark_module_constant_mutable(self):
        self.write('assets/js/rl/model.mjs', 'const VALUE = 4;\nfunction local() { let VALUE = 2; return VALUE; }\nexport { VALUE, local };\n')
        self.write('assets/js/rl/example.mjs', "import {VALUE, local} from './model.mjs';\nglobalThis.result = [VALUE, local()];\n")
        self.build_preview(); self.package_preview()
        code = re.search(r'<script type="module">\s*(.*?)</script>', self.output.read_text(), re.S).group(1)
        result = subprocess.run(['node', '--input-type=module', '-e', code + '\nconsole.log(JSON.stringify(globalThis.result));'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), [4, 2])

    def test_multiple_exported_constant_declarators(self):
        self.write('assets/js/rl/model.mjs', 'export const FIRST = 1, SECOND = 2;\n')
        self.write('assets/js/rl/example.mjs', "import {FIRST, SECOND} from './model.mjs';\nglobalThis.result = FIRST + SECOND;\n")
        self.build_preview(); self.package_preview()
        code = re.search(r'<script type="module">\s*(.*?)</script>', self.output.read_text(), re.S).group(1)
        result = subprocess.run(['node', '--input-type=module', '-e', code + '\nconsole.log(JSON.stringify(globalThis.result));'], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), 3)

    def test_invalid_original_export_binding_fails(self):
        self.write('assets/js/rl/example.mjs', 'export { missing };\n')
        self.build_preview()
        with self.assertRaisesRegex(ValueError, 'Original module syntax'):
            self.package_preview()

    def test_cyclic_module_dependencies_fail(self):
        self.write('assets/js/rl/example.mjs', "import './model.mjs';\n")
        self.write('assets/js/rl/model.mjs', "import './example.mjs';\n")
        self.build_preview()
        with self.assertRaisesRegex(ValueError, 'Cyclic ES module'):
            self.package_preview()

    def test_destructured_exports_fail_instead_of_exposing_false_bindings(self):
        self.write('assets/js/rl/example.mjs', 'export const {value: count} = {value: 1};\n')
        self.build_preview()
        with self.assertRaisesRegex(ValueError, 'Destructured export'):
            self.package_preview()

    def test_missing_module_dependency_fails(self):
        self.write('assets/js/rl/example.mjs', "import {VALUE} from './missing.mjs';\n")
        self.build_preview()
        with self.assertRaises(FileNotFoundError):
            self.package_preview()

    def test_dynamic_import_fails_without_network(self):
        self.write('assets/js/rl/example.mjs', "import('./other.mjs');\n")
        self.build_preview()
        with self.assertRaises(ValueError):
            self.package_preview()

    def test_missing_preview_media_fails(self):
        self.build_preview()
        (self.preview / 'assets/media/rl/example/hero.svg').unlink()
        with self.assertRaises(FileNotFoundError):
            self.package_preview()

    def test_external_stylesheet_fails_without_network(self):
        self.build_preview()
        document = (self.preview / 'index.html').read_text().replace('/assets/css/rl/example.css', 'https://example.test/external.css')
        (self.preview / 'index.html').write_text(document)
        with self.assertRaises(ValueError):
            self.package_preview()

    def test_css_imports_relative_media_fonts_and_srcset(self):
        self.write('assets/css/rl/extra.css', '.extra { background: url("../../media/rl/example/hero.svg"); }\n')
        self.write('assets/fonts/example.woff2', 'fixture font bytes')
        self.write('assets/css/rl/example.css', '@import "extra.css" screen;\n@font-face {font-family: example;src:url("../../fonts/example.woff2")}\n')
        self.body += '\n<img src="/assets/media/rl/example/hero.svg" srcset="/assets/media/rl/example/hero.svg 1x, /assets/media/rl/example/hero.svg 2x">'
        self.build_preview()
        report = self.package_preview()
        document = self.output.read_text()
        self.assertIn('@media screen', document)
        self.assertIn('data:font/woff2;base64,', document)
        self.assertIn(' 1x, data:image/svg+xml;base64,', document)
        self.assertEqual(report['local_media'], 2)

    def test_inline_style_media_and_download_links(self):
        self.body += '\n<style>.inline {background:url("/assets/media/rl/example/hero.svg")}</style>\n<a href="/assets/media/rl/example/hero.svg">Download</a>'
        self.build_preview()
        self.package_preview()
        document = self.output.read_text()
        self.assertNotIn('/assets/', document)
        self.assertIn('download="hero.svg"', document)

    def test_media_urls_inside_module_strings_are_inlined(self):
        self.write('assets/js/rl/example.mjs', 'globalThis.mediaSource = "/assets/media/rl/example/hero.svg";\n')
        self.build_preview()
        self.package_preview()
        self.assertNotIn('/assets/', self.output.read_text())

    def test_package_output_inside_source_checkout_fails(self):
        self.build_preview()
        with self.assertRaisesRegex(ValueError, 'outside the checkout'):
            package(self.preview, self.root / 'review.html', self.root)

    def test_package_output_inside_preview_fails(self):
        self.build_preview()
        with self.assertRaises(ValueError):
            package(self.preview, self.preview / 'review.html')


if __name__ == '__main__':
    unittest.main()
