# Q-learning draft: editorial handoff

## Two-file manifest and scope

- `_posts/<date>-q-learning-one-update-at-a-time.md`: exploration-first educational article with two independent browser learners, source-grounded code examples, and the separate native repository demonstration.
- `tools/qlearning/EDITORIAL_NOTES.md`: this handoff and review boundary.

Only those two files were edited in the existing `ali/qlearning-educational-pilot` worktree. This review runs no Git operations, staging, commits, training, tests, browser work, builds, environment installs, publication, or outreach. UI, CSS, core, config, and media remain parent-owned. Reader commands in the article were retained, not executed.

## Figure 1: actual sampled experience

The exact shared core was read. `createExplorationTrace` constructs `createLearner` and calls `learner.step()` without action overrides. Every recorded transition contains its actual selection evidence, before/after Q-tables, and episode metadata. Episode summaries preserve paths, lengths, actions, selections, and outcomes. No fixed successful route is used by either browser figure. The older fixed-action helper remains only a test control and is not part of the public story.

The parent's verified default trace uses `SFFF/FHFH/FFFH/HFFG`, alpha 0.1, gamma 0.95, epsilon 0.3, seed 7, cap 60, and 120 episodes totaling 843 transitions. The article states these as default trace facts, not promised outcomes for different settings. The trace includes failures, wall actions, revisits, goals, and unchanged updates rather than showing successful experience alone.

Opening episodes are explicitly varied: episode 1 lasts 12 moves and ends in hole 7; episodes 2 and 3 last five and four moves and end in hole 5. State resets retain the learner's Q-table. All 120 complete episode records remain seekable; the episode selector, actual path/outcome/length display, selection labels, playback, and phase controls are parent-owned presentation.

## Observed milestones and preserved arithmetic

The following numbers are from the parent's verified default trace, not newly executed by this editorial child:

- Index 0: episode 1, `0 Up -> 0`, epsilon-explore selection, wall interaction, zero reward/old value/target/TD error.
- Index 11: episode 1, `6 Right -> 7`, first hole, reward 0, true terminal.
- Index 210: episode 29, `14 Right -> 15`, first goal, selected through `greedy-tie`, terminal reward 1, old 0, target 1, TD error 1, new 0.1.
- Index 550: episode 70, `13 Right -> 14`, first positive zero-reward bootstrap, epsilon-explore selection, next maximum 0.1, old 0, target 0.095, TD error 0.095, new 0.0095.
- Index 735: episode 103, `0 Down -> 4`, first positive start-state action, epsilon-explore selection, old 0, target 2.86298946875e-5, new 2.86298946875e-6. Public prose rounds the new value to approximately `2.863e-6`.

The nine display equations remain intact: return, general target/TD/update, first-goal arithmetic, and first-bootstrap arithmetic. Episode labels and narrative now match sampled milestones rather than adjacent prescribed episodes. No old forced-route episode count, transition count, action sequence, or third-episode arithmetic remains in the public draft.

Values propagate through later observed revisits, never a retroactive sweep. A zero residual can reflect lack of downstream evidence rather than complete learning. The first goal and first positive bootstrap are separated by the intervening recorded experience; snapshots are never replaced with a newly zeroed table or an unrelated final table.

## Selection evidence and independent histories

The article distinguishes `explore`, `greedy`, and `greedy-tie` selection. A random maximizing tie is not an epsilon-exploration event. Conversely, the epsilon branch can choose a currently best action. Random-looking actions therefore do not identify the branch by themselves.

Figure 1 inspects individual sampled experience. Figure 2 independently trains in 500-episode batches using the same world, TD update, defaults, and constant selected epsilon. Each learner begins with its own zero table; neither imports the other's learned values. Alpha, gamma, and epsilon are now shared controls, and changing any of them resets both histories. The previous epsilon-only-Figure-2 description was removed.

Parent's unchanged Figure 2 default baseline is 267 goals, 233 holes, and 3,336 interactions for 500 episodes. This is a parent regression target, not an additional public benchmark claim. Neither figure's interaction cap marks a still-continuing next state as truly terminal; bootstrap remains intact.

## Portable highlights and poster

The article references the existing `q-update.png`, `q-update.gif`, and `q-update.webm` paths with revised descriptions. Parent must replace and verify those exports before handoff.

- Poster target: sharper 2x PNG of episode 70's first positive zero-reward bootstrap. Alt text states `13 Right -> 14`, target 0.095, new value 0.0095. It explicitly does not imply a new zero-table run beginning at this snapshot.
- GIF/video target: edited highlights of complete episodes 1, 2, 29, 70, and 103, totaling 40 selected transitions. They are not a continuous 40-step training run.
- Visible jump notices and captions must account for omitted episodes and updates. Each shown snapshot retains their effects. All omitted experience remains available in the interactive figure.
- No newly verified export, sharpness, duration, or browser appearance is claimed by this child. Compact white layout and media/UI changes are exclusively parent-owned.

## Retained code, references, and native repository section

Four Python examples and their preceding `rlql-code-caption` paragraphs remain: NumPy table construction, one-cell update, adapted update-before-stop training interaction, and deterministic/epsilon-greedy action selection. They remain partial implementation excerpts, not standalone programs. The YAML selection and README-grounded fresh-uv training/evaluation/GIF commands are unchanged. The existing HTML map wrapper is preserved, with no CSS or highlighting edits.

Previously read exact pinned sources remain the basis for these examples: `agent.py`, `main.py`, `Qlearning/README.md`, `frozenlake.yaml`, `utils/evaluate.py`, and `utils/make_gif.py`, revision `27ea78dc267363afec2d447f1ba0278bfccdf89e`. Public Watkins/Dayan, canonical Sutton/Barto, and Gymnasium references are retained. The off-policy maximum, terminal/time-limit semantics, coverage/learning-rate conditions, constant-alpha limitations, and DQN caveats are preserved.

The native repository section retains its separate `{% include rl/qlearning-native.html %}` and facts: deterministic 8 by 8 `FrozenLake-v1`, 64 states, alpha 0.1, gamma 0.99, cap 200, recipe budget 5,000, seed 42, exponential epsilon decay 1 to 0.05 at rate 0.001, and CPU NumPy learning with PyTorch checkpoint serialization.

Native saved-checkpoint scope remains unchanged: selected at training episode 1011 using a ten-episode training window; fresh unfiltered evaluation reached the goal in 200 of 200 same-map/start episodes, length 16 each, with the Q-table unchanged and no new training. Neither independent-map generalization, slippery-dynamics evidence, shortest-path optimality, nor full table convergence is claimed.

The native GIF remains a distinct byte-exact copy of the committed repository GIF, with 51 frames, 11.16 seconds, and three showcase repeats of one saved-policy route. Its poster/pause include and native asset paths are separate from the new 4 by 4 sampled-experience highlights. Only the caption's obsolete description of the browser animation was corrected; the native experiment facts and commands were not changed.

## Remaining verification and publication boundary

The post is publication-ready in `_posts/`; the draft flags were removed when the owner approved publishing. Keep both existing browser includes plus the native include. This notes file must stay out of public site output. Public copy must contain no private paths, Task IDs, internal links, personal/company claims, or em/en dashes. Medium and Substack adaptations are in `platform-drafts/`.

This contribution claims exact-source reading and editorial review only. Parent owns final tests, full-trace milestone checks, baseline regression, shared-control resets, compact rendering, selection labels, phase playback, poster sharpness, and highlight exports/jump notices. No browser/runtime/media/build verification or blocked-toolchain workaround was attempted here. No content-direction question remains unresolved.
