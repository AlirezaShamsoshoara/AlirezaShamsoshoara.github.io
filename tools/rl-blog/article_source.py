"""Shared source loading for RL From Zero review and validation tools."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml


FRONT_MATTER = re.compile(r'\A---\r?\n(.*?)^---[ \t]*(?:\r?\n|$)(.*)\Z', re.S | re.M)
RL_INCLUDE = re.compile(r'''{%\s*include\s+['"]?(rl/[\w./-]+\.html)['"]?\s*%}''')
ASSET_REFERENCE = re.compile(r'''(?<![\w./-])/assets/[^\s'"<>|)]+''')


def repository_root():
    return Path(__file__).resolve().parents[2]


def resolve_post(root, post):
    root = Path(root).resolve()
    post = Path(post)
    post = (root / post).resolve() if not post.is_absolute() else post.resolve()
    relative = post.relative_to(root)
    if relative.parts[0] not in ('_drafts', '_posts') or post.suffix != '.md':
        raise ValueError('The post must be Markdown under _drafts/ or _posts/')
    if not post.is_file():
        raise FileNotFoundError(relative)
    return post


def split_front_matter(source):
    match = FRONT_MATTER.fullmatch(source)
    if not match:
        raise ValueError('Expected YAML front matter delimited by --- lines')
    page = yaml.safe_load(match.group(1)) or {}
    if not isinstance(page, dict):
        raise ValueError('Front matter must be a mapping')
    return page, match.group(2)


def load_post(root, post):
    post = resolve_post(root, post)
    page, body = split_front_matter(post.read_text(encoding='utf-8'))
    if page.get('layout') != 'rl-article':
        raise ValueError('Expected layout: rl-article')
    return post, page, body


def expand_includes(root, body):
    """Inline every literal rl/*.html include, including nested includes."""
    root = Path(root).resolve()
    sources = []
    include_root = root / '_includes/rl'

    def expand(text, chain):
        def replace(match):
            path = (root / '_includes' / match.group(1)).resolve()
            path.relative_to(include_root)
            if path in chain:
                raise ValueError('Cyclic article include: ' + match.group(1))
            if not path.is_file():
                raise FileNotFoundError(match.group(1))
            sources.append(path)
            return expand(path.read_text(encoding='utf-8'), (*chain, path))
        result = RL_INCLUDE.sub(replace, text)
        if re.search(r'{%-?\s*include\b', result):
            raise ValueError('Use literal {% include rl/name.html %} article includes')
        return result

    return expand(body, ()), list(dict.fromkeys(sources))


def site_context(root):
    root = Path(root)
    config = yaml.safe_load((root / '_config.yml').read_text(encoding='utf-8'))
    series = root / '_data/blog_series.yml'
    config['data'] = {'blog_series': yaml.safe_load(series.read_text(encoding='utf-8')) if series.is_file() else []}
    return config


def render_liquid(source, page, site, **extra):
    from liquid import DictLoader, Environment
    env = Environment(loader=DictLoader({}), autoescape=False)
    base = str(site.get('baseurl') or '').rstrip('/')

    def relative_url(*args):
        value = str(args[-1])
        if urlsplit(value).scheme or value.startswith(('//', '#')):
            return value
        return base + '/' + value.lstrip('/')

    env.filters['relative_url'] = relative_url
    env.filters['absolute_url'] = lambda *args: str(site.get('url') or '').rstrip('/') + relative_url(*args)
    return env.parse(source).render({'page': page, 'site': site, **extra})


def local_asset(root, reference, baseurl=''):
    """Resolve a public asset URL, never a filesystem path outside the root."""
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc:
        raise ValueError('Expected a local asset URL: ' + reference)
    path = unquote(parsed.path)
    base = baseurl.rstrip('/')
    if base and path.startswith(base + '/'):
        path = path[len(base):]
    if not path.startswith('/assets/'):
        raise ValueError('Expected an /assets/ URL: ' + reference)
    destination = (Path(root).resolve() / path.lstrip('/')).resolve()
    destination.relative_to(Path(root).resolve() / 'assets')
    if not destination.is_file():
        raise FileNotFoundError(path)
    return destination


def asset_references(text):
    return sorted(set(ASSET_REFERENCE.findall(text)))


def media_slugs(page, rendered):
    references = rendered + '\n' + str(page.get('hero_image') or '')
    slugs = set(re.findall(r'/assets/media/rl/([\w-]+)/', references))
    if not slugs and page.get('permalink'):
        slugs.add(str(page['permalink']).strip('/').split('/')[-1])
    return sorted(slugs)


def outside_checkout(root, destination):
    root = Path(root).resolve()
    destination = Path(destination).resolve()
    if destination == root or root in destination.parents:
        raise ValueError('Review output must be outside the checkout')
    return destination
