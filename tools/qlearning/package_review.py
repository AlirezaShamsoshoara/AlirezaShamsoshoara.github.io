#!/usr/bin/env python3
"""Package a self-contained, unpublished interactive review HTML.

Inline the exact local preview's scripts/styles/portable media so no remote
assets or module paths are needed. This is still not a Jekyll production build.
"""
import argparse
import base64
from pathlib import Path
import re

import sass


def package(root: Path, preview: Path, out: Path):
    document = (preview / 'index.html').read_text()
    for source in ('/assets/css/main.css', '/assets/css/rl/qlearning.css'):
        css = (preview / source.lstrip('/')).read_text()
        # Theme icons are unnecessary in the self-contained article preview.
        css = re.sub(r'@font-face\s*\{[^}]*\}', '', css, flags=re.S)
        css = sass.compile(string=css, output_style='compressed')
        document = document.replace(f'<link rel="stylesheet" href="{source}">', '<style>' + css + '</style>')
    for name, mime in (('q-learning-hero.svg', 'image/svg+xml'), ('q-update.png', 'image/png'), ('q-update.gif', 'image/gif'), ('q-update.webm', 'video/webm'), ('q-update.mp4', 'video/mp4'), ('frozenlake-8x8.png', 'image/png'), ('frozenlake-8x8.gif', 'image/gif')):
        media = root / 'assets/media/rl/qlearning' / name
        uri = f'data:{mime};base64,' + base64.b64encode(media.read_bytes()).decode()
        document = document.replace('/assets/media/rl/qlearning/' + name, uri)
        document = document.replace(f'href="{uri}"', f'href="{uri}" download="{name}"')
    core = (root / 'assets/js/rl/qlearning-core.mjs').read_text()
    core = re.sub(r'^export ', '', core, flags=re.M)
    ui = (root / 'assets/js/rl/qlearning-article.mjs').read_text()
    ui = re.sub(r'^import .*?;\n', '', ui, count=1)
    inline = '<script type="module">\n' + core + '\n' + ui + '\n</script>'
    document = document.replace('<script type="module" src="/assets/js/rl/qlearning-article.mjs"></script>', inline)
    document = document.replace('href="/blog/projects/"', 'href="https://AlirezaShamsoshoara.github.io/blog/projects/"')
    document = document.replace('href="/blog/rl-from-zero/"', 'href="https://AlirezaShamsoshoara.github.io/blog/rl-from-zero/"')
    if re.search(r'(src|href)="/assets/', document):
        raise ValueError('Some local assets remain unresolved')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(document)
    print(out, out.stat().st_size)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--preview', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    package(args.root, args.preview, args.out)
