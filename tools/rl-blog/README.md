# Shared RL article tools

These tools work with any `layout: rl-article` post in `_drafts/` or `_posts/`.
The preview uses the real article layout and includes, Python Markdown,
python-liquid and libSass. It is not a production Jekyll build.

## Front matter

Keep the normal `title`, `layout`, `permalink`, `series: rl-from-zero`,
`series_part`, `categories`, `tags`, `hero_image` and `hero_alt` fields.
A draft needs `published: false` and `sitemap: false`.

Optional article fields:

- `stylesheets`: a list of local stylesheet URLs. Shared `article.css` always
  loads first; list only the part-specific styles here.
- `scripts`: a list of local ES module URLs. Include
  `/assets/js/rl/article-common.mjs` for code-copy controls and recorded GIFs,
  followed by the part's controller module.
- `series_label`: text beside the series link. Defaults to `Part N`.
- `lede`: plain-text introduction below the title illustration. Omitted if absent.
- `read_time_text`: the complete byline label, including any reading-time text.
  Omitted if absent. `read_time` remains a separate theme setting.
- `jump_links`: a list of `href` and `label` mappings. Fragment URLs stay fragments.
- `footer_part_label`: the complete footer heading. Defaults to
  `Part N of RL From Zero`.
- `next_teaser`: the complete teaser sentence, including a `Next:` prefix if wanted.
- `previous_part` and `next_part`: optional mappings with `url` and `title` for
  footer navigation. Link only to approved public parts, not unpublished drafts.

The title image, draft notice, per-part Medium/Substack links and the series
follow line retain their existing behavior. Omitting optional fields creates
no empty lede, read-time span, shortcuts or navigation links.

Use literal `{% include rl/name.html %}` tags. Nested RL includes are supported;
missing includes and cycles fail. Media directories are inferred from
`hero_image` and the article's `/assets/media/rl/<slug>/` URLs, so they do not
have to match the permalink's spelling. Keep part assets under `assets/css/rl`,
`assets/js/rl` and `assets/media/rl/<slug>`.

## Exact commands for a new post

From the repository root, replace `example` with the new post's slug:

```bash
POST=_drafts/example.md
S=$(mktemp -d)
uv venv "$S/rl-blog-review" --python 3.12
PY="$S/rl-blog-review/bin/python"
uv pip install --python "$PY" \
  pyyaml markdown libsass pygments python-liquid wandb
export WANDB_MODE=offline PYTHONDONTWRITEBYTECODE=1

"$PY" tools/rl-blog/check_post.py --post "$POST" --state draft
"$PY" tools/rl-blog/check_article_code.py --post "$POST"
"$PY" tools/rl-blog/build_review_preview.py --post "$POST" --out "$S/preview"
"$PY" tools/rl-blog/package_review.py --preview "$S/preview" \
  --out ../example-review.html
rm -rf "$S"
```

Python 3.12, `uv` and Node are needed. Node checks the bundled module syntax
without executing it. The packager takes all its inputs from the preview,
not from a second checkout. Package output must be outside both the source
checkout and the preview directory; preview output must be outside the checkout.
`--root` defaults to the tool's repository and can name an isolated source copy.
Use a fresh preview directory: rebuilding into an existing directory merges
asset copies and does not remove files left by a previous preview.

Open `example-review.html` in Chrome with Command-O. It needs no server:
local CSS, module dependencies, fonts and media are embedded. Asset links
become downloads. The packager fails on missing assets, external resources,
unresolved references or a file at least 50 MiB in size.

Static local imports support named, aliased, default, namespace and side-effect
bindings. Module scopes stay separate and dependencies execute once, before
users of their exports. Cycles, dynamic imports, `import.meta`, destructured
export declarations, unclassified export aliases and value imports of mutable
exports (including default aliases) require the served site and fail rather
than producing a silently broken review file.

For an approved published post, set `POST` to its `_posts/` path and run the
same checks with `--state published`. Do not change publication state merely
to build a review. `check_post.py` checks state, series, hero and media files,
optional fields, jump targets, unique IDs across all includes, and public
source hygiene. `check_article_code.py` checks excerpts without running them.

## Video export

In a fresh scratch environment with `wandb` installed, and with `ffmpeg` and
`ffprobe` available, transcode verified media:

```bash
"$PY" tools/rl-blog/export_mp4.py \
  --source "$S/preview/assets/media/rl/example/lesson.webm" \
  --out ../example-review.mp4 --log-dir "$S/video-checks"
```

Run this before deleting that scratch folder. The exporter logs offline W&B
metrics and verifies H.264, yuv420p, TV range, bt709 and duration agreement
within 0.1 seconds. It never overwrites the source file.

## Compatibility and regression tests

The Q-learning preview, packager and MP4 entry points are thin wrappers.
Their existing command-line options still work. The algorithm-specific Node,
source and browser checks remain in `tools/qlearning/`; the browser checker
re-exports media and must use `--root` on an isolated source copy for a
read-only regression run.

Run the shared tool regression tests in the fresh environment:

```bash
"$PY" -m unittest discover -s tools/rl-blog -p 'test_*.py' -v
```

Keep previews, environments, logs and exported review files outside the
checkout. A successful standalone review still requires a real Jekyll build
before merging.
