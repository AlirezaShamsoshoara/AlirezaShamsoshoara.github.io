# Q-learning platform drafts: owner review and publishing guide

## What is ready

- `medium.md`: a self-contained technical article adapted for Medium.
- `substack.md`: a newsletter-oriented lesson with the same core mathematics, code, and real environment connection.
- `media/first-goal.gif` and `media/first-bootstrap.gif`: short excerpts of the approved code-rendered lesson, not new generated demonstrations.
- `media/first-goal.png` and `media/first-bootstrap.png`: static fallback images.
- `media/manifest.json`: exact source intervals, hashes, duration and interpretation for those clips.

The private review bundle includes `medium-review.html`, `substack-review.html`, and a static-media `substack-email-review.html`. Download a file and open it in Chrome with Command-O. The styles and images are embedded; no local server, Python or Ruby is needed.

To rebuild these copies in a fresh named review environment:

```bash
REVIEW_ENV=$(mktemp -d /tmp/ql-platform-review-env-XXXXXX)
uv venv "$REVIEW_ENV"
uv pip install --python "$REVIEW_ENV/bin/python" \
  markdown pygments pyyaml playwright pillow wandb
"$REVIEW_ENV/bin/python" tools/qlearning/build_platform_previews.py \
  --out /tmp/ql-platform-review
```

Generated HTML stays outside the checkout. The existing extraction and browser-check tools are in `tools/qlearning/`; their media manifest records the original verified clip intervals.

These files are **not loaded into either platform's account**. Nothing has been posted, emailed to subscribers or published. Account credentials are not needed for this content handoff.

## Source and editorial decisions

The approved personal-blog article remains the authoritative source:

```text
_posts/<date>-q-learning-one-update-at-a-time.md
```

The platform versions preserve its essential update mathematics, alpha/gamma/epsilon distinction, actual exploratory milestones, terminal versus time-limit handling, convergence qualifications, and native8×8 FrozenLake demonstration. They have different narrative structure rather than being renamed copies.

Medium is organized as a technical article with code excerpts. Substack is organized as a lesson for subscribers and remains understandable when motion is unavailable. Neither relies on running custom JavaScript inside the platform.

Both put the algorithm-specific header illustration immediately below their title. Short GIFs focus on the first reward and later bootstrap; captions explicitly distinguish episode29 from episode70. They are not consecutive moves from a new training run. The real repository GIF is a separate native8×8 showcase.

The original source and learning model are not changed by these adaptations. `tools/` is excluded from Jekyll output, so this draft folder does not become a public page when committed.

## Media to upload

The image references in the Markdown are local working references. Upload the actual files in the platform editor; do not publish a relative filesystem path as a link.

| Placement | File | Meaning |
| --- | --- | --- |
| Below title | `assets/media/rl/qlearning/q-learning-hero.png` | Sharp algorithm-specific header illustration |
| First terminal reward | `tools/qlearning/platform-drafts/media/first-goal.gif` | Episode29, one recorded goal transition |
| Later zero-reward bootstrap | `tools/qlearning/platform-drafts/media/first-bootstrap.gif` | Episode70, one recorded revisit |
| Static alternative | Corresponding `first-goal.png` / `first-bootstrap.png` | Complete still explanation when motion is unavailable |
| Native environment section | `assets/media/rl/qlearning/frozenlake-8x8.gif` | Actual saved agent in the repository8×8 environment |
| Optional full lesson video | `assets/media/rl/qlearning/q-update.mp4` | H.264 export of edited exploratory highlights |

The private bundle contains these assets under its `media/` folder for easier download. Each short GIF is below Medium's 25 MB image limit. Alt text is supplied in each article, and the following italic paragraph supplies its caption. Keep code as code, not an image. On narrow screens, treat diagram microcopy as supplementary: retain the full mathematical explanation in the prose, and check image enlargement/placement in the actual platform draft.

## Medium editor handoff

1. Create a new **draft story** in your own account.
2. Set the title and subtitle from `medium.md`; insert the header picture directly below the title area.
3. Paste the prose in sections and preserve headings, bold/inline-code formatting and public reference links.
4. Insert the supplied GIF/image files at their matching paragraphs. Copy their alt text and captions.
5. Use Medium's native code-block control for Python and shell snippets. The equations are plain readable text/code; they do not require JavaScript or an external math renderer.
6. Review narrow-screen layout, code indentation, GIF playback, images and outbound links in the platform draft before publishing.

The HTML review file is for content review, not raw HTML to paste into Medium. Supported video URL embeds are an alternative to a large GIF, but no public video-host URL has been created here.

## Substack editor and email handoff

1. Create a new **draft post** in your publication.
2. Use the title, subtitle, prose and header image from `substack.md`.
3. Add GIFs through the image control. Put the complete explanatory text beside them, as in the draft, so no point depends on animation.
4. Preserve code indentation with the editor's code block. The text-form equations can be used as written; native LaTeX equation blocks are optional, not required by this draft.
5. If you choose video, upload the H.264 MP4 or use a supported public URL. In-email playback is not promised; make the email work as text and still images with a click-through link.
6. Use the platform's preview and a test email sent only to yourself to review the actual email rendering before sending to subscribers.

`substack-email-review.html` is a static-media reading check, not a real email-client or Substack rendering test. Actual GIF behavior varies across email clients. Do not paste our custom interactive blog HTML into the post editor.

## Publication and PR gates

The drafts reference this **planned** personal-blog URL:

```text
https://AlirezaShamsoshoara.github.io/blog/rl-from-zero/q-learning/
```

It is not marked as already live. Publish/verify the personal blog first, then check every companion link before publishing the adaptations. Do not use private Meta Artifact URLs as public blog links. Once the original is live, use Medium's canonical-link setting to identify that original source where appropriate.

The main post now lives in `_posts/` without draft flags, so merging the branch publishes it once GitHub Pages rebuilds.

Run the real Jekyll build before merging (see `tools/qlearning/README.md`). It was not run from this session because the RubyGems download was refused by the chat's internet policy. The platform HTML previews do not replace it.

The owner handles staging, commits, pushes and PR creation in the isolated worktree:

```text
/home/alisol/projects/blog-qlearning-education
branch: ali/qlearning-educational-pilot
```

The daily-update master checkout stays untouched. Do not stage the untracked platform `.claude/` directory or temporary environments/evidence. No repository cleanup request was resumed during this drafting turn.

## Skill and announcement

The reusable educational-content skill comes after review of these adaptations. It has not been written in this turn. No LinkedIn announcement or public account post has been drafted or sent; those follow reviewed platform versions and verified live links.

## Format references

- Medium images: https://help.medium.com/hc/en-us/articles/215679797-Using-images
- Medium embeds and JavaScript limits: https://help.medium.com/hc/en-us/articles/214981378-Using-embeds
- Medium code blocks: https://help.medium.com/hc/en-us/articles/35756844492439-Using-code-blocks-and-inline-code
- Substack images/GIF/video and editor limits: https://support.substack.com/hc/en-us/articles/360037832971-How-do-I-embed-media-in-my-post-e-g-images-video-GIFs
