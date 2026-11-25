#!/usr/bin/env python3
"""Check one RL From Zero post in its expected draft or published state."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

import markdown

from article_source import (
    asset_references, expand_includes, load_post, local_asset, render_liquid,
    repository_root, site_context, split_front_matter,
)


LOCAL_PATH = re.compile(r'''file://|(?<!\w)[A-Za-z]:[\\/]|(?<![\w:])/(?:home|Users|tmp|private|var|opt|mnt|srv|workspace)[/\\]|(?<!\w)~[/\\]''')
MODULE_PATH = re.compile(r'''\b(?:import|export)\s+(?:[^;]*?\s+from\s+)?['"](\.[^'"]+)['"]''')
TEXT_SUFFIXES = {'.md', '.html', '.css', '.mjs', '.js', '.json', '.svg', '.txt', '.yml', '.yaml'}


class Identifiers(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
    def handle_starttag(self, _tag, attrs):
        self.ids.extend(value for key, value in attrs if key == 'id')
    handle_startendtag = handle_starttag


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check(root: Path, post: Path, state: str):
    root = root.resolve()
    post, page, body = load_post(root, post)
    relative = post.relative_to(root)
    checks = []
    require(isinstance(page.get('title'), str) and page['title'].strip(), 'The post needs a title')
    if state == 'draft':
        require(relative.parts[0] == '_drafts', 'Drafts belong in _drafts/')
        require(page.get('published') is False and page.get('sitemap') is False, 'Drafts need published: false and sitemap: false')
    else:
        require(relative.parts[0] == '_posts', 'Published posts belong in _posts/')
        stamp = re.fullmatch(r'(\d{4}-\d{2}-\d{2})-.+\.md', post.name)
        require(stamp is not None, 'Published filenames need a date prefix')
        require(str(page.get('date')) == stamp.group(1), 'Front matter date must match the filename')
        require(page.get('published', True) is not False and page.get('sitemap', True) is not False, 'Remove the draft flags before publishing')
    checks.append('front matter matches the expected publication state')
    require(re.fullmatch(r'/blog/rl-from-zero/[a-z0-9]+(?:-[a-z0-9]+)*/', str(page.get('permalink') or '')) is not None, 'Use a /blog/rl-from-zero/slug/ permalink')
    checks.append('series permalink')
    require(page.get('series') == 'rl-from-zero', 'Expected series: rl-from-zero')
    part = page.get('series_part')
    require(type(part) is int and part > 0, 'series_part must be a positive integer')
    require('interesting-blogs' in (page.get('categories') or []), 'Include the interesting-blogs category')
    require('rl-from-zero' in (page.get('tags') or []), 'Include the rl-from-zero tag')
    site = site_context(root)
    require(any(row.get('id') == page['series'] for row in site['data']['blog_series']), 'The series must be listed in _data/blog_series.yml')
    checks.append('series identity, order, category and tag')
    require(bool(page.get('hero_image')) and bool(page.get('hero_alt')), 'The post needs hero_image and descriptive hero_alt')
    hero = local_asset(root, page['hero_image'], str(site.get('baseurl') or ''))
    checks.append('hero image exists and has alt text')
    sources = {post, root / '_layouts/rl-article.html', hero,
               local_asset(root, '/assets/css/rl/article.css')}
    for field in ('series_label', 'lede', 'read_time_text', 'footer_part_label', 'next_teaser'):
        require(page.get(field) is None or isinstance(page[field], str), field + ' must be text')
    for field in ('stylesheets', 'scripts'):
        values = page.get(field) or []
        require(isinstance(values, list), field + ' must be a list')
        for value in values:
            require(isinstance(value, str) and bool(value.strip()), field + ' cannot contain empty paths')
            sources.add(local_asset(root, value, str(site.get('baseurl') or '')))
    jumps = page.get('jump_links') or []
    require(isinstance(jumps, list), 'jump_links must be a list')
    for link in jumps:
        require(isinstance(link, dict) and bool(link.get('href')) and bool(link.get('label')), 'Each jump link needs href and label')
    for field in ('previous_part', 'next_part'):
        link = page.get(field)
        if link is not None:
            require(isinstance(link, dict) and bool(link.get('url')) and bool(link.get('title')), field + ' needs url and title')
            parsed = urlsplit(link['url'])
            require(parsed.scheme in ('', 'https', 'http') and (parsed.scheme or link['url'].startswith('/blog/rl-from-zero/')), field + ' must link to a public part')
    checks.append('optional article fields and asset lists')
    expanded, includes = expand_includes(root, body)
    sources.update(includes)
    rendered = render_liquid(expanded, page, site)
    media = set()
    for reference in asset_references(rendered):
        path = local_asset(root, reference, str(site.get('baseurl') or ''))
        sources.add(path)
        if path.relative_to(root).parts[1] == 'media':
            media.add(path)
            companion = path.with_suffix('.json')
            if companion.is_file():
                sources.add(companion)
    media.add(hero)
    checks.append('all referenced article media and assets exist')
    # Inspect local module dependencies too, not only the entry scripts.
    pending = list(sources)
    while pending:
        path = pending.pop()
        if path.suffix not in ('.mjs', '.js'):
            continue
        for reference in MODULE_PATH.findall(path.read_text(encoding='utf-8')):
            dependency = (path.parent / urlsplit(reference).path).resolve()
            dependency.relative_to(root / 'assets')
            require(dependency.is_file(), 'Missing module dependency: ' + reference)
            if dependency not in sources:
                sources.add(dependency); pending.append(dependency)
    content = markdown.markdown(rendered, extensions=['extra', 'toc', 'sane_lists', 'codehilite'], extension_configs={'codehilite': {'css_class': 'highlight', 'guess_lang': False, 'use_pygments': True}})
    _, layout = split_front_matter((root / '_layouts/rl-article.html').read_text(encoding='utf-8'))
    identifiers = Identifiers()
    identifiers.feed(render_liquid(layout, page, site, content=content))
    require(len(identifiers.ids) == len(set(identifiers.ids)), 'Element IDs collide across the layout, article and includes')
    checks.append('unique element IDs across the complete article')
    for link in jumps:
        if link['href'].startswith('#'):
            require(link['href'][1:] in identifiers.ids, 'Missing jump-link target: ' + link['href'])
    checks.append('jump-link targets exist')
    text_count = 0
    for path in sorted(sources):
        if path.suffix not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding='utf-8')
        text_count += 1
        label = str(path.relative_to(root))
        require(not re.search('[\u2014\u2013]', text), 'Long dash in ' + label)
        require(not LOCAL_PATH.search(text), 'Absolute local path in ' + label)
    checks.append('public source has no long dashes or absolute local paths')
    report = {
        'post': str(relative), 'state': state, 'checks_passed': len(checks), 'checks': checks,
        'includes': len(includes), 'unique_ids': len(identifiers.ids), 'media_files': len(media),
        'text_files_checked': text_count, 'production_jekyll_verified': False,
    }
    print(json.dumps(report, indent=2))
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=repository_root())
    parser.add_argument('--post', type=Path, required=True)
    parser.add_argument('--state', choices=('draft', 'published'), required=True)
    args = parser.parse_args(argv)
    check(args.root, args.post, args.state)


if __name__ == '__main__':
    main()
