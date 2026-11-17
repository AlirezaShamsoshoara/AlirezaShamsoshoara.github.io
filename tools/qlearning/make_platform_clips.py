#!/usr/bin/env python3
"""Extract short platform clips from the verified Q-learning lesson GIF.

No new learning or animation is synthesized. The clip boundaries come from the
exporter's recorded transition timeline; GIF disposal is composited by Pillow.
"""
import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageSequence
import wandb


def extract(args):
    root = args.root.resolve()
    source = root / 'assets/media/rl/qlearning/q-update.gif'
    timeline = json.loads(args.timeline.read_text())
    intervals = {}
    elapsed = 0
    for item in timeline:
        index = item['index']
        if index not in intervals:
            intervals[index] = [elapsed, elapsed]
        elapsed += item['duration_ms']
        intervals[index][1] = elapsed
    gif = Image.open(source)
    frames = []
    decoded_elapsed = 0
    for frame in ImageSequence.Iterator(gif):
        duration = frame.info.get('duration', 0)
        if duration <= 0:
            raise ValueError('GIF frame lacks a positive duration')
        frames.append((decoded_elapsed, decoded_elapsed + duration, frame.convert('RGB').copy()))
        decoded_elapsed += duration
    if decoded_elapsed != elapsed:
        raise ValueError(f'GIF timing {decoded_elapsed} does not match timeline {elapsed}')
    target = root / 'tools/qlearning/platform-drafts/media'
    target.mkdir(parents=True, exist_ok=True)
    args.out.mkdir(parents=True, exist_ok=True)
    run = wandb.init(project='rl-education', name='qlearning-platform-short-clips', mode='offline', dir=str(args.out), config={'source': 'verified exploratory lesson GIF', 'learning_performed': False})
    try:
        manifest = []
        for name, index, episode, description in (
            ('first-goal', 210, 29, 'True-terminal goal transition 14 Right -> 15; Q(14,Right) 0 -> 0.1'),
            ('first-bootstrap', 550, 70, 'Later zero-reward transition 13 Right -> 14; Q(13,Right) 0 -> 0.0095'),
        ):
            start, end = intervals[index]
            selected, durations = [], []
            for left, right, image in frames:
                duration = min(right, end) - max(left, start)
                if duration > 0:
                    selected.append(image.quantize(colors=128))
                    durations.append(duration)
            if not selected or sum(durations) != end - start:
                raise ValueError('Incomplete clip interval')
            output = target / f'{name}.gif'
            selected[0].save(output, save_all=True, append_images=selected[1:], duration=durations, loop=0, optimize=True, disposal=2)
            clip = Image.open(output)
            output_duration = sum(frame.info.get('duration', 0) for frame in ImageSequence.Iterator(clip))
            if output_duration != end - start:
                raise ValueError('Encoded clip timing changed')
            if output.stat().st_size >= 25_000_000:
                raise ValueError('Clip exceeds Medium image size limit')
            final = selected[-1].convert('RGB')
            final.save(target / f'{name}.png')
            manifest.append({
                'name': name, 'recorded_transition_index': index, 'recorded_episode': episode,
                'description': description, 'source_interval_ms': [start, end],
                'duration_ms': output_duration, 'encoded_frames': clip.n_frames,
                'width': clip.width, 'height': clip.height, 'bytes': output.stat().st_size,
                'sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
                'interpretation': 'Single recorded transition extracted from the full edited lesson, not a complete episode, new training run, or benchmark.'
            })
        report = {
            'source_gif_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'source_duration_ms': elapsed, 'clips': manifest,
            'learning_performed': False,
            'provenance': 'Byte-derived clips of the verified code-rendered lesson; every displayed Q-value comes from that original recording.'
        }
        (target / 'manifest.json').write_text(json.dumps(report, indent=2))
        (args.out / 'clip-verification.json').write_text(json.dumps(report, indent=2))
        run.log({'clips/count': len(manifest), 'clips/max_bytes': max(item['bytes'] for item in manifest), 'clips/max_seconds': max(item['duration_ms'] for item in manifest) / 1000})
        print(json.dumps(report, indent=2))
    finally:
        run.finish()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--timeline', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    extract(parser.parse_args())
