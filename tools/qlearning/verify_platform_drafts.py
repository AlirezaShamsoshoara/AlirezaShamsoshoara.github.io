#!/usr/bin/env python3
"""Check source consistency and local rendering of the platform draft package.

No accounts, publishers, email lists, training, or external image hosts are used.
The browser reviews are not substitutes for the platforms' own draft previews.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import textwrap

from PIL import Image, ImageSequence
from playwright.sync_api import sync_playwright
import wandb
import yaml


def verify(args):
    root = args.root.resolve()
    draft_dir = root / 'tools/qlearning/platform-drafts'
    args.out.mkdir(parents=True, exist_ok=True)
    approved_body_hash = '43ff65e6a10dbfde0b3d07333dc269ad5d1b39932b90000ed85e14011122661f'
    posts = sorted((root / '_posts').glob('*-q-learning-one-update-at-a-time.md'))
    assert len(posts) == 1, 'Expected exactly one dated Q-learning post in _posts/'
    _, metadata, body = posts[0].read_text().split('---', 2)
    assert hashlib.sha256(body.encode()).hexdigest() == approved_body_hash, 'Approved article body changed'
    config = yaml.safe_load(metadata)
    assert config.get('published', True) is not False and config['permalink'] == '/blog/rl-from-zero/q-learning/'
    assert 'tools' in yaml.safe_load((root / '_config.yml').read_text())['exclude']
    media_manifest = json.loads((draft_dir / 'media/manifest.json').read_text())
    assert media_manifest['source_gif_sha256'] == hashlib.sha256((root / 'assets/media/rl/qlearning/q-update.gif').read_bytes()).hexdigest()
    for clip in media_manifest['clips']:
        file = draft_dir / 'media' / (clip['name'] + '.gif')
        assert hashlib.sha256(file.read_bytes()).hexdigest() == clip['sha256']
        assert file.stat().st_size < 25_000_000
        with Image.open(file) as image:
            assert sum(frame.info.get('duration', 0) for frame in ImageSequence.Iterator(image)) == clip['duration_ms'] == 12920
    assert [(item['recorded_episode'], item['recorded_transition_index']) for item in media_manifest['clips']] == [(29, 210), (70, 550)]
    source_checks = []
    for platform in ('medium', 'substack'):
        text = (draft_dir / f'{platform}.md').read_text()
        assert text.startswith('# ')
        images = re.findall(r'!\[([^\]]+)\]\(([^)]+)\)', text)
        assert images[0][1].endswith('q-learning-hero.png')
        assert len(images) == 4
        for alt, href in images:
            assert len(alt) > 30
            path = (draft_dir / href).resolve()
            assert path.is_relative_to(root) and path.is_file()
        for marker in ('internalmeta.com', 'internalfb.com', 'facebook.com', '/home/alisol', 'devvm', 'T296474467', 'WANDB_API_KEY', '\u2014', '{%', '{{'):
            assert marker not in text, (platform, marker)
        for pattern in (r'\b120\b', r'\b843\b', r'\b29\b', r'\b70\b', r'\b103\b', r'\b0\.0095\b', r'\b0\.95\b', r'\b0\.99\b', r'\b200\b', r'\b16\b'):
            assert re.search(pattern, text), (platform, pattern)
        assert 'https://AlirezaShamsoshoara.github.io/blog/rl-from-zero/q-learning/' in text
        assert '27ea78dc267363afec2d447f1ba0278bfccdf89e' in text
        assert 'same fixed map' in text.lower()
        assert 'not a standalone' in text or 'not standalone' in text
        assert 'first-goal.gif' in text and 'first-bootstrap.gif' in text
        assert 'not' in text[text.index('first-bootstrap.gif'):text.index('first-bootstrap.gif') + 650].lower()
        blocks = re.findall(r'^```([^\n]*)\n(.*?)^```\s*$', text, re.M | re.S)
        python_count = shell_count = 0
        for language, source in blocks:
            if language.strip() == 'python':
                compile('def __excerpt__():\n' + textwrap.indent(source, '    '), '<platform excerpt>', 'exec')
                python_count += 1
            elif language.strip() in ('bash', 'sh'):
                subprocess.run(['bash', '-n'], input=source, text=True, capture_output=True, check=True)
                shell_count += 1
        assert python_count >= 3 and shell_count >= 1
        source_checks.append({'platform': platform, 'python_excerpts': python_count, 'shell_examples': shell_count, 'image_count': len(images), 'word_count_approx': len(re.findall(r'\b\w+\b', re.sub(r'https?://\S+', '', text)))})
    run = wandb.init(project='rl-education', name='qlearning-platform-draft-verification', mode='offline', dir=str(args.out), config={'scope': 'static sources and local HTML only', 'accounts_accessed': False})
    browser_checks = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=str(args.browser), headless=True)
            try:
                for name, static in (('medium-review.html', False), ('substack-review.html', False), ('substack-email-review.html', True)):
                    errors = []; external_requests = []
                    for width in (390, 1440):
                        page = browser.new_page(viewport={'width': width, 'height': 1000}, java_script_enabled=False)
                        page.on('pageerror', lambda error: errors.append(str(error)))
                        page.on('request', lambda request: external_requests.append(request.url) if request.url.startswith(('http://', 'https://')) else None)
                        page.goto((args.review / name).resolve().as_uri(), wait_until='load', timeout=60000)
                        assert page.locator('article h1').count() == 1
                        assert 'Unpublished' in page.locator('.review-notice').inner_text()
                        assert page.locator('article img').count() == 4
                        assert page.locator('article img').first.get_attribute('class') == 'hero-image'
                        assert page.locator('article h1').evaluate('(el)=>el.nextElementSibling.querySelector(".hero-image")!==null')
                        assert page.locator('article img').evaluate_all('images=>images.every(el=>el.complete&&el.naturalWidth>0)')
                        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'), (name, width)
                        if static:
                            assert page.locator('article img').evaluate_all('images=>images.every(el=>el.src.startsWith("data:image/png;"))')
                        else:
                            assert page.locator('article img').evaluate_all('images=>images.filter(el=>el.src.startsWith("data:image/gif;")).length') == 3
                        assert page.locator('.highlight pre').count() >= 5
                        assert page.locator('.highlight .k, .highlight .kn').count() > 8
                        token_contrast = page.locator('.highlight pre').evaluate_all('''blocks=>{
                          const lum=color=>color.match(/[0-9.]+/g).slice(0,3).map(Number).map(x=>x/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4).reduce((s,x,i)=>s+x*[.2126,.7152,.0722][i],0);
                          return blocks.flatMap(pre=>[...pre.querySelectorAll('span')].filter(el=>el.textContent.trim()).map(el=>{
                            const f=lum(getComputedStyle(el).color),b=lum(getComputedStyle(pre).backgroundColor);
                            return(Math.max(f,b)+.05)/(Math.min(f,b)+.05);
                          }));
                        }''')
                        assert token_contrast and min(token_contrast) >= 4.5
                        if page.locator('.highlight pre').first.evaluate('(el)=>el.scrollWidth>el.clientWidth'):
                            pre = page.locator('.highlight pre').first
                            pre.evaluate('(el)=>el.scrollLeft=50')
                            assert pre.evaluate('(el)=>el.scrollLeft') > 0
                        page.locator('article').screenshot(path=str(args.out / f'{name.replace(".html", "")}-{width}-top.png'), animations='disabled') if width == 1440 else page.screenshot(path=str(args.out / f'{name.replace(".html", "")}-{width}-top.png'))
                        page.locator('.highlight').first.screenshot(path=str(args.out / f'{name.replace(".html", "")}-{width}-code.png'))
                        page.locator('article img').nth(2).screenshot(path=str(args.out / f'{name.replace(".html", "")}-{width}-bootstrap.png'))
                        browser_checks.append({'file': name, 'viewport': width, 'images_loaded': 4, 'static_media': static, 'minimum_code_contrast': min(token_contrast), 'page_overflow': False})
                        page.close()
                    assert not errors and not external_requests, (errors, external_requests)
            finally:
                browser.close()
        report = {'source_checks': source_checks, 'browser_checks': browser_checks, 'approved_blog_body_unchanged': True, 'short_clips_verified': 2,
                  'accounts_accessed': False, 'posted_or_published': False, 'platform_native_rendering_verified': False,
                  'note': 'These browser-openable drafts verify content and portable rendering, not Medium/Substack editor or real email-client behavior. The companion-blog destination still needs publication and live-link verification.'}
        (args.out / 'platform-verification.json').write_text(json.dumps(report, indent=2))
        run.log({'verification/platform_sources': len(source_checks), 'verification/browser_views': len(browser_checks), 'verification/clips': 2, 'verification/approved_blog_unchanged': 1})
        print(json.dumps(report, indent=2))
    finally:
        run.finish()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--review', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--browser', type=Path, required=True)
    verify(parser.parse_args())
