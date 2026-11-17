#!/usr/bin/env python3
"""Assemble the explicit private platform review package.

Markdown review copies only normalize local image paths for the package folder.
The repository's platform source drafts are not rewritten.
"""
import argparse
import json
from pathlib import Path
import re
import shutil


def assemble(root, review, out):
    source = root / 'tools/qlearning/platform-drafts'
    out.mkdir(parents=True, exist_ok=True)
    media = out / 'media'; media.mkdir(exist_ok=True)
    assets = {
        'q-learning-hero.png': root / 'assets/media/rl/qlearning/q-learning-hero.png',
        'frozenlake-8x8.gif': root / 'assets/media/rl/qlearning/frozenlake-8x8.gif',
        'frozenlake-8x8.png': root / 'assets/media/rl/qlearning/frozenlake-8x8.png',
        'first-goal.gif': source / 'media/first-goal.gif',
        'first-bootstrap.gif': source / 'media/first-bootstrap.gif',
        'first-goal.png': source / 'media/first-goal.png',
        'first-bootstrap.png': source / 'media/first-bootstrap.png',
        'manifest.json': source / 'media/manifest.json'
    }
    for name, path in assets.items():
        shutil.copy2(path, media / name)
    for platform in ('medium', 'substack'):
        text = (source / f'{platform}.md').read_text()
        def image_path(match):
            alt, href = match.groups()
            name = Path(href).name
            if name not in assets:
                raise ValueError(f'Unknown platform image {href}')
            return f'![{alt}](media/{name})'
        normalized = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', image_path, text)
        (out / f'{platform}.md').write_text(normalized)
        shutil.copy2(review / f'{platform}-review.html', out / f'{platform}-review.html')
    shutil.copy2(review / 'substack-email-review.html', out / 'substack-email-review.html')
    shutil.copy2(source / 'README.md', out / 'PUBLISHING_GUIDE.md')
    (out / 'package-provenance.json').write_text(json.dumps({
        'kind': 'unpublished platform adaptation review',
        'repository_source_dir': 'tools/qlearning/platform-drafts',
        'markdown_transformation': 'Local image references normalized to media/<file> only; source drafts unchanged.',
        'accounts_accessed': False, 'published': False,
        'platform_native_rendering_verified': False
    }, indent=2))
    print(out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--review', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.out.resolve().is_relative_to(root):
        raise ValueError('Private package output must stay outside the checkout')
    assemble(root, args.review, args.out)
