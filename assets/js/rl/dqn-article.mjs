/*
 * Controller for the DQN post (RL From Zero, Part 2).
 * Figures 1, 2 and 4 draw values recorded from the repository's training run;
 * Figure 3 runs random exploration on the verified MountainCar physics.
 */
import { ACTIONS, ACTION_SHORT, hillHeight, runExplorationProbe, formatValue as fmt, decodeInt16, decodeUint8 } from './dqn-core.mjs';

const NS = 'http://www.w3.org/2000/svg';
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)');
const int = n => Math.round(n).toLocaleString('en-US');
const pct = x => `${Math.round(x * 100)}%`;
const clamp = (x, lo, hi) => Math.min(hi, Math.max(lo, x));
const ACTION_COLORS = ['#996418', '#7b8794', '#2356a8'];

function el(tag, attrs = {}, text) {
  const node = document.createElementNS(NS, tag);
  for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, value);
  if (text !== undefined) node.textContent = text;
  return node;
}
function html(tag, attrs = {}, text) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, value);
  if (text !== undefined) node.textContent = text;
  return node;
}
async function loadJSON(url) {
  if (!url) throw new Error('the figure has no data source');
  if (url.startsWith('data:')) {
    // Review files embed the recorded data as data: URLs. Decode them here: sandboxed viewers block fetch().
    const comma = url.indexOf(',');
    const header = url.slice(5, comma), body = url.slice(comma + 1);
    const text = /;base64$/i.test(header)
      ? new TextDecoder().decode(Uint8Array.from(atob(body), ch => ch.charCodeAt(0)))
      : decodeURIComponent(body);
    return JSON.parse(text);
  }
  const response = await fetch(url);
  if (!response.ok) throw new Error(`could not load ${url} (${response.status})`);
  return response.json();
}
function decodeInt32(base64) {
  const bytes = Uint8Array.from(atob(base64), ch => ch.charCodeAt(0));
  return new Int32Array(bytes.buffer, bytes.byteOffset, bytes.byteLength / 4);
}
function percentile(values, q) {
  const sorted = Float64Array.from(values).sort();
  if (!sorted.length) return 0;
  const i = (sorted.length - 1) * q, lo = Math.floor(i), hi = Math.ceil(i);
  return sorted[lo] + (sorted[hi] - sorted[lo]) * (i - lo);
}

/* ---------- shared phase-space map ---------- */
const MAP = { width: 864, height: 560, left: 74, right: 14, top: 14, bottom: 56 };
MAP.plotW = MAP.width - MAP.left - MAP.right;
MAP.plotH = MAP.height - MAP.top - MAP.bottom;
const mx = p => MAP.left + (p + 1.2) / 1.8 * MAP.plotW;
const my = v => MAP.top + (0.07 - v) / 0.14 * MAP.plotH;
const SEQ = [[248, 250, 252], [218, 228, 241], [150, 176, 216], [71, 112, 180], [27, 59, 122]];
const UNVISITED = [234, 237, 241];
const mix = (a, b, t) => a.map((x, i) => Math.round(x + (b[i] - x) * t));
function seqColor(t) {
  const n = SEQ.length - 1, u = clamp(t, 0, 1) * n, i = Math.min(n - 1, Math.floor(u));
  return mix(SEQ[i], SEQ[i + 1], u - i);
}
const divColor = t => (t < 0 ? mix([255, 255, 255], [153, 100, 24], clamp(-t, 0, 1)) : mix([255, 255, 255], [35, 86, 168], clamp(t, 0, 1)));
const cssColor = c => `rgb(${c[0]},${c[1]},${c[2]})`;
const legendGradient = mode => (mode === 'delta'
  ? `linear-gradient(90deg, ${cssColor(divColor(-1))}, #fff, ${cssColor(divColor(1))})`
  : `linear-gradient(90deg, ${SEQ.map(cssColor).join(', ')})`);

function prepareCanvas(canvas) {
  canvas.width = MAP.width * 2;
  canvas.height = MAP.height * 2;
  return canvas;
}
function drawField(canvas, grid, values, visited, mode, scale) {
  const { nx, ny } = grid;
  const off = document.createElement('canvas');
  off.width = nx; off.height = ny;
  const ctx = off.getContext('2d');
  const image = ctx.createImageData(nx, ny);
  for (let row = 0; row < ny; row += 1) {
    for (let col = 0; col < nx; col += 1) {
      const src = row * nx + col, dst = ((ny - 1 - row) * nx + col) * 4;
      const color = !visited[src] ? UNVISITED
        : mode === 'delta' ? divColor(values[src] / scale.max)
          : seqColor((values[src] - scale.low) / Math.max(1e-9, scale.high - scale.low));
      image.data.set([color[0], color[1], color[2], 255], dst);
    }
  }
  ctx.putImageData(image, 0, 0);
  const out = canvas.getContext('2d'), k = canvas.width / MAP.width;
  out.setTransform(1, 0, 0, 1, 0, 0);
  out.clearRect(0, 0, canvas.width, canvas.height);
  out.imageSmoothingEnabled = true;
  out.imageSmoothingQuality = 'high';
  out.drawImage(off, MAP.left * k, MAP.top * k, MAP.plotW * k, MAP.plotH * k);
}
function drawAxes(svg, { goalLabel = true } = {}) {
  const g = el('g', { class: 'rldq-axes' });
  g.append(el('rect', { x: MAP.left, y: MAP.top, width: MAP.plotW, height: MAP.plotH, class: 'rldq-axis' }));
  for (const p of [-1.2, -0.9, -0.6, -0.3, 0, 0.3, 0.6]) {
    g.append(el('line', { x1: mx(p), x2: mx(p), y1: MAP.top + MAP.plotH, y2: MAP.top + MAP.plotH + 6, class: 'rldq-axis' }));
    g.append(el('text', { x: mx(p), y: MAP.top + MAP.plotH + 22, 'text-anchor': 'middle', class: 'rldq-tick' }, fmt(p)));
  }
  for (const v of [-0.07, -0.035, 0, 0.035, 0.07]) {
    g.append(el('line', { x1: MAP.left - 6, x2: MAP.left, y1: my(v), y2: my(v), class: 'rldq-axis' }));
    g.append(el('text', { x: MAP.left - 10, y: my(v) + 5, 'text-anchor': 'end', class: 'rldq-tick' }, fmt(v)));
  }
  g.append(el('line', { x1: MAP.left, x2: MAP.left + MAP.plotW, y1: my(0), y2: my(0), stroke: '#8d99a6', 'stroke-width': 1, 'stroke-dasharray': '3 5', opacity: 0.8 }));
  g.append(el('line', { x1: mx(0.5), x2: mx(0.5), y1: MAP.top, y2: MAP.top + MAP.plotH, stroke: '#39754d', 'stroke-width': 1.5, 'stroke-dasharray': '6 5' }));
  if (goalLabel) g.append(el('text', { x: mx(0.5) - 6, y: MAP.top + 18, 'text-anchor': 'end', class: 'rldq-note', fill: '#2f6545' }, 'flag'));
  g.append(el('text', { x: MAP.left + MAP.plotW / 2, y: MAP.height - 8, 'text-anchor': 'middle', class: 'rldq-label' }, 'Position'));
  const vy = MAP.top + MAP.plotH / 2;
  g.append(el('text', { x: 18, y: vy, 'text-anchor': 'middle', class: 'rldq-label', transform: `rotate(-90 18 ${vy})` }, 'Velocity'));
  svg.append(g);
}
function arrowMarker(svg, id, color) {
  const defs = el('defs');
  const marker = el('marker', { id, viewBox: '0 0 10 10', refX: 8, refY: 5, markerWidth: 7, markerHeight: 7, orient: 'auto-start-reverse' });
  marker.append(el('path', { d: 'M0,0 L10,5 L0,10 z', fill: color }));
  defs.append(marker);
  svg.append(defs);
}
function visitedMask(firstVisit, step, nx, ny) {
  const raw = new Uint8Array(firstVisit.length);
  for (let i = 0; i < firstVisit.length; i += 1) raw[i] = firstVisit[i] < step ? 1 : 0;
  // Morphological closing (3 by 3): fills single-cell gaps along the visited region's edge.
  const pass = (src, keep) => {
    const out = new Uint8Array(src.length);
    for (let r = 0; r < ny; r += 1) {
      for (let c = 0; c < nx; c += 1) {
        let hit = keep ? 1 : 0;
        for (let dr = -1; dr <= 1; dr += 1) {
          for (let dc = -1; dc <= 1; dc += 1) {
            const rr = r + dr, cc = c + dc;
            const value = rr < 0 || rr >= ny || cc < 0 || cc >= nx ? (keep ? 1 : 0) : src[rr * nx + cc];
            if (keep && !value) hit = 0;
            if (!keep && value) hit = 1;
          }
        }
        out[r * nx + c] = hit;
      }
    }
    return out;
  };
  return pass(pass(raw, false), true);
}
function niceTicks(lo, hi, count = 5) {
  const raw = (hi - lo) / count, mag = 10 ** Math.floor(Math.log10(raw)), err = raw / mag;
  const step = (err >= 7.5 ? 10 : err >= 3.5 ? 5 : err >= 1.5 ? 2 : 1) * mag;
  const ticks = [];
  for (let v = Math.ceil(lo / step) * step; v <= hi + step * 1e-9; v += step) ticks.push(Math.round(v / step) * step);
  return ticks;
}
function valueScale(values, mask) {
  const visited = [];
  for (let i = 0; i < values.length; i += 1) if (mask[i]) visited.push(values[i]);
  return { low: percentile(visited, 0.02), high: percentile(visited, 0.98) };
}
function setLegend(node, mode, low, high) {
  node.replaceChildren();
  node.append(html('span', {}, mode === 'delta' ? `−${fmt(low, 2)}` : `${fmt(low, 3)} farther`));
  const bar = html('i'); bar.style.background = legendGradient(mode);
  node.append(bar, html('span', {}, mode === 'delta' ? `+${fmt(high, 2)}` : `${fmt(high, 3)} closer`));
}

/* ---------- car on the hill ---------- */
const HILL = { width: 360, height: 150, left: 14, right: 14, top: 24, bottom: 12 };
const hx = p => HILL.left + (p + 1.2) / 1.8 * (HILL.width - HILL.left - HILL.right);
const hy = p => HILL.top + (1 - (hillHeight(p) - 0.1) / 0.9) * (HILL.height - HILL.top - HILL.bottom);
function drawHill(svg) {
  svg.replaceChildren();
  const points = [];
  for (let i = 0; i <= 180; i += 1) { const p = -1.2 + 1.8 * i / 180; points.push(`${hx(p).toFixed(1)},${hy(p).toFixed(1)}`); }
  svg.append(el('polyline', { points: points.join(' '), fill: 'none', stroke: '#8d99a6', 'stroke-width': 2 }));
  const fx = hx(0.5), fy = hy(0.5);
  svg.append(el('line', { x1: fx, x2: fx, y1: fy, y2: fy - 26, stroke: '#39754d', 'stroke-width': 2 }));
  svg.append(el('path', { d: `M${fx},${fy - 26} l14,5 l-14,5 z`, fill: '#39754d' }));
  const car = el('g', { 'data-car': '' });
  car.append(el('rect', { x: -11, y: -13, width: 22, height: 9, rx: 2, fill: '#2a3846' }));
  car.append(el('circle', { cx: -6, cy: -3, r: 3, fill: '#56616e' }), el('circle', { cx: 6, cy: -3, r: 3, fill: '#56616e' }));
  svg.append(car);
  return car;
}
function placeCar(car, p) {
  const dx = hx(p + 0.002) - hx(p - 0.002), dy = hy(p + 0.002) - hy(p - 0.002);
  car.setAttribute('transform', `translate(${hx(p).toFixed(2)} ${hy(p).toFixed(2)}) rotate(${(Math.atan2(dy, dx) * 180 / Math.PI).toFixed(2)})`);
}
function animatePath(car, xs, onDone, stepsPerSecond = 30) {
  let frame = null, start = null;
  if (reduceMotion.matches) { placeCar(car, xs[xs.length - 1]); onDone?.(); return () => {}; }
  const tick = time => {
    if (start === null) start = time;
    const i = Math.min(xs.length - 1, Math.floor((time - start) / 1000 * stepsPerSecond));
    placeCar(car, xs[i]);
    if (i < xs.length - 1) frame = requestAnimationFrame(tick); else onDone?.();
  };
  frame = requestAnimationFrame(tick);
  return () => cancelAnimationFrame(frame);
}

/* ---------- Figure 1: one update ---------- */
const PHASES = ['Collect', 'Sample', 'Look ahead', 'Target', 'Error', 'Step'];
const PHASE_MS = [2600, 2800, 3200, 3000, 3200, 4400];
function updateNote(u, sync, scale) {
  const prev = sync && u.number > 1 && u.number <= sync.window ? { target: sync.mean_target[u.number - 2], loss: sync.loss[u.number - 2] } : null;
  switch (u.key) {
    case 'first-update': return `Update 1, at step ${int(u.step)}. Until now the car only explored. The network has never been trained, so its values are close to zero and every target is close to −1.`;
    case 'first-goal-sample': return `Update ${u.number}, at step ${int(u.step)}. One of the 64 samples is a transition that reached the flag. Its target is just the reward: there is nothing after the goal to look ahead to.`;
    case 'after-first-sync': {
      const mean = u.batch.y.reduce((a, b) => a + b, 0) / u.batch.y.length;
      return `Update ${u.number}, at step ${int(u.step)}. The target network was just replaced by the online network.${prev ? ` The average target jumps from ${fmt(prev.target, 3)} one update earlier to ${fmt(mean, 3)}, and the loss from ${fmt(prev.loss, 2)} to ${fmt(u.loss, 2)}.` : ''}`;
    }
    case 'first-greedy-goal': return `Update ${int(u.number)}, at step ${int(u.step)}. In episode ${u.episode}, the car has just reached the flag using only the network's greedy choices, with no random steps. The update still learns from 64 stored transitions; the new success is 1 of ${int(u.buffer_size)}.`;
    default: return `Update ${int(u.number)}, at step ${int(u.step)}: the checkpoint the repository selected as best. Visited states\u2019 values now span about ${fmt(scale.low, 2)} to ${fmt(scale.high, 2)}, and one step moves them by at most ${fmt(u.grid.delta_scale, 2)}.`;
  }
}

function initUpdateFigure(root, data, sync) {
  const q = sel => root.querySelector(sel);
  const canvas = prepareCanvas(q('[data-map-canvas]'));
  const svg = q('[data-map-overlay]');
  const grid = data.grid;
  const firstVisit = decodeInt32(grid.first_visit);
  const state = { update: 0, phase: 0, tracked: data.updates[0].tracked, timer: null };
  const decoded = data.updates.map(u => {
    const before = Float32Array.from(decodeInt16(u.grid.v_before), x => x / 100);
    const delta = Float32Array.from(decodeInt16(u.grid.delta), x => x / 32767 * u.grid.delta_scale);
    const mask = visitedMask(firstVisit, u.step, grid.nx, grid.ny);
    return { before, delta, mask, scale: valueScale(before, mask) };
  });
  const chips = q('[data-update-chips]');
  data.updates.forEach((u, i) => {
    const button = html('button', { type: 'button', 'aria-pressed': 'false' });
    button.append(document.createTextNode(u.label), html('small', {}, `update ${int(u.number)}`));
    button.addEventListener('click', () => { stop(); state.update = i; state.phase = 0; state.tracked = u.tracked; render(); });
    chips.append(button);
  });
  root.querySelectorAll('[data-phase]').forEach(button => button.addEventListener('click', () => { stop(); state.phase = Number(button.dataset.phase); render(); }));
  const controls = q('[data-update-controls]');
  controls.querySelector('[data-action="previous"]').addEventListener('click', () => { stop(); state.phase = Math.max(0, state.phase - 1); render(); });
  controls.querySelector('[data-action="next"]').addEventListener('click', () => { stop(); state.phase = Math.min(5, state.phase + 1); render(); });
  controls.querySelector('[data-action="sample"]').addEventListener('click', () => { state.tracked = (state.tracked + 1) % data.batch_size; render(); });
  const playButton = controls.querySelector('[data-action="play"]');
  playButton.addEventListener('click', () => (state.timer ? stop() : play()));
  function play() {
    if (state.phase === 5) state.phase = 0;
    playButton.textContent = 'Pause';
    render();
    const advance = () => {
      if (state.phase >= 5) { stop(); return; }
      state.phase += 1; render();
      state.timer = setTimeout(advance, PHASE_MS[state.phase]);
    };
    state.timer = setTimeout(advance, PHASE_MS[state.phase]);
  }
  function stop() { clearTimeout(state.timer); state.timer = null; playButton.textContent = 'Play this update'; }

  function render() {
    const u = data.updates[state.update], d = decoded[state.update], b = u.batch, t = state.tracked, phase = state.phase;
    chips.querySelectorAll('button').forEach((button, i) => button.setAttribute('aria-pressed', String(i === state.update)));
    q('[data-update-note]').textContent = updateNote(u, sync, decoded[state.update].scale);
    root.querySelectorAll('[data-phase]').forEach(button => {
      const i = Number(button.dataset.phase);
      button.classList.toggle('is-current', i === phase);
      button.classList.toggle('is-done', i < phase);
      button.setAttribute('aria-current', i === phase ? 'step' : 'false');
    });
    const s = b.s[t], a = b.a[t], s2 = b.s2[t], r = b.r[t], z = b.done[t];
    const qb = b.q_before[t], qa = b.q_after[t], qo = b.q_next_online[t], qt = b.q_next_target[t], star = b.a_star[t], y = b.y[t];
    const errors = b.y.map((target, i) => target - b.q_before[i][b.a[i]]);

    // Map: values before the update, or the change after it.
    const mode = phase === 5 ? 'delta' : 'value';
    if (mode === 'delta') {
      drawField(canvas, grid, d.delta, d.mask, 'delta', { max: u.grid.delta_scale });
      q('[data-map-title]').textContent = 'Change in each state\u2019s value from this one update';
      setLegend(q('[data-map-legend]'), 'delta', u.grid.delta_scale, u.grid.delta_scale);
    } else {
      drawField(canvas, grid, d.before, d.mask, 'value', d.scale);
      q('[data-map-title]').textContent = 'Value of each state before the update, max over actions';
      setLegend(q('[data-map-legend]'), 'value', d.scale.low, d.scale.high);
    }
    svg.replaceChildren();
    arrowMarker(svg, 'rldq-arrow-update', '#1d2733');
    drawAxes(svg);
    const path = u.episode_path;
    const line = path.map(([x, v]) => `${mx(x).toFixed(1)},${my(v).toFixed(1)}`).join(' ');
    if (phase <= 1) svg.append(el('polyline', { points: line, fill: 'none', stroke: '#1d2733', 'stroke-width': phase === 0 ? 2.2 : 1.4, opacity: phase === 0 ? 0.85 : 0.3 }));
    if (phase === 0) {
      for (const item of u.recent) svg.append(el('circle', { cx: mx(item.s2[0]), cy: my(item.s2[1]), r: 5, fill: item.explore ? '#996418' : '#2356a8', stroke: '#fff', 'stroke-width': 1.5 }));
      const last = path[path.length - 1], right = mx(last[0]) > MAP.left + MAP.plotW * 0.72;
      svg.append(el('text', { x: mx(last[0]) + (right ? -12 : 10), y: my(last[1]) - 10, 'text-anchor': right ? 'end' : 'start', class: 'rldq-note' }, 'car now'));
    }
    if (phase >= 1) {
      b.s.forEach(([x, v], i) => {
        if (phase === 5) svg.append(el('circle', { cx: mx(x), cy: my(v), r: 4.2, fill: 'none', stroke: '#1d2733', 'stroke-width': 1.2, opacity: 0.7 }));
        else svg.append(el('circle', { cx: mx(x), cy: my(v), r: 4.6, fill: ACTION_COLORS[b.a[i]], stroke: '#fff', 'stroke-width': 1.2, opacity: i === t ? 1 : 0.85 }));
      });
      svg.append(el('circle', { cx: mx(s[0]), cy: my(s[1]), r: 10, fill: 'none', stroke: '#1d2733', 'stroke-width': 2 }));
    }
    if (phase >= 2 && phase <= 4) {
      svg.append(el('line', { x1: mx(s[0]), y1: my(s[1]), x2: mx(s2[0]), y2: my(s2[1]), stroke: '#1d2733', 'stroke-width': 2, 'marker-end': 'url(#rldq-arrow-update)' }));
      svg.append(el('text', { x: mx(s2[0]) + 12, y: my(s2[1]) + 18, class: 'rldq-note' }, 's\u2032'));
      svg.append(el('text', { x: mx(s[0]) - 14, y: my(s[1]) - 14, 'text-anchor': 'end', class: 'rldq-note' }, 's'));
    }
    q('[data-map-caption]').textContent = mapCaption(u, phase);

    // Explanation and numbers.
    const title = q('[data-step-title]'), copy = q('[data-step-copy]'), numbers = q('[data-numbers]'), residuals = q('[data-residuals]');
    numbers.replaceChildren(); residuals.replaceChildren();
    title.textContent = `${phase + 1} · ${PHASES[phase]}`;
    const where = `s = (${fmt(s[0])}, ${fmt(s[1])})`;
    if (phase === 0) {
      const sources = u.recent.map(x => (x.explore ? 'random' : 'greedy'));
      const allSame = sources.every(x => x === sources[0]);
      const taken = allSame ? `all ${sources[0]}` : sources.join(', ');
      copy.textContent = u.number === 1
        ? `Episode ${u.episode}, step ${u.episode_step}. This is the first update: for ${int(data.learning_starts)} steps the car explored at random without learning, and every step was stored. Its newest ${u.recent.length} steps were ${taken}. Replay now holds ${int(u.buffer_size)} transitions, room for ${int(data.buffer_capacity)}. Epsilon is ${fmt(u.epsilon, 3)}.`
        : `Episode ${u.episode}, step ${u.episode_step}. The agent learns once every ${data.train_freq} steps, so it has taken ${u.recent.length} steps since the last update, ${taken}. Each was stored: replay now holds ${int(u.buffer_size)} transitions, room for ${int(data.buffer_capacity)}. Epsilon is ${fmt(u.epsilon, 3)}.`;
      numbers.append(recentTable(u));
    } else if (phase === 1) {
      const ages = b.age, current = ages.filter(age => age < u.episode_step).length;
      const actionsCount = [0, 1, 2].map(k => b.a.filter(x => x === k).length);
      copy.textContent = `The update ignores the order of experience. It draws ${data.batch_size} stored transitions uniformly at random. Their ages range from ${int(Math.min(...ages))} to ${int(Math.max(...ages))} steps, and ${current === 0 ? 'none' : current} of them come from the current episode. Dots are colored by the action taken: ${actionsCount[0]} left, ${actionsCount[1]} none, ${actionsCount[2]} right.`;
      numbers.append(sampleTable(b, t));
    } else if (phase === 2) {
      copy.textContent = z
        ? `The tracked transition reached the flag (terminated = 1). There is no next state to score, so both networks are skipped for this sample.`
        : `Double DQN splits the look-ahead in two. The online network picks the best next action at s\u2032: ${ACTIONS[star].toLowerCase()}. The target network, ${u.number <= data.target_update_interval ? 'still the copy made before training started' : u.updates_since_sync === 0 ? 'copied from the online network just before this update' : `last copied ${u.updates_since_sync} updates ago`}, scores that choice.`;
      numbers.append(lookaheadTable(qo, qt, star, z));
      if (z) numbers.append(html('p', { class: 'rldq-map-caption' }, 'Shown for reference only: these values are not used, because the transition reached the flag.'));
    } else if (phase === 3) {
      copy.textContent = z
        ? 'The same target as Part 1. At a goal transition the look-ahead term is multiplied by zero, so the target is the reward alone.'
        : 'The same target as Part 1, with the table lookup replaced by the target network\u2019s score of the chosen next action.';
      numbers.append(arith(z
        ? `target = r + gamma × (1 − terminated) × Q(s′, a*; theta⁻)<br>= ${fmt(r)} + ${data.gamma} × (1 − 1) × Q(s′, a*; theta⁻)<br>= <b>${fmt(y)}</b>`
        : `target = r + gamma × (1 − terminated) × Q(s′, a*; theta⁻)<br>= ${fmt(r)} + ${data.gamma} × (1 − 0) × (${fmt(qt[star])})<br>= <b>${fmt(y)}</b>`));
    } else if (phase === 4) {
      copy.textContent = `Each of the ${data.batch_size} samples has its own error. The loss is the average squared error, and one gradient step reduces that average; it does not fix any one error exactly.`;
      numbers.append(arith(`TD error = target − Q(s, a) = ${fmt(y)} − (${fmt(qb[a])})<br>= <b>${fmt(y - qb[a])}</b><br>loss = mean of TD error² over the ${data.batch_size} samples = <b>${fmt(u.loss)}</b>`));
      const maxAbs = Math.max(...errors.map(Math.abs)) || 1;
      errors.forEach((e, i) => {
        const span = html('span', { class: i === t ? 'is-tracked' : '' });
        const bar = html('i');
        const h = Math.abs(e) / maxAbs * 50;
        bar.style.height = `${Math.max(1, h)}%`;
        bar.style[e < 0 ? 'top' : 'bottom'] = '50%';
        span.append(bar); residuals.append(span);
      });
    } else {
      const share = (qa[a] - qb[a]) / (y - qb[a]);
      const moved = share < 0 ? 'away from its target, because the other samples pulled the shared weights the other way'
        : share > 1 ? 'past its target, because the other samples pushed the shared weights further' : `${pct(share)} of the way to its target`;
      copy.textContent = `Adam, with learning rate ${data.lr}, nudges every weight at once. Q(s, a) moved from ${fmt(qb[a])} to ${fmt(qa[a])}, ${moved}. The map shows the change in every state\u2019s value: the largest is ${fmt(u.grid.delta_scale, 3)}, and ${int(u.grid['cells_changed_over_1e-3'])} of ${int(grid.nx * grid.ny)} map cells moved by more than 0.001. In Part 1, one update changed one table cell.`;
      numbers.append(moveBar(qb[a], qa[a], y));
    }
    q('[data-sync]').textContent = u.number <= data.target_update_interval
      ? `Target network: the copy made before training started. The first sync comes after update ${data.target_update_interval}.`
      : `Target network: copied from the online network ${u.updates_since_sync === 0 ? 'just before this update' : `${u.updates_since_sync} updates ago`}; it is copied again every ${data.target_update_interval} updates.`;
    q('[data-update-live]').textContent = `${u.label}, step ${phase + 1} of 6: ${PHASES[phase]}. Tracking sample ${t + 1} of ${data.batch_size}, ${where}.`;
  }

  function mapCaption(u, phase) {
    if (phase === 5) return 'Blue means the value went up, ochre that it went down. Circles mark the 64 sampled states. Gray marks regions the run had not reached yet; the network still outputs values there, but no data supports them.';
    if (phase === 0) return 'The dark line is the current episode so far, and the newest 4 states are marked (ochre: random, blue: greedy). Darker blue means a higher value, fewer steps from the flag; colors span the middle 96% of visited states. Gray marks regions the run had not reached yet.';
    return `Each dot is one sampled state, colored by the action taken (ochre left, gray none, blue right). The ring marks the tracked sample.${phase === 1 ? ' The faint loop is the current episode.' : ''} Darker blue means a higher value, fewer steps from the flag; gray marks regions the run had not reached yet.`;
  }
  function recentTable(u) {
    const table = html('table');
    table.innerHTML = '<thead><tr><th>Newest steps</th><th>Position</th><th>Velocity</th><th>Push</th><th>Source</th></tr></thead>';
    const body = html('tbody');
    u.recent.forEach((x, i) => {
      const row = html('tr');
      row.append(html('td', {}, `${i + 1}`), html('td', {}, fmt(x.s2[0])), html('td', {}, fmt(x.s2[1])), html('td', {}, ACTION_SHORT[x.a]), html('td', {}, x.explore ? 'random' : 'greedy'));
      body.append(row);
    });
    table.append(body);
    return table;
  }
  function sampleTable(b, t) {
    const table = html('table');
    table.innerHTML = `<thead><tr><th>Tracked sample</th><th>${t + 1} of ${b.s.length}</th></tr></thead>`;
    const body = html('tbody');
    for (const [name, value] of [
      ['State s (position, velocity)', `(${fmt(b.s[t][0])}, ${fmt(b.s[t][1])})`], ['Action a', ACTIONS[b.a[t]]], ['Reward r', fmt(b.r[t])],
      ['Next state s′', `(${fmt(b.s2[t][0])}, ${fmt(b.s2[t][1])})${b.done[t] ? ', at the flag' : ''}`], ['Stored', `${int(b.age[t])} steps ago`]]) {
      const row = html('tr'); row.append(html('td', {}, name), html('td', {}, value)); body.append(row);
    }
    table.append(body);
    return table;
  }
  function lookaheadTable(qo, qt, star, z) {
    const table = html('table', { class: z ? 'is-unused' : '' });
    table.innerHTML = `<thead><tr><th>At s′</th>${ACTION_SHORT.map(name => `<th>${name}</th>`).join('')}</tr></thead>`;
    const body = html('tbody');
    for (const [label, values, cls] of [['Online network, Q(s′, ·; theta)', qo, 'is-pick'], ['Target network, Q(s′, ·; theta⁻)', qt, 'is-used']]) {
      const row = html('tr');
      row.append(html('td', {}, label));
      values.forEach((value, k) => row.append(html('td', { class: !z && k === star ? cls : '' }, fmt(value))));
      body.append(row);
    }
    table.append(body);
    return table;
  }
  function arith(content) { const box = html('div', { class: 'rldq-arith' }); box.innerHTML = content; return box; }
  function moveBar(before, after, target) {
    // Progress space: before at 0, target at 1, after at its share of the way (it can overshoot or go backward).
    const share = (after - before) / (target - before || 1);
    const lo = Math.min(0, share), hi = Math.max(1, share), span = hi - lo;
    const pos = x => `${((x - lo) / span * 100).toFixed(2)}%`;
    const wrap = html('div');
    const row = html('div', { class: 'rldq-move' });
    const bar = html('div', { class: 'rldq-move-bar' });
    const fill = html('b'); fill.style.left = pos(Math.min(0, share)); fill.style.width = `${(Math.abs(share) / span * 100).toFixed(2)}%`;
    const start = html('i', { class: 'is-start' }); start.style.left = pos(0);
    const mark = html('i'); mark.style.left = pos(1);
    bar.append(fill, start, mark);
    row.append(html('span', {}, `before ${fmt(before)}`), bar, html('span', {}, `target ${fmt(target)}`));
    wrap.append(row, html('p', { class: 'rldq-map-caption' }, `Blue: how far Q(s, a) moved in one step, to ${fmt(after)}. The ochre tick is the target.`));
    return wrap;
  }

  render();
  return {
    exportFrame(updateIndex, phase, tracked = null, note = '') {
      stop();
      state.update = updateIndex; state.phase = phase;
      state.tracked = tracked ?? data.updates[updateIndex].tracked;
      root.dataset.exportMode = 'true';
      const label = q('[data-export-note]');
      label.hidden = !note; label.textContent = note;
      render();
    },
    updates: data.updates.map(u => ({ number: u.number, key: u.key, step: u.step, tracked: u.tracked })),
  };
}

/* ---------- Figure 2: target network between syncs ---------- */
function initTargetFigure(root, data) {
  const svg = root.querySelector('[data-target-chart]');
  const chips = root.querySelector('[data-target-chips]');
  const caption = root.querySelector('[data-target-caption]');
  const options = [{ key: 'average', label: 'Minibatch averages' }, ...data.probes.map((p, i) => ({ key: i, label: p.name }))];
  let current = 'average';
  options.forEach(option => {
    const button = html('button', { type: 'button', 'aria-pressed': 'false' }, option.label);
    button.addEventListener('click', () => { current = option.key; render(); });
    chips.append(button);
  });
  const P = { left: 112, right: 18, top: 18, height: 236, lossTop: 290, lossHeight: 66, width: 960 };
  const n = data.window;
  const px = u => P.left + (u - 1) / (n - 1) * (P.width - P.left - P.right);
  function render() {
    chips.querySelectorAll('button').forEach((button, i) => button.setAttribute('aria-pressed', String(options[i].key === current)));
    const online = current === 'average' ? data.mean_q : data.probes[current].online;
    const target = current === 'average' ? data.mean_target : data.probes[current].target;
    const all = online.concat(target);
    const ticksY = niceTicks(Math.min(...all), Math.max(...all), 5);
    const step = ticksY[1] - ticksY[0];
    const lo = Math.min(ticksY[0], Math.floor(Math.min(...all) / step) * step), hi = Math.max(ticksY[ticksY.length - 1], Math.ceil(Math.max(...all) / step) * step);
    const py = v => P.top + (hi - v) / (hi - lo) * P.height;
    svg.replaceChildren();
    svg.append(el('rect', { x: P.left, y: P.top, width: P.width - P.left - P.right, height: P.height, class: 'rldq-axis' }));
    for (let v = lo; v <= hi + step * 1e-9; v += step) {
      svg.append(el('line', { x1: P.left - 5, x2: P.left, y1: py(v), y2: py(v), class: 'rldq-axis' }));
      svg.append(el('text', { x: P.left - 9, y: py(v) + 5, 'text-anchor': 'end', class: 'rldq-tick' }, fmt(Math.round(v / step) * step, 3)));
    }
    for (const u of [1, 250, 500, 750, 1000, 1250, 1500]) svg.append(el('text', { x: px(u), y: P.lossTop + P.lossHeight + 24, 'text-anchor': u === 1 ? 'start' : u === 1500 ? 'end' : 'middle', class: 'rldq-tick' }, int(u)));
    for (const s of data.syncs) {
      svg.append(el('line', { x1: px(s + 0.5), x2: px(s + 0.5), y1: P.top, y2: P.lossTop + P.lossHeight, stroke: '#996418', 'stroke-width': 1, 'stroke-dasharray': '4 4', opacity: 0.7 }));
    }
    svg.append(el('text', { x: px(250.5) + 6, y: P.top + 16, class: 'rldq-note', fill: '#6f4a10' }, 'sync'));
    const pathOf = (values, y) => values.map((v, i) => `${i ? 'L' : 'M'}${px(i + 1).toFixed(1)},${y(v).toFixed(1)}`).join('');
    svg.append(el('path', { d: pathOf(target, py), fill: 'none', stroke: '#996418', 'stroke-width': 2.4 }));
    svg.append(el('path', { d: pathOf(online, py), fill: 'none', stroke: '#2356a8', 'stroke-width': 1.6 }));
    const names = current === 'average' ? ['Target y, minibatch average', 'Online Q(s, a), minibatch average'] : ['Target network\u2019s value at this state', 'Online network\u2019s value at this state'];
    const legend = root.querySelector('[data-target-legend]');
    legend.replaceChildren();
    [['#996418', names[0]], ['#2356a8', names[1]]].forEach(([color, name]) => {
      const item = html('span'); const swatch = html('i'); swatch.style.background = color; item.append(swatch, document.createTextNode(name)); legend.append(item);
    });
    // Loss on a log scale.
    const logs = data.loss.map(x => Math.log10(Math.max(x, 1e-6)));
    const llo = Math.min(...logs), lhi = Math.max(...logs);
    const ly = v => P.lossTop + (lhi - v) / (lhi - llo || 1) * P.lossHeight;
    svg.append(el('rect', { x: P.left, y: P.lossTop, width: P.width - P.left - P.right, height: P.lossHeight, class: 'rldq-axis' }));
    svg.append(el('path', { d: pathOf(logs, ly), fill: 'none', stroke: '#6b7f99', 'stroke-width': 1 }));
    for (let e = Math.ceil(llo); e <= Math.floor(lhi); e += 2) {
      svg.append(el('line', { x1: P.left - 5, x2: P.left, y1: ly(e), y2: ly(e), class: 'rldq-axis' }));
      svg.append(el('text', { x: P.left - 9, y: ly(e) + 5, 'text-anchor': 'end', class: 'rldq-tick' }, e >= 0 ? String(10 ** e) : `0.${'0'.repeat(-e - 1)}1`));
    }
    svg.append(el('text', { x: P.left + 8, y: P.lossTop + 16, class: 'rldq-note' }, 'Loss, log scale'));
    svg.append(el('text', { x: (P.left + P.width - P.right) / 2, y: P.lossTop + P.lossHeight + 70, 'text-anchor': 'middle', class: 'rldq-label' }, 'Gradient update'));
    const before = data.mean_target[249], after = data.mean_target[250];
    caption.textContent = current === 'average'
      ? `Just before the first sync, the minibatch target averaged ${fmt(before, 3)}; just after it, ${fmt(after, 3)}. Every sync lets the targets look about one more step ahead, so values keep falling toward their real size, and the loss spikes each time the target moves.`
      : `At this one state, the target network\u2019s value (ochre) is flat between syncs and jumps at each one, while the online value (blue) moves after every update.`;
  }
  render();
}

/* ---------- Figure 3: exploration lab ---------- */
const HOLDS = [
  { label: '1 step', min: 1, max: 1, copy: 'A new random push every step. Pushes mostly cancel out, so the car jiggles near the bottom of the valley.' },
  { label: '5 to 15', min: 5, max: 15, copy: 'Short holds add up to small swings, but rarely enough to climb out.' },
  { label: '20 to 60', min: 20, max: 60, copy: 'About as long as half a swing. A held push can build momentum, and swings sometimes add up to the flag. The repository\u2019s recipe uses this range.' },
  { label: '30 to 70', min: 30, max: 70, copy: 'Longer holds often keep pushing after the moment to turn around, which works against the swing.' },
  { label: '50 to 80', min: 50, max: 80, copy: 'Very long holds fight the car\u2019s own motion for much of each swing.' },
];
function initExploreFigure(root) {
  const svg = root.querySelector('[data-explore-map]');
  const chips = root.querySelector('[data-explore-chips]');
  const hillSvg = root.querySelector('[data-explore-hill] svg');
  const W = 640, H = 420, L = 58, R = 10, T = 12, B = 46;
  const ex = p => L + (p + 1.2) / 1.8 * (W - L - R);
  const ev = v => T + (0.07 - v) / 0.14 * (H - T - B);
  let seed = 7, current = 2, results = [], replayIndex = 0, cancel = () => {};
  HOLDS.forEach((hold, i) => {
    const button = html('button', { type: 'button', 'aria-pressed': 'false' }, hold.label);
    if (i === 2) button.append(html('small', {}, 'used in training'));
    button.addEventListener('click', () => { current = i; replayIndex = 0; render(); });
    chips.append(button);
  });
  root.querySelector('[data-action="seed"]').addEventListener('click', () => { seed += 1; compute(); replayIndex = 0; render(); });
  root.querySelector('[data-action="replay"]').addEventListener('click', () => { replayIndex += 1; replay(); });
  function compute() { results = HOLDS.map(h => runExplorationProbe({ holdMin: h.min, holdMax: h.max, episodes: 500, seed })); }
  function render() {
    const result = results[current];
    chips.querySelectorAll('button').forEach((button, i) => button.setAttribute('aria-pressed', String(i === current)));
    svg.replaceChildren();
    svg.append(el('rect', { x: L, y: T, width: W - L - R, height: H - T - B, class: 'rldq-axis' }));
    for (const p of [-1.2, -0.6, 0, 0.6]) svg.append(el('text', { x: ex(p), y: H - B + 20, 'text-anchor': 'middle', class: 'rldq-tick' }, fmt(p)));
    for (const v of [-0.07, 0, 0.07]) svg.append(el('text', { x: L - 8, y: ev(v) + 5, 'text-anchor': 'end', class: 'rldq-tick' }, fmt(v)));
    svg.append(el('line', { x1: ex(0.5), x2: ex(0.5), y1: T, y2: H - B, stroke: '#39754d', 'stroke-width': 1.5, 'stroke-dasharray': '6 5' }));
    svg.append(el('text', { x: ex(0.5) - 6, y: T + 16, 'text-anchor': 'end', class: 'rldq-note', fill: '#2f6545' }, 'flag'));
    svg.append(el('text', { x: (L + W - R) / 2, y: H - 6, 'text-anchor': 'middle', class: 'rldq-label' }, 'Position'));
    svg.append(el('text', { x: 14, y: (T + H - B) / 2, 'text-anchor': 'middle', class: 'rldq-label', transform: `rotate(-90 14 ${(T + H - B) / 2})` }, 'Velocity'));
    for (const run of result.paths) {
      svg.append(el('polyline', { points: run.path.map(([x, v]) => `${ex(x).toFixed(1)},${ev(v).toFixed(1)}`).join(' '), fill: 'none', stroke: run.goal ? '#39754d' : '#7d93b2', 'stroke-width': run.goal ? 1.8 : 1, opacity: run.goal ? 0.95 : 0.55 }));
    }
    root.querySelector('[data-explore-count]').textContent = `${result.goals} of ${result.episodes} episodes reached the flag`;
    root.querySelector('[data-explore-copy]').textContent = `${HOLDS[current].copy} Green traces reached the flag within 200 steps.`;
    const head = root.querySelector('[data-explore-table] thead tr'), counts = root.querySelector('[data-explore-table] tbody tr');
    head.replaceChildren(html('th', { scope: 'row' }, 'Hold length'));
    counts.replaceChildren(html('th', { scope: 'row' }, 'Goals in 500'));
    results.forEach((r, i) => {
      head.append(html('th', { scope: 'col', class: i === current ? 'is-current' : '' }, HOLDS[i].label));
      counts.append(html('td', { class: i === current ? 'is-current' : '' }, `${r.goals}`));
    });
    root.querySelector('[data-explore-seed]').textContent = `Seed ${seed}. Your counts change with the seed; the pattern holds.`;
    replay();
  }
  function replay() {
    cancel();
    const result = results[current];
    const ordered = [...result.paths].sort((a, b) => (b.goal - a.goal) || (Math.max(...b.path.map(p => p[0])) - Math.max(...a.path.map(p => p[0]))));
    const run = ordered[replayIndex % ordered.length];
    const car = drawHill(hillSvg);
    cancel = animatePath(car, run.path.map(p => p[0]));
  }
  compute();
  render();
}

/* ---------- Figure 4: training explorer ---------- */
function initTrainingFigure(root, data) {
  const canvas = prepareCanvas(root.querySelector('[data-map-canvas]'));
  const svg = root.querySelector('[data-map-overlay]');
  const slider = root.querySelector('[data-training-slider]');
  const label = root.querySelector('[data-training-label]');
  const startsBox = root.querySelector('[data-training-starts]');
  const hillSvg = root.querySelector('[data-training-hill] svg');
  const curve = root.querySelector('[data-training-curve]');
  const grid = data.grid, firstVisit = decodeInt32(grid.first_visit);
  const checkpoints = [...data.checkpoints].sort((a, b) => a.step - b.step);
  const decoded = checkpoints.map(c => {
    const values = Float32Array.from(decodeInt16(c.v), x => x / data.scales.value);
    const mask = visitedMask(firstVisit, c.step, grid.nx, grid.ny);
    return { values, actions: decodeUint8(c.a), mask, scale: valueScale(values, mask) };
  });
  const bestIndex = checkpoints.findIndex(c => c.name === 'best.pt');
  const state = { index: bestIndex, start: 5, timer: null };
  slider.max = String(checkpoints.length - 1);
  slider.value = String(state.index);
  let cancel = () => {};
  data.starts.forEach((start, i) => {
    const button = html('button', { type: 'button', 'aria-pressed': 'false' }, fmt(start));
    button.addEventListener('click', () => { state.start = i; render(true); });
    startsBox.append(button);
  });
  slider.addEventListener('input', () => { stop(); state.index = Number(slider.value); render(true); });
  const playButton = root.querySelector('[data-action="play-training"]');
  playButton.addEventListener('click', () => (state.timer ? stop() : play()));
  root.querySelector('[data-action="drive"]').addEventListener('click', () => render(true));
  function play() {
    if (state.index >= checkpoints.length - 1) state.index = 0;
    playButton.textContent = 'Pause';
    const advance = () => {
      render(false);
      if (state.index >= checkpoints.length - 1) { stop(); render(true); return; }
      state.index += 1; slider.value = String(state.index);
      state.timer = setTimeout(advance, reduceMotion.matches ? 1600 : 900);
    };
    advance();
  }
  function stop() { clearTimeout(state.timer); state.timer = null; playButton.textContent = 'Play training'; }
  const rollout = (c, i) => {
    const r = c.rollouts[i];
    const xs = Array.from(decodeInt16(r.x), x => x / data.scales.x), vs = Array.from(decodeInt16(r.v), v => v / data.scales.v);
    return { ...r, xs, vs };
  };
  function render(drive) {
    const c = checkpoints[state.index], d = decoded[state.index], r = rollout(c, state.start);
    const best = c.name === 'best.pt';
    label.textContent = `Step ${int(c.step)} · ${int(c.updates)} updates${best ? ' · selected' : ''}`;
    drawField(canvas, grid, d.values, d.mask, 'value', d.scale);
    setLegend(root.querySelector('[data-training-legend]'), 'value', d.scale.low, d.scale.high);
    svg.replaceChildren();
    drawAxes(svg);
    // Greedy push on a coarse grid, only where the run had been.
    for (let row = 1; row < grid.ny; row += 4) {
      for (let col = 1; col < grid.nx; col += 4) {
        const k = row * grid.nx + col;
        if (!d.mask[k]) continue;
        const x = mx(grid.positions[col]), y = my(grid.velocities[row]), action = d.actions[k];
        if (action === 1) svg.append(el('circle', { cx: x, cy: y, r: 1.8, fill: '#56616e', opacity: 0.8 }));
        else svg.append(el('path', { d: action === 2 ? `M${x - 6},${y} L${x + 5},${y} M${x + 1},${y - 4} L${x + 5},${y} L${x + 1},${y + 4}` : `M${x + 6},${y} L${x - 5},${y} M${x - 1},${y - 4} L${x - 5},${y} L${x - 1},${y + 4}`, stroke: '#1d2733', 'stroke-width': 1.3, fill: 'none', opacity: 0.55 }));
      }
    }
    svg.append(el('polyline', { points: r.xs.map((x, i) => `${mx(x).toFixed(1)},${my(r.vs[i]).toFixed(1)}`).join(' '), fill: 'none', stroke: '#1d2733', 'stroke-width': 2.4 }));
    svg.append(el('circle', { cx: mx(r.xs[0]), cy: my(r.vs[0]), r: 6, fill: '#fff', stroke: '#1d2733', 'stroke-width': 2 }));
    const endX = mx(r.xs[r.xs.length - 1]), endY = my(r.vs[r.vs.length - 1]);
    svg.append(el('circle', { cx: endX, cy: endY, r: 6, fill: r.goal ? '#39754d' : '#996418', stroke: '#fff', 'stroke-width': 1.5 }));
    startsBox.querySelectorAll('button').forEach((button, i) => button.setAttribute('aria-pressed', String(i === state.start)));
    root.querySelector('[data-training-outcome]').textContent = r.goal
      ? `From ${fmt(r.start)}: reached the flag in ${r.steps} steps`
      : `From ${fmt(r.start)}: still short of the flag at the 200-step limit`;
    root.querySelector('[data-training-summary]').textContent = `This checkpoint\u2019s greedy policy reaches the flag from ${c.goals} of ${data.starts.length} starts.`;
    drawCurve(c);
    cancel();
    const car = drawHill(hillSvg);
    if (drive) cancel = animatePath(car, r.xs); else placeCar(car, r.xs[r.xs.length - 1]);
  }
  const ends = data.episodes.end_step, goals = data.episodes.goal;
  const rate = ends.map((_, i) => { const lo = Math.max(0, i - 19); let s = 0; for (let j = lo; j <= i; j += 1) s += goals[j]; return s / (i - lo + 1); });
  function drawCurve(c) {
    const W = 960, H = 150, L = 34, R = 14, T = 10, B = 28;
    const cx = step => L + step / 300000 * (W - L - R), cy = v => T + (1 - v) * (H - T - B);
    curve.replaceChildren();
    curve.append(el('rect', { x: L, y: T, width: W - L - R, height: H - T - B, class: 'rldq-axis' }));
    curve.append(el('path', { d: rate.map((v, i) => `${i ? 'L' : 'M'}${cx(ends[i]).toFixed(1)},${cy(v).toFixed(1)}`).join(''), fill: 'none', stroke: '#7d93b2', 'stroke-width': 1.2 }));
    for (const k of checkpoints) curve.append(el('circle', { cx: cx(k.step), cy: cy(k.goals / data.starts.length), r: 2.6, fill: '#2356a8' }));
    curve.append(el('line', { x1: cx(c.step), x2: cx(c.step), y1: T, y2: H - B, stroke: '#996418', 'stroke-width': 1.5 }));
    for (const s of [0, 50000, 100000, 150000, 200000, 250000, 300000]) curve.append(el('text', { x: cx(s), y: H - 8, 'text-anchor': s === 300000 ? 'end' : s ? 'middle' : 'start', class: `rldq-tick${s % 100000 ? ' rldq-minor' : ''}` }, s === 0 ? '0' : s === 300000 ? '300k steps' : `${s / 1000}k`));
    curve.append(el('text', { x: L - 6, y: cy(1) + 5, 'text-anchor': 'end', class: 'rldq-tick' }, '1'));
    curve.append(el('text', { x: L - 6, y: cy(0) + 5, 'text-anchor': 'end', class: 'rldq-tick' }, '0'));
  }
  render(false);
  return {
    exportFrame(index, start = 5, position = null) {
      stop(); state.index = index; state.start = start; slider.value = String(index);
      root.dataset.exportMode = 'true';
      render(false);
      if (position !== null) placeCar(hillSvg.querySelector('[data-car]'), position);
    },
    rolloutPositions(index, start = 5) { return rollout(checkpoints[index], start).xs; },
    checkpoints: checkpoints.map(c => ({ name: c.name, step: c.step, goals: c.goals })),
  };
}

/* ---------- boot ---------- */
const settle = promise => promise.then(value => ({ value }), error => ({ error }));
function showFailure(root, error) {
  root.append(html('p', { class: 'rldq-fallback' }, 'This figure could not load its recorded data. The text describes the same numbers.'));
  console.error(`${root.id}:`, error);
}
async function boot() {
  const api = {};
  window.DQNPilot = api;
  const updateRoot = document.querySelector('[data-dqn-update]');
  const targetRoot = document.querySelector('[data-dqn-target]');
  const trainingRoot = document.querySelector('[data-dqn-training]');
  const exploreRoot = document.querySelector('[data-dqn-explore]');
  let failures = 0;
  const run = (root, init) => {
    try { return init(); } catch (error) { failures += 1; showFailure(root, error); return undefined; }
  };
  // Figure 3 needs no recorded data, so it starts at once and never waits on the others.
  if (exploreRoot) run(exploreRoot, () => initExploreFigure(exploreRoot));
  // Each figure loads and starts on its own: one failure cannot blank the rest.
  const [sync, updates, training] = await Promise.all([targetRoot, updateRoot, trainingRoot].map(root => (root ? settle(loadJSON(root.dataset.src)) : Promise.resolve(null))));
  const loaded = (root, result) => {
    if (!root || !result) return false;
    if (result.error) { failures += 1; showFailure(root, result.error); return false; }
    return true;
  };
  if (loaded(targetRoot, sync)) run(targetRoot, () => initTargetFigure(targetRoot, sync.value));
  if (loaded(updateRoot, updates)) api.update = run(updateRoot, () => initUpdateFigure(updateRoot, updates.value, sync && sync.value ? sync.value : null));
  if (loaded(trainingRoot, training)) api.training = run(trainingRoot, () => initTrainingFigure(trainingRoot, training.value));
  document.documentElement.dataset.dqnReady = failures ? 'partial' : 'true';
}
boot();
