#!/usr/bin/env python3
"""Stills and a short clip for the DQN post's Medium and Substack drafts, from the rendered figures.

Writes into the platform drafts' media folder:
  first-update.gif  update 1 of the run, opening on its gradient step, then collect, look ahead, target, error and step
  first-update.png  the gradient step at its natural height and 2x, for email clients that show a still
  target-sync.png   Figure 2 (minibatch averages) at 2x
  exploration.png   Figure 3 (holds of 20 to 60 steps, seed 7) at 2x
  manifest.json     sources, sizes, hashes, timings and what each file does not show

Usage: make_platform_media.py --site <built preview> --out <media dir> --browser <chrome>
"""
import argparse
import functools
import hashlib
import http.server
import io
import json
import pathlib
import sys
import threading

from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from export_media import write_gif  # noqa: E402

# The Sample phase's table makes it the tallest frame; leaving it out keeps the shared frame height close to every phase's own.
PHASES = [(5, 3200), (0, 2600), (2, 3200), (3, 3000), (4, 3200), (5, 4400)]
NOTE = 'Update 1 of 70,001 from the training run, recorded, shown step by step.'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--site', type=pathlib.Path, required=True)
    p.add_argument('--out', type=pathlib.Path, required=True)
    p.add_argument('--browser', required=True)
    p.add_argument('--url', default='/blog/rl-from-zero/dqn/')
    a = p.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    handler = type('Quiet', (http.server.SimpleHTTPRequestHandler,), {'log_message': lambda *x: None})
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(handler, directory=str(a.site)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=a.browser)
            page = browser.new_page(viewport={'width': 1280, 'height': 1000}, device_scale_factor=2)
            errors = []
            page.on('pageerror', lambda e: errors.append(str(e)))
            page.goto(f'http://127.0.0.1:{server.server_port}{a.url}', wait_until='networkidle')
            page.wait_for_function('document.documentElement.dataset.dqnReady === "true"', timeout=30000)
            update = page.locator('[data-dqn-update]')
            page.evaluate('([p, n]) => window.DQNPilot.update.exportFrame(0, p, null, n)', [5, NOTE])
            update.screenshot(path=str(a.out / 'first-update.png'), animations='disabled')
            tallest = 0
            for phase, _ in PHASES:
                page.evaluate('([p, n]) => window.DQNPilot.update.exportFrame(0, p, null, n)', [phase, NOTE])
                tallest = max(tallest, update.bounding_box()['height'])
            update.evaluate('(el, h) => { el.style.height = h + "px"; }', int(tallest) + 2)
            frames = []
            for phase, _ in PHASES:
                page.evaluate('([p, n]) => window.DQNPilot.update.exportFrame(0, p, null, n)', [phase, NOTE])
                frames.append(Image.open(io.BytesIO(update.screenshot(animations='disabled'))).convert('RGB'))
            update.evaluate('el => { el.style.height = ""; }')
            write_gif(frames, [ms for _, ms in PHASES], a.out / 'first-update.gif')
            for selector, name in (('[data-dqn-target]', 'target-sync.png'), ('[data-dqn-explore]', 'exploration.png')):
                root = page.locator(selector)
                root.evaluate('el => { el.dataset.exportMode = "true"; }')
                root.screenshot(path=str(a.out / name), animations='disabled')
            assert not errors, errors
            browser.close()
    finally:
        server.shutdown()
    gif = Image.open(a.out / 'first-update.gif')
    manifest = {
        'what': 'Media for the Medium and Substack versions of RL From Zero Part 2 (DQN), captured at device scale factor 2 from the post\u2019s own figures.',
        'files': {
            'first-update.gif': {'bytes': (a.out / 'first-update.gif').stat().st_size, 'sha256': sha(a.out / 'first-update.gif'), 'size': list(gif.size), 'frames': gif.n_frames,
                                 'duration_ms': sum(ms for _, ms in PHASES), 'source': 'Figure 1, update 1 of the recorded run: the gradient step first, then collect, look ahead, target, error and step',
                                 'interpretation': 'One recorded update, not an animation of training. The first frame is the gradient step, so a still copy makes sense alone.'},
            'first-update.png': {'bytes': (a.out / 'first-update.png').stat().st_size, 'sha256': sha(a.out / 'first-update.png'), 'size': list(Image.open(a.out / 'first-update.png').size), 'source': 'the gradient step (the GIF\u2019s first frame) at its natural height and 2x'},
            'target-sync.png': {'bytes': (a.out / 'target-sync.png').stat().st_size, 'sha256': sha(a.out / 'target-sync.png'), 'size': list(Image.open(a.out / 'target-sync.png').size),
                                'source': 'Figure 2, minibatch averages over the first 1,500 recorded updates'},
            'exploration.png': {'bytes': (a.out / 'exploration.png').stat().st_size, 'sha256': sha(a.out / 'exploration.png'), 'size': list(Image.open(a.out / 'exploration.png').size),
                                'source': 'Figure 3, holds of 20 to 60 steps, seed 7, computed in the browser with the MountainCar equations',
                                'interpretation': 'Random exploration only, not the training run; counts depend on the seed.'},
        },
        'also_used': {'title image': 'assets/media/rl/dqn/dqn-hero.png', 'training clip': 'assets/media/rl/dqn/dqn-training.gif (and .png, its first frame)',
                      'real agent': 'assets/media/rl/dqn/mountaincar-dqn.gif (and .png)'},
    }
    (a.out / 'manifest.json').write_text(json.dumps(manifest, indent=1) + '\n')
    print(json.dumps({k: (v.get('bytes'), v.get('size')) for k, v in manifest['files'].items()}))


if __name__ == '__main__':
    main()
