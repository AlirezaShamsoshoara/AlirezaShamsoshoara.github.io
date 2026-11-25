#!/usr/bin/env python3
"""Compatibility entry point for the shared verified H.264 exporter."""
from pathlib import Path
import runpy
import sys


SHARED = Path(__file__).resolve().parents[1] / 'rl-blog'
sys.path.insert(0, str(SHARED))
TOOL = runpy.run_path(str(SHARED / 'export_mp4.py'))
probe = TOOL['probe']
export = TOOL['export']


if __name__ == '__main__':
    TOOL['main']()
