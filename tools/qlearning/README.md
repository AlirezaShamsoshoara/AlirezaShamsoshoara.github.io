# Q-learning post: tools and review guide

## Scope

The post is `_posts/2026-11-15-q-learning-one-update-at-a-time.md`, published at
`/blog/rl-from-zero/q-learning/`. Make changes on a fresh branch and open a PR;
merging into `master` publishes them through GitHub Pages.

Run the production check below before merging: the standalone preview is not a
Jekyll build.

## Two views of real exploratory learning

Both browser figures use the same deterministic4x4 map, action order, goal-only
reward, true-terminal holes/goal, and bootstrap-preserving60-step cap. Default
settings are α0.1, γ0.95, ε0.3 and seed7. Their Q-tables are independent.

**Figure1 records individual epsilon-greedy interactions.** It does not follow
prescribed actions. The default120-episode recording contains843 transitions,
including wall moves, failed attempts, varied routes and goals. Each action's
selection evidence distinguishes the random epsilon branch, a unique maximizing
action, and random tie-breaking among maximal estimates. The random branch can
choose a currently best action too; tie-breaking is not an epsilon event.

Before/after tables and episode paths are immutable snapshots from ordinary
`createLearner.step()` calls. Selecting or replaying a record does not apply a
second update or copy learned values into Figure2. The first goal appears in
episode29; the first positive zero-reward bootstrap in episode70; the first
positive start-state update in episode103 at default settings. Other settings
can change those events or leave them absent within the finite budget.

The old fixed-route helper is retained only as an arithmetic unit-test control.
Neither public figure invokes it.

**Figure2 runs an independent experiment in batches.** Greedy replay samples no
randomness and makes no updates. All three settings are shared: changing alpha,
gamma or epsilon rebuilds Figure1's recording and resets Figure2's separate
table. Each remains fixed until changed; the repository recipe instead decays
exploration with training steps.

## Captures and edited media

The static PNG is a native2x browser capture of the first positive zero-reward
bootstrap, not an upscaled or JPEG-compressed old screenshot. The interactive
uses a natural-height compact layout; fixed-height measurement applies only to
portable animation frames, not the live page.

GIF/video exports are explicitly edited highlights of complete recorded
episodes1,2,29,70 and103:40 selected transitions, not a continuous40-step training
run. Labels identify omitted intervals, and every intervening update remains
in the recorded Q-table snapshots and full interactive history. Key events
receive readable explanation holds; repeated moves are faster. The GIF must fit
Medium's documented25MB image limit. Exact media dimensions, bytes and timing
are recorded in `assets/media/rl/qlearning/q-update.json`.

## Actual repository connection

Figure 3 remains the verified native 8x8 FrozenLake showcase, using the committed
repository GIF and a real Gymnasium static map. The GIF starts by itself, from its
first frame, when the figure scrolls into view; readers can pause it, and it stays
on the still poster when reduced motion is requested. Its source and checkpoint
provenance are in `frozenlake-8x8.json`. The saved-policy evaluation is separate
from a selected clip and from the browser's 4x4 teaching models. Repeated success
on one deterministic map is not generalization or full convergence evidence.

Captioned Python/YAML/shell examples are statically highlighted in the review
file. Code-copy controls add no network or model call. Partial Python excerpts
are identified as parts of surrounding methods, not standalone programs.

## Review from your Mac

Download the newest `qlearning-review.html` from the private bundle and open it
in Chrome with Command-O. No Python, Ruby, Node, server or SSH tunnel is needed.
Styles, JavaScript and media are embedded; media links download their bytes for
local viewing. The page is visibly labeled as a standalone preview. Developer
verification uses offline W&B, not telemetry in readers' browsers.

## Local verification tools

Create a fresh named environment outside the checkout, so it is never committed:

```bash
REVIEW_ENV=$(mktemp -d /tmp/ql-review-env-XXXXXX)
uv venv "$REVIEW_ENV/ql-review"
PY="$REVIEW_ENV/ql-review/bin/python"
uv pip install --python "$PY" \
  playwright pillow wandb numpy pyyaml markdown libsass pygments python-liquid
node tools/qlearning/core.test.mjs
"$PY" tools/qlearning/build_review_preview.py --out /tmp/ql-exploration-preview
WANDB_MODE=offline "$PY" \
  tools/qlearning/verify_browser.py --site /tmp/ql-exploration-preview \
  --out /tmp/ql-exploration-checks --browser /path/to/chrome-headless-shell
"$PY" tools/qlearning/package_review.py --preview /tmp/ql-exploration-preview \
  --out /tmp/qlearning-review.html
rm -rf "$REVIEW_ENV"
```

`verify_browser.py` also re-exports the lesson media into
`assets/media/rl/qlearning/`. To check without changing them, run it with
`--root` pointing at a copy of the repository.

Tests cover real action-selection evidence, variable episode paths and bounds,
one-cell updates, chronological carry-over, terminal/cap handling, truthful
milestone discovery, independent histories, settings/reset/stop behavior,
keyboard/responsive/reduced-motion/static views, native2x capture, edited-media
provenance, GIF size and video decoding/timing. Builds/evidence stay outside the
checkout. All scripts under `tools/` are excluded from public site output.

## Shared article infrastructure

The preview, packager and MP4 exporter now delegate to `tools/rl-blog/`.
Their existing commands and `--root` options remain supported. The shared
[review guide](../rl-blog/README.md) documents front matter and commands for
other installments, plus draft/published source and code checks.

## Required production check

Run once wherever Ruby, Bundler and internet access are available (for example
your Mac), from a checkout of this branch:

```bash
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000/blog/rl-from-zero/q-learning/` and check the title
image, Figures 1 to 3, equations and code blocks; the post should also be listed
on `/blog/projects/`. GitHub Pages builds this site from `master` with the
`github-pages` gem and has no pull-request build check, so a broken build would
only show up after merging. The previous site stays online, but later updates,
including the daily papers posts, would not deploy until the build is fixed.

Publish the personal blog first, then the Medium and Substack adaptations in
`platform-drafts/`, which link back to it.
