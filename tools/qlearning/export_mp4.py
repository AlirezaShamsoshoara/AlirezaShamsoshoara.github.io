#!/usr/bin/env python3
"""Encode the verified lesson video as a broadly playable H.264 MP4.

No generation occurs here: the existing code-rendered WebM is transcoded.
"""
import argparse
import json
from pathlib import Path
import subprocess

import wandb


def probe(path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_name,pix_fmt,color_range,width,height', '-of', 'json', str(path)], text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def export(args):
    args.log_dir.mkdir(parents=True, exist_ok=True)
    run = wandb.init(project='rl-education', name='qlearning-h264-video-export', mode='offline', dir=str(args.log_dir))
    try:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(args.source), '-vf', 'scale=out_range=tv:out_color_matrix=bt709,format=yuv420p', '-c:v', 'libx264', '-threads', '2', '-preset', 'medium', '-crf', '20', '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-movflags', '+faststart', str(args.out)], text=True, capture_output=True, check=True)
        source, output = probe(args.source), probe(args.out)
        assert output['streams'][0]['codec_name'] == 'h264'
        assert output['streams'][0]['pix_fmt'] == 'yuv420p'
        assert output['streams'][0]['color_range'] == 'tv'
        assert abs(float(source['format']['duration']) - float(output['format']['duration'])) < .1
        report = {'kind': 'H.264 transcode of the verified code-rendered exploratory lesson', 'stream': output['streams'][0], 'duration_seconds': float(output['format']['duration']), 'bytes': args.out.stat().st_size}
        (args.log_dir / 'mp4-verification.json').write_text(json.dumps(report, indent=2))
        run.log({'export/duration_seconds': report['duration_seconds'], 'export/bytes': report['bytes'], 'export/h264_tv_pass': 1})
        print(json.dumps(report, indent=2))
    finally:
        run.finish()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--log-dir', type=Path, required=True)
    export(parser.parse_args())
