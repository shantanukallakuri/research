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

A space for general non-scientific topics I am interested in:

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