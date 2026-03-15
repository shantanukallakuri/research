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

A pretty random space for general non-scientific topics:
<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
<script src="https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"></script>
<!-- <script src="https://cdn.plot.ly/plotly-latest.min.js"></script> -->

## 1. NutritionCode
<div class="demo-section">
<button class="btn" onclick="plotNutrition()" style="margin-bottom:1rem;">Plot</button>
<div style="margin-bottom:1rem;">
<strong style="font-size:0.85rem;">Select Foods</strong>
<div style="font-size:0.72rem; color:#888; margin-bottom:0.3rem;">Click a cell to toggle. Click a column header to toggle the whole category.</div>
<div style="overflow-x:auto;">
<table id="food-table" style="border-collapse:collapse; font-size:0.68rem; min-width:100%;"></table>
</div>
</div>
<div style="margin-bottom:1rem;">
<strong style="font-size:0.85rem;">Select Nutrients</strong>
<div style="font-size:0.72rem; color:#888; margin-bottom:0.3rem;">Click a cell to toggle. Click a column header to toggle the whole category. Each nutrient has a unique color + pattern.</div>
<div style="overflow-x:auto;">
<table id="nutrient-table" style="border-collapse:collapse; font-size:0.62rem; min-width:100%;"></table>
</div>
</div>
<div id="nutrition-plot" style="width:100%;"></div>
<div id="nutrition-table" style="margin-top:1rem; overflow-x:auto;"></div>
<div id="nutrition-status" style="font-size:0.82rem; color:#555; margin-top:0.5rem;">Loading Python runtime...</div>
<div id="nutrition-debug" style="font-size:0.78rem; color:red;"></div>
</div>
<script src="/assets/js/nutrition.js"></script>