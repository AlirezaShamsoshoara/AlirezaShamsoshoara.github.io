---
title: "DQN: when a table is not enough"
date: 2026-11-23
layout: rl-article
hero_image: /assets/media/rl/dqn/dqn-hero.svg
hero_alt: "One recorded DQN update: a minibatch drawn from replay across the MountainCar position and velocity map, a target built from the frozen target network, and one gradient step that changes the value of every state on the map."
permalink: /blog/rl-from-zero/dqn/
categories: [interesting-blogs, reinforcement-learning]
series: rl-from-zero
series_part: 2
tags: [rl-from-zero, dqn, interactive]
excerpt: "Replace the table with a network, then follow one real gradient step through replay, a frozen target, and a value map that changes everywhere at once."
read_time: true
stylesheets:
  - /assets/css/rl/dqn.css
scripts:
  - /assets/js/rl/article-common.mjs
  - /assets/js/rl/dqn-article.mjs
series_label: "02 · DQN"
lede: "MountainCar has no cells to fill. Follow one recorded gradient step through a Q-network, and the two ideas that keep it from chasing its own tail."
read_time_text: "Interactive explainer · 20-minute read"
jump_links:
  - href: "#dqn-update-title"
    label: "Step through an update ↓"
  - href: "#dqn-explore-title"
    label: "Try the exploration lab ↓"
  - href: "#dqn-training-title"
    label: "Watch training ↓"
  - href: "#follow-the-equations-into-the-code"
    label: "Read the code ↓"
footer_part_label: "Part 02 of RL From Zero"
previous_part:
  url: /blog/rl-from-zero/q-learning/
  title: "Q-learning: watch a table learn"
next_teaser: "Next: what if the agent learned how to act directly, instead of scoring every action?"
---

[Part 1](/blog/rl-from-zero/q-learning/) ended with one picture to keep: an experience arrives, the agent builds a target, and a prediction moves toward it. In FrozenLake you could point to the exact cell that moved.

This part keeps that picture and removes the cell.

The task is MountainCar. The agent still learns action values, and its target is still a reward plus the best value it expects next. But the values now come out of a small neural network, and one update moves the whole network. That single change brings two new problems, and DQN is mostly the pair of fixes for them.

Figures 1, 2 and 4 replay the actual training run that produced the trained agent at the end of this post: the same minibatches, targets and saved checkpoints, not a simulation of them. Figure 3 runs random exploration on the same physics, live in your browser.

## A state you cannot put in a table

A car sits in a valley between two hills. The flag is on top of the right hill, and the engine is too weak to drive straight up. The only way out is to rock back and forth: go up the left slope, roll down, and use that speed to climb the right one.

The car's state is two numbers, its **position** and its **velocity**. Each step, the agent chooses one of three actions: push left, no push, or push right. Every step costs a reward of −1, including the step that reaches the flag, so fewer steps means a better return. An episode ends when the car reaches the flag at position 0.5, or it is cut off after 200 steps.

<div class="rlql-map-matrix" role="img" aria-label="MountainCar's state, actions, reward and episode end.">
<pre class="rlql-map-grid"><code>state      position in [−1.2, 0.6], velocity in [−0.07, 0.07]
start      position in [−0.6, −0.4], velocity 0
actions    push left, no push, push right
reward     −1 every step
ends       flag reached (position ≥ 0.5), or 200 steps pass</code></pre>
</div>

In FrozenLake, the agent visited the same 16 squares again and again, and each had its own row in the table. Here, position and velocity are real numbers. The car almost never lands on exactly the same state twice, so a table indexed by state would see almost every entry once.

You could chop the map into a grid of cells and keep a table anyway. But then each cell learns alone. A correction near one state teaches its neighbors nothing, even though a car at position −0.501 and one at −0.500 are in nearly the same situation. What we want is a function that gives similar answers for similar states, and that improves everywhere a little when it is corrected anywhere.

## Replace the table with a function

DQN keeps the Q-learning target and swaps the table for a neural network. The network takes a state and returns three numbers, one value per action:

<p class="rl-equation"><code>Q(s, a; theta) ≈ expected return after action a in state s</code></p>

Here *theta* is the network's weights. The network in this run is small: the two inputs are first rescaled to the range −1 to 1, then pass through two hidden layers of 128 units each, then out to three values. That is 17,283 weights and biases in total, and **every one of them is shared by every state**.

The Q-learning target from Part 1 survives almost unchanged:

<p class="rl-equation"><code>target = r + gamma * (1 - terminated) * max<sub>a'</sub> Q(s', a'; theta)</code></p>

What changes is how a prediction moves toward it. A table could simply nudge one cell. A network can only adjust its weights, so the update becomes a small step of gradient descent on the squared gap:

<p class="rl-equation"><code>loss(theta) = (target - Q(s, a; theta))<sup>2</sup></code></p>
<p class="rl-equation"><code>theta ← theta - learning rate * gradient of loss(theta)</code></p>

The target is treated as a fixed number: no gradient flows through it. In practice the run averages the loss over a minibatch of 64 transitions and uses the Adam optimizer, which scales the step for each weight.

Because every state shares the same weights, that step changes the predicted value of states the update never looked at. That is the point of using a network, since nearby states should learn together. It is also the source of the trouble, as the next figure shows.

Figure 1 shows a complete DQN update, including two parts explained right after it: a replay buffer that supplies the 64 transitions, and a frozen target network that is refreshed every 250 updates, a step called a *sync*.

{% include rl/dqn-update.html %}

## The math, with numbers from the run

Here is the first update in Figure 1, worked by hand. The network has never been trained, so its outputs are small numbers near zero. The tracked sample was stored late in the random warm-up, 3,606 steps before this update: the car was on the left slope at position −1.115, moving right with velocity 0.0145, and the stored action was **push left**.

DQN in this run uses the Double DQN target, which splits the look-ahead in two. The online network, the one being trained, chooses the next action. A second copy, the **target network** with weights *theta⁻*, scores it:

<p class="rl-equation"><code>a* = argmax<sub>a'</sub> Q(s', a'; theta)</code></p>
<p class="rl-equation"><code>target = r + gamma * (1 - terminated) * Q(s', a*; theta<sup>-</sup>)</code></p>

At the next state, the online network's three values are −0.1231 (left), −0.1478 (none) and −0.3092 (right), so it picks left. Before the first sync, the target network is an exact copy, so it scores left at −0.1231 too:

<p class="rl-equation"><code>target = −1 + 0.99 * (1 - 0) * (−0.1231) = −1.122</code></p>
<p class="rl-equation"><code>TD error = −1.122 - (−0.1229) = −0.999</code></p>

After one step of the Adam optimizer, Q(s, left) has moved from −0.1229 to −0.1424. That is about 2% of the way to the target. The update averages 64 samples, not one, and a learning rate of 0.00025 asks for a small step.

Look at the step's map in Figure 1. One update changed the value of every one of the 4,032 cells on the map, by up to 0.022. In Part 1, one update changed exactly one cell.

A goal transition is the one place the target does not look ahead. Update 32 contains one, a step that crossed the flag at position 0.501:

<p class="rl-equation"><code>target = −1 + 0.99 * (1 - 1) * (anything) = −1</code></p>

Every other target bootstraps from the network itself. Only goal transitions anchor the values to something real, which is why reaching the flag at all matters so much here.

What does a value mean in this task? Each step costs −1, so if the car is T steps from the flag, its discounted return is

<p class="rl-equation"><code>−(1 + 0.99 + 0.99<sup>2</sup> + ... + 0.99<sup>T−1</sup>) = −(1 − 0.99<sup>T</sup>) / 0.01</code></p>

A value near −63 means roughly 100 steps to go. A car that never reaches the flag approaches −100. Values above −1 are impossible for any state that is not already at the flag.

## Two problems a network brings

Part 1 warned that a network would bring two difficulties: updates that affect many states, and targets that move as the network learns. DQN answers each with one idea.

### Problem one: consecutive experience is nearly identical

Within an episode, each state is a tiny step from the last one. Training on experience in the order it arrives would keep pushing the shared weights toward whatever patch of the map the car is in right now, and let it forget the rest.

**Experience replay** stores every transition in a buffer, up to the last 100,000, and trains on a random minibatch of 64 of them every 4 steps. In Figure 1's Sample phase, the 64 transitions spread across the whole visited map, and in all five updates shown there, none of the 64 came from the episode the car was driving at the time. Replay also reuses data: over the whole run, each transition was sampled about 15 times on average.

### Problem two: the target moves with every step

The target is built from the network's own predictions. If the same weights produced both the prediction and its target, every update would also move the target, including for the very states just updated. Learning would chase its own tail.

The **target network** is a frozen copy of the online network that computes targets. It is copied from the online network every 250 updates, and between copies it does not change at all:

<p class="rl-equation"><code>every 250 updates: theta<sup>-</sup> ← theta</code></p>

{% include rl/dqn-target.html %}

Figure 2 shows what that does early in training. In the first 250 updates, the online network learns to predict the frozen targets, which drift to −1.27 by update 250: one step of cost plus a small guess. Then the copy lands. The targets jump to −2.23, because they now bootstrap from a network that has learned that one step costs about 1. The loss jumps from 0.0084 to 0.94, and the chase starts again. Each sync lets the values look roughly one step further ahead. By about update 29,000, near step 136,000 and after about 115 syncs, the average target has fallen past −60. Later it rises again, to about −34 by the end of training, as the car reaches the flag in fewer steps.

### Why Double DQN?

Plain DQN lets the target network both choose and score the next action:

<p class="rl-equation"><code>target = r + gamma * (1 - terminated) * max<sub>a'</sub> Q(s', a'; theta<sup>-</sup>)</code></p>

Taking a max over noisy estimates tends to pick the ones that happen to be too high, so this target is biased upward. Double DQN chooses with the online network and scores with the target network, as in the worked example above. Because the target network lags behind, the two networks' errors only partly overlap (right after a sync they are identical), so the upward bias usually shrinks. It does not disappear, and nothing here measures how much it shrank in this run.

## Follow the equations into the code

The excerpts below come from the [RL-from-zero DQN source, pinned to one revision](https://github.com/AlirezaShamsoshoara/RL-from-zero/tree/f1563be804410939adf0b45ff93fd6f09f589cc3/deepQN). They are excerpts, not standalone programs.

<p class="rlql-code-caption"><strong>Collect, store, learn.</strong> Adapted from <code>train</code> in <code>deepQN/main.py</code>; logging, episode bookkeeping, checkpoints and the final-observation fallback that sets <code>transition_next_obs</code> are omitted. Only <code>terminated</code>, never <code>truncated</code>, becomes the done mask.</p>

```python
action, exploratory = explorer.act(agent, obs, epsilon)
next_obs, reward, terminated, truncated, info = env.step(action)
buffer.add(obs, action, float(reward), transition_next_obs, float(terminated))
obs = next_obs
if (
    step >= cfg.learning_starts
    and step % cfg.train_freq == 0
    and buffer.can_sample(cfg.batch_size)
):
    update_metrics.append(asdict(agent.update(buffer.sample(cfg.batch_size))))
```

Learning waits for `learning_starts`, 20,000 steps of exploration, then runs one update every `train_freq` steps, which is 4 here. A step cut off by the 200-step limit keeps a done mask of 0, so its target still looks ahead: the task did not end, the clock did.

<p class="rlql-code-caption"><strong>Uniform replay.</strong> Excerpt from <code>ReplayBuffer.sample</code> in <code>deepQN/dqn/replay_buffer.py</code>. Every stored transition is equally likely, whatever its age.</p>

```python
indices = np.random.randint(0, self.size, size=batch_size)
return {
    "obs": torch.as_tensor(self.obs[indices], device=self.device),
    "actions": torch.as_tensor(self.actions[indices], device=self.device),
    "rewards": torch.as_tensor(self.rewards[indices], device=self.device),
    "next_obs": torch.as_tensor(self.next_obs[indices], device=self.device),
    "dones": torch.as_tensor(self.dones[indices], device=self.device),
}
```

<p class="rlql-code-caption"><strong>One update.</strong> Adapted from <code>DQNAgent.update</code> in <code>deepQN/dqn/agent.py</code>: the batch checks, the non-finite-loss check and the returned statistics are omitted. The target network only scores; the optimizer never trains it.</p>

```python
obs, next_obs = self._encode(obs), self._encode(next_obs)
actions = actions_raw.long()
action_values = self.q_network(obs).gather(1, actions.unsqueeze(1)).squeeze(1)
with torch.no_grad():
    if self.double_dqn:
        next_actions = self.q_network(next_obs).argmax(dim=1, keepdim=True)
        next_target_values = (
            self.target_q_network(next_obs).gather(1, next_actions).squeeze(1)
        )
    else:
        next_target_values = self.target_q_network(next_obs).max(dim=1).values
    targets = rewards + self.gamma * (1.0 - dones) * next_target_values
loss = F.mse_loss(action_values, targets)
self.optimizer.zero_grad()
loss.backward()
if self.max_grad_norm > 0:
    nn.utils.clip_grad_norm_(self.q_network.parameters(), self.max_grad_norm)
self.optimizer.step()
self.train_steps += 1
if self.train_steps % self.target_update_interval == 0:
    self.update_target_network()
```

Line by line, this is the math above. `gather` picks Q(s, a) for the action actually taken. Inside `no_grad`, the online network chooses `next_actions` and the target network scores them, so no gradient flows into the target. The loss is the mean squared error over the minibatch. Gradient clipping rescales the gradient whenever its norm exceeds 10 (`max_grad_norm`), and every 250th update copies the weights into the target network.

## The real difficulty: finding the flag at all

Everything so far assumes that some transitions reach the flag. Until one does, every target is "−1 plus a guess," and the network has nothing to learn except that time passes.

Reaching the flag by accident is hard. Random actions that change every step mostly cancel out, and the car just jiggles near the bottom of the valley. What works is commitment: push one way long enough to build a swing, then the other.

{% include rl/dqn-explore.html %}

The repository's own probe found the same pattern. In 500 fully random episodes per setting, independent actions reached the flag 0 times. Holding each random action for 20 to 60 steps reached it 64 times, 30 to 70 steps 43 times, and 50 to 80 steps only 8 times. Figure 3 uses its own random numbers, so its counts differ slightly, but the shape is the same.

So the training recipe explores with **held random pulses**. With probability *p*, the agent starts a random action and keeps it for 20 to 60 steps; otherwise it takes the network's greedy action. During the first 20,000 steps, every action is random, and in those 104 warm-up episodes the car reached the flag 20 times, first in episode 7. After warm-up, epsilon falls from 1 to 0.02 over the next 100,000 steps.

Because one pulse lasts many steps, *p* cannot simply equal epsilon. If pulses last *H* steps on average, the code starts them with probability

<p class="rl-equation"><code>p = epsilon / (H * (1 - epsilon) + epsilon)</code></p>

so that epsilon is roughly the fraction of random steps (exactly only over long stretches at a fixed epsilon, since pulses are cut off when an episode ends). With epsilon at 0.5 and an average hold of 40 steps, a pulse starts on only about 1 in 41 of the steps where no pulse is running, yet about half of all steps come from pulses. This changes how data is collected, not the reward or the physics. When the trained agent is tested, it never holds an action; it acts greedily every step.

## Watch training, checkpoint by checkpoint

The run saved a checkpoint every 5,000 steps. Figure 4 loads one every 10,000 steps, plus the first one and the checkpoint the repository selected as best, and lets the car drive with each one's greedy choices.

{% include rl/dqn-training.html %}

Three things stand out.

First, the values take shape long before the policy works. Once updates begin at step 20,000, the maps soon start to rank states, but the greedy car reaches the flag from at most 1 of the 11 test starts until step 90,000, where it suddenly succeeds from all of them.

Second, learning is not monotonic. At step 110,000, the same network that had succeeded from every start reaches the flag from only 3 of 11. It recovers by step 140,000 and still dips at times later on. One likely cause is that shared weights let an improvement in one region damage another, while the targets keep moving with every sync. This is why the repository keeps checkpoints and selects one instead of trusting the last.

Third, look at the gray areas. The network outputs a value for every state, including fast-moving states near the walls that the car never reached. Those values are extrapolation. At the selected checkpoint, 156 unvisited cells, and even 18 rarely visited ones, have values above −1, which is impossible for a state that has not yet reached the flag. Where data is missing or thin, a network's confident-looking number is a guess.

The first time the car reached the flag with no random step at all was episode 384, at step 74,124. Figure 1's fourth update is the one that ran right after it, and it shows another side of replay: that new success is one transition among 74,124, and the update samples from all of them.

## The real repository run

Figures 1, 2 and 4, the title image and the Figure 5 GIF all come from one run of the repository's recommended recipe, unchanged; Figure 3 runs in your browser. Before using that run, I re-ran that recipe with the locked dependencies on one CPU thread and compared all 61 saved checkpoints tensor by tensor. All 61 matched exactly, so the minibatches and targets above are the ones that trained the agent below. A different CPU or thread count can round floating-point sums differently and drift.

<p class="rlql-code-caption"><strong>Recipe settings.</strong> Selected unchanged fields from <code>deepQN/configs/mountaincar_exploration.yaml</code>, not a complete config.</p>

```yaml
env_id: MountainCar-v0
seed: 42
hidden_sizes: [128, 128]
normalize_observations: true
total_steps: 300000
learning_starts: 20000
train_freq: 4
batch_size: 64
buffer_size: 100000
gamma: 0.99
lr: 0.00025
target_update_interval: 250
max_grad_norm: 10.0
double_dqn: true
epsilon_start: 1.0
epsilon_end: 0.02
epsilon_decay_steps: 100000
exploration_hold_min: 20
exploration_hold_max: 60
```

{% include rl/dqn-native.html %}

The selected checkpoint was saved at step 251,392, where the average return of the previous 20 training episodes peaked at −96.05. The repository then evaluated it greedily on 200 new starts, seeds 40000 to 40099 and 50000 to 50099, with no action holds and no filtering. It reached the flag in all 200, with a mean return of −100.46 and a standard deviation of 9.21, above the environment's −110 threshold for solving the task. Re-running the repository's evaluator reproduced both summaries exactly.

Those test starts vary the car's position, not the physics. One training seed reached this result, and the same seed's earlier recipes did not: the stock 200,000-step recipe and the first rescaled recipe both reached the flag 0 times in 100 greedy tests on each seed range tested.

<p class="rlql-code-caption"><strong>Fresh environment, training and evaluation.</strong> Runnable shell commands. Offline W&amp;B keeps metrics locally without uploading.</p>

```bash
git clone https://github.com/AlirezaShamsoshoara/RL-from-zero.git
cd RL-from-zero
git checkout f1563be804410939adf0b45ff93fd6f09f589cc3
uv venv .venv-dqn --python 3.12
source .venv-dqn/bin/activate
uv sync --active
WANDB_MODE=offline OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  uv run --active python -m deepQN.main train \
  --config deepQN/configs/mountaincar_exploration.yaml
```

<p class="rlql-code-caption"><strong>Greedy evaluation and the GIF.</strong> The evaluator reports every episode; the GIF helper keeps the best episodes for display and is not an evaluation statistic.</p>

```bash
uv run --active python -m deepQN.utils.evaluate \
  --config deepQN/configs/mountaincar_exploration.yaml \
  --episodes 100 --seed 40000 --out review/evaluation.json
SDL_VIDEODRIVER=dummy uv run --active python -m deepQN.utils.make_gif \
  --config deepQN/configs/mountaincar_exploration.yaml --out review/dqn_mountaincar.gif
```

## What these results do not show

**"A small loss means a good policy."** No. The loss measures how well the network matches its own bootstrapped targets. It was 0.0071 after 100 updates, while greedy checkpoints from that stage, at steps 20,000 and 30,000, reached the flag from none of the 11 test starts.

**"The value is the chance of success."** It is a discounted sum of −1 rewards, in the units of the equation above. A value of −63 means about 100 steps to go, not a 63% anything.

**"Matching values and returns means the network is calibrated."** The repository compares the network's starting value with the actual discounted return of each greedy test episode: −66.31 against −63.25 on one set of seeds. Close, but the network is about 3 points pessimistic, and agreement on test starts says nothing about states the agent never visits.

**"DQN is guaranteed to converge."** Tabular Q-learning has convergence results under conditions from Part 1. Combining function approximation, bootstrapping and off-policy data, the combination Sutton and Barto call the deadly triad, has no such guarantee in general. Replay and target networks often make it work in practice, though this repository's earlier recipes failed with both in place; they do not make it a theorem.

**"The recipe proves held exploration was the fix."** The repository's earlier recipes failed, and the successful one changed several settings at once: input scaling, learning rate, target cadence, training length, exploration, warm-up and checkpoint selection. It is also one training seed. The probe shows why holds help a random explorer; it does not isolate their effect on DQN.

## Next: learn how to act, not just what each action is worth

DQN acts by taking the argmax over its value estimates, and it explores by mixing in random pulses from outside. Everything it learns is about values; the policy is whatever the argmax says.

Part 3 changes what the network learns. A3C trains a policy that outputs action probabilities directly, so exploration comes from sampling that policy instead of from bolted-on randomness. A critic beside it judges how good each situation is, and several workers learn in parallel on their own copies of the environment instead of replaying old experience. Keep the picture from this post: a prediction, a target, and one step toward it. The critic will look familiar.

## References and further reading

- Mnih and colleagues, **Playing Atari with Deep Reinforcement Learning** (2013), the first DQN paper: [arXiv:1312.5602](https://arxiv.org/abs/1312.5602). The fuller version with target networks is **Human-level control through deep reinforcement learning**, *Nature* 518, 529-533 (2015): [doi:10.1038/nature14236](https://doi.org/10.1038/nature14236).
- van Hasselt, Guez and Silver, **Deep Reinforcement Learning with Double Q-learning** (2016): [arXiv:1509.06461](https://arxiv.org/abs/1509.06461).
- Lin, **Self-improving reactive agents based on reinforcement learning, planning and teaching** (1992), *Machine Learning* 8, 293-321, where experience replay comes from: [doi:10.1007/BF00992699](https://doi.org/10.1007/BF00992699).
- Sutton and Barto, **Reinforcement Learning: An Introduction**, second edition (2018), [the authors' book page](http://incompleteideas.net/book/the-book-2nd.html). Chapters 9 to 11 cover function approximation; Section 11.3 names the deadly triad.
- **RL-from-zero**, [the DQN agent source used here, pinned to one revision](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/f1563be804410939adf0b45ff93fd6f09f589cc3/deepQN/dqn/agent.py), with the [held-action explorer](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/f1563be804410939adf0b45ff93fd6f09f589cc3/deepQN/dqn/exploration.py) and the [training loop](https://github.com/AlirezaShamsoshoara/RL-from-zero/blob/f1563be804410939adf0b45ff93fd6f09f589cc3/deepQN/main.py).
- **Gymnasium**, [MountainCar environment documentation](https://gymnasium.farama.org/environments/classic_control/mountain_car/), for the physics, rewards and episode limits. The task comes from Andrew Moore's PhD thesis (1990).
