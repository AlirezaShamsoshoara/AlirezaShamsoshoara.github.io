---
layout: archive
title: "RL From Zero"
permalink: /blog/rl-from-zero/
author_profile: true
excerpt: "An overview of the RL From Zero series: reinforcement learning algorithms built from scratch and explained one idea at a time."
---

{% include base_path %}

<figure class="rlfz-announcement" style="margin:0 0 1.5em;">
  <video muted loop playsinline preload="auto" width="1920" height="1080" poster="{{ '/assets/media/rl/rl-from-zero/rl-from-zero-announcement.png' | relative_url }}" aria-label="A trained A3C agent landing in LunarLander, then the camera pulls back to show all 13 RL From Zero algorithms as tiles, each a trained agent in its environment." style="display:block;box-sizing:border-box;width:100%;height:auto;border:1px solid #e2e6eb;border-radius:3px;background:#fff;">
    <source src="{{ '/assets/media/rl/rl-from-zero/rl-from-zero-announcement.mp4' | relative_url }}" type="video/mp4">
    <img src="{{ '/assets/media/rl/rl-from-zero/rl-from-zero-announcement.gif' | relative_url }}" alt="All 13 RL From Zero algorithms as tiles, each a trained agent in its environment.">
  </video>
  <figcaption style="font-size:.8em;color:#56616e;margin-top:.5em;">Every tile is a trained agent from the RL-from-zero repository. The series starts with Q-learning, outlined in blue. <button type="button" data-rlfz-toggle hidden style="margin-left:.4em;padding:.15em .6em;font:inherit;color:#33475c;background:#fff;border:1px solid #d5dbe2;border-radius:3px;cursor:pointer;">Pause animation</button></figcaption>
</figure>
<script>
(function () {
  var video = document.querySelector('.rlfz-announcement video');
  var button = document.querySelector('[data-rlfz-toggle]');
  if (!video || !button) return;
  var reduce = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : null;
  function label() { button.textContent = video.paused ? 'Play animation' : 'Pause animation'; }
  function play() { video.muted = true; var started = video.play(); if (started && started.catch) started.catch(label); }
  video.addEventListener('play', label);
  video.addEventListener('pause', label);
  button.addEventListener('click', function () { if (video.paused) play(); else video.pause(); label(); });
  if (reduce && reduce.addEventListener) reduce.addEventListener('change', function () { if (reduce.matches) video.pause(); });
  button.hidden = false;
  if (!(reduce && reduce.matches)) play();
  label();
})();
</script>

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
