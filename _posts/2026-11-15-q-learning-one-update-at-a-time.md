---
title: "Q-learning: watch a table learn"
date: 2026-11-15
layout: rl-article
hero_image: /assets/media/rl/qlearning/q-learning-hero.svg
hero_alt: "Q-learning connects an observed gridworld move to a Q-table and updates one action value from 0 to 0.0095."
permalink: /blog/rl-from-zero/q-learning/
medium_url: https://medium.com/@a.shamsoshoara/q-learning-watch-a-table-learn-one-experience-at-a-time-82f20585f257
substack_url: https://ali1956283.substack.com/p/q-learning-how-a-table-learns-from
categories: [interesting-blogs, reinforcement-learning]
series: rl-from-zero
series_part: 1
tags: [rl-from-zero, q-learning, interactive]
excerpt: "Follow one experience into one changed table cell, then watch exploration and delayed rewards turn local updates into a policy."
read_time: true
---

A Q-learning agent does not start with a route to the goal. It starts with a table of guesses.

Each row represents a situation, each column an action. Their intersection asks: **How much future reward might this action lead to?** Starting from zeros, the agent acts, observes what happened, and revises one guess.

Those small revisions are the engine. No neural network is hiding behind them. Repeated local updates can produce a useful policy even when most actions earn nothing immediately.

Let's slow the process down until we can explain every number that changes.

## A table, a transition, and three different knobs

The two browser figures use the same deterministic 4 by 4 FrozenLake-style world, with 16 states and four actions in the order Left, Down, Right, Up:

<div class="rlql-map-matrix" data-map-matrix role="img" aria-label="Four by four map. Start at the upper-left, goal at the lower-right. Holes are at row 2 columns 2 and 4, row 3 column 4, and row 4 column 1.">
<pre class="rlql-map-grid" aria-hidden="true"><code>S F F F
F H F H
F F F H
H F F G</code></pre>
</div>

`S` is the start, `F` a safe tile, `H` a hole, and `G` the goal. States are numbered 0 through 15, left to right across each row. Reaching the goal gives reward 1; every other transition gives 0. Holes and the goal truly terminate the task. Actions do not slip randomly to another direction.

The agent's **state** is its current tile. An **episode** is one attempt, beginning at the start and ending at a terminal tile or an interaction limit.

A state should contain what is needed to predict the next outcome given an action. A tile identifier suffices here; other tasks might also need velocity or time remaining.

Write the table entry as `Q(s, a)`: the current estimate for action `a` in state `s`. One observed **transition** supplies a current state, chosen action, reward, next state, and whether the task truly terminated.

Three knobs do different jobs:

- **Alpha, the learning rate:** how far this update moves the old estimate toward new evidence.
- **Gamma, the discount factor:** how much later rewards count relative to nearer ones.
- **Epsilon, the exploration probability:** how often training chooses a random action instead of a currently best action.

Alpha changes learning. Gamma changes the objective. Epsilon changes data collection. They are not interchangeable ways to make the agent more adventurous.

**Figure 1 records real exploration, not a supplied route.** Starting from a zero table, the learner chooses epsilon-greedy actions in this world. At default alpha **0.1**, gamma **0.95**, epsilon **0.3**, and seed **7**, it records 120 varied episodes and 843 transitions, including walls, revisits, holes, and goals. Its table persists between episodes. The seed makes this trace repeatable, not a guarantee for other settings or runs.

{% include rl/qlearning-lab.html %}

## What is the number trying to estimate?

A reward is the immediate feedback from one transition. A **return** is the discounted sum of rewards from that point onward:

<p class="rl-equation"><code>G<sub>t</sub> = r<sub>t+1</sub> + gamma * r<sub>t+2</sub> + gamma<sup>2</sup> * r<sub>t+3</sub> + ...</code></p>

The first reward counts fully. Each later step adds another factor of gamma; true termination ends the sum. With gamma below one, an otherwise identical reward contributes more when received sooner.

Q-learning estimates expected return from taking an action, then acting optimally. This is not a guarantee about the next attempt: random transitions can give good actions bad outcomes.

Instead of waiting for the whole future, it updates using the observed reward and an existing table prediction. Learning partly from another estimate is **bootstrapping**.

## One update, in three lines

For a continuing transition, look at the next state's row and take its largest entry. That is the current estimate of the best continuation. For a true terminal transition, there is no continuation to add.

<p class="rl-equation"><code>target = r + gamma * (1 - terminated) * max<sub>a'</sub> Q(s', a')</code></p>
<p class="rl-equation"><code>TD error = target - Q(s, a)</code></p>
<p class="rl-equation"><code>Q<sub>new</sub>(s, a) = Q<sub>old</sub>(s, a) + alpha * TD error</code></p>

Here `s'` is the observed next state; `a'` ranges over its actions. `terminated` is one for true termination, zero otherwise. **TD**, temporal difference, measures the gap between the old estimate and this one-step target.

A positive gap raises the estimate; a negative gap lowers it; zero leaves it unchanged. Default alpha 0.1 applies one tenth of that correction.

Importantly, **only the cell for the state and action actually experienced is updated**. Reading the next row does not rewrite it. Nor does one transition replace every value in the current row.

## The first reward, then the first bootstrap

Follow the default trace's opening action: **state 0, Up, state 0**. The random epsilon branch chooses Up, but the upper boundary keeps the agent in place. Reward, old value, target, and TD error are zero. This is a real interaction, even though neither position nor value changes.

Episode one ends after 12 moves in hole 7. Episodes two and three last five and four moves, both ending in hole 5. The learner is not repeating a successful route.

Its **first goal arrives in episode 29**, on **state 14, Right, state 15**. Right is action index 2, selected by random tie-breaking among maximizing values, not the epsilon branch. The goal gives reward 1 and terminates. Using the default alpha, there is no future term to add:

<p class="rl-equation"><code>target = 1; TD error = 1 - 0 = 1</code></p>
<p class="rl-equation"><code>Q<sub>new</sub>(14, Right) = 0 + 0.1 * 1 = 0.1</code></p>

Only `Q(14, Right)` gains value, not every earlier action in the episode. Termination removes bootstrapping, not learning from the final reward.

The **first positive zero-reward bootstrap arrives in episode 70**: **state 13, Right, state 14**, selected through epsilon exploration. Reward is 0, but the next row contains the previously learned 0.1. With default gamma 0.95:

<p class="rl-equation"><code>target = 0 + 0.95 * 0.1 = 0.095</code></p>
<p class="rl-equation"><code>TD error = 0.095 - 0 = 0.095</code></p>
<p class="rl-equation"><code>Q<sub>new</sub>(13, Right) = 0 + 0.1 * 0.095 = 0.0095</code></p>

That correction comes entirely from a continuation estimate, not an extra reward for a safe tile: terminal reward first, bootstrapping on a later revisit.

<figure>
  <img src="{{ '/assets/media/rl/qlearning/q-update.png' | relative_url }}" alt="Episode 70's first positive zero-reward bootstrap: state 13, Right, state 14; target 0.095 and updated Q-value 0.0095.">
  <figcaption>Figure 1. The first positive zero-reward bootstrap in sampled experience. Earlier episodes supplied the next-state estimate; this snapshot does not begin a new zero-table run.</figcaption>
</figure>

The [animated GIF]({{ '/assets/media/rl/qlearning/q-update.gif' | relative_url }}), [WebM video]({{ '/assets/media/rl/qlearning/q-update.webm' | relative_url }}), and [H.264 MP4]({{ '/assets/media/rl/qlearning/q-update.mp4' | relative_url }}) are edited highlights of complete episodes **1, 2, 29, 70, and 103**, comprising 40 selected transitions. They are **not a continuous 40-step training run**. Jump notices identify skipped experience; each shown snapshot retains the effects of intervening updates. All 120 episodes remain available in the interactive figure. The equations above also work as a static explanation without JavaScript or animation.

Select an episode to inspect its actual path, length, and outcome, then play it or examine a transition's phases and before/after estimates. Selection labels distinguish epsilon exploration, a unique greedy choice, and random tie-breaking among maxima. **Resetting position does not reset the table.** Display values use at most four significant digits and scientific notation for tiny nonzero signals.

## Follow the equation into the code

The [pinned RL-from-zero agent](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/27ea78dc267363afec2d447f1ba0278bfccdf89e/Qlearning/ql/agent.py) makes the connection direct. These Python excerpts are parts of the implementation, **not standalone programs**: `self`, transition indices, and the environment belong to the surrounding agent and training loop.

<p class="rlql-code-caption"><strong>Table construction.</strong> Inside <code>QLearningAgent.__init__</code>, with one row per state and one column per action.</p>

```python
import numpy as np

self.Q = np.zeros((self.n_states, self.n_actions), dtype=np.float32)
```

The browser world needs 16 by 4 entries; the repository's default 8 by 8 world needs 64 by 4.

A `Transition` carries `s`, `a`, `r`, `s2`, and `done`. Here `done` means true termination, not an external time limit:

<p class="rlql-code-caption"><strong>One-cell update.</strong> Excerpt from <code>update</code>, after index and reward validation.</p>

```python
target = float(tr.r) + (
    0.0 if tr.done else self.gamma * float(np.max(self.Q[next_state]))
)
td_error = target - float(self.Q[state, action])
updated = float(self.Q[state, action]) + self.alpha * td_error
self.Q[state, action] = updated
```

The conditional implements the terminal mask. Returned `QLearningStats` exposes the target, TD error, and updated Q-value. Reward alone cannot explain the correction, because a continuing target also includes an estimated future.

The [training loop in `main.py`](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/27ea78dc267363afec2d447f1ba0278bfccdf89e/Qlearning/main.py) connects interaction to that update:

<p class="rlql-code-caption"><strong>Experience collection.</strong> Adapted from <code>train</code>; logging and checkpoint code are omitted. The environment, agent, configuration, and episode counter already exist.</p>

```python
state, _ = env.reset(seed=cfg.seed + episode)
state = int(state)
for step in range(cfg.max_steps_per_episode):
    action = agent.act(state)
    next_state, reward, terminated, truncated, _ = env.step(action)
    next_state = int(next_state)
    agent.update(Transition(
        state, action, float(reward), next_state, bool(terminated)
    ))
    state = next_state
    if terminated or truncated:
        break
```

Notice the order: update from the final observation, then stop. The terminal mask uses `terminated`, not `terminated or truncated`; the loop also ends at its configured step cap without changing that mask.

## Why explore if the table already recommends an action?

Early recommendations are mostly ignorance. When all four values are zero, the table has no evidence that Left is better than Right.

During epsilon-greedy training, the epsilon branch selects a uniformly random action; otherwise the agent selects a maximizing action, breaking maximizing ties randomly. These are distinct reasons for a random-looking choice. Tie-breaking is not an epsilon-exploration event, and the epsilon branch can itself pick a currently best action. Epsilon therefore is not the probability of making a visibly different choice.

The repository decays epsilon with training steps. Both browser figures instead hold it fixed at the selected value until a control changes. Too-rapid decay can leave useful routes undiscovered, especially when many unrewarded moves precede the first goal visit.

For deterministic evaluation, the same agent uses `np.argmax`, which returns the first maximum. That path neither samples randomness nor advances the exploration schedule:

<p class="rlql-code-caption"><strong>Action selection.</strong> Excerpt from <code>act</code>, after state validation.</p>

```python
if deterministic:
    return int(np.argmax(self.Q[state]))
self.global_step += 1
if np.random.rand() < self.epsilon():
    return int(np.random.randint(self.n_actions))
candidates = np.flatnonzero(self.Q[state] == np.max(self.Q[state]))
return int(np.random.choice(candidates))
```

Evaluation picks the first maximizing column; training samples a random action or maximizing tie. A repeatable choice from an unlearned row is still not evidence of knowledge.

### The subtle part: the target is off-policy

Suppose exploration will choose Down at the next state, while Right currently has the largest Q-value. The update above still uses the value of Right.

Why? Experience comes from an exploratory behavior policy, but the target evaluates the best continuation. That separation makes Q-learning **off-policy**: it uses the next-row maximum, not the Q-value of the next explored action.

SARSA instead evaluates the next action actually selected, making it on-policy. Both can explore; they evaluate different future behavior. Either still needs coverage: unseen actions cannot teach the table their values.

## How a distant reward travels backward

On a safe move, reward is zero. Does that mean nothing can be learned? No: the estimate can still change when the discounted best continuation differs from the current Q-value. It is the TD error, not the reward alone, that determines the correction.

In the default trace, a start-state action first gains value in **episode 103**: epsilon exploration chooses **state 0, Down, state 4**. Its old value is zero; a now-positive continuation estimate raises it to approximately `2.863e-6`. That small, rounded number reflects downstream evidence accumulated over many sampled visits.

Why not at the first goal? Reaching the goal does not revisit or retroactively rewrite earlier transitions. This is **not an instantaneous backward sweep**: later observed revisits expose earlier actions to improved estimates. The complete trace includes the unsuccessful and unchanged updates between milestones.

A zero TD error only says this observed target and estimate agree. Both can be zero because useful downstream evidence has not arrived, not because learning is complete.

## Watch a policy form, not just a cell change

**Figure 2 explores in bulk.** Figure 1 examines individual sampled transitions; Figure 2 runs an independent learner in 500-episode batches. Both use the same world, TD update, default epsilon **0.3**, and seed **7**, starting from separate zero tables.

They share settings, not histories. Changing **alpha, gamma, or epsilon resets both learners**. Neither figure copies learned Q-values into the other.

{% include rl/qlearning-policy.html %}

**Figure 2.** Training collects exploratory experience; greedy replay follows its current table. Arrows summarize best-valued actions, not a supplied solution. A fixed seed supports repeatability, not guaranteed success within a particular budget.

Without JavaScript, browser-local training does not run, but the static map and equations still explain the update. Both figures use a 60-step interaction boundary: a still-continuing transition retains bootstrap when collection stops.

These are two views of tabular learning, **not benchmarks of the repository's default deterministic 8 by 8 setup**.

## Ending an episode is not always ending the task

Two events can stop a loop: the task terminates, or collection stops before the task terminates. They do not automatically deserve the same learning target.

A hole or goal truly ends this task. Suppress the continuation term. An external limit can merely interrupt a still-continuing task. In that case, retain the continuation estimate from the final observed state, not from the reset state of the next attempt.

But do not turn that rule into "ignore every time limit." If a deadline is part of the task itself, reaching it can be a genuine terminal event. A finite-horizon state may need to include time remaining. Decide what the task means before deciding the mask. A library's loop-stop flag alone is not a complete specification of the objective.

## Three misconceptions worth catching

**"A Q-value is a success percentage."** Not generally. It estimates discounted reward, and its scale depends on the reward design and gamma. The first learned value of 0.1 is a partial update toward a target, not a measured 10 percent success rate.

**"A zero cell means the action is bad."** It might mean the action has not been tried, or that useful downstream reward has not propagated yet. The table alone does not report visit counts. A greedy arrow can conceal this uncertainty.

**"A successful replay means the whole table converged."** It shows that a particular policy worked on that attempt. It says little about unvisited states, alternative actions, or a different environment. Repeating deterministic evaluation with the same seed and map is not testing independent maps.

Finite tabular Q-learning has convergence results, but they come with assumptions. For the usual discounted finite Markov setting, these include bounded rewards, repeated coverage of the relevant state-action pairs, and suitable learning rates. Along each pair's updates, a standard condition is that the learning rates sum to infinity while their squares sum to a finite value.

A fixed-alpha recipe, such as alpha 0.1, does not satisfy that decreasing-rate condition. It can be useful in practice, but running it for a finite episode budget does not prove that every Q entry has converged. A careful report separates observed policy performance, coverage, and theoretical guarantees.

## Connecting the lesson to RL-from-zero: FrozenLake 8x8

The browser figures isolate the arithmetic. The repository also provides a real Gymnasium `FrozenLake-v1` recipe and a saved greedy-policy demonstration. Its [pinned configuration](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/27ea78dc267363afec2d447f1ba0278bfccdf89e/Qlearning/configs/frozenlake.yaml) includes:

<p class="rlql-code-caption"><strong>Native recipe settings.</strong> Selected unchanged fields from <code>frozenlake.yaml</code>, not a complete config.</p>

```yaml
env_id: FrozenLake-v1
env_kwargs:
  is_slippery: false
  map_name: "8x8"
alpha: 0.1
gamma: 0.99
max_steps_per_episode: 200
total_episodes: 5000
```

This means 64 states and four actions, with gamma **0.99** and cap **200**, versus the browser's 0.95 and 60. Training uses seed 42 and step-based epsilon decay from 1 to 0.05 at rate 0.001. The Q-table learns on CPU; PyTorch serves checkpoint serialization, not a neural network.

{% include rl/qlearning-native.html %}

**Native demonstration.** Gymnasium renders the repository's committed GIF, separate from the browser figures' sampled 4 by 4 experience. Its three showcase repeats follow the same 16-move saved-policy route. The static poster preserves the environment view without animation.

The checkpoint was selected at training episode 1011 using a ten-episode window. A fresh CPU evaluation, **without new training**, reached the goal in **200 of 200 unfiltered episodes**, each taking 16 moves, with the Q-table unchanged. All used the **same fixed map and start**: repeatability, not independent-map or slippery-dynamics evidence. Neither shortest-path optimality nor convergence of every entry is established.

### Run the repository recipe

Use a separate working copy to preserve the supplied checkpoint. From its repository root, the [README](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/27ea78dc267363afec2d447f1ba0278bfccdf89e/Qlearning/README.md) setup and training pattern is:

<p class="rlql-code-caption"><strong>Fresh environment and training.</strong> These are runnable shell commands, unlike the partial Python excerpts. Offline W&amp;B keeps metrics locally without uploading.</p>

```bash
uv venv .venv-qlearning-article
source .venv-qlearning-article/bin/activate
uv sync --active

WANDB_MODE=offline OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  uv run --active python -m Qlearning.main train \
  --config Qlearning/configs/frozenlake.yaml
```

Training writes new checkpoints; it is not required to replay the supplied saved policy. With a trusted checkpoint available at the configured path, evaluate every requested episode and export a separate showcase:

<p class="rlql-code-caption"><strong>Evaluation and headless GIF export.</strong> Outputs go to a separate review directory; the GIF helper selects showcase episodes and is not an evaluation statistic.</p>

```bash
uv run --active python -m Qlearning.utils.evaluate \
  --config Qlearning/configs/frozenlake.yaml --episodes 100 --seed 10000 \
  --out qlearning-review/evaluation.json

SDL_VIDEODRIVER=dummy uv run --active python -m Qlearning.utils.make_gif \
  --config Qlearning/configs/frozenlake.yaml \
  --out qlearning-review/frozenlake-8x8.gif
```

These commands do not promise identical training outcomes or GIF bytes. The [evaluator](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/27ea78dc267363afec2d447f1ba0278bfccdf89e/Qlearning/utils/evaluate.py) records every episode; the [GIF helper](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/27ea78dc267363afec2d447f1ba0278bfccdf89e/Qlearning/utils/make_gif.py) selects a showcase. Inspect their outputs separately.

## Next: keep the idea, replace the table

A table is wonderfully inspectable, but it needs an entry for every state-action pair. That becomes impractical when states are images or large combinations of features. It also does not generalize a correction to similar, separately indexed states.

Deep Q-learning predicts action-values with a neural network, keeping the reward, best-continuation estimate, and TD gap. But shared-parameter updates affect many states, and bootstrapped targets can move as the network learns. Replay buffers and target networks help manage these difficulties; tabular convergence arguments do not simply carry over.

Before taking that next step, keep one mental picture: an experience arrives, the agent builds a target, and a prediction moves toward it. In this article, you can point to the exact cell.

## References and further reading

- Watkins and Dayan, **Q-learning** (1992), *Machine Learning*, 8, 279-292. The original convergence paper: [doi:10.1007/BF00992698](https://doi.org/10.1007/BF00992698).
- Sutton and Barto, **Reinforcement Learning: An Introduction**, second edition (2018). The [authors' canonical book page](http://incompleteideas.net/book/the-book-2nd.html) provides the text; Chapter 6 develops temporal-difference control, including SARSA and Q-learning.
- **RL-from-zero**, [the agent source used here, pinned to a specific revision](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/27ea78dc267363afec2d447f1ba0278bfccdf89e/Qlearning/ql/agent.py). Read `act` beside `update` to distinguish how experience is collected from how its target is constructed.
- **Gymnasium**, [FrozenLake environment documentation](https://gymnasium.farama.org/environments/toy_text/frozen_lake/), for map symbols, actions, rewards, and slipperiness.
