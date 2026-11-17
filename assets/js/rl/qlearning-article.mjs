import { ACTIONS, ARROWS, MAP, DEFAULTS, createExplorationTrace, createLearner, greedyRollout, formatQ } from './qlearning-core.mjs';

const worked = document.querySelector('[data-ql-worked]');
const policy = document.querySelector('[data-ql-policy]');
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
const rate = value => value.toFixed(2);
let params = { alpha: DEFAULTS.alpha, gamma: DEFAULTS.gamma, epsilon: DEFAULTS.epsilon };
let trace = createExplorationTrace(params), moveIndex = 0, phase = 0;
let playback = null, replayGeneration = 0, lastRenderedMove = -1;
let learner = createLearner(params), active = false, generation = 0, scheduled = null, scheduledKind = null;
const titles = ['Inspect the selected action', 'Observe the move', 'Read the reward', 'Read the next estimate', 'Form the target', 'Update one entry'];
const point = state => ({ x: 66 + (state % 4) * 76, y: 66 + Math.floor(state / 4) * 76 });
const episodeFor = record => trace.episodeSummaries[record.episode - 1];

function pauseExplanation() {
  if (playback !== null) clearTimeout(playback);
  playback = null; replayGeneration += 1;
  if (worked) {
    const button = worked.querySelector('[data-worked-play]');
    button.textContent = 'Play this episode'; button.setAttribute('aria-pressed', 'false');
  }
}
function selectionLabel(record) {
  return record.selection === 'explore' ? 'Explore · random action'
    : record.selection === 'greedy-tie' ? 'Greedy branch · random maximal tie'
      : 'Greedy branch · highest estimate';
}
function selectionExplanation(record) {
  if (record.selection === 'explore') {
    return `The recorded random draw ${formatQ(record.exploreDraw)} is below ε = ${rate(record.epsilon)}. Choose a uniformly random action: ${ACTIONS[record.action]}. It can happen to be a currently best action too.`;
  }
  if (record.selection === 'greedy-tie') {
    return `The draw is not below ε = ${rate(record.epsilon)}. Several actions share the maximum; the greedy branch randomly chooses ${ACTIONS[record.action]} among those ties. This is not an ε-exploration event.`;
  }
  return `The draw is not below ε = ${rate(record.epsilon)}. ${ACTIONS[record.action]} has the largest current estimate, so the greedy branch selects it.`;
}
function populateEpisodes() {
  if (!worked) return;
  worked.querySelector('[data-trace-episode]').innerHTML = trace.episodeSummaries.map((episode, index) =>
    `<option value="${index}">${episode.episode} · ${episode.length} moves · ${episode.outcome}</option>`).join('');
  worked.querySelector('#ql-guided-move').max = String(trace.records.length - 1);
}
function drawWorld(record, table, movement) {
  const tiles = MAP.join('').split('');
  worked.querySelector('[data-guided-tiles]').innerHTML = tiles.map((tile, state) => {
    const x = 12 + state % 4 * 76, y = 12 + Math.floor(state / 4) * 76;
    const estimate = Math.max(...table[state]);
    const strength = Math.max(0, Math.min(1, estimate));
    let fill = tile === 'H' ? '#f8eeee' : tile === 'G' ? '#e8f2eb'
      : `rgb(${Math.round(250 - strength * 33)},${Math.round(251 - strength * 20)},${Math.round(252 - strength * 29)})`;
    let stroke = tile === 'H' ? '#dfc6c6' : tile === 'G' ? '#a2c0ac' : '#cdd5de';
    if (state === record.state) { fill = '#eef4ff'; stroke = '#2356a8'; }
    if (state === record.nextState) {
      fill = record.hole ? '#f8eeee' : '#edf5ef';
      stroke = record.hole ? '#994848' : '#39754d';
    }
    const highlighted = state === record.state || state === record.nextState;
    return `<rect data-guided-state="${state}" x="${x}" y="${y}" width="68" height="68" rx="3" fill="${fill}" stroke="${stroke}" stroke-width="${highlighted ? 2 : 1}"/><text x="${x + 6}" y="${y + 15}" class="rlql-grid-id">${state}</text>${'SHG'.includes(tile) ? `<text x="${x + 34}" y="${y + 39}" text-anchor="middle" class="rlql-grid-letter">${tile}</text>` : ''}${!'HG'.includes(tile) && estimate > 0 ? `<text x="${x + 34}" y="${y + 57}" text-anchor="middle" class="rlql-grid-value">${formatQ(estimate)}</text>` : ''}`;
  }).join('');
  const start = point(record.state), end = point(record.nextState);
  const length = Math.hypot(end.x - start.x, end.y - start.y);
  const arrow = worked.querySelector('[data-guided-action-arrow]');
  arrow.setAttribute('visibility', length === 0 ? 'hidden' : 'visible');
  if (length > 0) {
    const dx = (end.x - start.x) / length, dy = (end.y - start.y) / length;
    for (const [key, value] of Object.entries({ x1: start.x + dx * 12, y1: start.y + dy * 12, x2: end.x - dx * 16, y2: end.y - dy * 16 })) arrow.setAttribute(key, String(value));
  }
  const episode = episodeFor(record);
  const seen = episode.states.slice(0, record.episodeStep + (phase >= 1 ? 1 : 0));
  worked.querySelector('[data-trace-path]').setAttribute('points', seen.map(state => `${point(state).x},${point(state).y}`).join(' '));
  worked.querySelector('[data-trace-path-copy]').textContent = `Path so far: ${seen.join(' → ')}`;
  const fraction = movement === null ? (phase >= 1 ? 1 : 0) : movement;
  const agent = worked.querySelector('[data-worked-agent]');
  const resetMotion = moveIndex !== lastRenderedMove || movement !== null;
  if (resetMotion) agent.style.transition = 'none';
  agent.style.transform = `translate(${start.x + (end.x - start.x) * fraction}px,${start.y + (end.y - start.y) * fraction}px)`;
  if (resetMotion && movement === null) { getComputedStyle(agent).transform; agent.style.transition = ''; }
  lastRenderedMove = moveIndex;
  worked.querySelector('#ql-world-desc').textContent = `Recorded episode ${record.episode}, move ${record.episodeStep}. ${selectionLabel(record)}: ${ACTIONS[record.action]} from ${record.state} to ${record.nextState}. ${record.hole ? 'A true-terminal hole.' : record.goal ? 'The true-terminal goal.' : length === 0 ? 'The boundary keeps the agent in place.' : 'A continuing move.'}`;
}
function renderWorked(announce = false, movement = null) {
  if (!worked) return;
  const r = trace.records[moveIndex], episode = episodeFor(r), table = phase === 5 ? r.qAfter : r.qBefore;
  worked.dataset.phase = String(phase); worked.dataset.move = String(moveIndex); worked.dataset.episode = String(r.episode);
  worked.querySelector('[data-guided-position]').textContent = `Episode ${r.episode} / ${trace.episodes} · Move ${r.episodeStep} / ${episode.length}`;
  const selection = worked.querySelector('[data-trace-selection]');
  selection.textContent = selectionLabel(r); selection.dataset.selection = r.selection;
  worked.querySelector('[data-worked-table-title]').textContent = phase === 5 ? 'Q-table after this update' : 'Q-table before this update';
  const states = r.state === r.nextState ? [r.state] : [r.state, r.nextState];
  worked.querySelector('[data-worked-table]').innerHTML = states.map((state, row) => {
    const terminalNext = state === r.nextState && r.terminated;
    return `<tr${terminalNext ? ' class="rlql-terminal-row"' : ''}><th scope="row">${state} (${states.length === 1 ? 's=s′' : row === 0 ? 's' : 's′'})</th>${table[state].map((value, action) => {
      const current = row === 0 && action === r.action;
      const next = state === r.nextState && phase >= 3 && !r.terminated && r.nextMax > 0 && r.qBefore[state][action] === r.nextMax;
      const classes = [current ? 'rlql-current' : '', current && phase === 5 ? 'rlql-updated' : '', next ? 'rlql-next-max' : ''].filter(Boolean).join(' ');
      return `<td${classes ? ` class="${classes}"` : ''}${current ? ' data-current-q' : ''} title="${value.toPrecision(12)}">${formatQ(value)}</td>`;
    }).join('')}</tr>`;
  }).join('');
  worked.querySelector('[data-guided-full-table]').innerHTML = table.map((row, state) => `<tr><th scope="row">${state}</th>${row.map(value => `<td title="${value.toPrecision(12)}">${formatQ(value)}</td>`).join('')}</tr>`).join('');
  worked.querySelector('[data-guided-next-note]').textContent = r.terminated
    ? `${r.hole ? 'The hole' : 'The goal'} truly terminates the task: future bootstrap is zero.`
    : r.nextMax === 0 ? 'The next maximum is still zero; useful downstream evidence may not have arrived.'
      : `Best next Q = ${formatQ(r.nextMax)}, learned from earlier recorded visits.`;
  worked.querySelector('[data-guided-start-value]').textContent = formatQ(phase === 5 ? r.startValueAfter : r.startValueBefore);
  const seenSelections = episode.selections.slice(0, r.episodeStep);
  const knownOutcome = (r.terminated || r.truncated) && phase >= 2;
  worked.querySelector('[data-trace-summary]').textContent = `${seenSelections.filter(choice => choice === 'explore').length} random-branch selections through this move · ${table.flat().filter(value => value > 0).length} positive Q entries${knownOutcome ? ` · episode ends at ${episode.outcome}` : ''}`;
  worked.querySelector('[data-guided-observation]').textContent = `${r.state} → ${r.nextState} · ${ACTIONS[r.action]} · reward ${phase >= 2 ? r.reward : '?'}${r.state === r.nextState ? ' · wall: stays in place' : ''}`;
  drawWorld(r, table, movement);
  const copies = [
    selectionExplanation(r),
    r.state === r.nextState ? `The action meets a boundary. State remains ${r.state}; a wall does not terminate the task.` : `Observe ${ACTIONS[r.action]} from ${r.state} to ${r.nextState}. No estimate has changed in this phase.`,
    r.goal ? 'Goal entry gives reward 1 and truly terminates.' : r.hole ? 'Hole entry gives reward 0 and truly terminates.' : 'This continuing move gives reward 0. A future estimate can still produce a nonzero update.',
    r.terminated ? 'No continuation is added at a true terminal, even if a next-row estimate were positive.' : `The best next estimate is ${formatQ(r.nextMax)}. The target uses that maximum, not the next explored action.`,
    `Target ${formatQ(r.target)} minus old Q ${formatQ(r.oldValue)} gives TD error ${formatQ(r.error)}.`,
    r.increment === 0 ? `The update increment α × TD error is zero; Q(${r.state}, ${ACTIONS[r.action]}) stays ${formatQ(r.newValue)}. ${r.error === 0 ? 'A zero residual does not prove convergence.' : 'Here α is zero even though the TD error is nonzero.'}` : `Apply α × error = ${formatQ(r.increment)}. Only Q(${r.state}, ${ACTIONS[r.action]}) changes to ${formatQ(r.newValue)}.`
  ];
  worked.querySelector('[data-worked-step-number]').textContent = `${phase + 1} / 6`;
  worked.querySelector('[data-worked-step-title]').textContent = titles[phase];
  worked.querySelector('[data-worked-step-copy]').textContent = copies[phase];
  worked.querySelector('[data-worked-old]').textContent = formatQ(r.oldValue);
  worked.querySelector('[data-worked-alpha]').textContent = rate(params.alpha);
  worked.querySelector('[data-worked-error]').textContent = phase >= 4 ? formatQ(r.error) : '?';
  worked.querySelector('[data-worked-new]').textContent = phase >= 5 ? formatQ(r.newValue) : '?';
  worked.querySelector('[data-worked-target]').textContent = phase >= 4
    ? `${r.terminated ? `Terminal target = ${r.reward}` : `Target = ${r.reward} + ${rate(params.gamma)} × ${formatQ(r.nextMax)} = ${formatQ(r.target)}`}; error = ${formatQ(r.error)}.`
    : 'Target = reward + discounted best next Q. No future term at true terminals.';
  for (const [index, item] of [...worked.querySelector('[data-worked-phases]').children].entries()) {
    item.classList.toggle('is-current', index === phase); item.classList.toggle('is-done', index < phase);
    if (index === phase) item.setAttribute('aria-current', 'step'); else item.removeAttribute('aria-current');
  }
  for (const button of worked.querySelectorAll('[data-guided-chapter]')) {
    button.disabled = trace.milestones[button.dataset.guidedChapter] === null;
    button.title = button.disabled ? 'No such event was observed in this finite recording at these settings.' : 'Inspect the actual recorded transition';
  }
  worked.querySelector('[data-trace-episode]').value = String(r.episode - 1);
  worked.querySelector('#ql-guided-move').value = String(moveIndex);
  worked.querySelector('#ql-guided-move').setAttribute('aria-valuetext', `Recorded transition ${moveIndex + 1} of ${trace.records.length}, episode ${r.episode}, move ${r.episodeStep} of ${episode.length}`);
  worked.querySelector('[data-guided-move-output]').value = `${moveIndex + 1} / ${trace.records.length}`;
  worked.querySelector('[data-worked-back]').disabled = moveIndex === 0 && phase === 0;
  worked.querySelector('[data-worked-next]').disabled = moveIndex === trace.records.length - 1 && phase === 5;
  worked.querySelector('[data-guided-next-move]').disabled = moveIndex === trace.records.length - 1;
  worked.querySelector('[data-trace-previous-episode]').disabled = r.episode === 1;
  worked.querySelector('[data-trace-next-episode]').disabled = r.episode === trace.episodes;
  if (announce) worked.querySelector('[data-worked-live]').textContent = `Episode ${r.episode}, move ${r.episodeStep}. ${selectionLabel(r)}. ${titles[phase]}. ${copies[phase]}`;
}
function seek(index, nextPhase = 0) {
  if (!Number.isInteger(index) || index < 0 || index >= trace.records.length || !Number.isInteger(nextPhase) || nextPhase < 0 || nextPhase > 5) throw new RangeError('Invalid recorded position');
  pauseExplanation(); moveIndex = index; phase = nextPhase; renderWorked(true);
}
function advance() {
  if (phase < 5) phase += 1;
  else if (moveIndex < trace.records.length - 1) { moveIndex += 1; phase = 0; }
  renderWorked(true);
}
function chooseEpisode(index) {
  if (index >= 0 && index < trace.episodeSummaries.length) seek(trace.episodeSummaries[index].startIndex);
}
function stopPolicy() {
  active = false; generation += 1;
  if (scheduled !== null) {
    if (scheduledKind === 'raf') cancelAnimationFrame(scheduled); else clearTimeout(scheduled);
    scheduled = null; scheduledKind = null;
  }
  if (policy) {
    policy.querySelector('[data-policy-train]').disabled = false;
    policy.querySelector('[data-policy-replay]').disabled = false;
    policy.querySelector('[data-policy-stop]').disabled = true;
  }
}
function setBusy() {
  active = true;
  policy.querySelector('[data-policy-train]').disabled = true;
  policy.querySelector('[data-policy-replay]').disabled = true;
  policy.querySelector('[data-policy-stop]').disabled = false;
}
function renderPolicy(agentState = null, visited = []) {
  if (!policy) return;
  const snapshot = learner.snapshot(), tiles = MAP.join('').split('');
  const grid = policy.querySelector('[data-policy-grid]');
  grid.innerHTML = tiles.map((tile, state) => {
    const best = Math.max(...snapshot.q[state]);
    const arrow = best > 0 && !'HG'.includes(tile) ? ARROWS[snapshot.q[state].indexOf(best)] : '·';
    const classes = ['rlql-tile', tile === 'H' ? 'is-hole' : '', tile === 'G' ? 'is-goal' : '', tile === 'S' ? 'is-start' : '', agentState === state ? 'is-agent' : '', visited.includes(state) ? 'is-visited' : ''].filter(Boolean).join(' ');
    const strength = Math.max(0, Math.min(1, best));
    const style = 'HG'.includes(tile) ? '' : ` style="background:rgb(${Math.round(250 - strength * 33)},${Math.round(251 - strength * 20)},${Math.round(252 - strength * 29)})"`;
    return `<div class="${classes}" data-policy-state="${state}"${style}><small>${state}</small><span>${'SHG'.includes(tile) ? tile : arrow}</span></div>`;
  }).join('');
  grid.setAttribute('aria-label', `Same four by four world. ${snapshot.episodes} exploratory episodes, ${snapshot.goals} goals. ${agentState === null ? 'Arrows show first greedy maxima.' : `Greedy replay at state ${agentState}.`}`);
  policy.querySelector('[data-policy-episodes]').textContent = String(snapshot.episodes);
  policy.querySelector('[data-policy-goals]').textContent = String(snapshot.goals);
  policy.querySelector('[data-policy-value]').textContent = formatQ(Math.max(...snapshot.q[0]));
  policy.querySelector('[data-policy-table]').innerHTML = snapshot.q.map((row, state) => `<tr><th scope="row">${state}</th>${row.map(value => `<td title="${value.toPrecision(12)}">${formatQ(value)}</td>`).join('')}</tr>`).join('');
  const end = Math.max(1, snapshot.episodes), history = snapshot.history.filter((_, index) => index % Math.max(1, Math.floor(snapshot.history.length / 100)) === 0);
  policy.querySelector('[data-policy-line]').setAttribute('points', history.map(row => `${30 + row.episode / end * 350},${130 - Math.min(1, row.startValue) * 110}`).join(' '));
  policy.querySelector('[data-policy-sparkline]').setAttribute('aria-label', `Start-state estimate after ${snapshot.episodes} episodes: ${formatQ(Math.max(...snapshot.q[0]))}. Not a convergence proof.`);
  policy.querySelector('[data-policy-settings]').textContent = `Shared α = ${rate(params.alpha)}, γ = ${rate(params.gamma)}, ε = ${rate(params.epsilon)}; seed ${snapshot.seed}. Each figure has its own table.`;
}
function resetPolicy(message = 'Reset: this independent experiment starts with all 64 values zero.') {
  stopPolicy(); learner = createLearner(params); renderPolicy();
  if (policy) policy.querySelector('[data-policy-status]').textContent = message;
}
function changeSettings() {
  pauseExplanation(); trace = createExplorationTrace(params); moveIndex = 0; phase = 0; lastRenderedMove = -1;
  populateEpisodes(); renderWorked(true);
  resetPolicy('Settings changed. Both independent experiments reset; no recorded values were copied here.');
}
if (worked) {
  worked.querySelector('[data-interactive-controls]').hidden = false;
  populateEpisodes();
  worked.querySelector('[data-worked-next]').addEventListener('click', () => { pauseExplanation(); advance(); });
  worked.querySelector('[data-worked-back]').addEventListener('click', () => { pauseExplanation(); if (phase > 0) phase -= 1; else if (moveIndex > 0) { moveIndex -= 1; phase = 5; } renderWorked(true); });
  worked.querySelector('[data-guided-next-move]').addEventListener('click', () => { if (moveIndex < trace.records.length - 1) seek(moveIndex + 1); });
  worked.querySelector('[data-worked-reset]').addEventListener('click', () => seek(0));
  worked.querySelector('#ql-guided-move').addEventListener('input', event => seek(Number(event.target.value)));
  worked.querySelector('[data-trace-episode]').addEventListener('change', event => chooseEpisode(Number(event.target.value)));
  worked.querySelector('[data-trace-previous-episode]').addEventListener('click', () => chooseEpisode(trace.records[moveIndex].episode - 2));
  worked.querySelector('[data-trace-next-episode]').addEventListener('click', () => chooseEpisode(trace.records[moveIndex].episode));
  worked.querySelector('[data-guided-result]').addEventListener('click', () => seek(episodeFor(trace.records[moveIndex]).endIndex, 5));
  for (const button of worked.querySelectorAll('[data-guided-chapter]')) button.addEventListener('click', () => {
    const index = trace.milestones[button.dataset.guidedChapter]; if (index !== null) seek(index, 5);
  });
  worked.querySelector('[data-worked-play]').addEventListener('click', () => {
    if (playback !== null) { pauseExplanation(); return; }
    const end = episodeFor(trace.records[moveIndex]).endIndex;
    if (moveIndex === end && phase === 5) { moveIndex = episodeFor(trace.records[moveIndex]).startIndex; phase = 0; renderWorked(true); }
    const token = replayGeneration;
    worked.querySelector('[data-worked-play]').textContent = 'Pause this episode'; worked.querySelector('[data-worked-play]').setAttribute('aria-pressed', 'true');
    const tick = () => {
      if (playback === null || token !== replayGeneration) return;
      advance();
      if (moveIndex === end && phase === 5) pauseExplanation();
      else playback = setTimeout(tick, trace.records[moveIndex].phaseDurationsMs[phase]);
    };
    playback = setTimeout(tick, trace.records[moveIndex].phaseDurationsMs[phase]);
  });
  for (const input of worked.querySelectorAll('[data-param]')) input.addEventListener('input', () => {
    params[input.dataset.param] = Number(input.value);
    worked.querySelector(`[data-${input.dataset.param}-output]`).value = rate(params[input.dataset.param]);
    changeSettings();
  });
  worked.querySelector('[data-guided-defaults]').addEventListener('click', () => {
    params = { alpha: DEFAULTS.alpha, gamma: DEFAULTS.gamma, epsilon: DEFAULTS.epsilon };
    for (const name of Object.keys(params)) {
      worked.querySelector(`[data-param="${name}"]`).value = String(params[name]);
      worked.querySelector(`[data-${name}-output]`).value = rate(params[name]);
    }
    changeSettings();
  });
  renderWorked();
}
if (policy) {
  policy.querySelector('[data-interactive-controls]').hidden = false; renderPolicy();
  const status = policy.querySelector('[data-policy-status]');
  policy.querySelector('[data-policy-reset]').addEventListener('click', () => resetPolicy());
  policy.querySelector('[data-policy-stop]').addEventListener('click', () => { stopPolicy(); status.textContent = 'Stopped. Completed episodes and learned values are retained.'; });
  policy.querySelector('[data-policy-train]').addEventListener('click', () => {
    stopPolicy(); setBusy(); const token = generation, end = learner.snapshot().episodes + 500;
    const batch = () => {
      if (!active || token !== generation) return;
      learner.train(Math.min(20, end - learner.snapshot().episodes)); renderPolicy(); const snapshot = learner.snapshot();
      status.textContent = `Learning in batches: ${snapshot.episodes} completed episodes, ${snapshot.goals} goals. All updates computed locally.`;
      if (snapshot.episodes < end) { scheduledKind = 'raf'; scheduled = requestAnimationFrame(batch); }
      else {
        stopPolicy(); const rollout = greedyRollout(snapshot.q);
        status.textContent = `Finished ${snapshot.episodes} exploratory episodes (${snapshot.goals} goals, ${snapshot.holes} holes, ${snapshot.timeouts} limits). ${rollout.goal ? `The frozen greedy route reaches the goal in ${rollout.transitions.length} moves.` : 'The greedy policy does not yet reach the goal; keep learning or reset.'}`;
      }
    };
    scheduledKind = 'raf'; scheduled = requestAnimationFrame(batch);
  });
  policy.querySelector('[data-policy-replay]').addEventListener('click', () => {
    stopPolicy(); const rollout = greedyRollout(learner.snapshot().q), token = generation;
    const completed = () => rollout.goal ? `Goal reached in ${rollout.transitions.length} moves. Replay made no Q-table updates.` : `Replay ended at ${rollout.hole ? 'a hole' : 'the 60-step limit'}. The table is unchanged.`;
    if (reducedMotion.matches || rollout.states.every(state => state === 0)) { renderPolicy(rollout.states.at(-1), rollout.states); status.textContent = completed(); return; }
    setBusy(); let index = 0;
    const frame = () => {
      if (!active || token !== generation) return;
      renderPolicy(rollout.states[index], rollout.states.slice(0, index + 1));
      status.textContent = `Frozen greedy replay: state ${rollout.states[index]}, move ${index} of ${rollout.transitions.length}. No exploration or learning.`;
      if (index < rollout.states.length - 1) { index += 1; scheduledKind = 'timer'; scheduled = setTimeout(frame, 320); }
      else { stopPolicy(); status.textContent = completed(); }
    };
    frame();
  });
}
function stopForContext(reason) {
  const wasActive = active; pauseExplanation(); stopPolicy();
  if (wasActive && policy) policy.querySelector('[data-policy-status]').textContent = `Stopped ${reason}. Completed episodes and values retained; use Learn or Replay to continue.`;
}
document.addEventListener('visibilitychange', () => { if (document.hidden) stopForContext('while this tab was hidden'); });
reducedMotion.addEventListener('change', () => stopForContext('because the motion preference changed'));

// Static highlighting stays readable without JavaScript; these controls only copy text.
for (const pre of document.querySelectorAll('.rlql-prose .highlight pre')) {
  const container = pre.closest('.highlighter-rouge') || pre.closest('.highlight');
  if (!container || container.querySelector('.rlql-code-toolbar')) continue;
  const toolbar = document.createElement('div'); toolbar.className = 'rlql-code-toolbar';
  const label = document.createElement('span'); label.textContent = 'Code example';
  const button = document.createElement('button'); button.type = 'button'; button.textContent = 'Copy code';
  button.addEventListener('click', async () => {
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(pre.textContent);
      else {
        const field = document.createElement('textarea'); field.value = pre.textContent; field.style.position = 'fixed'; field.style.opacity = '0'; document.body.append(field); field.select();
        const copied = document.execCommand('copy'); field.remove(); button.focus(); if (!copied) throw new Error('Copy unavailable');
      }
      button.textContent = 'Copied';
    } catch { button.textContent = 'Select text to copy'; }
  });
  toolbar.append(label, button); container.prepend(toolbar);
}
const nativeDemo = document.querySelector('[data-native-demo]');
let nativePlaying = false, nativeUserPaused = false, nativeObserver = null;
function setNativePlaying(playing) {
  if (!nativeDemo) return;
  nativePlaying = playing;
  const image = nativeDemo.querySelector('[data-native-image]'); image.src = playing ? image.dataset.gifSrc : image.dataset.posterSrc;
  const button = nativeDemo.querySelector('[data-native-play]');
  button.textContent = playing ? 'Pause real agent GIF' : 'Play real agent GIF'; button.setAttribute('aria-pressed', String(playing));
}
function disarmNativeAutoplay() {
  if (nativeObserver) { nativeObserver.disconnect(); nativeObserver = null; }
}
// Start once, from the first frame, when Figure 3 is in view. A reader's pause or a reduced-motion preference wins.
function armNativeAutoplay() {
  if (!nativeDemo || nativePlaying || nativeUserPaused || reducedMotion.matches || nativeObserver) return;
  if (!('IntersectionObserver' in window)) { setNativePlaying(true); return; }
  nativeObserver = new IntersectionObserver(entries => {
    if (!entries.some(entry => entry.isIntersecting && entry.intersectionRatio >= 0.4)) return;
    disarmNativeAutoplay();
    if (!nativeUserPaused && !reducedMotion.matches) setNativePlaying(true);
  }, { threshold: 0.4 });
  nativeObserver.observe(nativeDemo.querySelector('[data-native-image]'));
}
if (nativeDemo) {
  const image = nativeDemo.querySelector('[data-native-image]'); image.dataset.posterSrc = image.getAttribute('src');
  nativeDemo.querySelector('[data-native-controls]').hidden = false;
  nativeDemo.querySelector('[data-native-play]').addEventListener('click', () => {
    disarmNativeAutoplay(); nativeUserPaused = nativePlaying; setNativePlaying(!nativePlaying);
  });
  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches) { disarmNativeAutoplay(); setNativePlaying(false); } else armNativeAutoplay();
  });
  armNativeAutoplay();
}
window.QLearningPilot = Object.freeze({
  exploration: () => ({ phase, moveIndex, params: { ...params }, transition: trace.records[moveIndex], episode: episodeFor(trace.records[moveIndex]), length: trace.records.length, episodes: trace.episodes }),
  trace: () => trace,
  policy: () => learner.snapshot(),
  exportFrame: (index, nextPhase, movement = nextPhase >= 1 ? 1 : 0, note = '') => {
    if (!Number.isInteger(index) || index < 0 || index >= trace.records.length || !Number.isInteger(nextPhase) || nextPhase < 0 || nextPhase > 5 || !Number.isFinite(movement) || movement < 0 || movement > 1 || typeof note !== 'string') throw new RangeError('Invalid export position');
    pauseExplanation(); moveIndex = index; phase = nextPhase; worked.dataset.exportMode = 'true';
    const label = worked.querySelector('[data-trace-export-note]'); label.hidden = false;
    label.textContent = note || 'Edited highlights. All omitted episodes and updates remain in the interactive recording.';
    renderWorked(false, movement);
  }
});
