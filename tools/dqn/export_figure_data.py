#!/usr/bin/env python3
"""Export the data the DQN post's figures load, from the recorded training run.

Inputs are the rerun of the committed recipe (verified identical to every committed
checkpoint), its per-transition and per-update logs, full weight snapshots at a few
updates, and the committed checkpoints. Every value written here comes from the
repository's own PyTorch network; the browser only draws it.

Usage:
  export_figure_data.py --repo <RL-from-zero copy> --record <pass dir> --snapshots <snapshots.pt>
                        --checkpoints <dir> --gif <repository GIF> --revision <sha> --out <dir>
"""
import argparse
import base64
import hashlib
import json
import pathlib
import sys

import numpy as np

FEATURED = [
    (1, 'first-update', 'The first gradient step'),
    (32, 'first-goal-sample', 'First minibatch with a goal transition'),
    (251, 'after-first-sync', 'First update after a target sync'),
    (13532, 'first-greedy-goal', 'Right after the first goal with no random steps'),
    (57849, 'selected-checkpoint', 'The update at the selected checkpoint'),
]
NX, NY = 72, 56
STARTS = [round(-0.60 + 0.02 * i, 2) for i in range(11)]
EXPLORER_STEPS = [5000] + list(range(10000, 300001, 10000))


def b64(array):
    return base64.b64encode(np.ascontiguousarray(array).tobytes()).decode('ascii')


def r6(x):
    return float(f'{float(x):.6g}')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=pathlib.Path, required=True)
    p.add_argument('--record', type=pathlib.Path, required=True)
    p.add_argument('--snapshots', type=pathlib.Path, required=True)
    p.add_argument('--checkpoints', type=pathlib.Path, required=True)
    p.add_argument('--gif', type=pathlib.Path, required=True)
    p.add_argument('--revision', required=True)
    p.add_argument('--out', type=pathlib.Path, required=True)
    a = p.parse_args()
    sys.path.insert(0, str(a.repo.resolve()))
    import os
    os.chdir(a.repo)
    import torch
    import gymnasium as gym
    from deepQN.dqn.agent import DQNAgent
    from deepQN.dqn.config import Config

    cfg = Config.from_yaml('deepQN/configs/mountaincar_exploration.yaml')
    env = gym.make('MountainCar-v0')
    agent = DQNAgent(env.observation_space, env.action_space, cfg.hidden_sizes, cfg.activation, cfg.lr, cfg.gamma,
                     cfg.target_update_interval, cfg.max_grad_norm, cfg.double_dqn, 'cpu', cfg.normalize_observations)
    T = dict(np.load(a.record / 'transitions.npz'))
    U = dict(np.load(a.record / 'updates.npz'))
    snaps = torch.load(a.snapshots, map_location='cpu', weights_only=False)
    a.out.mkdir(parents=True, exist_ok=True)

    positions = np.linspace(-1.2, 0.6, NX + 1)[:-1] + 1.8 / NX / 2
    velocities = np.linspace(-0.07, 0.07, NY + 1)[:-1] + 0.14 / NY / 2
    grid_states = torch.tensor([[x, v] for v in velocities for x in positions], dtype=torch.float32)  # row = velocity

    def evaluate_grid(state_dict):
        agent.q_network.load_state_dict(state_dict)
        with torch.no_grad():
            q = agent.q_network(agent._encode(grid_states)).numpy()
        return q.max(1), q.argmax(1).astype(np.uint8)

    # First transition index that visited each map cell (states the run had seen by then).
    ix = np.clip(((T['obs'][:, 0] + 1.2) / 1.8 * NX).astype(int), 0, NX - 1)
    iy = np.clip(((T['obs'][:, 1] + 0.07) / 0.14 * NY).astype(int), 0, NY - 1)
    first_visit = np.full(NX * NY, np.iinfo(np.int32).max, np.int64)
    np.minimum.at(first_visit, iy * NX + ix, np.arange(len(ix)))
    grid = {'first_visit': b64(first_visit.astype('<i4')), 'never_visited': int((first_visit == np.iinfo(np.int32).max).sum()),
            'nx': NX, 'ny': NY, 'positions': [r6(x) for x in positions], 'velocities': [r6(v) for v in velocities],
            'order': 'row-major, rows are velocities from low to high, columns are positions from left to right'}

    # Episodes from the transition log.
    ended = (T['terminated'] | T['truncated']).astype(bool)
    ends = np.flatnonzero(ended)
    starts = np.concatenate([[0], ends[:-1] + 1])
    episodes = {
        'end_step': (ends + 1).tolist(),
        'length': (ends - starts + 1).tolist(),
        'goal': T['terminated'][ends].astype(int).tolist(),
        'explore_fraction': [round(float(T['exploratory'][s:e + 1].mean()), 3) for s, e in zip(starts, ends)],
        'max_position': [round(float(T['next_obs'][s:e + 1, 0].max()), 4) for s, e in zip(starts, ends)],
    }
    goal = np.array(episodes['goal'], bool)
    expl = np.array(episodes['explore_fraction'])
    first_goal = int(np.argmax(goal))
    greedy = np.flatnonzero(goal & (expl == 0))
    syncs = (np.flatnonzero(U['synced']) + 1).tolist()

    def since_sync(update):
        previous = [s for s in syncs if s < update]
        return update - (previous[-1] if previous else 0) - 1

    # Figure 1: featured updates, full minibatches and value maps before and after.
    featured = []
    for number, key, label in FEATURED:
        u = number - 1
        snap = snaps[number]
        step = int(U['step'][u])
        idx = U['indices'][u].astype(int)
        v_before, a_before = evaluate_grid(snap['online_before'])
        v_after, a_after = evaluate_grid(snap['online_after'])
        delta = v_after - v_before
        scale = float(np.abs(delta).max()) or 1.0
        done = T['terminated'][idx].astype(int)
        tracked = int(np.argmax(done)) if key == 'first-goal-sample' else 0
        recent = list(range(step - 4, step))
        episode = int(np.searchsorted(ends, step - 1))
        episode_start = int(starts[episode])
        episode_path = [[r6(x) for x in T['obs'][g]] for g in range(episode_start, step)] + [[r6(x) for x in T['next_obs'][step - 1]]]
        featured.append({
            'number': number, 'key': key, 'label': label, 'step': step,
            'epsilon': r6(T['epsilon'][step - 1]), 'buffer_size': int(min(step, cfg.buffer_size)),
            'updates_since_sync': since_sync(number), 'syncs_after': bool(U['synced'][u]),
            'episode': episode + 1, 'episode_step': step - episode_start, 'episode_path': episode_path,
            'episode_explore_fraction': round(float(T['exploratory'][episode_start:step].mean()), 3),
            'loss': r6(U['loss'][u]), 'td_error': r6(U['td_error'][u]), 'tracked': tracked,
            'recent': [{'s': [r6(x) for x in T['obs'][g]], 'a': int(T['action'][g]), 's2': [r6(x) for x in T['next_obs'][g]],
                        'explore': int(T['exploratory'][g]), 'pulse_start': int(T['pulse_start'][g]), 'hold_left': int(T['hold_remaining'][g]),
                        'done': int(T['terminated'][g]), 'truncated': int(T['truncated'][g])} for g in recent],
            'batch': {
                'index': idx.tolist(), 'age': (step - 1 - idx).tolist(),
                's': [[r6(x) for x in T['obs'][g]] for g in idx], 'a': T['action'][idx].astype(int).tolist(),
                'r': [r6(x) for x in T['reward'][idx]], 's2': [[r6(x) for x in T['next_obs'][g]] for g in idx], 'done': done.tolist(),
                'q_before': [[r6(x) for x in row] for row in snap['q_before_all']],
                'q_after': [[r6(x) for x in row] for row in snap['q_after_all']],
                'q_next_online': [[r6(x) for x in row] for row in snap['q_next_online_all']],
                'q_next_target': [[r6(x) for x in row] for row in snap['q_next_target_all']],
                'a_star': U['a_star'][u].astype(int).tolist(), 'y': [r6(x) for x in U['target'][u]],
            },
            'grid': {'v_before': b64(np.round(v_before * 100).astype('<i2')), 'a_before': b64(a_before),
                     'v_after': b64(np.round(v_after * 100).astype('<i2')), 'a_after': b64(a_after),
                     'delta': b64(np.round(delta / scale * 32767).astype('<i2')), 'delta_scale': r6(scale),
                     'delta_mean_abs': r6(np.abs(delta).mean()), 'cells_changed_over_1e-3': int((np.abs(delta) > 1e-3).sum()),
                     'v_range': [r6(v_before.min()), r6(v_before.max())]},
        })
        # Consistency: the recorded per-sample values match the full snapshots.
        q_sa = np.take_along_axis(np.asarray(snap['q_before_all']), np.array(featured[-1]['batch']['a'])[:, None], 1)[:, 0]
        assert np.allclose(q_sa, U['q_sa_before'][u], atol=1e-6)
    update_doc = {'schema': 1, 'grid': grid, 'gamma': cfg.gamma, 'lr': cfg.lr, 'batch_size': cfg.batch_size,
                  'train_freq': cfg.train_freq, 'target_update_interval': cfg.target_update_interval,
                  'learning_starts': cfg.learning_starts, 'buffer_capacity': cfg.buffer_size, 'updates': featured}
    (a.out / 'dqn-update-steps.json').write_text(json.dumps(update_doc, separators=(',', ':')))

    # Figure 2: targets between syncs (first 1,500 updates) and the long view.
    window = 1500
    probe_names = ['start, at rest', 'valley, moving right fast', 'left hill, at rest', 'left hill, heading right',
                   'right slope, climbing fast', 'right slope, sliding back', 'just short of the flag', 'valley, heading left']
    report = json.loads((a.record / 'record-report.json').read_text())
    sync_doc = {
        'schema': 1, 'window': window, 'target_update_interval': cfg.target_update_interval, 'syncs': [s for s in syncs if s <= window],
        'mean_target': [r6(x) for x in U['target'][:window].mean(1)], 'mean_q': [r6(x) for x in U['q_sa_before'][:window].mean(1)],
        'loss': [r6(x) for x in U['loss'][:window]],
        'probes': [{'state': report['probe_states'][i], 'name': probe_names[i],
                    'online': [r6(x) for x in U['probe_online'][:window, i].max(1)],
                    'target': [r6(x) for x in U['probe_target'][:window, i].max(1)]} for i in range(len(probe_names))],
        'long': {'every': 100, 'update': list(range(1, len(U['step']) + 1, 100)),
                 'mean_target': [r6(x) for x in U['target'][::100].mean(1)], 'loss': [r6(x) for x in U['loss'][::100]]},
    }
    (a.out / 'dqn-target-sync.json').write_text(json.dumps(sync_doc, separators=(',', ':')))

    # Figure 4: committed checkpoints, value maps and greedy rollouts from fixed starts.
    def rollout(start):
        env.reset(seed=0)
        env.unwrapped.state = np.array([start, 0.0])
        obs = np.array(env.unwrapped.state, dtype=np.float32)
        path, actions = [env.unwrapped.state.copy()], []
        for _ in range(200):
            action = agent.act(obs, epsilon=0.0, deterministic=True)
            obs, _, terminated, truncated, _ = env.step(action)
            path.append(np.array(env.unwrapped.state, dtype=np.float64))
            actions.append(action)
            if terminated or truncated:
                break
        return np.array(path), actions, bool(terminated)

    names = [f'checkpoint_{s}.pt' for s in EXPLORER_STEPS] + ['best.pt']
    checkpoints = []
    for name in names:
        data = torch.load(a.checkpoints / name, map_location='cpu', weights_only=True)
        v, act = evaluate_grid(data['q_network'])
        agent.load_state_dict(data)
        rolls = []
        for start in STARTS:
            path, actions, success = rollout(start)
            rolls.append({'start': start, 'steps': len(actions), 'goal': success,
                          'x': b64(np.round(path[:, 0] * 10000).astype('<i2')), 'v': b64(np.round(path[:, 1] * 100000).astype('<i2')),
                          'actions': b64(np.array(actions, np.uint8))})
        checkpoints.append({'name': name, 'step': int(data['step']), 'updates': int(data['train_steps']),
                            'sha256': hashlib.sha256((a.checkpoints / name).read_bytes()).hexdigest(),
                            'v': b64(np.round(v * 100).astype('<i2')), 'a': b64(act),
                            'v_range': [r6(v.min()), r6(v.max())], 'goals': sum(r['goal'] for r in rolls), 'rollouts': rolls})
    training_doc = {
        'schema': 1, 'grid': grid, 'starts': STARTS, 'scales': {'x': 10000, 'v': 100000, 'value': 100},
        'checkpoints': checkpoints, 'episodes': episodes,
        'milestones': {'first_goal_episode': first_goal + 1, 'first_goal_step': int(ends[first_goal] + 1),
                       'warmup_episodes': int((ends < cfg.learning_starts).sum()), 'warmup_goals': int(goal[ends < cfg.learning_starts].sum()),
                       'first_greedy_goal_episode': int(greedy[0] + 1), 'first_greedy_goal_step': int(ends[greedy[0]] + 1),
                       'greedy_goal_episodes': int(len(greedy)), 'episodes': int(len(ends)), 'goal_episodes': int(goal.sum()),
                       'first_update_step': int(U['step'][0]), 'updates': int(len(U['step'])), 'syncs': len(syncs)},
        'epsilon': {'start': cfg.epsilon_start, 'end': cfg.epsilon_end, 'decay_steps': cfg.epsilon_decay_steps,
                    'learning_starts': cfg.learning_starts, 'hold_min': cfg.exploration_hold_min, 'hold_max': cfg.exploration_hold_max},
    }
    (a.out / 'dqn-checkpoints.json').write_text(json.dumps(training_doc, separators=(',', ':')))

    summary = {
        'revision': a.revision, 'gif_sha256': hashlib.sha256(a.gif.read_bytes()).hexdigest(),
        'record': {k: report[k] for k in ('transitions', 'updates', 'checkpoints_compared', 'checkpoints_identical', 'torch', 'gymnasium', 'numpy', 'threads', 'transitions_sha256')},
        'files': {name: {'bytes': (a.out / name).stat().st_size, 'sha256': hashlib.sha256((a.out / name).read_bytes()).hexdigest()}
                  for name in ('dqn-update-steps.json', 'dqn-target-sync.json', 'dqn-checkpoints.json')},
        'featured': [{k: f[k] for k in ('number', 'key', 'step', 'epsilon', 'updates_since_sync', 'loss', 'tracked')} | {
            'delta_scale': f['grid']['delta_scale'], 'cells_changed': f['grid']['cells_changed_over_1e-3'],
            'tracked_values': {'s': f['batch']['s'][f['tracked']], 'a': f['batch']['a'][f['tracked']], 's2': f['batch']['s2'][f['tracked']],
                               'done': f['batch']['done'][f['tracked']], 'q_before': f['batch']['q_before'][f['tracked']],
                               'q_next_online': f['batch']['q_next_online'][f['tracked']], 'q_next_target': f['batch']['q_next_target'][f['tracked']],
                               'a_star': f['batch']['a_star'][f['tracked']], 'y': f['batch']['y'][f['tracked']], 'q_after': f['batch']['q_after'][f['tracked']]}}
                     for f in featured],
        'checkpoint_goals': {c['name']: c['goals'] for c in checkpoints},
        'milestones': training_doc['milestones'],
    }
    (a.out / 'export-summary.json').write_text(json.dumps(summary, indent=1))
    print(json.dumps(summary, indent=1))


if __name__ == '__main__':
    main()
