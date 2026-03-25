---
title: "Fundamentals in Physics, Chemistry and Materials Science"
layout: single
excerpt: "Fundamentals in Chemistry, Physics and Materials Science"
permalink: /learning/
author_profile: true
toc: true
toc_label: "Contents"
toc_icon: "list"
toc_sticky: true
#redirect_from: 
#  - /blog/
#  - /blog.html
---

<!--
## Section One (Test plot - Damped Oscillator Slider)
<div class="demo-section">
  <h4>Python (Pyodide) — Damped Oscillator (Interactive)</h4>
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
<script src="/assets/js/oscillator-slider.js"></script>

## Section Two (Test plot inline)
<canvas id="myChart"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const ctx = document.getElementById('myChart');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar'],
      datasets: [{ label: 'Value', data: [10, 20, 15] }]
    }
  });
</script>

## Section Three (Test chart)
<canvas id="tickerChart"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="/assets/js/ticker.js"></script>

## Section Four (Test live chart)
<div class="demo-section">
  <h4>Live Ticker — Alpha Vantage API</h4>
  <div style="margin-bottom:0.8rem;">
    <input class="ticker-input" id="tickerInput" type="text" value="AAPL" placeholder="AAPL" />
    <button class="btn" onclick="fetchTicker()">Load</button>
    <button class="btn" onclick="document.getElementById('tickerInput').value='MSFT'; fetchTicker()">MSFT</button>
    <button class="btn" onclick="document.getElementById('tickerInput').value='TSLA'; fetchTicker()">TSLA</button>
  </div>
  <canvas id="tickerChart" height="130"></canvas>
  <p id="tickerStatus" class="loading"></p>
</div>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="/assets/js/ticker.js"></script>

## Section Five
## 5 · Hydrogen Atom Wave Functions
<div class="demo-section">
<h4>Python (Pyodide) — Hydrogen Orbitals</h4>
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
<script src="/assets/js/hydrogen.js"></script>


## 2. Oscillator
<script src="https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<div class="demo-section">
<h4>Python (Pyodide) — Damped Oscillator</h4>
<div style="margin-bottom:0.8rem;">
<label style="font-size:0.9rem;">
Damping γ:
<input id="gammaInput" type="number" value="0.1" step="0.05" min="0" max="2" style="width:70px; padding:0.3rem; border:1px solid #ccc; border-radius:4px;">
</label>
<button class="btn" id="calcBtn" onclick="runCalc()">Calculate</button>
</div>
<div id="pyplot" style="width:100%; height:300px;"></div>
<div id="pyout" style="font-size:0.85rem; color:#555; margin-top:0.5rem;">Loading Python runtime...</div>
<div id="debug" style="font-size:0.8rem; color:red; margin-top:0.5rem;"></div>
</div>
<script src="/assets/js/oscillator.js"></script>

-->
<script src="https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@4/tex-mml-chtml.js"></script>

Work in progress:

## The Hydrogen Atom

The hydrogen atom is the simplest bound quantum system — a single electron of charge $$-e$$ bound to a proton of charge <b><span style="color: #4183C4;">$$+e$$</span></b> by the Coulomb potential:<br />
&emsp; $$ V(r) = -\frac{e^2}{4\pi\epsilon_0 r} $$<br />
The time-independent Schrödinger equation in spherical coordinates is:<br />
&emsp; $$ \left[ -\frac{\hbar^2}{2m_e}\nabla^2 + V(r) \right] \psi(r,\theta,\phi) = E\psi(r,\theta,\phi) $$<br />
Separating variables, the wavefunction factorizes as:<br />
&emsp; $$ \psi_{n\ell m}(r,\theta,\phi) = R_{n\ell}(r)\, Y_\ell^m(\theta,\phi) $$<br />
where $R_{n\ell}$ are the radial wavefunctions and $Y_\ell^m$ are the spherical harmonics.


## 1. Damped Oscillator (Test plot)
<div class="demo-section">
<h4>Python (Pyodide) — Damped Oscillator (Interactive)</h4>
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
<script src="/assets/js/oscillator-slider.js"></script>

## 2. Hydrogen Atom Wave Functions

<div class="demo-section">
<h4>Python (Pyodide) — Hydrogen Orbitals</h4>
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
<script src="/assets/js/hydrogen.js"></script>