#!/usr/bin/env python3
"""Compatibility entry point for the published Q-learning review preview."""
import argparse
from pathlib import Path
import runpy
import sys


SHARED = Path(__file__).resolve().parents[1] / 'rl-blog'
sys.path.insert(0, str(SHARED))
TOOL = runpy.run_path(str(SHARED / 'build_review_preview.py'))


def article_path(root: Path) -> Path:
    matches = sorted((root / '_posts').glob('*-q-learning-one-update-at-a-time.md'))
    if len(matches) != 1:
        raise FileNotFoundError('Expected exactly one dated Q-learning post in _posts/')
    return matches[0]


def build(root: Path, out: Path):
    return TOOL['build'](root, article_path(root), out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    build(args.root, args.out)
