# RL From Zero launch post: Medium and Substack

- `medium.md` and `substack.md`: the series launch post for each platform. Both put the announcement animation directly below the title and link to the blog's RL From Zero page, Part 1 (Q-learning) and the repository.
- `media/rl-from-zero-announcement-grid-first.gif`: the same 8.9 s loop as the blog animation, rotated so its first frame is the full grid. Email clients and post previews that show only the first frame still show all 13 agents. 1280x720, 178 frames, 4.6 MB, well under Medium's 25 MB image limit.
- `media/rl-from-zero-announcement-grid-first.png`: that first frame as a still, for anywhere a static image works better.

## Publishing order

1. Merge `ali/rl-from-zero-announcement` so the blog's RL From Zero page (https://alirezashamsoshoara.github.io/blog/rl-from-zero/) shows the animation. The page itself is already live.
2. Medium: publish the launch post. Under More settings, then Advanced Settings, select "This story was originally published elsewhere" and use the RL From Zero page URL as the canonical link.
3. Substack: publish the launch post and send it to subscribers, after a test email to yourself.
4. LinkedIn: announce with the GIF or the LinkedIn MP4 and the blog, Medium and Substack links.
5. Then publish Part 1 (Q-learning) on Medium and Substack from `tools/qlearning/platform-drafts/`, with its canonical link set to the blog post. Later parts follow the same way.

Editor steps (pasting the text, uploading the GIF, code blocks) are the same as for Part 1; see `tools/qlearning/platform-drafts/README.md`. Upload the GIF file itself in each editor; the `media/` path in the Markdown is only a local reference.

## Review copies

The browser review files (`medium-review.html`, `substack-review.html`, and the still-image `substack-email-review.html`) are generated from these Markdown files and kept out of the repository, since each embeds the images. Rebuild them in a fresh environment:

```bash
REVIEW_ENV=$(mktemp -d /tmp/rlfz-launch-review-env-XXXXXX)
uv venv "$REVIEW_ENV"
uv pip install --python "$REVIEW_ENV/bin/python" markdown pygments pillow
"$REVIEW_ENV/bin/python" tools/qlearning/build_platform_previews.py \
  --drafts-dir tools/rl-from-zero/platform-drafts --out /tmp/rlfz-launch-review
```
