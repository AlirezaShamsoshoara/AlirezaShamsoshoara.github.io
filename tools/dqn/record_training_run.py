#!/usr/bin/env python3
"""Re-run the committed DQN MountainCar recipe and record what the blog figures need.

The run uses the repository's own code and config unchanged. The recording hooks
only read values: they make no extra random draws and change no parameters, so the
rerun can be compared tensor by tensor with the saved checkpoints.

Usage:
  record_training_run.py --repo <RL-from-zero copy> --original <saved checkpoint dir>
                    --out <dir> [--snapshot-updates 1,2,3]
"""
import argparse
import copy
import hashlib
import json
import os
import pathlib
import sys
import time

import numpy as np

PROBE_STATES = [
    (-0.50, 0.000),   # start region, at rest
    (-0.50, 0.040),   # valley floor, moving right fast
    (-1.00, 0.000),   # high on the left hill, at rest
    (-0.90, 0.030),   # left hill, heading right
    (0.00, 0.050),    # climbing the right slope fast
    (0.20, -0.020),   # right slope, sliding back
    (0.45, 0.030),    # just short of the flag, still climbing
    (-0.30, -0.040),  # valley, heading left
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=pathlib.Path, required=True)
    parser.add_argument('--original', type=pathlib.Path, required=True)
    parser.add_argument('--out', type=pathlib.Path, required=True)
    parser.add_argument('--config', default='deepQN/configs/mountaincar_exploration.yaml')
    parser.add_argument('--snapshot-updates', default='')
    args = parser.parse_args()
    repo = args.repo.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    os.chdir(repo)
    sys.path.insert(0, str(repo))
    (repo / 'deepQN/logs').mkdir(parents=True, exist_ok=True)

    import torch
    import gymnasium as gym
    import deepQN.main as M
    from deepQN.dqn.agent import DQNAgent
    from deepQN.dqn.config import Config
    from deepQN.dqn.exploration import ActionHoldExplorer
    from deepQN.dqn.replay_buffer import ReplayBuffer

    cfg = Config.from_yaml(args.config)
    total = cfg.total_steps
    snapshot_updates = {int(x) for x in args.snapshot_updates.split(',') if x.strip()}

    # Per-transition log, filled in the order the training loop stores replay data.
    T = {
        'obs': np.zeros((total, 2), np.float32), 'next_obs': np.zeros((total, 2), np.float32),
        'action': np.zeros(total, np.int8), 'reward': np.zeros(total, np.float32),
        'terminated': np.zeros(total, np.uint8), 'truncated': np.zeros(total, np.uint8),
        'exploratory': np.zeros(total, np.int8), 'pulse_start': np.zeros(total, np.uint8),
        'hold_remaining': np.zeros(total, np.int16), 'epsilon': np.zeros(total, np.float32),
    }
    n_updates_max = total // cfg.train_freq + 2
    batch = cfg.batch_size
    U = {
        'step': np.zeros(n_updates_max, np.int32),
        'indices': np.zeros((n_updates_max, batch), np.int32),
        'q_sa_before': np.zeros((n_updates_max, batch), np.float32),
        'a_star': np.zeros((n_updates_max, batch), np.int8),
        'q_target_a_star': np.zeros((n_updates_max, batch), np.float32),
        'target': np.zeros((n_updates_max, batch), np.float32),
        'q_sa_after': np.zeros((n_updates_max, batch), np.float32),
        'loss': np.zeros(n_updates_max, np.float32),
        'td_error': np.zeros(n_updates_max, np.float32),
        'synced': np.zeros(n_updates_max, np.uint8),
        'probe_online': np.zeros((n_updates_max, len(PROBE_STATES), 3), np.float32),
        'probe_target': np.zeros((n_updates_max, len(PROBE_STATES), 3), np.float32),
    }
    state = {'n': 0, 'u': 0, 'choice': None, 'step_flags': None, 'slot_to_global': None, 'indices': None}
    snapshots = {}

    # 1) Action selection: read the explorer's decision without changing it.
    original_act = ActionHoldExplorer.act

    def act(self, agent, obs, epsilon):
        remaining_before = self.remaining
        action, exploratory = original_act(self, agent, obs, epsilon)
        state['choice'] = (float(epsilon), bool(exploratory), remaining_before == 0 and bool(exploratory), int(self.remaining))
        return action, exploratory

    ActionHoldExplorer.act = act

    # 2) Environment: record terminated and truncated flags of each step.
    class StepRecorder(gym.Wrapper):
        def step(self, action):
            result = self.env.step(action)
            state['step_flags'] = (bool(result[2]), bool(result[3]))
            return result

    original_make_env = M.make_env

    def make_env(*a, **k):
        return StepRecorder(original_make_env(*a, **k))

    M.make_env = make_env

    # 3) Replay: map buffer slots to global transition indices.
    original_add = ReplayBuffer.add

    def add(self, obs, action, reward, next_obs, done):
        slot = self.ptr
        original_add(self, obs, action, reward, next_obs, done)
        if state['slot_to_global'] is None:
            state['slot_to_global'] = np.full(self.capacity, -1, np.int64)
        g = state['n']
        state['slot_to_global'][slot] = g
        T['obs'][g] = obs
        T['next_obs'][g] = next_obs
        T['action'][g] = action
        T['reward'][g] = reward
        terminated, truncated = state['step_flags']
        assert float(done) == float(terminated)
        T['terminated'][g] = terminated
        T['truncated'][g] = truncated
        epsilon, exploratory, pulse_start, remaining = state['choice']
        T['epsilon'][g], T['exploratory'][g], T['pulse_start'][g], T['hold_remaining'][g] = epsilon, exploratory, pulse_start, remaining
        state['n'] = g + 1

    ReplayBuffer.add = add

    # Same code as ReplayBuffer.sample at the pinned revision, plus a copy of the indices.
    def sample(self, batch_size):
        if not self.can_sample(batch_size):
            raise ValueError('Insufficient samples in buffer')
        indices = np.random.randint(0, self.size, size=batch_size)
        state['indices'] = indices.copy()
        return {
            'obs': torch.as_tensor(self.obs[indices], device=self.device),
            'actions': torch.as_tensor(self.actions[indices], device=self.device),
            'rewards': torch.as_tensor(self.rewards[indices], device=self.device),
            'next_obs': torch.as_tensor(self.next_obs[indices], device=self.device),
            'dones': torch.as_tensor(self.dones[indices], device=self.device),
        }

    ReplayBuffer.sample = sample

    # 4) Updates: read values before and after the unchanged update.
    original_update = DQNAgent.update
    probes = torch.tensor(PROBE_STATES, dtype=torch.float32)

    def update(self, data):
        u = state['u']
        with torch.no_grad():
            obs = self._encode(data['obs'].to(self.device, dtype=torch.float32))
            next_obs = self._encode(data['next_obs'].to(self.device, dtype=torch.float32))
            actions = data['actions'].long()
            q_before = self.q_network(obs)
            q_next_online = self.q_network(next_obs)
            q_next_target = self.target_q_network(next_obs)
        number = self.train_steps + 1
        if number in snapshot_updates:
            snapshots[number] = {
                'online_before': copy.deepcopy(self.q_network.state_dict()),
                'target_before': copy.deepcopy(self.target_q_network.state_dict()),
            }
        stats = original_update(self, data)
        with torch.no_grad():
            q_after = self.q_network(obs)
            encoded_probes = self._encode(probes)
            probe_online = self.q_network(encoded_probes)
            probe_target = self.target_q_network(encoded_probes)
        a_star = q_next_online.argmax(dim=1)
        target_vals = q_next_target.gather(1, a_star.unsqueeze(1)).squeeze(1)
        y = data['rewards'].float() + self.gamma * (1.0 - data['dones'].float()) * target_vals
        assert abs(float(y.mean()) - stats.target_value) < 1e-4, (float(y.mean()), stats.target_value)
        U['step'][u] = state['n']
        U['indices'][u] = state['slot_to_global'][state['indices']]
        U['q_sa_before'][u] = q_before.gather(1, actions.unsqueeze(1)).squeeze(1).numpy()
        U['a_star'][u] = a_star.numpy()
        U['q_target_a_star'][u] = target_vals.numpy()
        U['target'][u] = y.numpy()
        U['q_sa_after'][u] = q_after.gather(1, actions.unsqueeze(1)).squeeze(1).numpy()
        U['loss'][u], U['td_error'][u] = stats.loss, stats.td_error
        U['synced'][u] = int(self.train_steps % self.target_update_interval == 0)
        U['probe_online'][u], U['probe_target'][u] = probe_online.numpy(), probe_target.numpy()
        if number in snapshots:
            snapshots[number].update({
                'online_after': copy.deepcopy(self.q_network.state_dict()),
                'target_after': copy.deepcopy(self.target_q_network.state_dict()),
                'q_before_all': q_before.numpy().copy(), 'q_after_all': q_after.numpy().copy(),
                'q_next_online_all': q_next_online.numpy().copy(), 'q_next_target_all': q_next_target.numpy().copy(),
            })
        state['u'] = u + 1
        return stats

    DQNAgent.update = update

    started = time.time()
    result = M.train(config=args.config, wandb_key='')
    seconds = time.time() - started
    n, nu = state['n'], state['u']
    assert n == total, (n, total)

    np.savez_compressed(out / 'transitions.npz', **T)
    np.savez_compressed(out / 'updates.npz', **{k: v[:nu] for k, v in U.items()})
    if snapshots:
        torch.save(snapshots, out / 'snapshots.pt')

    # Compare every committed checkpoint with the rerun, tensor by tensor.
    def same(a, b):
        if isinstance(a, torch.Tensor):
            return isinstance(b, torch.Tensor) and a.dtype == b.dtype and a.shape == b.shape and torch.equal(a, b)
        if isinstance(a, dict):
            return isinstance(b, dict) and a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
        if isinstance(a, (list, tuple)):
            return isinstance(b, (list, tuple)) and len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
        return a == b

    comparison = {}
    for path in sorted(args.original.glob('*.pt')):
        mine = repo / cfg.checkpoint_dir / path.name
        a = torch.load(path, map_location='cpu', weights_only=True)
        b = torch.load(mine, map_location='cpu', weights_only=True) if mine.exists() else None
        comparison[path.name] = {
            'identical': b is not None and same(a, b),
            'weights_identical': b is not None and same(a['q_network'], b['q_network']) and same(a['target_q_network'], b['target_q_network']),
            'step': a.get('step'), 'train_steps': a.get('train_steps'),
        }
    identical = sum(v['identical'] for v in comparison.values())
    report = {
        'config': args.config, 'seconds': round(seconds, 1), 'transitions': n, 'updates': nu,
        'train_result': {k: (float(v) if isinstance(v, (float, np.floating)) else v) for k, v in result.items()},
        'threads': torch.get_num_threads(), 'torch': torch.__version__, 'gymnasium': gym.__version__, 'numpy': np.__version__,
        'checkpoints_compared': len(comparison), 'checkpoints_identical': identical,
        'first_mismatch': next((k for k, v in comparison.items() if not v['identical']), None),
        'comparison': comparison, 'probe_states': PROBE_STATES,
        'snapshot_updates': sorted(snapshots),
        'transitions_sha256': hashlib.sha256((out / 'transitions.npz').read_bytes()).hexdigest(),
    }
    (out / 'record-report.json').write_text(json.dumps(report, indent=1))
    print(json.dumps({k: v for k, v in report.items() if k != 'comparison'}, indent=1))


if __name__ == '__main__':
    main()
