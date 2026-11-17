---
layout: archive
title: "RL From Zero"
permalink: /blog/rl-from-zero/
author_profile: true
excerpt: "An overview of the RL From Zero series: reinforcement learning algorithms built from scratch and explained one idea at a time."
---

{% include base_path %}

RL From Zero is a series about reinforcement learning algorithms, built from scratch and explained one idea at a time. Each post takes one algorithm from my open-source [RL-from-zero repository](https://github.com/AlirezaShamsoshoara/RL-from-zero) and shows how it actually learns, from its first update to a trained agent.

In the repository, each algorithm lives in its own self-contained package with a shared command-line interface, YAML-driven configuration, and optional experiment tracking with Weights & Biases. That means every post can point to real code you can run, not pseudocode.

## What each post includes

- **The core idea first**, in plain language, before any equation.
- **Interactive figures and animations** that show the algorithm learning, one step at a time.
- **The math, worked through** with real numbers from a recorded run.
- **The matching code** from the repository, and the commands to train and evaluate it yourself.
- **The real environment**, with the trained agent from the repository and a clear note on what the results do and do not show.

## Where the series goes

The repository spans tabular methods, deep value-based learning, policy gradients, actor-critic methods, offline RL, and multi-agent RL. The series starts at the simplest end, a table of Q-values, and builds toward the methods that replace that table with neural networks.

## Posts in this series

{% assign series_posts = site.posts | where: "series", "rl-from-zero" | sort: "series_part" %}
{% for post in series_posts %}
  {% include archive-single.html %}
{% endfor %}

[Browse all Interesting Blogs &rarr;](/blog/projects/)
