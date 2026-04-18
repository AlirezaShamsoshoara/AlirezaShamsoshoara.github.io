---
layout: archive
title: "AI Daily Paper Summary"
permalink: /blog/ai-papers/
author_profile: true
---

Daily summaries of trending AI and ML research papers, ranked by cross-platform community engagement. Updated every morning at 10 AM PT.

{% include base_path %}

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
{% assign current_year = "" %}
{% assign current_month = "" %}
{% assign found = false %}
{% for post in sorted_posts %}
  {% if post.categories contains 'ai-paper-summary' %}
    {% assign found = true %}
    {% assign post_year = post.date | date: "%Y" %}
    {% assign post_month = post.date | date: "%B %Y" %}
    {% if post_year != current_year %}
      {% assign current_year = post_year %}
      {% assign current_month = "" %}
<h2 class="archive__subtitle">{{ post_year }}</h2>
    {% endif %}
    {% if post_month != current_month %}
      {% assign current_month = post_month %}
<h3 class="archive__subtitle" style="margin-top: 0.5em; font-size: 1em; color: #6c757d;">{{ post_month }}</h3>
    {% endif %}
    {% include archive-single-minimal.html %}
  {% endif %}
{% endfor %}

{% unless found %}
<p><em>No paper summaries yet. Stay tuned!</em></p>
{% endunless %}
