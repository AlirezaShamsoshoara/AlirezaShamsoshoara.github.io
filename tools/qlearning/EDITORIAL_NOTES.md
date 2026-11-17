# Q-learning post: editorial notes

Facts the post relies on, and the limits it states. Use them when editing the post or its platform versions.

## Default recording (browser model)

- Map `SFFF/FHFH/FFFH/HFFG`, actions Left, Down, Right, Up. Goal reward 1, every other reward 0. Holes and the goal are true terminals; the 60-step cap keeps the bootstrap.
- Alpha 0.1, gamma 0.95, constant epsilon 0.3, seed 7: 120 episodes and 843 transitions, with failures, wall moves, revisits and goals.
- Episode 1 lasts 12 moves and ends in hole 7; episodes 2 and 3 last 5 and 4 moves and end in hole 5. Resets keep the Q-table.

## Milestones (index, episode, transition)

- 0, episode 1, `0 Up -> 0`: exploration into the wall; reward, old value, target and TD error all 0.
- 11, episode 1, `6 Right -> 7`: first hole; reward 0; true terminal.
- 210, episode 29, `14 Right -> 15`: first goal, chosen by a random tie among maximal values; target 1; Q goes from 0 to 0.1.
- 550, episode 70, `13 Right -> 14`: first positive zero-reward bootstrap, chosen by exploration; next maximum 0.1; target 0.095; Q goes from 0 to 0.0095.
- 735, episode 103, `0 Down -> 4`: first positive start-state value, chosen by exploration; target 2.86298946875e-5; new value 2.86298946875e-6 (the post says about 2.863e-6).

## Figures and media

- Figure 1 steps through the recording above. Its labels distinguish exploration, a unique greedy choice, and a random tie among maximal values: a tie is not exploration, and exploration can pick a currently best action.
- Figure 2 trains its own learner in 500-episode batches with the same settings, and changing alpha, gamma or epsilon resets both figures. Default baseline: 267 goals, 233 holes and 3,336 interactions in 500 episodes, then a 6-move greedy route.
- The poster is a 2x PNG of the episode 70 bootstrap. The GIF and videos are edited highlights of whole episodes 1, 2, 29, 70 and 103 (40 transitions) with notices for the omitted moves; they are not a continuous run.
- Figure 3 is a byte-exact copy of the repository's `Qlearning/assets/qlearning_frozenlake_8x8.gif` (51 frames, 11.16 s, three repeats of one saved-policy route).

## Repository facts (revision 27ea78dc267363afec2d447f1ba0278bfccdf89e)

- Deterministic `FrozenLake-v1` 8x8: 64 states, alpha 0.1, gamma 0.99, cap 200, 5,000 training episodes, seed 42, epsilon decaying from 1 to 0.05 at rate 0.001. Learning is a NumPy table on CPU; PyTorch only serializes checkpoints.
- The saved checkpoint was selected at training episode 1011 on a ten-episode training window. An unfiltered re-evaluation reached the goal in 200 of 200 episodes, 16 moves each, with no training and the table unchanged.
- Code excerpts come from `agent.py` and `main.py`; the commands follow `Qlearning/README.md`, `frozenlake.yaml`, `utils/evaluate.py` and `utils/make_gif.py`.

## Limits the post states

- Values propagate through later revisits, not a backward sweep. A zero residual can mean missing evidence rather than completed learning.
- Repeated success on the same fixed map and start is repeatability, not generalization to other maps or slippery dynamics, shortest-path optimality, or full convergence.
- A constant alpha does not meet the decreasing learning-rate conditions of the convergence results.
- Public copy has no private paths, Task IDs, internal links, or em and en dashes.
