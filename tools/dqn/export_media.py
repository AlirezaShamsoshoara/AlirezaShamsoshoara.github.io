#!/usr/bin/env python3
"""Export portable media for the DQN post from its rendered figures.

Captures Figure 1 (selected recorded updates, phase by phase) and Figure 4 (the saved
checkpoints in order) at device scale factor 2 from a built preview, then writes:
  dqn-update.png            2x lossless poster (update 1, the gradient step)
  dqn-update.gif/.webm/.mp4  edited highlights of five recorded updates
  dqn-training.png          2x poster (selected checkpoint)
  dqn-training.gif/.webm/.mp4 the value map checkpoint by checkpoint, then one greedy drive
  dqn-update.json, dqn-training.json  what each file is, its inputs, sizes and timings
The videos are encoded at 50 fps from the same lossless frames with the same durations as the GIF.
The GIFs use per-frame palettes that keep the article's accent colors exact.

Usage: export_media.py --site <preview dir> --out <dir> --browser <chrome> [--url /blog/rl-from-zero/dqn/]
"""
import argparse
import functools
import hashlib
import http.server
import io
import json
import pathlib
import subprocess
import threading

from PIL import Image
from playwright.sync_api import sync_playwright

UPDATE_SCHEDULE = [  # (index in dqn-update-steps.json, phase 0..5, hold ms)
    (0, 0, 2600), (0, 1, 2800), (0, 2, 3200), (0, 3, 3000), (0, 4, 3200), (0, 5, 4400),
    (1, 1, 2800), (1, 3, 3400), (1, 5, 3000),
    (2, 2, 3200), (2, 3, 3200), (2, 4, 3400),
    (3, 0, 3200), (3, 1, 3400),
    (4, 5, 3800),
]
LONG_HOLDS = {5000: 2200, 90000: 2600, 110000: 2600, 251392: 2400}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def even(image):
    w, h = image.size
    if w % 2 or h % 2:
        canvas = Image.new('RGB', (w + w % 2, h + h % 2), 'white')
        canvas.paste(image, (0, 0))
        return canvas
    return image


ACCENTS = [(255, 255, 255), (29, 39, 51), (86, 97, 110), (65, 77, 90), (35, 86, 168), (57, 117, 77), (153, 100, 24), (213, 219, 226),
           (183, 193, 204), (234, 237, 241), (238, 243, 251), (111, 74, 16), (47, 101, 69), (23, 63, 120), (125, 147, 178), (141, 153, 166)]


def quantize(frame):
    """Adaptive palette for the frame, with the article's accent colors reserved exactly."""
    adaptive = frame.quantize(colors=256 - len(ACCENTS), method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).getpalette()[: (256 - len(ACCENTS)) * 3]
    palette = [c for rgb in ACCENTS for c in rgb] + adaptive
    holder = Image.new('P', (1, 1))
    holder.putpalette(palette + [0] * (768 - len(palette)))
    return frame.quantize(palette=holder, dither=Image.Dither.NONE)


def write_gif(frames, durations, path, scale=0.5):
    small = [f.resize((round(f.width * scale), round(f.height * scale)), Image.LANCZOS) for f in frames]
    paletted = [quantize(f) for f in small]
    paletted[0].save(path, save_all=True, append_images=paletted[1:], duration=durations, loop=0, optimize=False, disposal=1)


def write_videos(frames, durations, stem, workdir, fps=50):
    """Encode from a 30 fps image sequence: each still is linked for exactly its hold."""
    workdir.mkdir(parents=True, exist_ok=True)
    count = 0
    for i, (frame, ms) in enumerate(zip(frames, durations)):
        assert ms * fps % 1000 == 0, f'hold {ms} ms is not a whole number of frames'
        still = workdir / f'still-{i:04d}.png'
        even(frame).save(still)
        for _ in range(ms * fps // 1000):
            (workdir / f'seq-{count:06d}.png').symlink_to(still.name)
            count += 1
    source = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-framerate', str(fps), '-i', str(workdir / 'seq-%06d.png')]
    color = ['-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-map_metadata', '-1']
    scale = ['-vf', 'scale=out_range=tv:out_color_matrix=bt709,format=yuv420p']
    subprocess.run(source + scale + ['-c:v', 'libx264', '-preset', 'slow', '-crf', '18', *color, '-movflags', '+faststart', f'{stem}.mp4'], check=True)
    subprocess.run(source + scale + ['-c:v', 'libvpx-vp9', '-b:v', '0', '-crf', '30', '-row-mt', '1', *color, f'{stem}.webm'], check=True)
    return count


def probe(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=codec_name,width,height,pix_fmt,color_range,color_space:format=duration',
                          '-of', 'json', str(path)], capture_output=True, text=True, check=True).stdout
    data = json.loads(out)
    stream = data['streams'][0]
    return {'codec': stream['codec_name'], 'size': [stream['width'], stream['height']], 'pix_fmt': stream['pix_fmt'], 'color_range': stream.get('color_range'),
            'color_space': stream.get('color_space'), 'duration_s': round(float(data['format']['duration']), 3)}


def describe(path, extra):
    return {'path': f'assets/media/rl/dqn/{path.name}', 'bytes': path.stat().st_size, 'sha256': sha(path), **extra}


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
            meta = page.evaluate('window.DQNPilot.update.updates')
            total_updates, total_steps = 70001, 300000
            update = page.locator('[data-dqn-update]')
            note = 'Edited highlights: 5 of 70,001 recorded updates from the training run, shown phase by phase.'
            # Natural-height poster first.
            page.evaluate('([i, p, n]) => window.DQNPilot.update.exportFrame(i, p, null, n)', [0, 5, note])
            poster = Image.open(io.BytesIO(update.screenshot(animations='disabled'))).convert('RGB')
            poster.save(a.out / 'dqn-update.png', optimize=True)
            # Fixed height for the animation so frames share one canvas.
            tallest = 0
            for i, phase, _ in UPDATE_SCHEDULE:
                page.evaluate('([i, p, n]) => window.DQNPilot.update.exportFrame(i, p, null, n)', [i, phase, note])
                tallest = max(tallest, update.bounding_box()['height'])
            update.evaluate('(el, h) => { el.style.height = h + "px"; }', int(tallest) + 2)
            frames, durations, schedule = [], [], []
            for i, phase, ms in UPDATE_SCHEDULE:
                page.evaluate('([i, p, n]) => window.DQNPilot.update.exportFrame(i, p, null, n)', [i, phase, note])
                frames.append(Image.open(io.BytesIO(update.screenshot(animations='disabled'))).convert('RGB'))
                durations.append(ms)
                schedule.append({'update': meta[i]['number'], 'step': meta[i]['step'], 'phase': phase + 1, 'hold_ms': ms})
            update.evaluate('el => { el.style.height = ""; }')
            write_gif(frames, durations, a.out / 'dqn-update.gif')
            write_videos(frames, durations, str(a.out / 'dqn-update'), a.out / 'frames-update')
            # Figure 4: checkpoints in order, then one greedy drive at the selected checkpoint.
            training = page.locator('[data-dqn-training]')
            cps = page.evaluate('window.DQNPilot.training.checkpoints')
            best = next(i for i, c in enumerate(cps) if c['name'] == 'best.pt')
            # Open on the trained map, so a still first frame (email clients) already shows the result.
            page.evaluate('([i]) => window.DQNPilot.training.exportFrame(i, 5)', [best])
            frames2 = [Image.open(io.BytesIO(training.screenshot(animations='disabled'))).convert('RGB')]
            durations2 = [2400]
            for index, c in enumerate(cps):
                page.evaluate('([i]) => window.DQNPilot.training.exportFrame(i, 5)', [index])
                frames2.append(Image.open(io.BytesIO(training.screenshot(animations='disabled'))).convert('RGB'))
                durations2.append(LONG_HOLDS.get(c['step'], 700))
            page.evaluate('([i]) => window.DQNPilot.training.exportFrame(i, 5)', [best])
            poster2 = Image.open(io.BytesIO(training.screenshot(animations='disabled'))).convert('RGB')
            poster2.save(a.out / 'dqn-training.png', optimize=True)
            drive = page.evaluate('([i]) => window.DQNPilot.training.rolloutPositions(i, 5)', [best])
            for k in range(len(drive)):  # every physics step, 25 steps per second
                page.evaluate('([i, x]) => window.DQNPilot.training.exportFrame(i, 5, x)', [best, drive[k]])
                frames2.append(Image.open(io.BytesIO(training.screenshot(animations='disabled'))).convert('RGB'))
                durations2.append(40)
            page.evaluate('([i, x]) => window.DQNPilot.training.exportFrame(i, 5, x)', [best, drive[-1]])
            frames2.append(Image.open(io.BytesIO(training.screenshot(animations='disabled'))).convert('RGB'))
            durations2.append(2400)
            sizes = {f.size for f in frames2}
            assert len(sizes) == 1, f'training frames must share one size, got {sizes}'
            write_gif(frames2, durations2, a.out / 'dqn-training.gif')
            write_videos(frames2, durations2, str(a.out / 'dqn-training'), a.out / 'frames-training')
            assert not errors, errors
            browser.close()
    finally:
        server.shutdown()

    for stem, frames_, durations_, extra in (
        ('dqn-update', frames, durations, {'schedule': schedule, 'what': 'Figure 1 of the DQN post, five recorded updates shown phase by phase.',
                                           'interpretation': 'Edited highlights of 5 of 70,001 recorded gradient updates. Every value comes from the training run; omitted updates are in the recording, not simulated.'}),
        ('dqn-training', frames2, durations2, {'what': 'Figure 4 of the DQN post: the selected checkpoint first, then the saved checkpoints in order, then one greedy drive at the selected checkpoint from position -0.5.',
                                               'interpretation': 'Checkpoints every 10,000 steps plus the first and the selected one. A greedy drive from one start is a demonstration, not an evaluation statistic.'})):
        gif, webm, mp4 = (a.out / f'{stem}.{ext}' for ext in ('gif', 'webm', 'mp4'))
        total = sum(durations_)
        info = {
            'what': extra['what'], 'interpretation': extra['interpretation'],
            'frames': len(frames_), 'duration_ms': total, 'capture': {'device_scale_factor': 2, 'viewport_css_px': [1280, 1000], 'frame_px': list(frames_[0].size)},
            'gif': describe(gif, {'size': list(Image.open(gif).size), 'scale_from_capture': 0.5}),
            'webm': describe(webm, probe(webm)), 'mp4': describe(mp4, probe(mp4)),
            'poster': describe(a.out / f'{stem}.png', {'size': list(Image.open(a.out / f'{stem}.png').size)}),
        }
        if 'schedule' in extra:
            info['schedule'] = extra['schedule']
        for kind in ('webm', 'mp4'):
            assert abs(info[kind]['duration_s'] * 1000 - total) <= 100, (kind, info[kind]['duration_s'], total)
        assert info['gif']['bytes'] < 25 * 1024 * 1024, 'GIF must stay under 25 MB for Medium'
        (a.out / f'{stem}.json').write_text(json.dumps(info, indent=1) + '\n')
        print(json.dumps({k: info[k] for k in ('frames', 'duration_ms')} | {k: (info[k]['bytes'], info[k].get('duration_s')) for k in ('gif', 'webm', 'mp4')}))


if __name__ == '__main__':
    main()
