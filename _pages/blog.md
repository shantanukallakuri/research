---
title: "Blog"
layout: single
excerpt: "Blog"
permalink: /blog/
author_profile: true
toc: true
toc_label: "Contents"
toc_icon: "list"
toc_sticky: true
#redirect_from: 
#  - /blog/
#  - /blog.html
---

A space for general non-scientific topics I am interested in:s

## 1. NutritionCode
<script src="https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="/assets/js/nutrition.js"></script>
<div class="demo-section">
<div style="margin-bottom:0.8rem; display:flex; flex-wrap:wrap; gap:0.8rem; align-items:center;">
<div><label style="font-size:0.82rem; font-weight:600; margin-right:0.3rem;">Macros:</label>
<select id="ctMacro" style="padding:0.35rem; border:1px solid #ccc; border-radius:4px; font-size:0.85rem;">
<option value="bar">H-Bar</option><option value="line">Line</option></select></div>
<div><label style="font-size:0.82rem; font-weight:600; margin-right:0.3rem;">Vitamins:</label>
<select id="ctVitamin" style="padding:0.35rem; border:1px solid #ccc; border-radius:4px; font-size:0.85rem;">
<option value="bar">H-Bar</option><option value="line">Line</option></select></div>
<div><label style="font-size:0.82rem; font-weight:600; margin-right:0.3rem;">Minerals:</label>
<select id="ctMineral" style="padding:0.35rem; border:1px solid #ccc; border-radius:4px; font-size:0.85rem;">
<option value="bar">H-Bar</option><option value="line">Line</option></select></div>
<div><label style="font-size:0.82rem; font-weight:600; margin-right:0.3rem;">Amino Acids:</label>
<select id="ctAmino" style="padding:0.35rem; border:1px solid #ccc; border-radius:4px; font-size:0.85rem;">
<option value="bar">H-Bar</option><option value="line">Line</option></select></div>
<div><label style="font-size:0.82rem; font-weight:600; margin-right:0.3rem;">Fatty Acids:</label>
<select id="ctFat" style="padding:0.35rem; border:1px solid #ccc; border-radius:4px; font-size:0.85rem;">
<option value="bar">H-Bar</option><option value="line">Line</option></select></div>
<div><label style="font-size:0.82rem; font-weight:600; margin-right:0.3rem;">Calories:</label>
<select id="ctCalories" style="padding:0.35rem; border:1px solid #ccc; border-radius:4px; font-size:0.85rem;">
<option value="bar">H-Bar</option><option value="line">Line</option></select></div>
<button class="btn" onclick="plotNutrition()">Plot</button>
</div>
<div style="margin-bottom:0.8rem;">
<strong style="font-size:0.85rem;">Select foods (all values per 100g):</strong>
<div id="food-grid"></div>
</div>
<div style="margin-bottom:1rem;">
<strong style="font-size:0.85rem;">Select nutrients to display:</strong>
<div style="display:flex; flex-wrap:wrap; gap:1.2rem; margin-top:0.5rem;">
<div><div style="font-size:0.76rem; font-weight:700; color:#0077cc; margin-bottom:0.3rem; text-transform:uppercase; letter-spacing:0.05em;">Macronutrients</div>
<div id="ng-macro" style="display:flex; flex-wrap:wrap; gap:0.3rem;"></div></div>
<div><div style="font-size:0.76rem; font-weight:700; color:#7c3aed; margin-bottom:0.3rem; text-transform:uppercase; letter-spacing:0.05em;">Vitamins</div>
<div id="ng-vitamin" style="display:flex; flex-wrap:wrap; gap:0.3rem;"></div></div>
<div><div style="font-size:0.76rem; font-weight:700; color:#0891b2; margin-bottom:0.3rem; text-transform:uppercase; letter-spacing:0.05em;">Minerals</div>
<div id="ng-mineral" style="display:flex; flex-wrap:wrap; gap:0.3rem;"></div></div>
<div><div style="font-size:0.76rem; font-weight:700; color:#16a34a; margin-bottom:0.3rem; text-transform:uppercase; letter-spacing:0.05em;">Amino Acids</div>
<div id="ng-amino" style="display:flex; flex-wrap:wrap; gap:0.3rem;"></div></div>
<div><div style="font-size:0.76rem; font-weight:700; color:#ca8a04; margin-bottom:0.3rem; text-transform:uppercase; letter-spacing:0.05em;">Fatty Acids</div>
<div id="ng-fat" style="display:flex; flex-wrap:wrap; gap:0.3rem;"></div></div>
<div><div style="font-size:0.76rem; font-weight:700; color:#dc2626; margin-bottom:0.3rem; text-transform:uppercase; letter-spacing:0.05em;">Calories</div>
<div id="ng-calories" style="display:flex; flex-wrap:wrap; gap:0.3rem;"></div></div>
</div>
</div>
<div style="display:flex; flex-direction:column; gap:1.5rem;">
<div><div style="font-size:0.82rem; font-weight:600; color:#0077cc; margin-bottom:0.3rem;">Macronutrients (g per 100g)</div>
<div id="plot-macro" style="width:100%;"></div></div>
<div><div style="font-size:0.82rem; font-weight:600; color:#7c3aed; margin-bottom:0.3rem;">Vitamins (mg / mcg per 100g)</div>
<div id="plot-vitamin" style="width:100%;"></div></div>
<div><div style="font-size:0.82rem; font-weight:600; color:#0891b2; margin-bottom:0.3rem;">Minerals (mg per 100g)</div>
<div id="plot-mineral" style="width:100%;"></div></div>
<div><div style="font-size:0.82rem; font-weight:600; color:#16a34a; margin-bottom:0.3rem;">Amino Acids (mg per 100g)</div>
<div id="plot-amino" style="width:100%;"></div></div>
<div><div style="font-size:0.82rem; font-weight:600; color:#ca8a04; margin-bottom:0.3rem;">Fatty Acids (g per 100g)</div>
<div id="plot-fat" style="width:100%;"></div></div>
<div><div style="font-size:0.82rem; font-weight:600; color:#dc2626; margin-bottom:0.3rem;">Calories (kcal per 100g)</div>
<div id="plot-calories" style="width:100%;"></div></div>
</div>
<div id="nutrition-table" style="margin-top:1.5rem; overflow-x:auto;"></div>
<div id="nutrition-status" style="font-size:0.85rem; color:#555; margin-top:0.5rem;">Loading Python runtime...</div>
<div id="nutrition-debug" style="font-size:0.8rem; color:red;"></div>
</div>

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

## 3. Damped Oscillator
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

## 4. Hydrogen Atom Wave Functions

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