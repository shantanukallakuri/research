---
title: "Learning"
layout: topic-page-uncolored
permalink: /learning/
author_profile: false
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

## 1. Atomic beginnings
---
### 1.1 Hydrogen

The hydrogen atom: electron $$\color{blue}{-e}$$, proton $$\color{blue}{+e}$$, Coulomb potential.

{% include sk/components/eqs.html
  id="eq-1.1"
  eq="\color{blue}E_n = -\tfrac{13.6\text{ eV}}{n^2}"
  num="1.1"
  leader="....."
%}
{% include sk/components/eqs.html
  id="eq-1.2"
  eq="\color{blue}V(r) = -\tfrac{e^2}{4\pi\epsilon_0 r}"
  num="1.2"
  leader="....."
%}
{% include sk/components/eqs.html
  id="eq-1.3"
  eq="\color{blue}E_n = -\tfrac{13.6\text{ eV}}{n^2}"
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
  eq="\psi_{n\ell m} = R_{n\ell}(r)\,Y_\ell^m(\theta,\phi)"
  num="1.4"
  leader="....."
%}

{% include sk/components/eqs.html
  id="eq-1.5"
  eq="\left[ -\tfrac{\hbar^2}{2m_e}\nabla^2 + V(r) \right] \psi = E\psi"
  num="1.5"
  leader="....."
%}

**Note:** Sliders adjust **parameters** (\(\gamma\), \(t_{\mathrm{end}}\), \(n\), \(\ell\)). The **plots** graph **coordinates** (\(t,x\); \(r\); \(x,z\)) — so axis labels use \(t,x,r,\ldots\), not the slider symbols. Edit axis text/ranges in the `.py` files.

#### Damped oscillator

\(x(t)\) vs \(t\); sliders: \(\gamma\) (horizontal), \(t_{\mathrm{end}}\) (vertical). Fixed axes in `oscillator_slider.py`.

$$
x(t)=e^{-\gamma t}(A\cos\omega_d t+B\sin\omega_d t),\quad \omega_d=\sqrt{1-\gamma^2}\ (\gamma<1)
$$

<div class="demo-section physics-demos">
<label class="physics-slider-label">γ: <span id="slider-gammaVal" class="physics-val">0.10</span></label>
<input id="slider-gammaInput" class="physics-hslider" type="range" min="0.01" max="1.99" step="0.01" value="0.10" oninput="document.getElementById('slider-gammaVal').textContent=parseFloat(this.value).toFixed(2); sliderDebouncePlot();">
<div class="physics-plot-row">
<div class="physics-plot-frame"><div id="slider-pyplot" class="physics-plot-inner" style="height:280px;"></div></div>
<div class="physics-vslider">
<span class="physics-vslider-cap">\(t_{\mathrm{end}}\)</span>
<div class="physics-vslider-track">
<input id="slider-tmaxInput" type="range" min="5" max="60" step="0.5" value="30" oninput="document.getElementById('slider-tmaxVal').textContent=parseFloat(this.value).toFixed(1); sliderDebouncePlot();">
</div>
<span id="slider-tmaxVal" class="physics-val">30.0</span>
</div>
</div>
<div id="slider-pyout" class="physics-status">Loading…</div>
<div id="slider-debug" class="physics-debug"></div>
</div>

#### Hydrogen demos

Radial \(R_{n\ell}(r)\) and orbital \(| \psi |^2\) in \(xz\). Each plot has its own \(n\) and \(\ell\) (independent). Fixed axes in `hydrogen.py`.

<div class="demo-section physics-demos">
<div class="physics-wf-radios">
<label><input type="radio" name="wf-plottype" value="psi" checked onchange="wfDebouncePlot()"> ψ(r)</label>
<label><input type="radio" name="wf-plottype" value="prob" onchange="wfDebouncePlot()"> r²|ψ|²</label>
</div>
<div class="physics-panel">
<div class="physics-panel-title">Radial</div>
<label class="physics-slider-label">\(n\): <span id="wf-nVal-rad" class="physics-val">1</span></label>
<input id="wf-nInput-rad" class="physics-hslider" type="range" min="1" max="4" step="1" value="1" oninput="wfOnN('rad',this.value)">
<div class="physics-plot-row">
<div class="physics-plot-frame"><div id="wf-pyplot" class="physics-plot-inner" style="height:300px;"></div></div>
<div class="physics-vslider">
<span class="physics-vslider-cap">ℓ</span>
<div class="physics-vslider-track">
<input id="wf-lInput-rad" type="range" min="0" max="3" step="1" value="0" oninput="wfOnL('rad',this.value)">
</div>
<span id="wf-lVal-rad" class="physics-val">0</span>
</div>
</div>
</div>
<div class="physics-panel">
<div class="physics-panel-title">Orbital (xz)</div>
<label class="physics-slider-label">\(n\): <span id="wf-nVal-orb" class="physics-val">1</span></label>
<input id="wf-nInput-orb" class="physics-hslider" type="range" min="1" max="4" step="1" value="1" oninput="wfOnN('orb',this.value)">
<div class="physics-plot-row">
<div class="physics-plot-frame"><div id="wf-orbital" class="physics-plot-inner" style="height:300px;"></div></div>
<div class="physics-vslider">
<span class="physics-vslider-cap">ℓ</span>
<div class="physics-vslider-track">
<input id="wf-lInput-orb" type="range" min="0" max="3" step="1" value="0" oninput="wfOnL('orb',this.value)">
</div>
<span id="wf-lVal-orb" class="physics-val">0</span>
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