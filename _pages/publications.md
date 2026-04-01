---
layout: archive
title: "Publications and Conferences"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% assign publication_pages = site.pages | where: "publication", true | sort: "date" %}
{% for post in publication_pages reversed %}
  {% include archive-single.html %}
{% endfor %}

<!--
<sup>*</sup> Equal authorship
-->