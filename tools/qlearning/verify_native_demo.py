#!/usr/bin/env python3
"""Verify a real repository Q-table and its native FrozenLake demonstration.

Loads a trusted repository checkpoint with weights_only=True and never trains it.
Writes sanitized media provenance plus an unfiltered same-map evaluation report.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

import gymnasium as gym
import numpy as np
from PIL import Image, ImageSequence
import torch
import wandb
import yaml


def run(args):
    os.environ['SDL_VIDEODRIVER'] = 'dummy'
    spec = importlib.util.spec_from_file_location('qlearning_reference', args.agent)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    cfg = yaml.safe_load(args.config.read_text())
    saved = torch.load(args.checkpoint, map_location='cpu', weights_only=True)
    table = saved['q_table'].detach().cpu().numpy().copy()
    assert table.shape == (64, 4) and np.isfinite(table).all()
    assert int(saved['step']) == 1011
    agent = module.QLearningAgent(64, 4, cfg['alpha'], cfg['gamma'], cfg['epsilon_start'], cfg['epsilon_end'], cfg['epsilon_decay'])
    agent.load_state_dict(saved)
    before = agent.state_dict()
    args.out.mkdir(parents=True, exist_ok=True)
    args.media.mkdir(parents=True, exist_ok=True)
    run = wandb.init(project='rl-education', name='qlearning-repository-native-demo-check', mode='offline', dir=str(args.out), config={'source_revision': args.revision, 'env_id': cfg['env_id'], 'env_kwargs': cfg['env_kwargs'], 'policy': 'saved checkpoint, deterministic first argmax, no training'})
    env = gym.make(cfg['env_id'], render_mode='rgb_array', **cfg['env_kwargs'])
    results = []
    try:
        desc = [b''.join(row).decode() for row in env.unwrapped.desc]
        first_frames = []
        for episode in range(200):
            seed = 10000 + episode if episode < 100 else 20000 + episode - 100
            state, _ = env.reset(seed=seed)
            states, actions, rewards = [int(state)], [], []
            if episode == 0:
                first_frames.append(env.render().copy())
            terminated = truncated = False
            for _ in range(cfg['max_steps_per_episode']):
                action = agent.act(int(state), deterministic=True)
                state, reward, terminated, truncated, _ = env.step(action)
                states.append(int(state)); actions.append(int(action)); rewards.append(float(reward))
                if episode == 0:
                    first_frames.append(env.render().copy())
                if terminated or truncated:
                    break
            result = {'seed': seed, 'states': states, 'actions': actions, 'rewards': rewards,
                      'length': len(actions), 'return': sum(rewards),
                      'discounted_return': sum(cfg['gamma']**i * reward for i, reward in enumerate(rewards)),
                      'terminated': bool(terminated), 'truncated': bool(truncated),
                      'goal': int(state) == 63 and sum(rewards) == 1}
            results.append(result)
        assert all(r['goal'] and r['length'] == 16 for r in results)
        assert np.array_equal(agent.Q, before['q_table']) and agent.global_step == before['global_step']
        assert all(r['states'] == results[0]['states'] for r in results)
        Image.fromarray(first_frames[0]).save(args.media / 'frozenlake-8x8.png')
        Image.fromarray(first_frames[-1]).save(args.out / 'native-goal.png')
        # The copied committed GIF remains the main demonstration. Verify its actual bytes.
        gif_path = args.media / 'frozenlake-8x8.gif'
        gif = Image.open(gif_path)
        durations = [frame.info.get('duration', 0) for frame in ImageSequence.Iterator(gif)]
        assert gif.n_frames > 1 and all(duration > 0 for duration in durations)
        provenance = {
            'kind': 'native Gymnasium FrozenLake rendering of the repository saved greedy policy',
            'source_revision': args.revision,
            'source_gif_path': 'Qlearning/assets/qlearning_frozenlake_8x8.gif',
            'source_gif_sha256': hashlib.sha256(gif_path.read_bytes()).hexdigest(),
            'checkpoint_sha256': hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
            'checkpoint_training_episode': int(saved['step']),
            'recipe_training_episodes': cfg['total_episodes'],
            'env_id': cfg['env_id'], 'env_kwargs': cfg['env_kwargs'], 'map': desc,
            'n_states': 64, 'n_actions': 4, 'alpha': cfg['alpha'], 'gamma': cfg['gamma'],
            'interaction_cap': cfg['max_steps_per_episode'],
            'seed_ranges': [[10000, 10099], [20000, 20099]],
            'evaluated_episodes': len(results), 'goal_episodes': sum(r['goal'] for r in results),
            'mean_length': sum(r['length'] for r in results) / len(results),
            'demo_states': results[0]['states'], 'demo_actions': results[0]['actions'],
            'gif_encoded_frames': gif.n_frames, 'gif_duration_ms': sum(durations),
            'gymnasium_version': gym.__version__,
            'interpretation': 'Same fixed map and start state; repeated deterministic rollouts are not independent maps or generalization evidence. The committed GIF is a selected showcase, not the evaluation statistic.',
            'training_performed': False,
        }
        (args.media / 'frozenlake-8x8.json').write_text(json.dumps(provenance, indent=2))
        (args.out / 'native-evaluation.json').write_text(json.dumps({'provenance': provenance, 'episodes': results}, indent=2))
        run.log({'native/goals': provenance['goal_episodes'], 'native/episodes': len(results), 'native/mean_length': provenance['mean_length'], 'native/table_unchanged': 1})
        print(json.dumps({k: provenance[k] for k in ('checkpoint_training_episode', 'evaluated_episodes', 'goal_episodes', 'mean_length', 'demo_states', 'gif_encoded_frames', 'gif_duration_ms')}), flush=True)
    finally:
        env.close()
        run.finish()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', type=Path, required=True)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--revision', required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--media', type=Path, default=Path(__file__).resolve().parents[2] / 'assets/media/rl/qlearning')
    run(parser.parse_args())
