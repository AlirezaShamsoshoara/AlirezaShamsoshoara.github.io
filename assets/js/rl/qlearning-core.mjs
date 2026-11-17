/* Pure teaching model shared by the detailed recording and batched learner. */
export const ACTIONS = Object.freeze(['Left', 'Down', 'Right', 'Up']);
export const ARROWS = Object.freeze(['←', '↓', '→', '↑']);
export const MAP = Object.freeze(['SFFF', 'FHFH', 'FFFH', 'HFFG']);
export const DEFAULTS = Object.freeze({ alpha: 0.1, gamma: 0.95, epsilon: 0.3, seed: 7, maxSteps: 60 });
// Fixed teaching actions, not an exploration policy or a supplied learned policy.
export const GUIDED_ACTIONS = Object.freeze([1, 1, 2, 1, 2, 2]);
export const GUIDED_MILESTONES = Object.freeze([5, 10, 30]);

// Presentation timing, shared by autoplay and portable-media export.
export function guidedPhaseTiming(record) {
  if (!record || !Number.isInteger(record.index) || record.index < 0) throw new TypeError('Invalid guided timing record');
  finite(record.error, 'guided TD error');
  if (GUIDED_MILESTONES.includes(record.index)) return Object.freeze([600, 720, 2500, 2500, 2800, 3800]);
  return Object.freeze(record.error === 0 ? [150, 720, 150, 150, 150, 300] : [150, 720, 150, 250, 600, 900]);
}

function finite(value, name) {
  if (typeof value !== 'number' || !Number.isFinite(value)) throw new TypeError(`${name} must be finite`);
  return value;
}
function unit(value, name) {
  finite(value, name);
  if (value < 0 || value > 1) throw new RangeError(`${name} must be between 0 and 1`);
  return value;
}
function index(value, limit, name) {
  if (!Number.isInteger(value) || value < 0 || value >= limit) throw new RangeError(`Invalid ${name}`);
}
function frozenTable(table) {
  return Object.freeze(table.map(row => Object.freeze(row.slice())));
}

export function formatQ(value) {
  finite(value, 'display value');
  if (value === 0) return '0';
  const magnitude = Math.abs(value);
  const text = magnitude < 0.001 || magnitude >= 1000 ? value.toExponential(3) : value.toPrecision(4);
  const [mantissa, exponent] = text.split('e');
  const compact = mantissa.includes('.') ? mantissa.replace(/0+$/, '').replace(/\.$/, '') : mantissa;
  return exponent === undefined ? compact : `${compact}e${exponent}`;
}

export function tdUpdate({ oldValue, reward, nextValues, alpha, gamma, terminated = false }) {
  finite(oldValue, 'oldValue'); finite(reward, 'reward'); unit(alpha, 'alpha'); unit(gamma, 'gamma');
  if (typeof terminated !== 'boolean') throw new TypeError('terminated must be boolean');
  if (!Array.isArray(nextValues) || nextValues.length === 0) throw new TypeError('nextValues must be a nonempty array');
  nextValues.forEach(value => finite(value, 'nextValue'));
  const nextMax = Math.max(...nextValues);
  const bootstrap = terminated ? 0 : gamma * nextMax;
  const target = reward + bootstrap;
  const error = target - oldValue;
  const increment = alpha * error;
  const newValue = oldValue + increment;
  [target, error, increment, newValue].forEach(value => finite(value, 'TD result'));
  return Object.freeze({ nextMax, bootstrap, target, error, increment, oldValue, newValue });
}

export function createRandom(seed = DEFAULTS.seed) {
  if (!Number.isInteger(seed) || seed < 0 || seed > 0xffffffff) throw new RangeError('seed must be an unsigned 32-bit integer');
  let state = seed >>> 0;
  return () => {
    state = (Math.imul(1664525, state) + 1013904223) >>> 0;
    return state / 4294967296;
  };
}

export function transition(state, action) {
  index(state, 16, 'state'); index(action, 4, 'action');
  const row = Math.floor(state / 4), col = state % 4;
  if ('HG'.includes(MAP[row][col])) throw new RangeError('Reset after a terminal tile');
  const moves = [[0, -1], [1, 0], [0, 1], [-1, 0]];
  const nextRow = Math.max(0, Math.min(3, row + moves[action][0]));
  const nextCol = Math.max(0, Math.min(3, col + moves[action][1]));
  const nextState = nextRow * 4 + nextCol;
  const tile = MAP[nextRow][nextCol];
  return Object.freeze({ state, action, nextState, reward: tile === 'G' ? 1 : 0,
    terminated: tile === 'G' || tile === 'H', goal: tile === 'G', hole: tile === 'H' });
}

export function greedyAction(values) {
  if (!Array.isArray(values) || !values.length || values.some(value => !Number.isFinite(value))) throw new TypeError('Invalid action values');
  return values.indexOf(Math.max(...values)); // First argmax, matching repository evaluation.
}

export function createLearner({ alpha = DEFAULTS.alpha, gamma = DEFAULTS.gamma,
  epsilon = DEFAULTS.epsilon, seed = DEFAULTS.seed, maxSteps = DEFAULTS.maxSteps } = {}) {
  unit(alpha, 'alpha'); unit(gamma, 'gamma'); unit(epsilon, 'epsilon');
  if (!Number.isInteger(maxSteps) || maxSteps <= 0) throw new RangeError('maxSteps must be positive');
  const random = createRandom(seed);
  const q = Array.from({ length: 16 }, () => [0, 0, 0, 0]);
  let current = 0, steps = 0, episodes = 0, goals = 0, holes = 0, timeouts = 0, interactions = 0;
  let last = null;
  const history = [{ episode: 0, startValue: 0, goals: 0 }];
  function act() {
    // Preserve the original random-draw order while recording how the action was chosen.
    const exploreDraw = random();
    if (exploreDraw < epsilon) return { action: Math.floor(random() * 4), selection: 'explore', exploreDraw };
    const max = Math.max(...q[current]);
    const tied = q[current].map((value, action) => value === max ? action : -1).filter(action => action >= 0);
    return { action: tied[Math.floor(random() * tied.length)], selection: tied.length > 1 ? 'greedy-tie' : 'greedy', exploreDraw };
  }
  function step(actionOverride) {
    if (actionOverride !== undefined) index(actionOverride, 4, 'guided action');
    const choice = actionOverride === undefined ? act() : { action: actionOverride, selection: 'guided', exploreDraw: null };
    const observed = transition(current, choice.action);
    const update = tdUpdate({ oldValue: q[current][observed.action], reward: observed.reward,
      nextValues: q[observed.nextState], alpha, gamma, terminated: observed.terminated });
    q[current][observed.action] = update.newValue;
    current = observed.nextState; steps += 1; interactions += 1;
    const truncated = !observed.terminated && steps >= maxSteps;
    last = Object.freeze({ ...observed, ...update, truncated, episode: episodes + 1, episodeStep: steps,
      behavior: actionOverride === undefined ? 'epsilon-greedy' : 'guided', selection: choice.selection,
      exploreDraw: choice.exploreDraw, epsilon });
    if (observed.terminated || truncated) {
      episodes += 1; goals += Number(observed.goal); holes += Number(observed.hole); timeouts += Number(truncated);
      history.push({ episode: episodes, startValue: Math.max(...q[0]), goals });
      current = 0; steps = 0;
    }
    return last;
  }
  function train(count) {
    if (!Number.isInteger(count) || count <= 0) throw new RangeError('Episode count must be positive');
    const end = episodes + count;
    while (episodes < end) step();
    return snapshot();
  }
  function snapshot() {
    return { q: q.map(row => row.slice()), current, steps, episodes, goals, holes, timeouts, interactions,
      last, history: history.map(row => ({ ...row })), alpha, gamma, epsilon, seed, maxSteps };
  }
  return Object.freeze({ step, train, snapshot });
}

// A fixed-action arithmetic control retained for unit tests, not used by the figures.
export function createGuidedWalkthrough({ alpha = DEFAULTS.alpha, gamma = DEFAULTS.gamma, episodes = 6 } = {}) {
  unit(alpha, 'alpha'); unit(gamma, 'gamma');
  if (!Number.isInteger(episodes) || episodes < 1 || episodes > 50) throw new RangeError('Guided episodes must be between 1 and 50');
  const learner = createLearner({ alpha, gamma, epsilon: 0 });
  const records = [], states = [0];
  let state = 0;
  for (const action of GUIDED_ACTIONS) {
    const observed = transition(state, action);
    state = observed.nextState; states.push(state);
  }
  if (state !== 15) throw new Error('The teaching route must finish at the goal');
  for (let episode = 1; episode <= episodes; episode += 1) {
    for (let move = 0; move < GUIDED_ACTIONS.length; move += 1) {
      const before = learner.snapshot();
      const update = learner.step(GUIDED_ACTIONS[move]);
      const after = learner.snapshot();
      if (update.hole || update.truncated || update.state !== states[move] || update.nextState !== states[move + 1]) {
        throw new Error('Invalid guided transition');
      }
      const recordIndex = records.length;
      records.push(Object.freeze({ ...update, index: recordIndex,
        phaseDurationsMs: guidedPhaseTiming({ ...update, index: recordIndex }),
        qBefore: frozenTable(before.q), qAfter: frozenTable(after.q),
        startValueBefore: Math.max(...before.q[0]), startValueAfter: Math.max(...after.q[0]) }));
    }
  }
  const final = learner.snapshot();
  return Object.freeze({ alpha, gamma, episodes, actions: GUIDED_ACTIONS, states: Object.freeze(states),
    records: Object.freeze(records), finalQ: frozenTable(final.q), goals: final.goals,
    behavior: 'fixed actions selected for teaching, not epsilon-greedy exploration' });
}

export function createExplorationTrace({ alpha = DEFAULTS.alpha, gamma = DEFAULTS.gamma,
  epsilon = DEFAULTS.epsilon, seed = DEFAULTS.seed, maxSteps = DEFAULTS.maxSteps, episodes = 120 } = {}) {
  if (!Number.isInteger(episodes) || episodes < 1 || episodes > 250) throw new RangeError('Trace episodes must be between 1 and 250');
  const learner = createLearner({ alpha, gamma, epsilon, seed, maxSteps });
  const records = [], summaries = [];
  let episodeStart = 0, states = [0], actions = [], selections = [];
  const milestones = { explore: null, hole: null, reward: null, bootstrap: null, start: null };
  while (learner.snapshot().episodes < episodes) {
    const before = learner.snapshot();
    const update = learner.step(); // No overrides: the same epsilon-greedy behavior used by Figure 2.
    const after = learner.snapshot(), index = records.length;
    const milestoneNames = [];
    const candidate = { explore: update.selection === 'explore', hole: update.hole, reward: update.goal,
      bootstrap: update.reward === 0 && !update.terminated && update.increment > 0,
      start: update.state === 0 && update.newValue > update.oldValue };
    for (const [name, present] of Object.entries(candidate)) {
      if (present && milestones[name] === null) { milestones[name] = index; milestoneNames.push(name); }
    }
    const slow = milestoneNames.length > 0;
    const phaseDurationsMs = Object.freeze(slow ? [600, 720, 2500, 2500, 2800, 3800]
      : update.increment === 0 ? [150, 720, 150, 150, 150, 300] : [150, 720, 150, 250, 600, 900]);
    records.push(Object.freeze({ ...update, index, qBefore: frozenTable(before.q), qAfter: frozenTable(after.q),
      startValueBefore: Math.max(...before.q[0]), startValueAfter: Math.max(...after.q[0]),
      milestoneNames: Object.freeze(milestoneNames), phaseDurationsMs }));
    states.push(update.nextState); actions.push(update.action); selections.push(update.selection);
    if (update.terminated || update.truncated) {
      summaries.push(Object.freeze({ episode: update.episode, startIndex: episodeStart, endIndex: index,
        length: actions.length, states: Object.freeze(states), actions: Object.freeze(actions),
        selections: Object.freeze(selections), goal: update.goal, hole: update.hole, truncated: update.truncated,
        outcome: update.goal ? 'goal' : update.hole ? 'hole' : 'time limit',
        exploreCount: selections.filter(selection => selection === 'explore').length,
        startValue: Math.max(...after.q[0]) }));
      episodeStart = index + 1; states = [0]; actions = []; selections = [];
    }
  }
  const final = learner.snapshot();
  // Portable media are explicitly edited highlights. Every omitted transition remains in the interactive.
  const highlightEpisodes = [...new Set([0, 1, ...Object.values(milestones).filter(index => index !== null)
    .map(index => records[index].episode - 1)])].sort((a, b) => a - b);
  const highlights = summaries.filter((_, index) => highlightEpisodes.includes(index))
    .flatMap(summary => records.slice(summary.startIndex, summary.endIndex + 1).map(record => record.index));
  return Object.freeze({ alpha, gamma, epsilon, seed, maxSteps, episodes,
    records: Object.freeze(records), episodeSummaries: Object.freeze(summaries),
    milestones: Object.freeze(milestones), highlightIndices: Object.freeze(highlights),
    finalQ: frozenTable(final.q), goals: final.goals, holes: final.holes, timeouts: final.timeouts,
    behavior: 'seeded epsilon-greedy interactions; no prescribed route or action overrides' });
}

export function greedyRollout(table, maxSteps = DEFAULTS.maxSteps) {
  if (!Array.isArray(table) || table.length !== 16 || table.some(row => !Array.isArray(row) || row.length !== 4 || row.some(v => !Number.isFinite(v)))) {
    throw new TypeError('Expected a finite 16 by 4 Q-table');
  }
  if (!Number.isInteger(maxSteps) || maxSteps <= 0) throw new RangeError('maxSteps must be positive');
  let state = 0;
  const states = [state], transitions = [];
  for (let t = 0; t < maxSteps; t += 1) {
    const observed = transition(state, greedyAction(table[state]));
    transitions.push(observed); state = observed.nextState;
    states.push(state);
    if (observed.terminated) return { states, transitions, goal: observed.goal, hole: observed.hole, truncated: false };
  }
  return { states, transitions, goal: false, hole: false, truncated: true };
}
