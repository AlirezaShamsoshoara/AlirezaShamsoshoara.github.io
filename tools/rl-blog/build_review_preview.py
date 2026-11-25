#!/usr/bin/env python3
"""Build a standalone RL article preview with Markdown, Sass and Liquid, not Jekyll."""
import argparse
import html
import json
from pathlib import Path
import shutil

import markdown
import sass

from article_source import (
    asset_references, expand_includes, load_post, local_asset, media_slugs,
    outside_checkout, render_liquid, repository_root, site_context, split_front_matter,
)


def build(root: Path, post: Path, out: Path):
    root = root.resolve()
    out = outside_checkout(root, out)
    post, page, body = load_post(root, post)
    site = site_context(root)
    body, includes = expand_includes(root, body)
    body = render_liquid(body, page, site)
    content = markdown.markdown(
        body, extensions=['extra', 'toc', 'sane_lists', 'codehilite'],
        extension_configs={'codehilite': {'css_class': 'highlight', 'guess_lang': False, 'use_pygments': True}},
    )
    _, layout = split_front_matter((root / '_layouts/rl-article.html').read_text(encoding='utf-8'))
    layout = render_liquid(layout, page, site, content=content)
    _, style = split_front_matter((root / 'assets/css/main.scss').read_text(encoding='utf-8'))
    compiled = sass.compile(string=style, include_paths=[str(root / '_sass')], output_style='expanded')
    (out / 'assets/css').mkdir(parents=True, exist_ok=True)
    (out / 'assets/css/main.css').write_text(compiled, encoding='utf-8')
    for path in ('assets/css/rl', 'assets/js/rl', 'assets/fonts'):
        if (root / path).is_dir():
            shutil.copytree(root / path, out / path, dirs_exist_ok=True)
    for slug in media_slugs(page, body):
        path = Path('assets/media/rl') / slug
        if (root / path).is_dir():
            shutil.copytree(root / path, out / path, dirs_exist_ok=True)

    origin = str(site.get('url') or '').rstrip('/')
    base = str(site.get('baseurl') or '').rstrip('/')
    author = html.escape(str((site.get('author') or {}).get('name') or site.get('title') or 'Home'))
    home = html.escape(origin + base + '/', quote=True)
    blog = html.escape(origin + base + '/blog/', quote=True)
    projects = html.escape(origin + base + '/projects/', quote=True)
    nav = f'''<div class="masthead"><div class="masthead__inner-wrap"><nav class="greedy-nav"><ul class="visible-links"><li class="masthead__menu-item masthead__menu-item--lg"><a href="{home}">{author}</a></li><li class="masthead__menu-item"><a href="{blog}">Blog</a></li><li class="masthead__menu-item"><a href="{projects}">Projects</a></li></ul></nav></div></div>'''
    warning = '<aside style="background:#fff;border-bottom:1px solid #d5dbe2;color:#56616e;padding:8px 20px;font:13px system-ui;text-align:center">Standalone review preview, rendered without Jekyll. Run the real Jekyll build before merging.</aside>'
    document = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>' + html.escape(page['title']) + ' | Review draft</title><link rel="stylesheet" href="' + base + '/assets/css/main.css"><style>.masthead .visible-links{display:flex;flex-wrap:wrap;white-space:normal}.masthead .visible-links li{display:block}.masthead .visible-links li a{margin:.25rem .7rem}</style></head><body>' + nav + warning + layout + '</body></html>'
    for reference in asset_references(document):
        if reference == base + '/assets/css/main.css' or reference == '/assets/css/main.css':
            continue
        source = local_asset(root, reference, base)
        destination = out / source.relative_to(root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    if base:
        prefix = out / base.lstrip('/')
        prefix.resolve().relative_to(out)
        shutil.copytree(out / 'assets', prefix / 'assets', dirs_exist_ok=True)
    permalink = str(page.get('permalink') or '')
    if not permalink.startswith('/') or not permalink.endswith('/'):
        raise ValueError('The post needs a slash-delimited permalink')
    destination = (out / (base + permalink).lstrip('/') / 'index.html').resolve()
    destination.relative_to(out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(document, encoding='utf-8')
    (out / 'index.html').write_text(document, encoding='utf-8')
    provenance = {
        'kind': 'standalone review preview', 'production_jekyll_verified': False,
        'published': page.get('published') is not False, 'post': str(post.relative_to(root)),
        'permalink': permalink, 'entry': str(destination.relative_to(out)),
        'includes': [str(path.relative_to(root)) for path in includes],
        'site_url': origin, 'baseurl': base,
        'renderer': 'Python Markdown, libSass and python-liquid, not Jekyll',
    }
    (out / 'review-provenance.json').write_text(json.dumps(provenance, indent=2), encoding='utf-8')
    print(destination)
    return destination


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=repository_root())
    parser.add_argument('--post', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args(argv)
    build(args.root, args.post, args.out)


if __name__ == '__main__':
    main()
