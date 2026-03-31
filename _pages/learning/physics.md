---
title: "Physics"
layout: topic-page-uncolored
permalink: /learning/physics/
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
(Work under progress)

## 1. Atomic beginnings
### 1.1 Hydrogen

The hydrogen atom is the simplest bound quantum system — it contains a single electron of charge&nbsp; $$\color{blue}{-e}$$ &nbsp;bound to a proton of charge&nbsp; $$\color{blue}{+e}$$ &nbsp;by the Coulomb potential:
<br />
{% include sk/components/eqs.html
  id="eq-1.1"
  eq="\color{blue}E_n = -\tfrac{13.6\text{ eV}}{n^2}"
  num="1.1"
  leader="....."
%}
<br />
{% include sk/components/eqs.html
  id="eq-1.2"
  eq="\color{#0077cc}V(r) = -\tfrac{e^2}{4\pi\epsilon_0 r}"
  num="1.2"
  leader="....."
%}
<br />
{% include sk/components/eqs.html
  id="eq-1.3"
  eq="\color{#7f00ff}E_n = -\tfrac{13.6\text{ eV}}{n^2}"
  num="1.3"
  leader="....."
%}
<br />
As shown in [eq. 1.1](#eq-1.1), the energy scales as $$\tfrac{1}{n^2}$$.

<details class="topic-code-fold">
  <summary>Code</summary>
  <pre><code class="language-python"># Python: assets/py/oscillator_slider.py, assets/py/hydrogen.py
# Browser glue: assets/js/learning-physics.js (Pyodide + Plotly)
</code></pre>
</details>

$$
\displaystyle \psi_{n\ell m} = R_{n\ell}(r)\,Y_\ell^m(\theta,\phi)
$$

The time-independent Schrödinger equation in spherical coordinates is:<br />
$$
\displaystyle \left[ -\tfrac{\hbar^2}{2m_e}\nabla^2 + V(r) \right] \psi(r,\theta,\phi) = E\psi(r,\theta,\phi)
$$

Separating variables, the wavefunction factorizes as:<br />
$$
\displaystyle \psi_{n\ell m}(r,\theta,\phi) = R_{n\ell}(r)\, Y_\ell^m(\theta,\phi)
$$

where $$\displaystyle R_{n\ell}$$ are the radial wavefunctions and $$\displaystyle Y_\ell^m$$ are the spherical harmonics.

Damped Oscillator (Test plot)
<div class="demo-section">
<div style="margin-bottom:0.8rem;">
<label style="font-size:0.9rem;">
Damping γ: <span id="slider-gammaVal" style="font-weight:600; color:#0077cc;">0.10</span>
<br>
<input id="slider-gammaInput" type="range" min="0.01" max="1.99" step="0.01" value="0.10"
style="width:250px; margin-top:0.4rem;"
oninput="document.getElementById('slider-gammaVal').textContent=parseFloat(this.value).toFixed(2); sliderDebouncePlot();">
</label>
</div>
<div id="slider-pyplot" style="width:100%; height:300px;"></div>
<div id="slider-pyout" style="font-size:0.85rem; color:#555; margin-top:0.5rem;">Loading Python runtime...</div>
<div id="slider-debug" style="font-size:0.8rem; color:red; margin-top:0.5rem;"></div>
</div>

Hydrogen Atom Wave Functions
<div class="demo-section">
<div style="margin-bottom:0.8rem; display:flex; flex-wrap:wrap; gap:1.2rem; align-items:flex-start;">
<label style="font-size:0.9rem;">
n (principal): <span id="wf-nVal" style="font-weight:600; color:#0077cc;">1</span><br>
<input id="wf-nInput" type="range" min="1" max="4" step="1" value="1"
style="width:200px; margin-top:0.4rem;"
oninput="wfOnN(this.value)">
</label>
<label style="font-size:0.9rem;">
ℓ (angular): <span id="wf-lVal" style="font-weight:600; color:#0077cc;">0</span><br>
<input id="wf-lInput" type="range" min="0" max="3" step="1" value="0"
style="width:200px; margin-top:0.4rem;"
oninput="wfOnL(this.value)">
</label>
</div>
<div style="margin-bottom:0.6rem;">
<label style="font-size:0.9rem; margin-right:1.2rem;">
<input type="radio" name="wf-plottype" value="psi" checked onchange="wfDebouncePlot()"> ψ(r)
</label>
<label style="font-size:0.9rem;">
<input type="radio" name="wf-plottype" value="prob" onchange="wfDebouncePlot()"> r²|ψ|² radial probability
</label>
</div>
<div style="display:flex; flex-wrap:wrap; gap:1rem;">
<div id="wf-pyplot" style="flex:1; min-width:280px; height:320px;"></div>
<div id="wf-orbital" style="flex:1; min-width:280px; height:320px;"></div>
</div>
<div id="wf-pyout" style="font-size:0.85rem; color:#555; margin-top:0.5rem;">Loading Python runtime...</div>
<div id="wf-debug" style="font-size:0.8rem; color:red; margin-top:0.3rem;"></div>
</div>

<script>
  window.__PHYSICS_PY_URLS__ = [
    "{{ '/assets/py/oscillator_slider.py' | relative_url }}",
    "{{ '/assets/py/hydrogen.py' | relative_url }}"
  ];
</script>
<script src="{{ '/assets/js/learning-physics.js' | relative_url }}"></script>
</div>

### 1.1 Hydrogen

### 1.1 Hydrogen

### 1.1 Hydrogen

### 1.1 Hydrogen

### 1.1 Hydrogen