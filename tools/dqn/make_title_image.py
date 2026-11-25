#!/usr/bin/env python3
"""Draw the DQN post's title image from one recorded update (update 1 of the run).

Left: Part 1's picture, one table cell. Middle: the Q-network with the update's real
inputs, outputs and target. Right: the change in every state's value after that one
gradient step, from the recorded weights. Writes an SVG and, with --png, a 2x PNG.

Usage: make_title_image.py --data <dqn-update-steps.json> --out <svg> [--png <png> --browser <chrome>]
"""
import argparse
import base64
import io
import json
import pathlib

import numpy as np
from PIL import Image

INK, MUTED, RULE, BLUE, OCHRE, GREEN = '#1d2733', '#56616e', '#d5dbe2', '#2356a8', '#996418', '#39754d'


def f(x, digits=4):
    text = f'{float(x):.{digits}g}'
    return text.replace('-', '\u2212')


def close_mask(mask):
    """3 by 3 closing, the same cleanup the figures apply to the visited region."""
    padded = np.pad(mask, 1, constant_values=False)
    dilated = np.zeros_like(mask)
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            dilated |= padded[1 + dr:1 + dr + mask.shape[0], 1 + dc:1 + dc + mask.shape[1]]
    padded = np.pad(dilated, 1, constant_values=True)
    closed = np.ones_like(mask)
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            closed &= padded[1 + dr:1 + dr + mask.shape[0], 1 + dc:1 + dc + mask.shape[1]]
    return closed


def delta_png(update, grid, first_visit):
    nx, ny = grid['nx'], grid['ny']
    delta = (np.frombuffer(base64.b64decode(update['grid']['delta']), '<i2').astype(float) / 32767 * update['grid']['delta_scale']).reshape(ny, nx)
    raw = (first_visit < update['step']).reshape(ny, nx)
    visited = delta[raw]
    least, most = float(-visited.max()), float(-visited.min())
    mask = close_mask(raw)
    t = 0.3 + 0.7 * np.clip((-delta - least) / (most - least), 0, 1)
    ochre = np.array([153, 100, 24], float)
    rgb = 255 + (ochre - 255) * t[..., None]
    rgb[~mask] = [234, 237, 241]
    image = Image.fromarray(np.flipud(rgb).astype(np.uint8), 'RGB').resize((nx * 8, ny * 8), Image.BICUBIC)
    buffer = io.BytesIO()
    image.save(buffer, 'PNG', optimize=True)
    return base64.b64encode(buffer.getvalue()).decode('ascii'), least, most


def build(data):
    update = next(u for u in data['updates'] if u['number'] == 1)
    grid = data['grid']
    first_visit = np.frombuffer(base64.b64decode(grid['first_visit']), '<i4')
    b, t = update['batch'], update['tracked']
    s, a, y = b['s'][t], b['a'][t], b['y'][t]
    q_before, q_after, q_target, star = b['q_before'][t], b['q_after'][t], b['q_next_target'][t], b['a_star'][t]
    png, least, most = delta_png(update, grid, first_visit)
    assert least > 0, 'this image assumes every visited value fell'
    out = []
    w = out.append
    w('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" '
      'aria-labelledby="dqn-hero-title dqn-hero-desc" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif">')
    w('<title id="dqn-hero-title">One recorded DQN update</title>')
    w(f'<desc id="dqn-hero-desc">A table cell from Part 1 next to a Q-network. The network reads one state, position {f(s[0])} and velocity {f(s[1])}. '
      f'Its value for pushing left moves from {f(q_before[a])} toward the target {f(y)}, and the same gradient step lowers the value of every visited state on the position and velocity map, by {f(least, 2)} to {f(most, 2)}.</desc>')
    w('<rect width="1200" height="420" fill="#ffffff"/>')
    arrow = lambda x1, x2, yy: w(f'<line x1="{x1}" y1="{yy}" x2="{x2 - 9}" y2="{yy}" stroke="{MUTED}" stroke-width="1.5"/><path d="M{x2 - 10},{yy - 6} L{x2},{yy} L{x2 - 10},{yy + 6} z" fill="{MUTED}"/>')
    # Panel A: Part 1's table, one cell.
    w(f'<text x="40" y="60" font-size="19" fill="{MUTED}">Part 1: a table</text>')
    x0, y0, cw, ch = 40, 120, 58, 32
    for r in range(5):
        for c in range(3):
            hit = (r, c) == (2, 2)
            w(f'<rect x="{x0 + c * cw}" y="{y0 + r * ch}" width="{cw}" height="{ch}" fill="{"#eef3fb" if hit else "#ffffff"}" stroke="{BLUE if hit else RULE}" stroke-width="{2 if hit else 1}"/>')
    w(f'<text x="{x0 + 2.5 * cw}" y="{y0 + 2 * ch + 21}" font-size="15" font-weight="700" fill="{BLUE}" text-anchor="middle">0.0095</text>')
    w(f'<text x="40" y="{y0 + 5 * ch + 32}" font-size="19" fill="{INK}">One update,</text>')
    w(f'<text x="40" y="{y0 + 5 * ch + 56}" font-size="19" fill="{INK}">one cell.</text>')
    arrow(224, 260, 200)
    # Panel B: the Q-network with update 1's numbers.
    w(f'<text x="276" y="60" font-size="19" fill="{MUTED}">Part 2: a Q-network, update 1 of the run</text>')
    inputs = [(300, 140, 'position', f(s[0])), (300, 262, 'velocity', f(s[1]))]
    hidden = [[(410, 104 + i * 32) for i in range(7)], [(500, 104 + i * 32) for i in range(7)]]
    outputs = [(590, 122 + i * 78) for i in range(3)]
    for ix, iy, _, _ in inputs:
        for hxp, hyp in hidden[0]:
            w(f'<line x1="{ix + 13}" y1="{iy}" x2="{hxp - 8}" y2="{hyp}" stroke="{RULE}" stroke-width="1"/>')
    for hxp, hyp in hidden[0]:
        for gx, gy in hidden[1]:
            w(f'<line x1="{hxp + 8}" y1="{hyp}" x2="{gx - 8}" y2="{gy}" stroke="#e8ecf1" stroke-width="1"/>')
    for gx, gy in hidden[1]:
        for ox, oy in outputs:
            w(f'<line x1="{gx + 8}" y1="{gy}" x2="{ox - 13}" y2="{oy}" stroke="{RULE}" stroke-width="1"/>')
    for ix, iy, name, value in inputs:
        w(f'<circle cx="{ix}" cy="{iy}" r="13" fill="#ffffff" stroke="{INK}" stroke-width="1.5"/>')
        w(f'<text x="{ix}" y="{iy - 22}" font-size="16" fill="{MUTED}" text-anchor="middle">{name}</text>')
        w(f'<text x="{ix}" y="{iy + 36}" font-size="17" font-weight="600" fill="{INK}" text-anchor="middle">{value}</text>')
    for layer in hidden:
        for hxp, hyp in layer:
            w(f'<circle cx="{hxp}" cy="{hyp}" r="8" fill="#ffffff" stroke="#8d99a6" stroke-width="1.2"/>')
    w(f'<text x="455" y="346" font-size="16" fill="{MUTED}" text-anchor="middle">2 \u00d7 128 hidden units,</text>')
    w(f'<text x="455" y="366" font-size="16" fill="{MUTED}" text-anchor="middle">shared by every state</text>')
    names = ['left', 'none', 'right']
    for k, (ox, oy) in enumerate(outputs):
        chosen = k == a
        w(f'<circle cx="{ox}" cy="{oy}" r="13" fill="{"#eef3fb" if chosen else "#ffffff"}" stroke="{BLUE if chosen else INK}" stroke-width="{2 if chosen else 1.5}"/>')
        w(f'<text x="{ox + 22}" y="{oy - 4}" font-size="17" font-weight="{700 if chosen else 400}" fill="{BLUE if chosen else INK}">Q(s, {names[k]})</text>')
        w(f'<text x="{ox + 22}" y="{oy + 17}" font-size="17" fill="{BLUE if chosen else MUTED}">{f(q_before[k]) + " \u2192 " + f(q_after[k]) if chosen else f(q_before[k])}</text>')
    w(f'<text x="276" y="402" font-size="17" fill="{OCHRE}">target = \u22121 + 0.99 \u00d7 ({f(q_target[star])}) = {f(y)}</text>')
    arrow(744, 812, 200)
    w(f'<text x="778" y="184" font-size="16" fill="{MUTED}" text-anchor="middle">one step</text>')
    # Panel C: the change in every state's value.
    mx0, my0, mw, mh = 872, 84, 280, 216
    w(f'<text x="836" y="60" font-size="19" fill="{MUTED}">\u2026 and every state moves</text>')
    w(f'<image x="{mx0}" y="{my0}" width="{mw}" height="{mh}" preserveAspectRatio="none" href="data:image/png;base64,{png}"/>')
    w(f'<rect x="{mx0}" y="{my0}" width="{mw}" height="{mh}" fill="none" stroke="#b7c1cc" stroke-width="1"/>')
    px = lambda p: mx0 + (p + 1.2) / 1.8 * mw
    py = lambda v: my0 + (0.07 - v) / 0.14 * mh
    w(f'<line x1="{px(0.5):.1f}" y1="{my0}" x2="{px(0.5):.1f}" y2="{my0 + mh}" stroke="{GREEN}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    for i, (x, v) in enumerate(b['s']):
        if i != t:
            w(f'<circle cx="{px(x):.1f}" cy="{py(v):.1f}" r="2.4" fill="{INK}" opacity="0.5"/>')
    w(f'<circle cx="{px(s[0]):.1f}" cy="{py(s[1]):.1f}" r="5" fill="#ffffff" stroke="{BLUE}" stroke-width="2"/>')
    w(f'<text x="{mx0}" y="{my0 + mh + 20}" font-size="15" fill="{MUTED}">position \u2192</text>')
    w(f'<text x="{px(0.5):.1f}" y="{my0 + mh + 20}" font-size="15" fill="{GREEN}" text-anchor="middle">flag</text>')
    w(f'<text x="{mx0 - 10}" y="{my0 + mh / 2}" font-size="15" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 {mx0 - 10} {my0 + mh / 2})">velocity \u2192</text>')
    w(f'<text x="836" y="{my0 + mh + 52}" font-size="18" fill="{INK}">Every visited state drops,</text>')
    w(f'<text x="836" y="{my0 + mh + 74}" font-size="18" fill="{INK}">by {f(least, 2)} to {f(most, 2)}.</text>')
    w(f'<text x="836" y="{my0 + mh + 100}" font-size="15" fill="{MUTED}">Darker: a larger drop. Dots: replayed states.</text>')
    w('</svg>')
    return '\n'.join(out)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data', type=pathlib.Path, required=True)
    p.add_argument('--out', type=pathlib.Path, required=True)
    p.add_argument('--png', type=pathlib.Path)
    p.add_argument('--browser')
    a = p.parse_args()
    svg = build(json.loads(a.data.read_text()))
    a.out.write_text(svg + '\n')
    print(f'wrote {a.out} ({a.out.stat().st_size} bytes)')
    if a.png:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=a.browser)
            page = browser.new_page(viewport={'width': 1200, 'height': 420}, device_scale_factor=2)
            page.set_content(f'<html><body style="margin:0;background:#fff">{svg}</body></html>')
            page.locator('svg').screenshot(path=str(a.png))
            browser.close()
        image = Image.open(a.png)
        assert image.size == (2400, 840), image.size
        print(f'wrote {a.png} {image.size}')


if __name__ == '__main__':
    main()
