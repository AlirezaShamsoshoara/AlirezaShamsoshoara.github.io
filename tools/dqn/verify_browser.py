#!/usr/bin/env python3
"""Headless-Chrome behavior checks for the DQN post: served preview, packaged review file opened
locally, and the packaged file inside a sandboxed viewer that blocks fetch() (strict CSP).

Usage: verify_browser.py --site <preview dir> --html <review html> --browser <chrome> --out <json>
"""
import argparse, functools, http.server, json, pathlib, threading
from playwright.sync_api import sync_playwright

URL = '/blog/rl-from-zero/dqn/'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--site', type=pathlib.Path, required=True)
    p.add_argument('--html', type=pathlib.Path, required=True)
    p.add_argument('--browser', required=True)
    p.add_argument('--out', type=pathlib.Path, required=True)
    a = p.parse_args()
    handler = type('Quiet', (http.server.SimpleHTTPRequestHandler,), {'log_message': lambda *x: None})
    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(handler, directory=str(a.site)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{server.server_port}{URL}'
    csp = ("sandbox allow-scripts; default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; "
           "img-src data: blob:; media-src data: blob:; font-src data:")

    class SandboxHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *x):
            pass

        def end_headers(self):
            self.send_header('Content-Security-Policy', csp)
            super().end_headers()

    sandbox = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(SandboxHandler, directory=str(a.html.resolve().parent)))
    threading.Thread(target=sandbox.serve_forever, daemon=True).start()
    sandboxed = f'http://127.0.0.1:{sandbox.server_port}/{a.html.name}'
    checks = []

    def check(name, ok, detail=''):
        checks.append({'check': name, 'passed': bool(ok), 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (f'  ({detail})' if detail else ''))

    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=a.browser)
            for label, target in (('served', base), ('packaged', a.html.resolve().as_uri()), ('sandboxed viewer', sandboxed)):
                page = browser.new_page(viewport={'width': 1440, 'height': 900})
                errors, external = [], []
                page.on('pageerror', lambda e: errors.append(str(e)))
                page.on('request', lambda r: external.append(r.url) if r.url.startswith('http') and not r.url.startswith('http://127.0.0.1') else None)
                page.goto(target, wait_until='networkidle')
                try:
                    page.wait_for_function('document.documentElement.dataset.dqnReady === "true"', timeout=30000)
                    ready = True
                except Exception:
                    ready = False
                check(f'{label}: every figure loads its data and starts', ready, page.evaluate('document.documentElement.dataset.dqnReady || "never"'))
                check(f'{label}: loads with no page errors', not errors, '; '.join(errors)[:200])
                check(f'{label}: no external requests', not external, ', '.join(external)[:200])
                if label != 'served':
                    state = page.evaluate('''() => ({
                      notes: [...document.querySelectorAll('.rldq-figure .rldq-fallback')].filter(n => !n.closest('noscript')).length,
                      explore: (document.querySelector('[data-explore-count]') || {}).textContent || '',
                      update: ((document.querySelector('[data-dqn-update] [data-numbers]') || {}).textContent || '').length,
                      sync: document.querySelectorAll('[data-dqn-target] [data-target-chart] path').length,
                      training: (document.querySelector('[data-training-label]') || {}).textContent || '' })''')
                    check(f'{label}: figures 1 to 4 render, with no failure notes', state['notes'] == 0 and state['explore'].startswith('71 of 500') and state['update'] > 0 and state['sync'] >= 3 and 'Step 251,392' in state['training'], json.dumps(state))
                    img = page.locator('[data-native-image]')
                    img.scroll_into_view_if_needed(); page.wait_for_timeout(800)
                    check(f'{label}: the real agent GIF starts when it scrolls into view', (img.get_attribute('src') or '').startswith('data:image/gif'))
                    page.close()
                    continue
                # Figure 1: chips, phases, controls.
                f1 = page.locator('[data-dqn-update]')
                f1.locator('[data-update-chips] button').nth(1).click()
                check('fig 1: goal chip selects update 32 and tracks the goal sample', '32' in f1.locator('[data-update-note]').inner_text() and 'reached the flag' in page.evaluate("document.querySelector('[data-dqn-update]').innerText"))
                f1.locator('[data-phase="3"]').click()
                check('fig 1: terminal target is the reward alone', '= −1' in f1.locator('[data-numbers]').inner_text())
                f1.locator('[data-action="next"]').click()
                check('fig 1: next step moves to the error phase', '5 · Error' in f1.locator('[data-step-title]').inner_text())
                before = f1.locator('[data-numbers]').inner_text()
                f1.locator('[data-action="sample"]').click()
                check('fig 1: tracking another sample changes the numbers', f1.locator('[data-numbers]').inner_text() != before)
                f1.locator('[data-update-chips] button').nth(0).click()
                f1.locator('[data-phase="5"]').click()
                text = f1.inner_text()
                check('fig 1: step phase reports the recorded move and the spread', 'from −0.1229 to −0.1424' in text and '4,032 of 4,032' in text, text[text.find('Adam'):text.find('Adam') + 120])
                f1.locator('[data-action="play"]').click()
                page.wait_for_timeout(300)
                playing = f1.locator('[data-action="play"]').inner_text() == 'Pause'
                f1.locator('[data-action="play"]').click()
                check('fig 1: play toggles to pause and back', playing and f1.locator('[data-action="play"]').inner_text() == 'Play this update')
                # Figure 2.
                f2 = page.locator('[data-dqn-target]')
                path_before = f2.locator('[data-target-chart] path').nth(0).get_attribute('d')
                f2.locator('[data-target-chips] button').nth(7).click()
                check('fig 2: a probe state redraws the chart', f2.locator('[data-target-chart] path').nth(0).get_attribute('d') != path_before and 'At this one state' in f2.locator('[data-target-caption]').inner_text())
                check('fig 2: six sync lines in 1,500 updates', f2.locator('[data-target-chart] line[stroke="#996418"]').count() == 6)
                # Figure 3.
                f3 = page.locator('[data-dqn-explore]')
                check('fig 3: default 20 to 60 holds, seed 7 reaches the flag 71 times', f3.locator('[data-explore-count]').inner_text().startswith('71 of 500'))
                f3.locator('[data-explore-chips] button').nth(0).click()
                check('fig 3: independent actions reach the flag 0 times', f3.locator('[data-explore-count]').inner_text().startswith('0 of 500'))
                f3.locator('[data-action="seed"]').click()
                check('fig 3: new seed recomputes the table', 'Seed 8' in f3.locator('[data-explore-seed]').inner_text())
                # Figure 4.
                f4 = page.locator('[data-dqn-training]')
                check('fig 4: opens at the selected checkpoint', 'Step 251,392' in f4.locator('[data-training-label]').inner_text() and 'selected' in f4.locator('[data-training-label]').inner_text())
                slider = f4.locator('[data-training-slider]')
                slider.evaluate("(el) => { el.value = '11'; el.dispatchEvent(new Event('input', { bubbles: true })); }")
                check('fig 4: slider shows step 110,000 with 3 of 11 greedy goals', 'Step 110,000' in f4.locator('[data-training-label]').inner_text() and '3 of 11' in f4.locator('[data-training-summary]').inner_text())
                f4.locator('[data-training-starts] button').nth(0).click()
                check('fig 4: start chips change the drive', 'From −0.6' in f4.locator('[data-training-outcome]').inner_text())
                # Code copy buttons and the native GIF.
                check('code: every excerpt has a copy button', page.locator('.rlql-code-toolbar button').count() == page.locator('.rlql-prose .highlight').count() and page.locator('.rlql-code-toolbar button').count() >= 6, str(page.locator('.rlql-code-toolbar button').count()))
                img = page.locator('[data-native-image]')
                img.scroll_into_view_if_needed()
                page.wait_for_timeout(800)
                check('fig 5: the real agent GIF starts when it scrolls into view', (img.get_attribute('src') or '').endswith('.gif'))
                page.close()
            # Reduced motion: no autoplay of the GIF.
            ctx = browser.new_context(viewport={'width': 1440, 'height': 900}, reduced_motion='reduce')
            page = ctx.new_page()
            page.goto(base, wait_until='networkidle')
            page.wait_for_function('document.documentElement.dataset.dqnReady === "true"', timeout=30000)
            img = page.locator('[data-native-image]')
            img.scroll_into_view_if_needed(); page.wait_for_timeout(800)
            check('reduced motion: the GIF stays a still until the reader presses play', (img.get_attribute('src') or '').endswith('.png'))
            ctx.close()
            # No JavaScript: fallbacks visible, article readable.
            ctx = browser.new_context(viewport={'width': 1440, 'height': 900}, java_script_enabled=False)
            page = ctx.new_page()
            page.goto(base, wait_until='load')
            visible = page.locator('noscript').count()
            text = page.locator('body').inner_text()
            check('no JavaScript: fallbacks present and the worked example still readable', visible >= 4 and 'target = −1 + 0.99 * (1 - 0) * (−0.1231) = −1.122' in text, f'{visible} noscript blocks')
            ctx.close()
            # Phone width.
            page = browser.new_page(viewport={'width': 390, 'height': 844})
            page.goto(base, wait_until='networkidle')
            page.wait_for_function('document.documentElement.dataset.dqnReady === "true"', timeout=30000)
            check('390 px: no horizontal overflow', page.evaluate('document.documentElement.scrollWidth - innerWidth') <= 0)
            page.close()
            browser.close()
    finally:
        server.shutdown()
        sandbox.shutdown()
    a.out.write_text(json.dumps({'passed': sum(c['passed'] for c in checks), 'total': len(checks), 'checks': checks}, indent=1))
    print(f"{sum(c['passed'] for c in checks)}/{len(checks)} passed")


if __name__ == '__main__':
    main()
