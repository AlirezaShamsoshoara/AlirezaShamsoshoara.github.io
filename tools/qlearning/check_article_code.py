#!/usr/bin/env python3
"""Static compilation checks for public article snippets and highlighted rendering."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import textwrap

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer


def check(root: Path):
    posts = sorted((root / '_posts').glob('*-q-learning-one-update-at-a-time.md'))
    assert len(posts) == 1, 'Expected exactly one dated Q-learning post in _posts/'
    article = posts[0].read_text()
    blocks = re.findall(r'^```([^\n]*)\n(.*?)^```\s*$', article, re.M | re.S)
    results = []
    for language, source in blocks:
        language = language.strip()
        if language == 'python':
            # Method excerpts can contain return statements and a supplied self.
            # Compile their function-body syntax, without pretending they are standalone programs.
            wrapped = 'def __article_excerpt__():\n' + textwrap.indent(source, '    ')
            compile(wrapped, '<article excerpt>', 'exec')
            rendered = highlight(source, PythonLexer(), HtmlFormatter())
            assert '<span class=' in rendered
            results.append({'language': language, 'lines': len(source.splitlines()), 'syntax': 'passed'})
        elif language in ('bash', 'sh'):
            subprocess.run(['bash', '-n'], input=source, text=True, check=True, capture_output=True)
            results.append({'language': language, 'lines': len(source.splitlines()), 'syntax': 'passed'})
    assert sum(row['language'] == 'python' for row in results) >= 3
    assert sum(row['language'] in ('bash', 'sh') for row in results) >= 1
    assert 'qlearning-native.html' in article
    assert 'FrozenLake-v1' in article and ('8×8' in article or '8 by 8' in article or '8x8' in article)
    print(json.dumps({'snippet_checks': results, 'note': 'Syntax and highlighting only; native environment/checkpoint validation is recorded separately.'}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    check(parser.parse_args().root)
