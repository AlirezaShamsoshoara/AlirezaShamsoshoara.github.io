#!/usr/bin/env python3
"""Transcode verified article media to H.264 MP4 and check its format and timing."""
import argparse
import json
from pathlib import Path
import subprocess

import wandb


def probe(path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_name,pix_fmt,color_range,color_space,color_transfer,color_primaries,width,height', '-of', 'json', str(path)], text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def export(args):
    if args.source.resolve() == args.out.resolve():
        raise ValueError('The output must not overwrite the source media')
    args.log_dir.mkdir(parents=True, exist_ok=True)
    run = wandb.init(project='rl-education', name='rl-article-h264-video-export', mode='offline', dir=str(args.log_dir))
    try:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(args.source), '-vf', 'pad=ceil(iw/2)*2:ceil(ih/2)*2,scale=out_range=tv:out_color_matrix=bt709,format=yuv420p', '-c:v', 'libx264', '-x264-params', 'colorprim=bt709:transfer=bt709:colormatrix=bt709', '-threads', '2', '-preset', 'medium', '-crf', '20', '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-movflags', '+faststart', str(args.out)], text=True, capture_output=True, check=True)
        source, output = probe(args.source), probe(args.out)
        stream = output['streams'][0]
        if (stream['codec_name'], stream['pix_fmt'], stream['color_range']) != ('h264', 'yuv420p', 'tv'):
            raise ValueError('Expected H.264, yuv420p and TV color range')
        if any(stream.get(key) != 'bt709' for key in ('color_space', 'color_transfer', 'color_primaries')):
            raise ValueError('Expected bt709 color metadata')
        difference = abs(float(source['format']['duration']) - float(output['format']['duration']))
        if difference >= .1:
            raise ValueError('Source and output durations differ by at least 0.1 seconds')
        report = {'kind': 'H.264 transcode of verified article media', 'stream': stream, 'duration_seconds': float(output['format']['duration']), 'duration_difference_seconds': difference, 'bytes': args.out.stat().st_size}
        (args.log_dir / 'mp4-verification.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
        run.log({'export/duration_seconds': report['duration_seconds'], 'export/bytes': report['bytes'], 'export/h264_tv_pass': 1})
        print(json.dumps(report, indent=2))
        return report
    finally:
        run.finish()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--log-dir', type=Path, required=True)
    export(parser.parse_args(argv))


if __name__ == '__main__':
    main()
