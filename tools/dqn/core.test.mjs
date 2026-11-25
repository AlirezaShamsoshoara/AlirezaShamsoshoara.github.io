// Node tests for the DQN post's pure model: node tools/dqn/core.test.mjs [gymnasium-reference.json]
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import {
  MOUNTAIN_CAR, mountainCarStep, hillHeight, createRandom, runRandomEpisode, runExplorationProbe,
  pulseStartProbability, formatValue, decodeInt16, decodeUint8,
} from '../../assets/js/rl/dqn-core.mjs';

const tests = [];
const test = (name, fn) => tests.push([name, fn]);

test('step follows the MountainCar update rule', () => {
  const { state, observation, reward, terminated } = mountainCarStep([-0.5, 0], 2);
  const velocity = 0.001 + Math.cos(-1.5) * -0.0025;
  assert.equal(state[1], velocity);
  assert.equal(state[0], -0.5 + velocity);
  assert.deepEqual(observation, [Math.fround(state[0]), Math.fround(state[1])]);
  assert.equal(reward, -1);
  assert.equal(terminated, false);
});

test('left wall stops the car and speed is clipped', () => {
  const wall = mountainCarStep([-1.199, -0.05], 0);
  assert.equal(wall.state[0], MOUNTAIN_CAR.minPosition);
  assert.equal(wall.state[1], 0);
  const fast = mountainCarStep([0, 0.07], 2);
  assert.ok(Math.abs(fast.state[1]) <= MOUNTAIN_CAR.maxSpeed);
});

test('goal needs position at least 0.5 and non-negative velocity', () => {
  assert.equal(mountainCarStep([0.49, 0.02], 2).terminated, true);
  assert.equal(mountainCarStep([0.52, -0.05], 0).terminated, false);
});

test('invalid actions are rejected', () => {
  assert.throws(() => mountainCarStep([0, 0], 3), RangeError);
  assert.throws(() => mountainCarStep([0, 0], 1.5), RangeError);
});

test('hill height matches the renderer formula', () => {
  assert.equal(hillHeight(0), 0.55);
  assert.ok(Math.abs(hillHeight(Math.PI / 6) - 1.0) < 1e-12);
});

test('seeded random numbers are reproducible and in [0, 1)', () => {
  const a = createRandom(7), b = createRandom(7), c = createRandom(8);
  const xs = Array.from({ length: 1000 }, a);
  assert.deepEqual(xs, Array.from({ length: 1000 }, b));
  assert.notDeepEqual(xs.slice(0, 5), Array.from({ length: 5 }, c));
  assert.ok(xs.every(x => x >= 0 && x < 1));
});

test('held actions really repeat for the drawn duration', () => {
  const random = createRandom(3);
  const run = runRandomEpisode({ holdMin: 20, holdMax: 20, random, startPosition: -0.5, keepPath: true });
  assert.equal(run.path.length, run.steps + 1);
  assert.equal(run.actions.length, run.steps);
  run.actions.forEach((action, t) => { if (t % 20) assert.equal(action, run.actions[t - 1], `action changed inside a hold at step ${t}`); });
  const independent = runRandomEpisode({ holdMin: 1, holdMax: 1, random: createRandom(3), startPosition: -0.5, keepPath: true });
  const changes = independent.actions.filter((action, t) => t && action !== independent.actions[t - 1]).length;
  assert.ok(changes > independent.steps / 2, `independent actions changed only ${changes} times`);
});

test('exploration probe is reproducible and counts goals honestly', () => {
  const a = runExplorationProbe({ holdMin: 20, holdMax: 60, episodes: 200, seed: 11 });
  const b = runExplorationProbe({ holdMin: 20, holdMax: 60, episodes: 200, seed: 11 });
  assert.deepEqual(a.lengths, b.lengths);
  assert.equal(a.goals, a.lengths.filter(n => n < MOUNTAIN_CAR.maxSteps).length);
  assert.ok(a.paths.length === 24 && a.paths.every(p => p.path.length >= 2));
  assert.ok(a.maxPositions.every(x => x >= MOUNTAIN_CAR.minPosition && x <= MOUNTAIN_CAR.maxPosition));
});

test('independent random actions rarely reach the goal; holds reach it more often', () => {
  const independent = runExplorationProbe({ holdMin: 1, holdMax: 1, episodes: 500, seed: 7 });
  const held = runExplorationProbe({ holdMin: 20, holdMax: 60, episodes: 500, seed: 7 });
  assert.ok(independent.goals <= 2, `independent goals ${independent.goals}`);
  assert.ok(held.goals > 20 * Math.max(1, independent.goals), `held goals ${held.goals}`);
});

test('pulse start probability matches the repository formula', () => {
  assert.equal(pulseStartProbability(1, 20, 60), 1);
  assert.equal(pulseStartProbability(0, 20, 60), 0);
  assert.ok(Math.abs(pulseStartProbability(0.5, 20, 60) - 0.5 / (40 * 0.5 + 0.5)) < 1e-15);
  assert.equal(pulseStartProbability(0.3, 1, 1), 0.3);
});

test('number formatting uses a true minus sign and short digits', () => {
  assert.equal(formatValue(-1.04812), '\u22121.048');
  assert.equal(formatValue(0), '0');
  assert.equal(formatValue(0.0095), '0.0095');
  assert.equal(formatValue(-0.00002), '\u22122.00e\u22125');
});

test('binary decoders read little-endian int16 and uint8', () => {
  const ints = new Int16Array([-12000, 0, 6000, 32767]);
  const base64 = Buffer.from(ints.buffer).toString('base64');
  assert.deepEqual(Array.from(decodeInt16(base64)), Array.from(ints));
  assert.deepEqual(Array.from(decodeUint8(Buffer.from([0, 1, 2, 255]).toString('base64'))), [0, 1, 2, 255]);
});

const reference = process.argv[2];
if (reference) {
  test('physics reproduces Gymnasium trajectories exactly', () => {
    const data = JSON.parse(readFileSync(reference, 'utf8'));
    let steps = 0, maxError = 0;
    for (const item of data.cases) {
      let state = item.start;
      item.actions.forEach((action, t) => {
        const next = mountainCarStep(state, action);
        const [x, v, terminated] = item.states[t];
        maxError = Math.max(maxError, Math.abs(next.state[0] - x), Math.abs(next.state[1] - v));
        assert.equal(next.terminated, terminated);
        state = next.state;
        steps += 1;
      });
    }
    assert.ok(maxError <= 1e-15, `largest difference ${maxError}`);
    console.log(`    ${data.cases.length} Gymnasium ${data.gymnasium} episodes, ${steps} steps, largest difference ${maxError}`);
  });
}

let failed = 0;
for (const [name, fn] of tests) {
  try { fn(); console.log(`ok   ${name}`); } catch (error) { failed += 1; console.log(`FAIL ${name}\n     ${error.message}`); }
}
console.log(`${tests.length - failed}/${tests.length} passed`);
process.exit(failed ? 1 : 0);
