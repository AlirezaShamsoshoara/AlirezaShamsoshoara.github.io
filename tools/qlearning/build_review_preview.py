#!/usr/bin/env python3
"""Build a standalone review preview, NOT a verified Jekyll production build.

Uses the actual article, includes, layout and CSS/JS. Python Markdown/libSass
provide local review rendering when Jekyll dependencies are unavailable.
"""
import argparse
import html
import json
from pathlib import Path
import re
import shutil

import markdown
import sass
import yaml


def article_path(root: Path) -> Path:
    matches = sorted((root / '_posts').glob('*-q-learning-one-update-at-a-time.md'))
    if len(matches) != 1:
        raise FileNotFoundError('Expected exactly one dated Q-learning post in _posts/')
    return matches[0]


def build(root: Path, out: Path):
    root = root.resolve()
    out = out.resolve()
    if out == root or root in out.parents:
        raise ValueError('Review output must be outside the checkout')
    out.mkdir(parents=True, exist_ok=True)
    source = article_path(root).read_text()
    _, frontmatter, body = source.split('---', 2)
    meta = yaml.safe_load(frontmatter)
    for name in ('qlearning-lab', 'qlearning-policy', 'qlearning-native'):
        body = body.replace('{% include rl/' + name + '.html %}', (root / f'_includes/rl/{name}.html').read_text())
    body = re.sub(r"{{\s*'([^']+)'\s*\|\s*relative_url\s*}}", lambda m: m.group(1), body)
    rendered = markdown.markdown(body, extensions=['extra', 'toc', 'sane_lists', 'codehilite'], extension_configs={'codehilite': {'css_class': 'highlight', 'guess_lang': False, 'use_pygments': True}})
    config = yaml.safe_load((root / '_config.yml').read_text())
    layout = (root / '_layouts/rl-article.html').read_text().split('---', 2)[2]
    hero_image = meta.get('hero_image', '')
    def render_hero(match):
        if not hero_image:
            return ''
        return match.group(1).replace('{{ page.hero_image | relative_url }}', html.escape(hero_image, quote=True)).replace('{{ page.hero_alt | escape }}', html.escape(meta.get('hero_alt', ''), quote=True))
    layout = re.sub(r'{% if page.hero_image %}(.*?){% endif %}', render_hero, layout, flags=re.S)
    unpublished = meta.get('published') is False
    layout = re.sub(r'{% if page.published == false %}(.*?){% endif %}', lambda m: m.group(1) if unpublished else '', layout, flags=re.S)
    layout = re.sub(r"{{\s*'([^']+)'\s*\|\s*relative_url\s*}}", lambda m: m.group(1), layout)
    layout = layout.replace('{{ page.title }}', html.escape(meta['title']))
    layout = layout.replace('{{ site.author.name }}', html.escape(config['author']['name']))
    layout = layout.replace('{{ content }}', rendered)
    style = (root / 'assets/css/main.scss').read_text().split('---', 2)[2]
    compiled = sass.compile(string=style, include_paths=[str(root / '_sass')], output_style='expanded')
    assets = out / 'assets'
    (assets / 'css').mkdir(parents=True, exist_ok=True)
    (assets / 'css/main.css').write_text(compiled)
    for path in ('assets/css/rl', 'assets/js/rl', 'assets/fonts'):
        if (root / path).exists():
            shutil.copytree(root / path, out / path, dirs_exist_ok=True)
    media = root / 'assets/media/rl/qlearning'
    if media.exists():
        shutil.copytree(media, out / 'assets/media/rl/qlearning', dirs_exist_ok=True)
    nav = '''<div class="masthead"><div class="masthead__inner-wrap"><nav class="greedy-nav"><ul class="visible-links"><li class="masthead__menu-item masthead__menu-item--lg"><a href="https://AlirezaShamsoshoara.github.io/">Alireza Shamsoshoara</a></li><li class="masthead__menu-item"><a href="https://AlirezaShamsoshoara.github.io/blog/">Blog</a></li><li class="masthead__menu-item"><a href="https://AlirezaShamsoshoara.github.io/projects/">Projects</a></li></ul></nav></div></div>'''
    warning = '<aside style="background:#fff;border-bottom:1px solid #d5dbe2;color:#56616e;padding:8px 20px;font:13px system-ui;text-align:center">Standalone review preview, rendered without Jekyll. Run the real Jekyll build before merging.</aside>'
    document = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>' + html.escape(meta['title']) + ' | Review draft</title><link rel="stylesheet" href="/assets/css/main.css"><style>.masthead .visible-links{display:flex;flex-wrap:wrap;white-space:normal}.masthead .visible-links li{display:block}.masthead .visible-links li a{margin:.25rem .7rem}</style></head><body>' + nav + warning + layout + '</body></html>'
    destination = out / 'blog/rl-from-zero/q-learning/index.html'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(document)
    (out / 'index.html').write_text(document)
    (out / 'review-provenance.json').write_text(json.dumps({'kind': 'standalone review preview', 'production_jekyll_verified': False, 'published': not unpublished, 'inputs': ['article post', 'actual includes', 'actual article layout', 'libSass compilation of theme', 'actual ES modules'], 'renderer': 'Python Markdown and libSass, not Jekyll/Liquid'}, indent=2))
    print(destination)
    return destination


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    build(args.root, args.out)
