#!/usr/bin/env python3
"""Compatibility entry point for self-contained Q-learning review packaging."""
import argparse
from pathlib import Path
import runpy
import sys


SHARED = Path(__file__).resolve().parents[1] / 'rl-blog'
sys.path.insert(0, str(SHARED))
TOOL = runpy.run_path(str(SHARED / 'package_review.py'))


def package(root: Path, preview: Path, out: Path):
    # Keep the legacy root argument. All package inputs now come from the preview.
    return TOOL['package'](preview, out, root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--preview', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    package(args.root, args.preview, args.out)
