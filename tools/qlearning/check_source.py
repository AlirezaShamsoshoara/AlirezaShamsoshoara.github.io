#!/usr/bin/env python3
"""Check the post is publication-ready, plus source hygiene, without a site build."""
import argparse
from pathlib import Path
import re

import yaml


def main(root):
    root=root.resolve()
    posts=sorted((root/'_posts').glob('*-q-learning-one-update-at-a-time.md'))
    assert len(posts)==1, 'Expected exactly one dated Q-learning post in _posts/'
    post=posts[0]
    assert not (root/'_drafts/q-learning-one-update-at-a-time.md').exists(), 'Remove the old draft copy'
    stamp=re.fullmatch(r'(\d{4}-\d{2}-\d{2})-q-learning-one-update-at-a-time\.md',post.name)
    assert stamp, post.name
    _,frontmatter,_=post.read_text().split('---',2)
    page=yaml.safe_load(frontmatter)
    assert page.get('published',True) is not False and page.get('sitemap',True) is not False
    assert str(page['date'])==stamp.group(1), 'Front matter date must match the file name'
    assert page['permalink']=='/blog/rl-from-zero/q-learning/'
    assert 'interesting-blogs' in page['categories'], 'The post must appear on /blog/projects/'
    assert page.get('series')=='rl-from-zero' and page.get('series_part')==1, 'The post must be part 1 of RL From Zero'
    series=yaml.safe_load((root/'_data/blog_series.yml').read_text())
    assert any(s['id']=='rl-from-zero' and s['url']=='/blog/rl-from-zero/' for s in series), 'RL From Zero must be listed in _data/blog_series.yml'
    assert (root/'_pages/blog-rl-from-zero.md').is_file(), 'Missing the RL From Zero series page'
    assert page['hero_image']=='/assets/media/rl/qlearning/q-learning-hero.svg' and page['hero_alt']
    assert (root/page['hero_image'].lstrip('/')).is_file()
    layout=(root/'_layouts/rl-article.html').read_text()
    assert '{% if page.published == false %}' in layout and 'unless page.published' not in layout, 'Draft note must stay hidden on published posts'
    seo=(root/'_includes/seo.html').read_text()
    assert 'page.published == false' in seo and 'noindex, nofollow' in seo
    assert 'page.date and page.published != false' in seo
    config=yaml.safe_load((root/'_config.yml').read_text())
    assert 'tools' in config['exclude'] and '.claude' in config['exclude']
    public_files=[post,root/'_layouts/rl-article.html',root/'_includes/rl/qlearning-lab.html',root/'_includes/rl/qlearning-policy.html',root/'_includes/rl/qlearning-native.html',root/'assets/css/rl/qlearning.css',root/'assets/js/rl/qlearning-core.mjs',root/'assets/js/rl/qlearning-article.mjs']
    for path in public_files:
        text=path.read_text()
        if path==post:
            for stale in ('s5','s6','3.3','4.6'):
                assert stale not in text, ('superseded illustration',stale)
            assert '120' in text and '843' in text and '0.0095' in text
        for name,pattern in (('internal link',r'internal(?:fb|meta)\.com'),('local home path',r'/home/[a-z]'),('internal hostname',r'\bdev(?:vm|gpu)\d'),('Task ID',r'(?<![\w/])T\d{8,}\b'),('W&B key name',r'WANDB_API_KEY'),('em or en dash','[\u2014\u2013]')):
            assert not re.search(pattern,text), (path,name)
    for name in ('q-learning-hero.svg','q-learning-hero.png','q-update.png','q-update.gif','q-update.webm','q-update.mp4','q-update.json','frozenlake-8x8.gif','frozenlake-8x8.png','frozenlake-8x8.json'):
        assert (root/'assets/media/rl/qlearning'/name).is_file(), name
    identifiers=[]
    for fragment in ('qlearning-lab','qlearning-policy','qlearning-native'):
        identifiers += re.findall(r'\bid="([^"]+)"',(root/f'_includes/rl/{fragment}.html').read_text())
    assert len(identifiers)==len(set(identifiers)), 'Widget ids collide'
    print(f'PASS publication-ready post {post.relative_to(root)}, source hygiene, media presence, and unique widget IDs')
    print('NOTE this static check does not replace a real Jekyll build')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    main(parser.parse_args().root)
