---
title: "Physika"
layout: topic-page-uncolored
permalink: /physika/
author_profile: true
toc: true
toc_label: "Contents"
toc_icon: "list"
toc_sticky: true
excerpt: "Introductory physics notes — structure, demos, and math."
---

{% include sk/head/math_head.html %}
{% include sk/head/plotly_head.html %}
{% include sk/head/pyodide_head.html %}
<div class="learning-quarto" markdown="1">

This page is meant to be a comprehensive consolidation of the physics I have learnt and have been learning. It will cover areas of mechanics, quantum mechanics, optics, photonics, electromagnetics, field theory, relativity, and gravity as well as learnings from other disciplines depending on the relevance. We will try to blur these disciplinary boundaries here, and embrace a more open approach in a simple, cohesive, manner starting from basic fundamentals. It is physically impossible to cover every topic in the realm of science of course, but the goal is to serve as a personal repository as well as to cover enough that one can venture into more depth once these fundamentals are understood. I will include references where applicable and write code, simulations, and plots for easy elucidation and my own learning. Thank you for your patience, let's begin! :)

## 1. Atomic beginnings
---
{% comment %}
  Subsections: edit Markdown under _pages/physika/_fragments/atomic/ (one file per subsection, leading ### heading).
  To add a subsection: create a new .md file, then add an include_relative line below in the order you want.
{% endcomment %}
{% include_relative physika/_fragments/atomic/01-bohr-model.md %}
{% include_relative physika/_fragments/atomic/02-hydrogen.md %}
{% include_relative physika/_fragments/atomic/03-damped-oscillator.md %}
{% include_relative physika/_fragments/atomic/04-hydrogen-demos.md %}

<script>
  window.__PHYSICS_PY_URLS__ = [
    "{{ '/assets/physika/atomic/oscillator_slider.py' | relative_url }}",
    "{{ '/assets/physika/atomic/hydrogen.py' | relative_url }}",
    "{{ '/assets/physika/atomic/bohr_model.py' | relative_url }}",
  ];
</script>
<script src="{{ '/assets/js/learning-physics.js' | relative_url }}"></script>
</div>
