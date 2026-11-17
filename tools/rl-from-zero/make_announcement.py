#!/usr/bin/env python3
"""Render the RL From Zero announcement animation from the repository's agent GIFs.

The camera starts on one trained agent (A3C landing in LunarLander), pulls back
while the other algorithms fade in as tiles, holds on the full grid, and (in the
looping cut) returns to the close-up as that landing finishes, so the loop
restarts exactly like an episode reset. Every tile is one of
the repository's committed demo GIFs; the only edits are cropping caption bands
and empty margins, and scaling into the tile.

Outputs: a looping GIF and MP4 for the blog, a LinkedIn MP4 that ends on the
full grid, a still poster, and a provenance JSON. With --platform-dir it also
writes a copy of the GIF loop that starts on the full grid (for Medium and
Substack, where emails and previews often show only the first frame).
"""
import argparse
import bisect
import hashlib
import json
import math
import multiprocessing as mp
import os
import pathlib
import subprocess
import tempfile

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageSequence

DESIGN_W, DESIGN_H = 1280, 720
WHITE, INK, MUTED, ACCENT, RULE, TILE_BG = (255, 255, 255), (29, 39, 51), (86, 97, 110), (35, 86, 168), (213, 219, 226), (246, 247, 249)
CAPTION_BAND = (17, 24, 39)

# Grid order, rows of 4, 5 and 4: value-based methods on top (starting with
# Q-learning, where the series starts), policy-gradient and actor-critic methods
# in the middle around the A3C close-up, then deterministic and multi-agent ones.
TILES = [
    ('Qlearning', 'Qlearning/assets/qlearning_frozenlake_8x8.gif', 'Q-learning', 'FrozenLake 8\u00d78'),
    ('Independent-QL', 'Independent-QL/assets/independent_ql_lineworld.gif', 'Independent QL', 'LineWorld'),
    ('Nash-QL', 'Nash-QL/assets/nash_ql_grid_soccer.gif', 'Nash Q-learning', 'Grid Soccer'),
    ('deepQN', 'deepQN/assets/dqn_mountaincar.gif', 'DQN', 'MountainCar'),
    ('PPO', 'PPO/assets/ppo_cartpole.gif', 'PPO', 'CartPole'),
    ('TRPO', 'TRPO/assets/trpo_acrobot.gif', 'TRPO', 'Acrobot'),
    ('A3C', 'A3C/assets/a3c_lunarlander.gif', 'A3C', 'LunarLander'),
    ('SAC', 'SAC/assets/sac_pendulum.gif', 'SAC', 'Pendulum'),
    ('IQL', 'IQL/assets/iql_pendulum.gif', 'IQL (offline)', 'Pendulum'),
    ('DDPG', 'DDPG/assets/ddpg_lunarlander.gif', 'DDPG', 'LunarLander'),
    ('TD3', 'TD3/assets/td3_mountaincar_continuous.gif', 'TD3', 'MountainCar'),
    ('MAPPO', 'MAPPO/assets/mappo_full_delivery.gif', 'MAPPO', 'MultiWalker'),
    ('MADDPG', 'MADDPG/assets/maddpg_simple_spread.gif', 'MADDPG', 'Simple Spread'),
]
ROWS = (4, 5, 4)
HERO = 'A3C'  # the close-up
HERO_SEGMENT_MS = (0, 8880)  # its first complete landing; the next episode starts at 8880 ms
SERIES_START = 'Qlearning'  # outlined in blue: the first post in the series
TILE_W, GAP_X, GAP_Y, LABEL_H, GRID_TOP = 220, 16, 14, 24, 152
TILE_H = round(TILE_W * 2 / 3)
TITLE = 'RL From Zero'
SUBTITLE = '13 reinforcement learning algorithms, built from scratch. Every tile is a trained agent.'
URL = 'alirezashamsoshoara.github.io/blog/rl-from-zero'
CLOSE_UP_FRACTION = 0.78  # share of the frame height used by the close-up tile and its label
TIMELINES = {
    'loop': [('close', 1.0), ('out', 2.0), ('full', 3.9), ('in', 1.5), ('close', 0.5)],
    'linkedin': [('close', 1.0), ('out', 2.0), ('full', 9.0)],
}

STATE = {}


def smootherstep(u):
    u = min(1.0, max(0.0, u))
    return u * u * u * (u * (6 * u - 15) + 10)


def smoothstep(lo, hi, v):
    return smootherstep((v - lo) / (hi - lo))


def font_path(pattern):
    return subprocess.run(['fc-match', '-f', '%{file}', pattern], capture_output=True, text=True, check=True).stdout


class Source:
    """Frames of one repository GIF, cropped to its content, with timing."""

    def __init__(self, path, needed_seconds):
        image = Image.open(path)
        frames, starts, elapsed, complete = [], [], 0, True
        for frame in ImageSequence.Iterator(image):
            if elapsed > (needed_seconds + 1) * 1000:
                complete = False
                break
            frames.append(frame.convert('RGB').copy())
            starts.append(elapsed)
            elapsed += frame.info.get('duration') or 100
        self.period_ms = elapsed if complete else None
        self.duration_ms = elapsed
        band = 0
        while band < frames[0].height // 3 and frames[0].getpixel((1, band)) == CAPTION_BAND:
            band += 1
        self.caption_band_px = band
        frames = [f.crop((0, band, f.width, f.height)) for f in frames]
        self.window = content_window(frames)
        self.frames = [f.crop(self.window) for f in frames]
        self.starts = starts

    def frame_at(self, seconds):
        ms = seconds * 1000
        if self.period_ms:
            ms %= self.period_ms
        return self.frames[max(0, bisect.bisect_right(self.starts, ms) - 1)]


def content_window(frames, aspect=1.5):
    """Union bounding box of non-background pixels, padded, widened towards 3:2."""
    width, height = frames[0].size
    background = Image.new('RGB', (width, height), frames[0].getpixel((2, 2)))
    box = None
    for frame in frames[::max(1, len(frames) // 40)]:
        mask = ImageChops.difference(frame, background).convert('L').point(lambda v: 255 if v > 24 else 0)
        found = mask.getbbox()
        if found:
            box = found if box is None else (min(box[0], found[0]), min(box[1], found[1]), max(box[2], found[2]), max(box[3], found[3]))
    if box is None:
        return (0, 0, width, height)
    pad = 0.06 * max(width, height)
    x0, y0, x1, y1 = box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad
    cx, cy, bw, bh = (x0 + x1) / 2, (y0 + y1) / 2, x1 - x0, y1 - y0
    w = max(bw, bh * aspect)
    h = w / aspect
    if w > width:
        w, h = width, max(bh, width / aspect)
    if h > height:
        h, w = height, min(width, max(bw, height * aspect))
    x0 = min(max(0, cx - w / 2), width - w)
    y0 = min(max(0, cy - h / 2), height - h)
    return (round(x0), round(y0), round(x0 + w), round(y0 + h))


def layout():
    rects, index = {}, 0
    for row, count in enumerate(ROWS):
        x0 = (DESIGN_W - (count * TILE_W + (count - 1) * GAP_X)) / 2
        y = GRID_TOP + row * (TILE_H + LABEL_H + GAP_Y)
        for col in range(count):
            rects[TILES[index][0]] = (x0 + col * (TILE_W + GAP_X), y, TILE_W, TILE_H)
            index += 1
    return rects


def draw_static(rects, k):
    """High-resolution static layers: the close-up tile on white, everything else on an overlay."""
    serif_bold, sans, sans_bold = font_path('Liberation Serif:style=Bold'), font_path('Liberation Sans'), font_path('Liberation Sans:style=Bold')
    base = Image.new('RGB', (DESIGN_W * k, DESIGN_H * k), WHITE)
    overlay = Image.new('RGBA', (DESIGN_W * k, DESIGN_H * k), (0, 0, 0, 0))
    for folder, _, name, environment in TILES:
        hero = folder == HERO
        draw = ImageDraw.Draw(base if hero else overlay)
        x, y, w, h = rects[folder]
        start = folder == SERIES_START
        draw.rectangle([x * k, y * k, (x + w) * k - 1, (y + h) * k - 1], fill=TILE_BG + (255,), outline=(ACCENT if start else RULE) + (255,), width=(2 if start else 1) * k)
        for size in (13, 12.5, 12, 11.5, 11):
            bold, regular = ImageFont.truetype(sans_bold, round(size * k)), ImageFont.truetype(sans, round(size * k))
            gap = 5 * k
            if bold.getlength(name) + gap + regular.getlength(environment) <= w * k:
                break
        baseline = (y + h + 17) * k
        draw.text((x * k, baseline), name, font=bold, fill=INK + (255,), anchor='ls')
        draw.text((x * k + bold.getlength(name) + gap, baseline), environment, font=regular, fill=MUTED + (255,), anchor='ls')
    draw = ImageDraw.Draw(overlay)
    draw.text((58 * k, 82 * k), TITLE, font=ImageFont.truetype(serif_bold, 46 * k), fill=INK + (255,), anchor='ls')
    draw.text((58 * k, 114 * k), SUBTITLE, font=ImageFont.truetype(sans, 17 * k), fill=MUTED + (255,), anchor='ls')
    draw.text((1222 * k, 82 * k), URL, font=ImageFont.truetype(sans, 16 * k), fill=ACCENT + (255,), anchor='rs')
    draw.rectangle([58 * k, 132 * k, 1222 * k, 133 * k - 1], fill=RULE + (255,))
    return base, overlay


def close_up_scale(rects):
    hero = rects[HERO]
    return CLOSE_UP_FRACTION * DESIGN_H / (hero[3] + LABEL_H)


def camera(t, timeline, rects):
    """Camera centre and scale in design units, and reveal progress (0 close-up, 1 full grid)."""
    hero = rects[HERO]
    s1, c1 = close_up_scale(rects), (hero[0] + hero[2] / 2, hero[1] + (hero[3] + LABEL_H) / 2)
    s0, c0 = 1.0, (DESIGN_W / 2, DESIGN_H / 2)
    p, start = None, 0.0
    for kind, length in timeline:
        if t < start + length:
            u = (t - start) / length
            p = {'close': 0.0, 'full': 1.0, 'out': smootherstep(u), 'in': 1 - smootherstep(u)}[kind]
            break
        start += length
    if p is None:
        p = {'close': 0.0, 'full': 1.0, 'out': 1.0, 'in': 0.0}[timeline[-1][0]]
    s = math.exp(math.log(s1) + (math.log(s0) - math.log(s1)) * p)
    reveal = (1 / s - 1 / s1) / (1 / s0 - 1 / s1)
    return c1[0] + (c0[0] - c1[0]) * reveal, c1[1] + (c0[1] - c1[1]) * reveal, s, reveal


def render_frame(index):
    st = STATE
    t = index / st['fps']
    cx, cy, s, reveal = camera(t, st['timeline'], st['rects'])
    width, height, k = st['width'], st['height'], st['k']
    s_out = s * width / DESIGN_W
    half_w, half_h = width / (2 * s_out), height / (2 * s_out)
    box = ((cx - half_w) * k, (cy - half_h) * k, (cx + half_w) * k, (cy + half_h) * k)
    frame = st['base'].resize((width, height), Image.LANCZOS, box=box, reducing_gap=3.0)
    alpha = smoothstep(0.12, 0.65, reveal)
    if alpha > 0.002:
        overlay = st['overlay'].resize((width, height), Image.LANCZOS, box=box, reducing_gap=3.0)
        if alpha < 0.998:
            overlay.putalpha(overlay.getchannel('A').point(lambda v: round(v * alpha)))
        frame.paste(overlay, (0, 0), overlay)
    for folder, source in st['sources'].items():
        hero = folder == HERO
        if not hero and alpha <= 0.002:
            continue
        x, y, w, h = st['rects'][folder]
        inset = 2 if folder == SERIES_START else 1
        x0, y0 = (x + inset - cx) * s_out + width / 2, (y + inset - cy) * s_out + height / 2
        x1, y1 = (x + w - inset - cx) * s_out + width / 2, (y + h - inset - cy) * s_out + height / 2
        if x1 < 0 or y1 < 0 or x0 > width or y0 > height:
            continue
        if hero:
            start_s, length_s = HERO_SEGMENT_MS[0] / 1000, (HERO_SEGMENT_MS[1] - HERO_SEGMENT_MS[0]) / 1000
            local = t * st['hero_stretch']
            image = source.frame_at(start_s + (local % length_s if st['hero_wrap'] else local))
        else:
            image = source.frame_at(t)
        fit = min((x1 - x0) / image.width, (y1 - y0) / image.height)
        size = (max(1, round(image.width * fit)), max(1, round(image.height * fit)))
        position = (round(x0 + (x1 - x0 - size[0]) / 2), round(y0 + (y1 - y0 - size[1]) / 2))
        tile = image.resize(size, Image.LANCZOS)
        if hero or alpha >= 0.998:
            frame.paste(tile, position)
        else:
            frame.paste(tile, position, Image.new('L', size, round(255 * alpha)))
    return frame.tobytes()


def render(sources, rects, timeline, width, height, fps, workers, hero_stretch, hero_wrap=False):
    seconds = sum(length for _, length in timeline)
    frames = round(seconds * fps)
    assert abs(frames - seconds * fps) < 1e-6, 'Timeline must be a whole number of frames'
    k = math.ceil(close_up_scale(rects) * width / DESIGN_W * 1.02)
    base, overlay = draw_static(rects, k)
    STATE.update(sources=sources, rects=rects, timeline=timeline, width=width, height=height, fps=fps, k=k, base=base, overlay=overlay, hero_stretch=hero_stretch, hero_wrap=hero_wrap)
    with mp.get_context('fork').Pool(workers) as pool:
        for data in pool.imap(render_frame, range(frames), chunksize=4):
            yield data


def encode_mp4(frames, width, height, fps, path):
    command = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{width}x{height}', '-r', str(fps), '-i', '-',
               '-vf', 'scale=out_range=tv:out_color_matrix=bt709,format=yuv420p', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18',
               '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-movflags', '+faststart', str(path)]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    count = 0
    for data in frames:
        process.stdin.write(data)
        count += 1
    process.stdin.close()
    if process.wait():
        raise RuntimeError(f'ffmpeg failed for {path}')
    return count


def encode_gif(frames, width, height, fps, path, colors, rotated=None):
    """Write the GIF; `rotated=(start_frame, gif_path, png_path)` also writes the same loop starting at start_frame."""
    graph = (f'split[a][b];[a]palettegen=max_colors={colors}:stats_mode=diff[p];'
             '[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle')
    with tempfile.TemporaryDirectory() as tmp:
        count = 0
        for count, data in enumerate(frames, 1):
            Image.frombytes('RGB', (width, height), data).save(f'{tmp}/f{count:04d}.png', compress_level=1)
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-framerate', str(fps), '-i', f'{tmp}/f%04d.png', '-lavfi', graph, '-loop', '0', str(path)], check=True)
        if rotated:
            start, rotated_gif, rotated_png = rotated
            os.mkdir(f'{tmp}/rotated')
            for j in range(count):
                os.symlink(f'{tmp}/f{(j + start) % count + 1:04d}.png', f'{tmp}/rotated/f{j + 1:04d}.png')
            subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-framerate', str(fps), '-i', f'{tmp}/rotated/f%04d.png', '-lavfi', graph, '-loop', '0', str(rotated_gif)], check=True)
            Image.open(f'{tmp}/rotated/f0001.png').save(rotated_png, optimize=True)
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-repo', type=pathlib.Path, required=True, help='RL-from-zero checkout (or a copy of its assets)')
    parser.add_argument('--source-revision', required=True)
    parser.add_argument('--out-dir', type=pathlib.Path, required=True, help='Blog media folder')
    parser.add_argument('--extra-dir', type=pathlib.Path, required=True, help='Folder for the LinkedIn cut, kept out of the repository')
    parser.add_argument('--platform-dir', type=pathlib.Path, help='Also write the grid-first GIF and its first frame here (Medium and Substack)')
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--gif-width', type=int, default=960)
    parser.add_argument('--gif-fps', type=int, default=20)
    parser.add_argument('--gif-colors', type=int, default=256)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    args.extra_dir.mkdir(parents=True, exist_ok=True)

    import wandb
    run = wandb.init(project='rl-education', name='rl-from-zero-announcement', mode='offline', dir=str(args.extra_dir))
    try:
        needed = max(sum(length for _, length in timeline) for timeline in TIMELINES.values())
        sources = {folder: Source(args.source_repo / gif, needed) for folder, gif, _, _ in TILES}
        loop_seconds = sum(length for _, length in TIMELINES['loop'])
        hero_stretch = (HERO_SEGMENT_MS[1] - HERO_SEGMENT_MS[0]) / 1000 / loop_seconds  # one complete landing per loop
        rects = layout()
        outputs = {}
        name = 'rl-from-zero-announcement'
        width, height = 1920, 1080
        outputs['loop_mp4'] = {'file': f'{name}.mp4', 'frames': encode_mp4(render(sources, rects, TIMELINES['loop'], width, height, 30, args.workers, hero_stretch, True), width, height, 30, args.out_dir / f'{name}.mp4'), 'fps': 30, 'size': [width, height]}
        outputs['linkedin_mp4'] = {'file': f'{name}-linkedin.mp4', 'frames': encode_mp4(render(sources, rects, TIMELINES['linkedin'], width, height, 30, args.workers, 1.0), width, height, 30, args.extra_dir / f'{name}-linkedin.mp4'), 'fps': 30, 'size': [width, height]}
        gif_w, gif_h = args.gif_width, args.gif_width * 9 // 16
        rotated = None
        if args.platform_dir:
            args.platform_dir.mkdir(parents=True, exist_ok=True)
            kinds = [kind for kind, _ in TIMELINES['loop']]
            full_start = round(sum(length for _, length in TIMELINES['loop'][:kinds.index('full')]) * args.gif_fps)
            rotated = (full_start, args.platform_dir / f'{name}-grid-first.gif', args.platform_dir / f'{name}-grid-first.png')
        outputs['loop_gif'] = {'file': f'{name}.gif', 'frames': encode_gif(render(sources, rects, TIMELINES['loop'], gif_w, gif_h, args.gif_fps, args.workers, hero_stretch, True), gif_w, gif_h, args.gif_fps, args.out_dir / f'{name}.gif', args.gif_colors, rotated), 'fps': args.gif_fps, 'size': [gif_w, gif_h]}
        if rotated:
            outputs['platform_gif'] = {'file': rotated[1].name, 'frames': outputs['loop_gif']['frames'], 'fps': args.gif_fps, 'size': [gif_w, gif_h], 'starts_at_frame': rotated[0], 'note': 'same loop, first frame is the full grid'}
            outputs['platform_still'] = {'file': rotated[2].name, 'size': [gif_w, gif_h], 'note': 'first frame of the grid-first GIF'}
        poster = list(render(sources, rects, [('full', 6.0)], width, height, 1, 1, 1.0))[-1]  # full grid, 5 s in, mid-motion
        Image.frombytes('RGB', (width, height), poster).save(args.out_dir / f'{name}.png', optimize=True)
        outputs['poster'] = {'file': f'{name}.png', 'size': [width, height]}
        for key, item in outputs.items():
            folder = args.extra_dir if key == 'linkedin_mp4' else args.platform_dir if key.startswith('platform_') else args.out_dir
            item['bytes'] = (folder / item['file']).stat().st_size
        provenance = {
            'kind': 'announcement animation composed from the RL-from-zero repository demo GIFs; no generated or retouched agent footage',
            'source_repository': 'https://github.com/AlirezaShamsoshoara/RL-from-zero',
            'source_revision': args.source_revision,
            'tiles': [{'folder': folder, 'gif': gif, 'label': f'{label} \u00b7 {environment}', 'sha256': hashlib.sha256((args.source_repo / gif).read_bytes()).hexdigest(),
                       'caption_band_cropped_px': sources[folder].caption_band_px, 'content_window': sources[folder].window,
                       'source_duration_ms': sources[folder].duration_ms, 'loops_within_cut': bool(sources[folder].period_ms)} for folder, gif, label, environment in TILES],
            'timelines_seconds': TIMELINES,
            'close_up': HERO,
            'close_up_segment_ms': HERO_SEGMENT_MS,
            'close_up_time_stretch_in_loop': hero_stretch,
            'series_start_outlined': SERIES_START,
            'outputs': outputs,
        }
        (args.out_dir / f'{name}.json').write_text(json.dumps(provenance, indent=2))
        run.log({f'{key}/bytes': item['bytes'] for key, item in outputs.items()})
        print(json.dumps(outputs, indent=2))
    finally:
        run.finish()


if __name__ == '__main__':
    main()
