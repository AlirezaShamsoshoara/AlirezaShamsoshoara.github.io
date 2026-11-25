// Locks every recorded number the DQN post states to the exported data: node tools/dqn/data.test.mjs
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { runExplorationProbe, pulseStartProbability } from '../../assets/js/rl/dqn-core.mjs';

const root = new URL('../../', import.meta.url);
const read = path => readFileSync(new URL(path, root), 'utf8');
const json = path => JSON.parse(read(path));
const updates = json('assets/media/rl/dqn/dqn-update-steps.json');
const sync = json('assets/media/rl/dqn/dqn-target-sync.json');
const training = json('assets/media/rl/dqn/dqn-checkpoints.json');
const native = json('assets/media/rl/dqn/mountaincar-dqn.json');
const post = read('_posts/2026-11-23-dqn-when-a-table-is-not-enough.md');
const text = post.replace(/\s+/g, ' ');
const minus = x => x.replace(/-/g, '\u2212');
const round = (x, d) => Number(x.toFixed(d));

const tests = [];
const test = (name, fn) => tests.push([name, fn]);
const says = (...phrases) => phrases.forEach(p => assert.ok(text.includes(p), `the post should say: ${p}`));

test('network size: 2 inputs, two layers of 128, 3 outputs', () => {
  const params = 2 * 128 + 128 + 128 * 128 + 128 + 128 * 3 + 3;
  assert.equal(params, 17283);
  says('17,283 weights and biases');
});

test('update 1 worked example', () => {
  const u = updates.updates.find(x => x.number === 1), b = u.batch, t = u.tracked;
  assert.equal(u.step, 20000);
  assert.equal(b.a[t], 0);
  assert.deepEqual(b.s[t].map(x => round(x, 4)), [-1.1154, 0.0145]);
  assert.deepEqual(b.q_next_online[t].map(x => round(x, 4)), [-0.1231, -0.1478, -0.3092]);
  assert.deepEqual(b.q_next_target[t], b.q_next_online[t], 'before the first sync the target network is an exact copy');
  assert.equal(b.a_star[t], 0);
  assert.equal(round(b.y[t], 3), -1.122);
  assert.equal(round(-1 + 0.99 * b.q_next_target[t][0], 3), -1.122);
  assert.equal(round(b.q_before[t][0], 4), -0.1229);
  assert.equal(round(b.q_after[t][0], 4), -0.1424);
  assert.equal(round(b.y[t] - b.q_before[t][0], 3), -0.999);
  assert.equal(Math.round((b.q_after[t][0] - b.q_before[t][0]) / (b.y[t] - b.q_before[t][0]) * 100), 2);
  assert.equal(round(u.grid.delta_scale, 3), 0.022);
  assert.equal(u.grid['cells_changed_over_1e-3'], 4032);
  assert.equal(updates.grid.nx * updates.grid.ny, 4032);
  assert.equal(b.age[t], 3606);
  says('3,606 steps before this update', 'position −1.115', 'velocity 0.0145', '−0.1231 (left), −0.1478 (none) and −0.3092 (right)', 'target = −1 + 0.99 * (1 - 0) * (−0.1231) = −1.122',
    'TD error = −1.122 - (−0.1229) = −0.999', 'from −0.1229 to −0.1424', 'about 2% of the way', 'every one of the 4,032 cells on the map, by up to 0.022');
});

test('update 32 contains a goal transition whose target is the reward alone', () => {
  const u = updates.updates.find(x => x.number === 32), b = u.batch, t = u.tracked;
  assert.equal(b.done[t], 1);
  assert.equal(b.y[t], -1);
  assert.equal(round(b.s2[t][0], 3), 0.501);
  says('Update 32 contains one, a step that crossed the flag at position 0.501');
});

test('first target sync: targets and loss jump', () => {
  assert.equal(sync.syncs[0], 250);
  assert.equal(round(sync.mean_target[249], 2), -1.27);
  assert.equal(round(sync.mean_target[250], 2), -2.23);
  assert.equal(round(sync.loss[249], 4), 0.0084);
  assert.equal(round(sync.loss[250], 2), 0.94);
  assert.equal(round(sync.loss[99], 4), 0.0071);
  const long = sync.long, past60 = long.update[long.mean_target.findIndex(v => v <= -60)];
  assert.ok(past60 > 28800 && past60 <= 29000, `first sampled update at or past −60: ${past60}`);
  assert.equal(Math.round(long.mean_target[long.mean_target.length - 1]), -34);
  says('By about update 29,000, near step 136,000 and after about 115 syncs, the average target has fallen past −60', 'to about −34 by the end of training');
  says('which drift to −1.27 by update 250', 'The targets jump to −2.23', 'The loss jumps from 0.0084 to 0.94', 'It was 0.0071 after 100 updates');
});

test('replay: no featured minibatch sample comes from the current episode', () => {
  for (const u of updates.updates) assert.equal(u.batch.age.filter(age => age < u.episode_step).length, 0, `update ${u.number}`);
  assert.equal(Math.round(70001 * 64 / 300000), 15);
  says('none of the 64 came from the episode the car was driving at the time', 'sampled about 15 times on average');
});

test('first greedy goal and its update', () => {
  const m = training.milestones, u = updates.updates.find(x => x.key === 'first-greedy-goal');
  assert.equal(m.first_greedy_goal_episode, 384);
  assert.equal(m.first_greedy_goal_step, 74124);
  assert.equal(u.step, 74124);
  assert.equal(u.buffer_size, 74124);
  assert.equal(u.episode_explore_fraction, 0);
  says('episode 384, at step 74,124', 'one transition among 74,124');
});

test('warm-up and exploration schedule', () => {
  const m = training.milestones;
  assert.equal(m.warmup_episodes, 104);
  assert.equal(m.warmup_goals, 20);
  assert.equal(m.first_goal_episode, 7);
  assert.equal(training.epsilon.learning_starts, 20000);
  assert.equal(training.epsilon.end, 0.02);
  assert.equal(training.epsilon.decay_steps, 100000);
  assert.deepEqual([training.epsilon.hold_min, training.epsilon.hold_max], [20, 60]);
  says('in those 104 warm-up episodes the car reached the flag 20 times, first in episode 7', 'epsilon falls from 1 to 0.02 over the next 100,000 steps', 'keeps it for 20 to 60 steps');
});

test('pulse start probability example', () => {
  assert.equal(Math.round(1 / pulseStartProbability(0.5, 20, 60)), 41);
  says('about 1 in 41 of the steps where no pulse is running');
});

test('checkpoint story: late success, then a dip', () => {
  const goals = Object.fromEntries(training.checkpoints.map(c => [c.step, c.goals]));
  assert.ok(training.checkpoints.filter(c => c.step <= 80000).every(c => c.goals <= 1));
  assert.equal(goals[90000], 11);
  assert.equal(goals[110000], 3);
  assert.equal(goals[140000], 11);
  const best = training.checkpoints.find(c => c.name === 'best.pt');
  assert.equal(best.step, 251392);
  assert.equal(best.updates, 57849);
  assert.equal(goals[20000], 0);
  assert.equal(goals[30000], 0);
  const first = Uint8Array.from(Buffer.from(training.grid.first_visit, 'base64'));
  const visit = new Int32Array(first.buffer, first.byteOffset, first.byteLength / 4);
  const values = new Int16Array(Uint8Array.from(Buffer.from(best.v, 'base64')).buffer);
  let unvisited = 0, visited = 0;
  values.forEach((v, i) => { if (v / 100 > -1) { if (visit[i] < best.step) visited += 1; else unvisited += 1; } });
  assert.equal(unvisited, 156);
  assert.equal(visited, 18);
  says('at most 1 of the 11 test starts until step 90,000', 'At step 110,000', 'only 3 of 11', 'recovers by step 140,000', 'at steps 20,000 and 30,000, reached the flag from none of the 11 test starts', '156 unvisited cells, and even 18 rarely visited ones');
});

test('evaluation and provenance', () => {
  const e = native.unfiltered_evaluation;
  assert.equal(e.ranges['40000'].goals + e.ranges['50000'].goals, 200);
  assert.equal(e.pooled.mean_return, -100.46);
  assert.equal(e.pooled.std_return, 9.21);
  assert.equal(native.checkpoint_selection.window_mean_return, -96.05);
  assert.equal(native.rerun.checkpoints_identical, 61);
  says('saved at step 251,392', 'peaked at −96.05', 'reached the flag in all 200, with a mean return of −100.46 and a standard deviation of 9.21', 'All 61 matched exactly');
});

test('exploration lab numbers quoted without JavaScript', () => {
  const independent = runExplorationProbe({ holdMin: 1, holdMax: 1, episodes: 500, seed: 7 });
  const held = runExplorationProbe({ holdMin: 20, holdMax: 60, episodes: 500, seed: 7 });
  assert.equal(independent.goals, 0);
  assert.equal(held.goals, 71);
  assert.ok(read('_includes/rl/dqn-explore.html').includes('reached the goal in 0 of 500 episodes and actions held for 20 to 60 steps reached it in 71'));
});

test('no em or en dashes in the post', () => {
  assert.ok(!/[\u2013\u2014]/.test(post));
});

let failed = 0;
for (const [name, fn] of tests) {
  try { fn(); console.log(`ok   ${name}`); } catch (error) { failed += 1; console.log(`FAIL ${name}\n     ${error.message}`); }
}
console.log(`${tests.length - failed}/${tests.length} passed`);
process.exit(failed ? 1 : 0);
