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

This page is meant to be a comprehensive consolidation of various scientific topics I have learnt and been learning, presented in a simple, cohesive manner. It will cover areas of mechanics, quantum mechanics, optics, photonics, electromagnetics, field theory, relativity, gravity, as well as details from other topics depending on the relevance. We will try to blur disciplinary boundaries here, integrate and correlate learnings as much as possible while embracing an open approach starting from basic fundamentals. 

It is physically impossible to cover every topic in the realm of science of course, but the goal is to serve as a personal repository as well as to introduce various topics sequentially, so that one can venture into more depth once the fundamentals are understood. I will include references where applicable and write code, simulations, and plots for easy elucidation and my own learning. Thank you for your patience, let's begin! :)

## 1. Atomic beginnings
---
{% comment %}
  Subsections: edit Markdown under _pages/physika/_fragments/atomic/ (one file per subsection, leading ### heading).
  To add a subsection: create a new .md file, then add an include_relative line below in the order you want.
{% endcomment %}
{% include_relative physika/_fragments/atomic/01-bohr-model.md %}
{% include_relative physika/_fragments/atomic/02-hydrogen.md %}

## 2. Bands and Orbitals
---
{% comment %}
  Subsections: edit Markdown under _pages/physika/_fragments/atomic/ (one file per subsection, leading ### heading).
  To add a subsection: create a new .md file, then add an include_relative line below in the order you want.
{% endcomment %}
{% include_relative physika/_fragments/simulators/01-damped-oscillator.md %}
{% include_relative physika/_fragments/simulators/02-hydrogen-demos.md %}

<script src="{{ '/assets/js/physika/physika-runtime.js' | relative_url }}"></script>
<script src="{{ '/assets/js/physika/demo-bohr.js' | relative_url }}"></script>
<script src="{{ '/assets/js/physika/demo-oscillator.js' | relative_url }}"></script>
<script src="{{ '/assets/js/physika/demo-hydrogen.js' | relative_url }}"></script>
</div>
