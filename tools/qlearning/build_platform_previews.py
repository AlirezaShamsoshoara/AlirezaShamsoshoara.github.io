#!/usr/bin/env python3
"""Build self-contained content-review copies of the platform adaptations.

The output is not a Medium/Substack account draft or a platform-rendering test.
No external styles, images, scripts, trackers, or model calls are required.
"""
import argparse
import base64
import html
import json
from pathlib import Path
import re

import markdown
from PIL import Image


STYLE = '''
*{box-sizing:border-box}body{margin:0;background:#fff;color:#253341;font:18px/1.8 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.review-notice{max-width:1100px;margin:0 auto;padding:12px 20px;border-bottom:1px solid #d5dbe2;color:#56616e;font-size:13px;text-align:center}
main{max-width:830px;margin:32px auto 64px;padding:0 24px}h1{font:700 clamp(2rem,4vw,3.25rem)/1.18 Georgia,"Times New Roman",serif;letter-spacing:-.02em;margin:0 0 24px}
h2{font:700 1.65rem/1.3 Georgia,"Times New Roman",serif;margin:2.4rem 0 1rem}h3{font-size:1.2rem;margin:1.9rem 0 1rem}p{margin:.9rem 0 1.2rem}li{margin:.4rem 0}
a{color:#2356a8;text-underline-offset:3px}img{display:block;max-width:100%;width:auto;height:auto;margin:18px auto;border:1px solid #e2e6eb;border-radius:3px}
.hero-image{width:100%;height:auto;margin:0 auto 24px}.native-image{width:512px;max-width:100%}.clip-image{width:100%;height:auto}
code{font:.86em ui-monospace,SFMono-Regular,Consolas,monospace;background:#f4f5f7;padding:.12em .28em;border-radius:3px;overflow-wrap:anywhere}
.highlight{border:1px solid #d5dbe2;background:#f8fafc;border-radius:4px;margin:1.2rem 0;max-width:100%;overflow:hidden}
.highlight pre{margin:0;padding:1rem 1.1rem;background:#f8fafc;font:.82rem/1.65 ui-monospace,SFMono-Regular,Consolas,monospace;color:#263545;white-space:pre;overflow-x:auto;text-align:left}
.highlight code{font:inherit;white-space:pre;padding:0;background:none;overflow-wrap:normal}.highlight span{color:#263545}
.highlight .k,.highlight .kd,.highlight .kn,.highlight .kp,.highlight .kr,.highlight .kc{color:#703b93;font-weight:600}
.highlight .nf,.highlight .nb,.highlight .bp,.highlight .nc{color:#175685}
.highlight .s,.highlight .s1,.highlight .s2,.highlight .sa,.highlight .sd{color:#2f6545}
.highlight .m,.highlight .mf,.highlight .mi,.highlight .il{color:#8a4f19}
.highlight .c,.highlight .c1,.highlight .cm{color:#5b6977;font-style:italic}
.highlight .o,.highlight .p,.highlight .n{color:#263545}
blockquote{margin:1.4rem 0;padding:.3rem 1rem;border-left:2px solid #879bb8;color:#414d5a}
@media(max-width:600px){body{font-size:17px}main{margin-top:24px;padding:0 16px}h1{font-size:2.35rem}h2{font-size:1.5rem}.highlight pre{font-size:.78rem}}
@media print{.review-notice{display:none}a{color:#253341}}
'''


def resolve_image(root, source_dir, href, static_media):
    path = (source_dir / href).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Article image leaves the checkout')
    if static_media and path.suffix == '.gif':
        alternate = path.with_suffix('.png')
        if not alternate.is_file():
            raise ValueError(f'No static fallback for {href}')
        path = alternate
    if not path.is_file():
        raise FileNotFoundError(path)
    mime = {'.png': 'image/png', '.gif': 'image/gif'}[path.suffix]
    with Image.open(path) as image:
        width, height = image.size
    encoded = base64.b64encode(path.read_bytes()).decode()
    return path, f'data:{mime};base64,{encoded}', width, height


def build(root, out, platform, static_media=False):
    source_dir = root / 'tools/qlearning/platform-drafts'
    source = source_dir / f'{platform}.md'
    text = source.read_text()
    heading = re.match(r'^#\s+(.+)', text)
    if not heading:
        raise ValueError('Draft requires an H1 title')
    document = markdown.markdown(text, extensions=['extra', 'sane_lists', 'codehilite'], extension_configs={'codehilite': {'css_class': 'highlight', 'guess_lang': False, 'use_pygments': True}})
    images = []
    def embed(match):
        href = html.unescape(match.group(1))
        path, uri, width, height = resolve_image(root, source_dir, href, static_media)
        images.append({'source': str(path.relative_to(root)), 'width': width, 'height': height, 'mime': path.suffix})
        kind = 'hero-image' if path.name == 'q-learning-hero.png' else 'native-image' if path.name.startswith('frozenlake-8x8') else 'clip-image'
        return f'src="{uri}" class="{kind}" width="{width}" height="{height}"'
    document = re.sub(r'src="([^"]+)"', embed, document)
    if re.search(r'{%|{{|<script|<iframe', document):
        raise ValueError('Platform adaptation contains executable/template markup')
    name = f'{platform}-email-review.html' if static_media else f'{platform}-review.html'
    notice = ('Static-media reading review. This is not an actual Substack/email-client rendering test.' if static_media else f'{platform.title()} content review. Not uploaded to a platform account.')
    notice += ' Unpublished; companion-blog links must be verified after the original is published.'
    output = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>' + html.escape(heading.group(1)) + ' | Draft review</title><style>' + STYLE + '</style></head><body><aside class="review-notice">' + html.escape(notice) + '</aside><main><article>' + document + '</article></main></body></html>'
    out.mkdir(parents=True, exist_ok=True)
    (out / name).write_text(output)
    return {'file': name, 'bytes': len(output.encode()), 'platform': platform, 'static_media': static_media, 'images': images, 'platform_account_accessed': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.out.resolve() == root or args.out.resolve().is_relative_to(root):
        raise ValueError('Generated review HTML must stay outside the checkout')
    manifest = [build(root, args.out, 'medium'), build(root, args.out, 'substack'), build(root, args.out, 'substack', static_media=True)]
    (args.out / 'platform-preview-manifest.json').write_text(json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2))
