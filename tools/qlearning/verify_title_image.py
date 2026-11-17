#!/usr/bin/env python3
"""Verify the algorithm-specific image below the approved article title.

Checks the self-contained review file, renders a sharp PNG copy of the SVG, and
smoke-tests the unchanged teaching figures. It does not run a Jekyll build.
"""
import argparse
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

from PIL import Image
from playwright.sync_api import sync_playwright
import wandb
import yaml


def verify(args):
    args.out.mkdir(parents=True, exist_ok=True)
    source = args.root / 'assets/media/rl/qlearning/q-learning-hero.svg'
    data = ET.fromstring(source.read_text())
    assert data.attrib['viewBox'] == '0 0 1200 420'
    assert not data.findall('.//{http://www.w3.org/2000/svg}script')
    assert not data.findall('.//{http://www.w3.org/2000/svg}image')
    posts = sorted((args.root / '_posts').glob('*-q-learning-one-update-at-a-time.md'))
    assert len(posts) == 1, 'Expected exactly one dated Q-learning post in _posts/'
    article = posts[0].read_text()
    _, frontmatter, _ = article.split('---', 2)
    meta = yaml.safe_load(frontmatter)
    assert meta['hero_image'] == '/assets/media/rl/qlearning/q-learning-hero.svg'
    assert meta['hero_alt'] and meta.get('published', True) is not False
    control = subprocess.run(['node', '--input-type=module', '-e', 'import {createExplorationTrace} from "./assets/js/rl/qlearning-core.mjs"; const t=createExplorationTrace();const r=t.records[t.milestones.bootstrap];console.log(JSON.stringify({state:r.state,action:r.action,nextState:r.nextState,reward:r.reward,oldValue:r.oldValue,newValue:r.newValue,nextMax:r.nextMax,alpha:t.alpha,gamma:t.gamma}));'], cwd=args.root, text=True, capture_output=True, check=True)
    update = json.loads(control.stdout)
    assert update['state'] == 13 and update['action'] == 2 and update['nextState'] == 14
    assert update['reward'] == 0 and update['oldValue'] == 0
    assert abs(update['newValue'] - .0095) < 1e-12 and update['nextMax'] == .1
    checks = []
    run = wandb.init(project='rl-education', name='qlearning-title-image-review', mode='offline', dir=str(args.out), config={'scope': 'title illustration only, not production Jekyll'})
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=str(args.browser), headless=True)
            try:
                image_page = browser.new_page(viewport={'width': 1200, 'height': 420}, device_scale_factor=2)
                image_page.goto(source.resolve().as_uri(), wait_until='load')
                image_page.screenshot(path=str(source.with_suffix('.png')))
                png = Image.open(source.with_suffix('.png'))
                assert png.size == (2400, 840)
                assert png.convert('RGB').getpixel((0, 0)) == (255, 255, 255)
                image_page.close()
                checks.append('White scalable SVG and sharp 2400×840 PNG share the checked Q-learning update')
                errors = []
                measurements = []
                for width in (320, 390, 768, 1440):
                    page = browser.new_page(viewport={'width': width, 'height': 1000})
                    page.on('pageerror', lambda error: errors.append(str(error)))
                    page.goto(args.html.resolve().as_uri(), wait_until='load', timeout=60000)
                    page.wait_for_function('window.QLearningPilot !== undefined')
                    image = page.locator('.rlql-title-figure img')
                    assert image.count() == 1
                    assert page.locator('.rlql-draft-note').count() == 0, 'Published post must not show the review-draft note'
                    box = image.bounding_box()
                    title = page.locator('#rlql-title').bounding_box()
                    lede = page.locator('.rlql-lede').bounding_box()
                    assert box['y'] >= title['y'] + title['height'] - 1
                    assert box['y'] + box['height'] <= lede['y'] + 1
                    assert page.locator('#rlql-title').evaluate('(el)=>el.nextElementSibling.classList.contains("rlql-title-figure")')
                    assert image.evaluate('(el)=>el.complete&&el.naturalWidth===1200&&el.naturalHeight===420')
                    assert image.get_attribute('alt') == meta['hero_alt']
                    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'), width
                    assert image.get_attribute('src').startswith('data:image/svg+xml;base64,')
                    page.locator('.rlql-hero').screenshot(path=str(args.out / f'header-{width}.png'), animations='disabled')
                    measurements.append({'viewport': width, 'image_width': box['width'], 'image_height': box['height'], 'title_bottom': title['y']+title['height'], 'image_top': box['y'], 'image_bottom': box['y']+box['height'], 'lede_top': lede['y']})
                    page.close()
                checks.append('Illustration is immediately below the title, above the lede, at 320/390/768/1440px with no page overflow')
                page = browser.new_page(viewport={'width': 1280, 'height': 1000})
                page.goto(args.html.resolve().as_uri(), wait_until='load', timeout=60000)
                page.wait_for_function('window.QLearningPilot !== undefined')
                assert page.locator('.highlight pre').count() == 7
                page.locator('[data-guided-chapter="bootstrap"]').click()
                assert page.locator('[data-current-q]').inner_text() == '0.0095'
                assert page.evaluate('window.QLearningPilot.policy().episodes') == 0
                page.locator('[data-policy-train]').click()
                page.wait_for_function('window.QLearningPilot.policy().episodes===500')
                assert page.evaluate('window.QLearningPilot.policy().goals') == 267
                page.wait_for_function('!document.querySelector("[data-policy-replay]").disabled')
                before = page.evaluate('window.QLearningPilot.policy()')
                page.locator('[data-policy-replay]').click()
                page.wait_for_function('document.querySelector("[data-policy-status]").textContent.includes("Goal reached in 6 moves")')
                assert page.evaluate('window.QLearningPilot.policy()') == before
                page.locator('[data-native-demo]').scroll_into_view_if_needed()
                page.wait_for_function('document.querySelector("[data-native-image]").src.startsWith("data:image/gif;")')
                assert page.locator('[data-native-play]').get_attribute('aria-pressed') == 'true'
                page.locator('[data-native-play]').click()
                assert page.locator('[data-native-image]').get_attribute('src').startswith('data:image/png;')
                page.close()
                reduced = browser.new_page(viewport={'width': 1280, 'height': 1000}, reduced_motion='reduce')
                reduced.goto(args.html.resolve().as_uri(), wait_until='load', timeout=60000)
                reduced.wait_for_function('window.QLearningPilot !== undefined')
                reduced.locator('[data-native-demo]').scroll_into_view_if_needed(); reduced.wait_for_timeout(400)
                assert reduced.locator('[data-native-image]').get_attribute('src').startswith('data:image/png;')
                reduced.close()
                checks.append('Approved code, exploratory lesson and independent training/replay remain intact; the native agent GIF autoplays in view, pauses on request, and stays still for reduced motion')
                nojs = browser.new_page(viewport={'width': 390, 'height': 1000}, java_script_enabled=False)
                nojs.goto(args.html.resolve().as_uri(), wait_until='load', timeout=60000)
                assert nojs.locator('.rlql-title-figure img').evaluate('(el)=>el.complete&&el.naturalWidth>0')
                assert nojs.locator('[data-native-demo] noscript a').is_visible()
                nojs.close()
                checks.append('Title illustration and the existing static fallbacks work without JavaScript')
                assert not errors, errors
            finally:
                browser.close()
        report = {'checks_passed': len(checks), 'checks': checks, 'viewports': measurements, 'illustrated_update': update, 'image_source': 'original SVG diagram, not a generated route or benchmark result', 'full_jekyll_build_verified': False}
        (args.out / 'title-image-verification.json').write_text(json.dumps(report, indent=2))
        run.log({'header/checks_passed': len(checks), 'header/png_width': 2400, 'header/png_height': 840})
        print(json.dumps(report, indent=2))
    finally:
        run.finish()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--html', type=Path, required=True)
    parser.add_argument('--browser', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    verify(parser.parse_args())
