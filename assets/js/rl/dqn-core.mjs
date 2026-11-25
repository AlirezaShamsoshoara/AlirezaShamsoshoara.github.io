/*
 * Pure model for the DQN post (RL From Zero, Part 2). No DOM.
 *
 * MountainCar-v0 physics follow Gymnasium 1.3.0 exactly (float64 state,
 * float32 observations). The exploration lab replays held random actions on
 * that physics. Everything else the figures show (network values, minibatches,
 * updates, rollouts) is recorded from the repository's own training run and
 * loaded as data, so the browser never re-trains or re-approximates the network.
 */

export const MOUNTAIN_CAR = Object.freeze({
  minPosition: -1.2,
  maxPosition: 0.6,
  maxSpeed: 0.07,
  goalPosition: 0.5,
  goalVelocity: 0,
  force: 0.001,
  gravity: 0.0025,
  maxSteps: 200,
  startLow: -0.6,
  startHigh: -0.4,
});
export const ACTIONS = Object.freeze(['Push left', 'No push', 'Push right']);
export const ACTION_SHORT = Object.freeze(['Left', 'None', 'Right']);

const clip = (value, low, high) => Math.min(high, Math.max(low, value));

/** One MountainCar transition, exactly as Gymnasium computes it. */
export function mountainCarStep(state, action) {
  if (!Number.isInteger(action) || action < 0 || action > 2) throw new RangeError('action must be 0, 1 or 2');
  const c = MOUNTAIN_CAR;
  let [position, velocity] = state;
  velocity += (action - 1) * c.force + Math.cos(3 * position) * (-c.gravity);
  velocity = clip(velocity, -c.maxSpeed, c.maxSpeed);
  position += velocity;
  position = clip(position, c.minPosition, c.maxPosition);
  if (position === c.minPosition && velocity < 0) velocity = 0;
  const terminated = position >= c.goalPosition && velocity >= c.goalVelocity;
  return { state: [position, velocity], observation: [Math.fround(position), Math.fround(velocity)], reward: -1, terminated };
}

/** Height of the hill at a position, as Gymnasium draws it. */
export const hillHeight = position => Math.sin(3 * position) * 0.45 + 0.55;

/** Small, fast, seeded generator (mulberry32). Returns numbers in [0, 1). */
export function createRandom(seed) {
  if (!Number.isInteger(seed) || seed < 0 || seed > 0xffffffff) throw new RangeError('seed must be a 32-bit unsigned integer');
  let t = seed >>> 0;
  return () => {
    t = (t + 0x6d2b79f5) >>> 0;
    let r = Math.imul(t ^ (t >>> 15), 1 | t);
    r = (r + Math.imul(r ^ (r >>> 7), 61 | r)) ^ r;
    return ((r ^ (r >>> 14)) >>> 0) / 4294967296;
  };
}

const randomInt = (random, low, high) => low + Math.floor(random() * (high - low + 1));

/**
 * Random exploration with held actions: each new random action is repeated for
 * a uniformly drawn number of steps in [holdMin, holdMax]. holdMin = holdMax = 1
 * is ordinary independent random actions. No learning happens here.
 */
export function runRandomEpisode({ holdMin, holdMax, random, startPosition = null, keepPath = false }) {
  if (!Number.isInteger(holdMin) || !Number.isInteger(holdMax) || holdMin < 1 || holdMax < holdMin) throw new RangeError('hold bounds must be ordered positive integers');
  const c = MOUNTAIN_CAR;
  const position = startPosition ?? (c.startLow + random() * (c.startHigh - c.startLow));
  let state = [position, 0];
  let action = 1, remaining = 0, maxPosition = position, steps = 0, goal = false;
  const path = keepPath ? [[...state]] : null;
  const actions = keepPath ? [] : null;
  while (steps < c.maxSteps) {
    if (remaining === 0) {
      action = randomInt(random, 0, 2);
      remaining = randomInt(random, holdMin, holdMax);
    }
    remaining -= 1;
    const next = mountainCarStep(state, action);
    state = next.state;
    steps += 1;
    maxPosition = Math.max(maxPosition, state[0]);
    if (path) { path.push([...state]); actions.push(action); }
    if (next.terminated) { goal = true; break; }
  }
  return { goal, steps, maxPosition, path, actions };
}

/** Many random episodes with one hold setting; keeps a few paths for drawing. */
export function runExplorationProbe({ holdMin, holdMax, episodes = 500, seed = 7, keepPaths = 24 }) {
  if (!Number.isInteger(episodes) || episodes < 1 || episodes > 5000) throw new RangeError('episodes must be between 1 and 5000');
  const random = createRandom(seed);
  let goals = 0, firstGoal = null;
  const maxPositions = [], lengths = [], paths = [];
  for (let i = 0; i < episodes; i += 1) {
    const run = runRandomEpisode({ holdMin, holdMax, random, keepPath: i < keepPaths });
    if (run.goal) { goals += 1; if (firstGoal === null) firstGoal = i; }
    maxPositions.push(run.maxPosition);
    lengths.push(run.steps);
    if (run.path) paths.push({ path: run.path, goal: run.goal });
  }
  return Object.freeze({ holdMin, holdMax, episodes, seed, goals, firstGoal, maxPositions, lengths, paths });
}

/** Start-probability correction used by the repository's held-action explorer. */
export function pulseStartProbability(epsilon, holdMin, holdMax) {
  if (!(epsilon >= 0 && epsilon <= 1)) throw new RangeError('epsilon must be in [0, 1]');
  const meanHold = (holdMin + holdMax) / 2;
  return epsilon / (meanHold * (1 - epsilon) + epsilon);
}

/** Display format: up to 4 significant digits, no exponent for ordinary values. */
export function formatValue(value, digits = 4) {
  if (!Number.isFinite(value)) return String(value);
  if (value === 0) return '0';
  const magnitude = Math.abs(value);
  if (magnitude < 1e-3) return value.toExponential(2).replace('e-', 'e\u2212').replace('-', '\u2212');
  const text = Number(value.toPrecision(digits)).toString();
  return text.replace('-', '\u2212');
}

/** Decode a base64 string of little-endian int16 values (used for value grids). */
export function decodeInt16(base64) {
  const bytes = typeof atob === 'function' ? Uint8Array.from(atob(base64), ch => ch.charCodeAt(0)) : new Uint8Array(Buffer.from(base64, 'base64'));
  return new Int16Array(bytes.buffer, bytes.byteOffset, bytes.byteLength / 2);
}

/** Decode a base64 string of uint8 values. */
export function decodeUint8(base64) {
  return typeof atob === 'function' ? Uint8Array.from(atob(base64), ch => ch.charCodeAt(0)) : new Uint8Array(Buffer.from(base64, 'base64'));
}
