---
layout: archive
title: "Interesting Blogs"
permalink: /blog/projects/
author_profile: true
---

Posts about open-source projects I'm working on, sharing outcomes, results, and lessons learned with the community. Posts are grouped into series, and each series has an overview page that lists its posts in reading order.

{% include base_path %}

{% for series in site.data.blog_series %}
{% assign series_posts = site.posts | where: "series", series.id | sort: "series_part" %}
<h2 class="archive__subtitle"><a href="{{ base_path }}{{ series.url }}">{{ series.title }}</a></h2>
<p>{{ series.summary }} <a href="{{ base_path }}{{ series.url }}">Series overview &rarr;</a></p>
{% for post in series_posts %}
  {% include archive-single.html %}
{% endfor %}
{% if series_posts.size == 0 %}
<p><em>First post coming soon.</em></p>
{% endif %}
{% endfor %}

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
{% assign standalone_count = 0 %}
{% for post in sorted_posts %}{% if post.categories contains 'interesting-blogs' %}{% unless post.series %}{% assign standalone_count = standalone_count | plus: 1 %}{% endunless %}{% endif %}{% endfor %}
{% if standalone_count > 0 %}
<h2 class="archive__subtitle">Other posts</h2>
{% for post in sorted_posts %}
  {% if post.categories contains 'interesting-blogs' %}{% unless post.series %}
  {% include archive-single.html %}
  {% endunless %}{% endif %}
{% endfor %}
{% endif %}
