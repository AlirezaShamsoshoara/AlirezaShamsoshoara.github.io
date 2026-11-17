#!/usr/bin/env python3
"""Verify real exploratory episodes, compact layout and portable lesson media.

The preview is a standalone rendering, not production Jekyll verification.
Portable media are explicitly edited highlights of whole recorded episodes.
"""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import io
import json
import math
from pathlib import Path
import shutil
import subprocess
import threading

from PIL import Image
from playwright.sync_api import sync_playwright
import wandb


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


def near(actual, expected, tolerance=1e-10):
    assert abs(actual - expected) <= tolerance, (actual, expected)


def main(args):
    args.out.mkdir(parents=True, exist_ok=True)
    captures = args.out / 'screenshots'; captures.mkdir(exist_ok=True)
    media = args.root / 'assets/media/rl/qlearning'; media.mkdir(parents=True, exist_ok=True)
    checks = []
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(args.site)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f'http://127.0.0.1:{server.server_port}/blog/rl-from-zero/q-learning/'
    run = wandb.init(project='rl-education', name='qlearning-real-exploration-browser', mode='offline', dir=str(args.out), config={'renderer': 'standalone, not Jekyll', 'trace_episodes': 120})
    def passed(name):
        checks.append(name); print('PASS', name, flush=True)
    def open_page(browser, width=1440, **options):
        page = browser.new_page(viewport={'width': width, 'height': 1000}, **options)
        page.goto(url, wait_until='networkidle')
        if options.get('java_script_enabled', True):
            page.wait_for_function('window.QLearningPilot !== undefined')
        return page
    def alignment(page, width):
        measured = page.evaluate('''() => {
          const center = el => { const b=el.getBoundingClientRect(); return (b.left+b.right)/2; };
          const prose=document.querySelector('.rlql-prose'), map=document.querySelector('[data-map-matrix]');
          return {equations:[...document.querySelectorAll('.rl-equation')].map(el=>({align:getComputedStyle(el).textAlign,offset:Math.abs(center(el)-center(prose))})),
            mapOffset:Math.abs(center(map)-center(prose)), gridOffset:Math.abs(center(map.querySelector('pre'))-center(map)),
            codeAlign:getComputedStyle(document.querySelector('.rlql-prose .highlight pre')).textAlign};
        }''')
        assert len(measured['equations']) == 9
        assert all(item['align'] == 'center' and item['offset'] < 2 for item in measured['equations']), (width, measured)
        assert measured['mapOffset'] < 2 and measured['gridOffset'] < 2
        assert measured['codeAlign'] in ('start', 'left')
        return measured
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=str(args.browser), headless=True)
            try:
                page = open_page(browser)
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                trace = page.evaluate('window.QLearningPilot.trace()')
                assert trace['episodes'] == 120 and len(trace['records']) == 843
                assert trace['milestones'] == {'explore': 0, 'hole': 11, 'reward': 210, 'bootstrap': 550, 'start': 735}
                assert all(r['behavior'] == 'epsilon-greedy' and r['selection'] != 'guided' for r in trace['records'])
                assert page.locator('#ql-epsilon').count() == 1
                assert page.locator('[data-trace-selection]').inner_text().startswith('Explore')
                assert page.locator('[data-guided-action-arrow]').get_attribute('visibility') == 'hidden'
                assert page.locator('[data-worked-table] tr').count() == 1
                passed('the detailed figure records true epsilon-greedy actions and handles its first random wall move without a false arrow')
                page.screenshot(path=str(captures / 'desktop-top.png'))
                page.locator('[data-ql-worked]').screenshot(path=str(captures / 'exploration-opening.png'), animations='disabled')
                paths = []
                for episode in range(120):
                    page.locator('[data-trace-episode]').select_option(str(episode))
                    state = page.evaluate('window.QLearningPilot.exploration()')
                    summary = trace['episodeSummaries'][episode]
                    assert state['moveIndex'] == summary['startIndex'] and state['phase'] == 0
                    assert state['transition']['state'] == 0
                    page.locator('[data-guided-result]').click()
                    state = page.evaluate('window.QLearningPilot.exploration()')
                    assert state['moveIndex'] == summary['endIndex'] and state['phase'] == 5
                    near(float(page.locator('[data-current-q]').get_attribute('title')), state['transition']['newValue'])
                    paths.append(summary['states'])
                assert paths[0] != paths[1] != paths[2]
                assert [len(path) - 1 for path in paths[:3]] == [12, 5, 4]
                assert any(summary['hole'] for summary in trace['episodeSummaries']) and any(summary['goal'] for summary in trace['episodeSummaries'])
                passed('all120 variable-length episodes are selectable and show their own different paths, failures and snapshots')
                page.locator('[data-worked-reset]').click()
                page.locator('[data-worked-next]').focus(); page.keyboard.press('Enter')
                assert page.evaluate('window.QLearningPilot.exploration().phase') == 1
                page.locator('[data-guided-next-move]').click()
                assert page.evaluate('window.QLearningPilot.exploration().moveIndex') == 1
                page.locator('[data-trace-next-episode]').click()
                assert page.evaluate('window.QLearningPilot.exploration().transition.episode') == 2
                passed('phase, move and episode navigation work with native controls and keyboard activation')
                for name, index in trace['milestones'].items():
                    page.locator(f'[data-guided-chapter="{name}"]').click()
                    state = page.evaluate('window.QLearningPilot.exploration()')
                    assert state['moveIndex'] == index and state['phase'] == 5
                    near(float(page.locator('[data-current-q]').get_attribute('title')), trace['records'][index]['newValue'])
                    if name == 'hole':
                        assert state['transition']['hole'] and state['transition']['bootstrap'] == 0
                        assert 'hole' in page.locator('[data-guided-next-note]').inner_text().lower()
                    if name == 'reward':
                        assert state['transition']['episode'] == 29 and state['transition']['selection'] == 'greedy-tie'
                        assert page.locator('[data-current-q]').inner_text() == '0.1'
                    if name == 'bootstrap':
                        assert state['transition']['episode'] == 70 and state['transition']['selection'] == 'explore'
                        assert page.locator('[data-current-q]').inner_text() == '0.0095'
                    if name == 'start':
                        assert state['transition']['episode'] == 103
                        assert 'e-' in page.locator('[data-current-q]').inner_text()
                    page.locator('[data-ql-worked]').screenshot(path=str(captures / f'event-{name}.png'), animations='disabled')
                passed('actual exploration, hole, goal and delayed-bootstrap milestones are labeled with the correct action-selection reason')
                page.locator('[data-guided-chapter="bootstrap"]').click()
                page.locator('[data-worked-back]').click()
                assert page.locator('[data-current-q]').inner_text() == '0'
                assert page.evaluate('window.QLearningPilot.policy().episodes') == 0
                passed('seeking and backward explanation restore recorded before/after values without training or copying into Figure2')
                page.locator('#ql-shared-settings > summary').click()
                page.locator('#ql-alpha').focus(); page.keyboard.press('ArrowRight')
                near(page.evaluate('window.QLearningPilot.exploration().params.alpha'), .15)
                near(page.evaluate('window.QLearningPilot.policy().alpha'), .15)
                page.locator('[data-guided-defaults]').click()
                page.locator('[data-policy-train]').click()
                page.wait_for_function('window.QLearningPilot.policy().episodes === 500')
                page.wait_for_function('!document.querySelector("[data-policy-replay]").disabled')
                policy_state = page.evaluate('window.QLearningPilot.policy()')
                assert policy_state['goals'] == 267 and policy_state['holes'] == 233 and policy_state['interactions'] == 3336
                page.locator('[data-policy-replay]').click()
                page.wait_for_function('document.querySelector("[data-policy-status]").textContent.includes("Goal reached in 6 moves")')
                assert page.evaluate('window.QLearningPilot.policy()') == policy_state
                page.locator('[data-ql-policy]').screenshot(path=str(captures / 'policy-desktop.png'), animations='disabled')
                passed('the independent batched learner preserves its verified default baseline and greedy replay never updates it')
                page.locator('#ql-epsilon').evaluate('(el)=>{el.value="0.6";el.dispatchEvent(new Event("input",{bubbles:true}));}')
                assert page.evaluate('window.QLearningPilot.policy().episodes') == 0
                near(page.evaluate('window.QLearningPilot.trace().epsilon'), .6)
                near(page.evaluate('window.QLearningPilot.policy().epsilon'), .6)
                assert page.evaluate('window.QLearningPilot.exploration().moveIndex') == 0
                passed('epsilon changes now reset both independent experiments and change the recorded exploration behavior')
                page.locator('#ql-epsilon').evaluate('(el)=>{el.value="0";el.dispatchEvent(new Event("input",{bubbles:true}));}')
                assert page.locator('[data-guided-chapter="explore"]').is_disabled()
                page.locator('#ql-epsilon').evaluate('(el)=>{el.value="0.3";el.dispatchEvent(new Event("input",{bubbles:true}));}')
                page.locator('#ql-alpha').evaluate('(el)=>{el.value="0";el.dispatchEvent(new Event("input",{bubbles:true}));}')
                assert page.locator('[data-guided-chapter="bootstrap"]').is_disabled()
                assert page.locator('[data-guided-chapter="start"]').is_disabled()
                page.locator('[data-guided-chapter="reward"]').click()
                assert 'TD error is nonzero' in page.locator('[data-worked-step-copy]').inner_text()
                assert page.locator('[data-worked-error]').inner_text() == '1'
                assert page.locator('[data-worked-new]').inner_text() == '0'
                passed('zero exploration or learning settings do not fabricate events or confuse a zero increment with a zero residual')
                page.locator('[data-guided-defaults]').click()
                page.locator('#ql-shared-settings > summary').click()
                page.evaluate('()=>{document.querySelector("[data-policy-train]").click();document.querySelector("[data-policy-stop]").click();}')
                stopped = page.evaluate('window.QLearningPilot.policy().episodes')
                page.wait_for_timeout(150)
                assert page.evaluate('window.QLearningPilot.policy().episodes') == stopped
                page.evaluate('()=>{document.querySelector("[data-policy-train]").click();Object.defineProperty(document,"hidden",{configurable:true,value:true});document.dispatchEvent(new Event("visibilitychange"));}')
                assert 'tab was hidden' in page.locator('[data-policy-status]').inner_text()
                page.evaluate('Object.defineProperty(document,"hidden",{configurable:true,value:false})')
                passed('stop and hidden-tab guards still invalidate in-flight training and replay')
                assert page.locator('.rlql-prose .highlight pre').count() == 7
                assert page.get_by_role('button', name='Copy code', exact=True).count() == 7
                page.locator('.rlql-prose .highlight').first.screenshot(path=str(captures / 'code-desktop.png'))
                native_image = page.locator('[data-native-image]')
                native_button = page.locator('[data-native-play]')
                page.locator('[data-native-demo]').scroll_into_view_if_needed()
                page.wait_for_function('document.querySelector("[data-native-image]").getAttribute("src").endsWith("frozenlake-8x8.gif")')
                assert native_button.get_attribute('aria-pressed') == 'true' and native_button.inner_text() == 'Pause real agent GIF'
                native_button.click()
                assert native_image.get_attribute('src').endswith('frozenlake-8x8.png')
                assert native_button.get_attribute('aria-pressed') == 'false'
                page.evaluate('window.scrollTo(0, 0)'); page.wait_for_timeout(200)
                page.locator('[data-native-demo]').scroll_into_view_if_needed(); page.wait_for_timeout(400)
                assert native_image.get_attribute('src').endswith('frozenlake-8x8.png'), 'Autoplay must not override a reader pause'
                native_button.click()
                assert native_image.get_attribute('src').endswith('frozenlake-8x8.gif')
                passed('highlighted code remains; the real8x8 agent GIF starts by itself in view, pauses on request and stays paused')
                layout = page.locator('[data-ql-worked]').evaluate('''el => ({
                  explicitHeight:el.style.height, copyMinHeight:getComputedStyle(el.querySelector('.rlql-step-copy')).minHeight,
                  stageHeight:el.querySelector('.rlql-worked-grid').getBoundingClientRect().height,
                  figureHeight:el.getBoundingClientRect().height
                })''')
                assert layout['explicitHeight'] == '' and layout['copyMinHeight'] == '0px'
                assert layout['stageHeight'] < 560, layout
                passed('the interactive uses natural-height compact panels instead of an exported fixed canvas or reserved blank description area')
                assert not errors, errors
                alignments = {'1440': alignment(page, 1440)}
                page.close()
                clock = open_page(browser, width=1280)
                clock.clock.install(); clock.locator('[data-worked-play]').click(); clock.clock.run_for(5000)
                assert clock.evaluate('window.QLearningPilot.exploration().phase') > 0
                clock.locator('[data-worked-play]').click()
                position = clock.evaluate('[window.QLearningPilot.exploration().moveIndex, window.QLearningPilot.exploration().phase]')
                clock.clock.run_for(10000)
                assert clock.evaluate('[window.QLearningPilot.exploration().moveIndex, window.QLearningPilot.exploration().phase]') == position
                clock.locator('[data-worked-play]').click(); clock.clock.run_for(200000)
                assert clock.evaluate('window.QLearningPilot.exploration().moveIndex') == 11
                assert clock.evaluate('window.QLearningPilot.exploration().phase') == 5
                assert clock.locator('[data-worked-play]').get_attribute('aria-pressed') == 'false'
                clock.close(); passed('recorded playback pauses, resumes and stops at the selected episode rather than replaying one prescribed path')
                for width in (320, 390, 768, 1440):
                    mobile = open_page(browser, width)
                    alignments[str(width)] = alignment(mobile, width)
                    assert mobile.evaluate('document.documentElement.scrollWidth <= innerWidth'), width
                    assert mobile.locator('[data-worked-next]').bounding_box()['height'] >= 44
                    assert mobile.locator('.rlql-exploration .rlql-step-copy').evaluate('(el)=>getComputedStyle(el).minHeight') == '0px'
                    if width == 390:
                        mobile.screenshot(path=str(captures / 'mobile-top.png'))
                        mobile.locator('[data-guided-chapter="bootstrap"]').click()
                        mobile.locator('[data-ql-worked]').screenshot(path=str(captures / 'exploration-mobile.png'), animations='disabled')
                        mobile.locator('.rlql-prose .highlight').first.screenshot(path=str(captures / 'code-mobile.png'))
                    mobile.close(); passed(f'{width}px layout stays centered, readable and free of page overflow or reserved description gaps')
                reduced = open_page(browser, 390, reduced_motion='reduce')
                assert reduced.locator('[data-worked-agent]').evaluate('(el)=>getComputedStyle(el).transitionDuration') == '0s'
                assert reduced.locator('[data-worked-play]').get_attribute('aria-pressed') == 'false'
                reduced.locator('[data-native-demo]').scroll_into_view_if_needed(); reduced.wait_for_timeout(400)
                assert reduced.locator('[data-native-image]').get_attribute('src').endswith('frozenlake-8x8.png')
                assert reduced.locator('[data-native-play]').get_attribute('aria-pressed') == 'false'
                reduced.close(); passed('reduced motion starts paused, disables moving transitions and keeps the real-agent GIF still')
                nojs = open_page(browser, 390, java_script_enabled=False)
                assert nojs.locator('[data-interactive-controls]').first.is_hidden()
                assert 'episode 29' in nojs.locator('noscript').first.inner_text()
                assert nojs.locator('[data-native-demo] noscript a').is_visible()
                assert nojs.locator('.rlql-prose .highlight pre').count() == 7
                nojs.locator('[data-ql-worked]').screenshot(path=str(captures / 'no-js-exploration.png'))
                nojs.close(); passed('static fallbacks explain actual exploratory experience and retain code and real-agent media access')

                # Sharp PNG: native2x browser rendering, no resize/upscale of an old screenshot.
                poster = open_page(browser, 1280, device_scale_factor=2)
                event = trace['milestones']['bootstrap']
                poster.evaluate('([index])=>window.QLearningPilot.exportFrame(index,5,1,"Episode70: first recorded positive zero-reward bootstrap.")', [event])
                poster.locator('[data-ql-worked]').screenshot(path=str(media / 'q-update.png'), animations='disabled')
                png = Image.open(media / 'q-update.png')
                poster_width = poster.locator('[data-ql-worked]').bounding_box()['width']
                assert png.width >= poster_width * 2 - 1
                assert png.width >= 2000
                poster.close(); passed('the new lossless poster is rendered natively at2x resolution instead of stretching the earlier screenshot')

                export = open_page(browser, 1280)
                full = export.evaluate('window.QLearningPilot.trace()')
                selected = full['highlightIndices']
                assert len(selected) == 40
                assert sorted(set(full['records'][index]['episode'] for index in selected)) == [1, 2, 29, 70, 103]
                schedule = []
                previous = -1
                current_note = 'Edited episode highlights. Intervening experience is retained in each Q-table snapshot.'
                for index in selected:
                    record = full['records'][index]
                    if index != previous + 1:
                        current_note = f"Edited highlights: {index - previous - 1} recorded moves omitted before episode {record['episode']}. Complete history stays in the interactive."
                    elif record['episodeStep'] == 1:
                        current_note = 'Edited episode highlights. Intervening experience is retained in each Q-table snapshot.'
                    note = current_note
                    if record['milestoneNames']:
                        timing = record['phaseDurationsMs']
                        parts = [(0, 0, timing[0])] + [(1, n / 4, timing[1] // 4) for n in range(1, 5)] + [(phase, 1, timing[phase]) for phase in (2, 3, 4, 5)]
                    else:
                        # Repeated moves are fast; milestone arithmetic receives readable holds.
                        parts = [(1, n / 4, 180) for n in range(1, 5)] + [(5, 1, 450)]
                    schedule.extend((index, phase, movement, duration, note) for phase, movement, duration in parts)
                    previous = index
                for episode in (29, 70, 103):
                    notes = {item[4] for item in schedule if full['records'][item[0]]['episode'] == episode}
                    assert len(notes) == 1 and 'recorded moves omitted' in next(iter(notes))
                height = 0
                for index, phase, movement, _, note in schedule:
                    export.evaluate('([i,p,m,n])=>window.QLearningPilot.exportFrame(i,p,m,n)', [index, phase, movement, note])
                    height = max(height, export.locator('[data-ql-worked]').bounding_box()['height'])
                export.locator('[data-ql-worked]').evaluate('(el,height)=>el.style.height=height+"px"', math.ceil(height) + 2)
                frames, durations, frame_metadata = [], [], []
                keys = args.out / 'key-frames'; keys.mkdir(exist_ok=True)
                geometry = None
                for index, phase, movement, duration, note in schedule:
                    export.evaluate('([i,p,m,n])=>window.QLearningPilot.exportFrame(i,p,m,n)', [index, phase, movement, note])
                    assert export.locator('[data-ql-worked]').evaluate('(el)=>el.scrollHeight <= el.clientHeight + 1')
                    image = Image.open(io.BytesIO(export.locator('[data-ql-worked]').screenshot(animations='disabled'))).convert('RGB')
                    if geometry is None: geometry = image.size
                    assert image.size == geometry
                    if phase == 5 and index in full['milestones'].values(): image.save(keys / f'event-{index}.png')
                    frames.append(image.quantize(colors=128)); durations.append(duration)
                    frame_metadata.append({'index': index, 'episode': full['records'][index]['episode'], 'phase': phase, 'movement': movement, 'duration_ms': duration, 'edit_note': note})
                frames[0].save(media / 'q-update.gif', save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=True, disposal=2)
                gif = Image.open(media / 'q-update.gif'); gif_duration = 0
                for index in range(gif.n_frames): gif.seek(index); gif_duration += gif.info.get('duration', 0)
                assert gif_duration == sum(durations)
                assert (media / 'q-update.gif').stat().st_size < 25 * 1000 * 1000, 'GIF exceeds Medium image upload limit'
                process = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(media / 'q-update.gif'), '-vf', 'pad=ceil(iw/2)*2:ceil(ih/2)*2,scale=out_range=tv,format=yuv420p', '-r', '20', '-c:v', 'libvpx-vp9', '-threads', '2', '-crf', '32', '-b:v', '0', '-color_range', 'tv', str(media / 'q-update.webm')], capture_output=True, text=True)
                if process.returncode: raise RuntimeError(process.stderr)
                video = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_name,pix_fmt,color_range,width,height', '-of', 'json', str(media / 'q-update.webm')], text=True, capture_output=True, check=True).stdout)
                video_ms = float(video['format']['duration']) * 1000
                assert abs(video_ms - gif_duration) <= 100
                assert video['streams'][0]['color_range'] == 'tv'
                meta = {'kind': 'edited highlights of real seeded epsilon-greedy experience, not a prescribed route',
                    'map': full['map'] if 'map' in full else ['SFFF','FHFH','FFFH','HFFG'], 'alpha': full['alpha'], 'gamma': full['gamma'], 'epsilon': full['epsilon'], 'seed': full['seed'],
                    'recorded_episodes': full['episodes'], 'recorded_transitions': len(full['records']), 'highlight_episodes': [1,2,29,70,103], 'highlight_transitions': len(selected),
                    'milestones': full['milestones'], 'poster_transition': event, 'poster_width': png.width, 'poster_height': png.height, 'poster_scale_factor': 2,
                    'submitted_frames': len(frames), 'encoded_frames': gif.n_frames, 'gif_bytes': (media/'q-update.gif').stat().st_size, 'duration_ms': gif_duration,
                    'video_duration_ms': video_ms, 'video_codec': 'vp9', 'video_color_range': 'tv', 'visual_style': 'compact white editorial figures',
                    'interpretation': 'Portable media omit intervals explicitly; every intervening update is retained in the shown snapshots and the complete interactive history. Not an8x8 benchmark.',
                    'renderer': 'same actual browser renderer and shared epsilon-greedy learner as the interactive'}
                (media / 'q-update.json').write_text(json.dumps(meta, indent=2))
                (args.out / 'export-frames.json').write_text(json.dumps(frame_metadata, indent=2))
                target = args.site / 'assets/media/rl/qlearning'; target.mkdir(parents=True, exist_ok=True)
                for file in media.iterdir():
                    if file.is_file(): shutil.copy2(file, target / file.name)
                export.evaluate('()=>{const v=document.createElement("video");v.src="/assets/media/rl/qlearning/q-update.webm";v.muted=true;document.body.append(v);window.__video=v;}')
                export.wait_for_function('window.__video.readyState >= 2')
                export.evaluate('window.__video.currentTime=window.__video.duration-.2')
                export.wait_for_function('!window.__video.seeking')
                assert export.evaluate('window.__video.videoWidth') > 0
                export.close(); passed('portable edited highlights identify omitted experience, fit the GIF upload limit, decode and agree on playback timing')
            finally:
                browser.close()
        report = {'checks_passed': len(checks), 'checks': checks, 'full_jekyll_build_verified': False, 'preview_kind': 'standalone', 'layout': layout, 'media': meta}
        (args.out / 'verification.json').write_text(json.dumps(report, indent=2))
        (args.out / 'math-alignment.json').write_text(json.dumps(alignments, indent=2))
        run.log({'verification/checks_passed': len(checks), 'poster/width': png.width, 'media/gif_bytes': meta['gif_bytes'], 'media/seconds': gif_duration / 1000})
        print(json.dumps(report, indent=2), flush=True)
    finally:
        server.shutdown(); server.server_close(); run.finish()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--site', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--browser', type=Path, required=True)
    main(parser.parse_args())
