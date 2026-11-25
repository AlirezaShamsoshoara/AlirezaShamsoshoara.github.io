# DQN platform drafts: review and publishing guide

## What is ready

- `medium.md`: a self-contained technical article adapted for Medium.
- `substack.md`: a newsletter lesson with the same substance, written so the email still reads correctly when every image shows only its first frame.
- `media/`: a short clip of update 1 and two stills from the post's figures, with `manifest.json` (sources, sizes, hashes, timings).

Review copies (`medium-review.html`, `substack-review.html` and a static-media `substack-email-review.html`) are in the private review bundle. Download one and open it in Chrome with Command-O. To rebuild them in a fresh environment:

```bash
REVIEW_ENV=$(mktemp -d /tmp/dqn-platform-review-env-XXXXXX)
uv venv "$REVIEW_ENV"
uv pip install --python "$REVIEW_ENV/bin/python" markdown pygments pyyaml playwright pillow wandb
"$REVIEW_ENV/bin/python" tools/qlearning/build_platform_previews.py \
  --drafts-dir tools/dqn/platform-drafts --out /tmp/dqn-platform-review
```

These are drafts to paste into each editor; they are not synced to either account. The published blog post is the source: `_posts/2026-11-23-dqn-when-a-table-is-not-enough.md`.

## Media to upload

The image paths in the Markdown are local references. Upload the files in each editor; never publish a file path as a link.

| Placement | File | What it shows |
| --- | --- | --- |
| Below the title | `assets/media/rl/dqn/dqn-hero.png` | Title image from update 1 of the run |
| One real update | `tools/dqn/platform-drafts/media/first-update.gif` | Update 1, opening on its gradient step (still: `first-update.png`) |
| Target network | `tools/dqn/platform-drafts/media/target-sync.png` | The first 1,500 recorded updates |
| Exploration | `tools/dqn/platform-drafts/media/exploration.png` | The browser exploration lab, holds of 20 to 60 steps |
| Watching training | `assets/media/rl/dqn/dqn-training.gif` | Saved checkpoints, opening on the selected one (still: `dqn-training.png`) |
| The real agent | `assets/media/rl/dqn/mountaincar-dqn.gif` | The repository's committed GIF (still: `mountaincar-dqn.png`) |

Every GIF is under Medium's 25 MB image limit, and each opens on a frame that makes sense alone. Keep code as code blocks, not images. Copy each image's alt text from the Markdown, and use the italic line below it as the caption.

## Medium

1. New story: title and subtitle from `medium.md`, the title image directly below the title.
2. Paste the text section by section; insert each image at its place; use Medium's code block for the Python, YAML and shell.
3. More settings, Advanced Settings, "This story was originally published elsewhere": canonical link `https://alirezashamsoshoara.github.io/blog/rl-from-zero/dqn/`.
4. Tags: Reinforcement Learning, Deep Learning, Machine Learning, Python, AI.
5. Publish after the blog post is live.

## Substack

1. New post: title, subtitle and text from `substack.md`; GIFs through the image button.
2. Preview, then send a test email to yourself.
3. Continue, tick "Schedule time to email and publish", and choose 8:00 AM tomorrow. Substack uses your device's time zone. The post goes live on the web and emails your subscribers at that time.

## Order

1. Tonight: merge the blog branch and wait for the GitHub Pages build to turn green; check the live post.
2. Tonight: publish on Medium with the canonical link.
3. Tonight: schedule Substack for 8:00 AM.
4. Tomorrow at 8:00 AM: Substack sends; post on LinkedIn with the links in the first comment.
5. Afterwards: add the Medium and Substack URLs to the blog post's front matter (`medium_url`, `substack_url`) so its footer links them.
