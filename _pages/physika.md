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

This page is meant to be a comprehensive consolidation of all the physics I have learnt and been learning. Physics is a multi-domain enterprise so this will cover areas of mechanics, quantum mechanics, optics, photonics, electromagnetics, field theory, relativity, and gravity. I will try to make it as simple and comprehensive as possible with a cohesive flow, starting from basic fundamentals. It is physically not possible to cover every topic in the realm of physics of course, but the goal is to serve as my personal repository as well as cover enough that one can venture to learn more in depth once these fundamentals are understood. I will include references where applicable and be writing code, simulations, and plots for easy elucidation and my own learning. Thanks for your patience, let's begin! :)

## 1. Atomic beginnings
---
### 1.1 Hydrogen

The hydrogen atom: electron $$\color{blue}{-e}$$, proton $$\color{blue}{+e}$$, Coulomb potential.

{% include sk/components/eqs.html
  id="eq-1.1"
  eq="\color{#000080}E_n = -\tfrac{13.6\text{ eV}}{n^2}"
  fontsize="1.00em"
  num="1.1"
  leader="....."
%}

{% include sk/components/eqs.html
  id="eq-1.2"
  eq="\color{#000080}V(r) = -\tfrac{e^2}{4\pi\epsilon_0 r}"
  fontsize="1.00em"
  num="1.2"
  leader="....."
%}

{% include sk/components/eqs.html
  id="eq-1.3"
  eq="\color{#000080}E_n = -\tfrac{13.6\text{ eV}}{n^2}"
  fontsize="1.00em"
  num="1.3"
  leader="....."
%}

Energy scales as $$1/n^2$$ ([eq. 1.1](#eq-1.1)).

<details class="topic-code-fold">
  <summary>Code</summary>
  {% highlight python %}
  import math
  OSCILLATOR_X_RANGE = (0.0, 60.0)
  OSCILLATOR_Y_RANGE = (-1.25, 1.25)
  OSCILLATOR_X_AXIS_TITLE = "Time (dimensionless), t"
  OSCILLATOR_Y_AXIS_TITLE = "Displacement (dimensionless), x"
  def run_calc_slider(gamma, t_max=30.0):
    n = 300
    dt = t_max / max(n - 1, 1)
    t = [i * dt for i in range(n)]
    if gamma < 1.0:
        wd = math.sqrt(1.0 - gamma**2)
        y = [math.exp(-gamma * ti) * math.cos(wd * ti) for ti in t]
    elif abs(gamma - 1.0) < 1e-9:
        y = [math.exp(-ti) * (1.0 + ti) for ti in t]
    else:
        s = math.sqrt(gamma**2 - 1.0)
        y = [math.exp(-gamma * ti) * math.cosh(s * ti) for ti in t]
    ep = [math.exp(-gamma * ti) for ti in t]
    en = [-math.exp(-gamma * ti) for ti in t]
    return t, y, ep, en, OSCILLATOR_X_RANGE, OSCILLATOR_Y_RANGE, OSCILLATOR_X_AXIS_TITLE, OSCILLATOR_Y_AXIS_TITLE
  {% endhighlight %}
</details>

{% include sk/components/eqs.html
  id="eq-1.4"
  eq="\color{#000080}\psi_{n\ell m} = R_{n\ell}(r)\,Y_\ell^m(\theta,\phi)"
  fontsize="1.00em"
  num="1.4"
  leader="....."
%}

{% include sk/components/eqs.html
  id="eq-1.5"
  eq="\color{#000080}\left[ -\tfrac{\hbar^2}{2m_e}\nabla^2 + V(r) \right] \psi = E\psi"
  fontsize="1.00em"
  num="1.5"
  leader="....."
%}

#### Damped oscillator

<div class="demo-section physics-demos">
<div class="physics-plot-aligned">
<div class="physics-plot-column">
<div class="physics-plot-formula">
\[
x(t)=e^{-\gamma t}(A\cos\omega_d t+B\sin\omega_d t),\quad \omega_d=\sqrt{1-\gamma^2}\ (\gamma&lt;1)
\]
</div>
<div class="physics-plot-frame"><div id="slider-pyplot" class="physics-plot-inner" style="height:280px;"></div></div>
<div class="physics-slider-stack">
<div class="physics-slider-row">
<div class="physics-slider-caption">\(t_{\mathrm{end}}\), value = <span id="slider-tmaxVal" class="physics-val">30.0</span></div>
<input id="slider-tmaxInput" class="physics-hslider" type="range" min="5" max="60" step="0.5" value="30" oninput="document.getElementById('slider-tmaxVal').textContent=parseFloat(this.value).toFixed(1); sliderDebouncePlot();">
</div>
<div class="physics-slider-row">
<div class="physics-slider-caption">γ, value = <span id="slider-gammaVal" class="physics-val">0.10</span></div>
<input id="slider-gammaInput" class="physics-hslider" type="range" min="0.01" max="1.99" step="0.01" value="0.10" oninput="document.getElementById('slider-gammaVal').textContent=parseFloat(this.value).toFixed(2); sliderDebouncePlot();">
</div>
</div>
</div>
</div>
<div id="slider-pyout" class="physics-status">Loading…</div>
<div id="slider-debug" class="physics-debug"></div>
</div>

#### Hydrogen demos

<div class="demo-section physics-demos">
<div class="physics-panel">
<div class="physics-plot-aligned">
<div class="physics-plot-column">
<div class="physics-plot-formula">
\[
\text{Radial:}\quad R_{n\ell}(r),\quad r^2|R_{n\ell}(r)|^2
\]
</div>
<div class="physics-plot-frame"><div id="wf-pyplot" class="physics-plot-inner" style="height:300px;"></div></div>
<div class="physics-slider-stack">
<div class="physics-slider-row">
<div class="physics-slider-caption">\(n\), value = <span id="wf-nVal-rad" class="physics-val">1</span></div>
<input id="wf-nInput-rad" class="physics-hslider" type="range" min="1" max="4" step="1" value="1" oninput="wfOnN('rad',this.value)">
</div>
<div class="physics-slider-row">
<div class="physics-slider-caption">ℓ, value = <span id="wf-lVal-rad" class="physics-val">0</span></div>
<input id="wf-lInput-rad" class="physics-hslider" type="range" min="0" max="3" step="1" value="0" oninput="wfOnL('rad',this.value)">
</div>
</div>
</div>
<div class="physics-controls-beside">
<div class="physics-wf-radios">
<label><input type="radio" name="wf-plottype" value="psi" checked onchange="wfDebouncePlot()"> ψ(r)</label>
<label><input type="radio" name="wf-plottype" value="prob" onchange="wfDebouncePlot()"> r²|ψ|²</label>
</div>
</div>
</div>
</div>
<div class="physics-panel">
<div class="physics-plot-aligned">
<div class="physics-plot-column">
<div class="physics-plot-formula">
\[
\text{Orbital slice }(xz)\text{:}\quad |\psi_{n\ell}(x,z)|^2
\]
</div>
<div class="physics-plot-frame"><div id="wf-orbital" class="physics-plot-inner" style="height:300px;"></div></div>
<div class="physics-slider-stack">
<div class="physics-slider-row">
<div class="physics-slider-caption">\(n\), value = <span id="wf-nVal-orb" class="physics-val">1</span></div>
<input id="wf-nInput-orb" class="physics-hslider" type="range" min="1" max="4" step="1" value="1" oninput="wfOnN('orb',this.value)">
</div>
<div class="physics-slider-row">
<div class="physics-slider-caption">ℓ, value = <span id="wf-lVal-orb" class="physics-val">0</span></div>
<input id="wf-lInput-orb" class="physics-hslider" type="range" min="0" max="3" step="1" value="0" oninput="wfOnL('orb',this.value)">
</div>
</div>
</div>
</div>
</div>
<div id="wf-pyout" class="physics-status physics-status--spaced">Loading…</div>
<div id="wf-debug" class="physics-debug"></div>
</div>

<script>
  window.__PHYSICS_PY_URLS__ = [
    "{{ '/assets/py/oscillator_slider.py' | relative_url }}",
    "{{ '/assets/py/hydrogen.py' | relative_url }}"
  ];
</script>
<script src="{{ '/assets/js/learning-physics.js' | relative_url }}"></script>
</div>