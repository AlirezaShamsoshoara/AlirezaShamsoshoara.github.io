---
layout: archive
title: "Interesting Projects"
permalink: /blog/projects/
author_profile: true
---

Posts about open-source projects I'm working on, sharing outcomes, results, and lessons learned with the community.

{% include base_path %}

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
{% assign found = false %}
{% for post in sorted_posts %}
  {% if post.categories contains 'interesting-projects' %}
    {% assign found = true %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

{% unless found %}
<p><em>No project posts yet. Stay tuned!</em></p>
{% endunless %}
