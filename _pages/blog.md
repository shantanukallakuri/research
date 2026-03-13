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
s
## 1. NutritionCode
<script src="https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
{% raw %}
<div class="demo-section">
<!-- ── Chart-type controls: one dropdown per chart group ── -->
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
<!-- ── Food selector grid — built dynamically from FOODS by JS ── -->
<div style="margin-bottom:0.8rem;">
<strong style="font-size:0.85rem;">Select foods (all values per 100g):</strong>
<div id="food-grid"></div>
</div>
<!-- ── Nutrient selector grids — one per chart group, built dynamically ── -->
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
<!-- ── Six stacked chart containers ── -->
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
<!-- ── Summary data table ── -->
<div id="nutrition-table" style="margin-top:1.5rem; overflow-x:auto;"></div>
<div id="nutrition-status" style="font-size:0.85rem; color:#555; margin-top:0.5rem;">Loading Python runtime...</div>
<div id="nutrition-debug" style="font-size:0.8rem; color:red;"></div>
</div>
<script>
// ── Colour palettes — one per nutrient group ──
const PALETTES = {
  macro:   ['#0077cc','#e05c00','#16a34a','#9333ea','#dc2626'],
  vitamin: ['#7c3aed','#a855f7','#6366f1','#8b5cf6','#c084fc','#d946ef','#e879f9','#f0abfc','#ddd6fe','#c4b5fd','#a78bfa','#818cf8'],
  mineral: ['#0891b2','#06b6d4','#0e7490','#155e75','#164e63','#0c4a6e','#1e3a5f','#1e40af'],
  amino:   ['#16a34a','#15803d','#166534','#14532d','#4ade80','#22c55e','#86efac','#bbf7d0','#059669'],
  fat:     ['#ca8a04','#a16207','#92400e','#78350f','#fbbf24'],
  calories:['#dc2626'],
};

// ── Food category display config ──
const CATEGORY_CONFIG = {
  "Fruit":     { label:"Fruits",     color:"#e05c00" },
  "Vegetable": { label:"Vegetables", color:"#16a34a" },
  "Nut":       { label:"Nuts",       color:"#92400e" },
  "Seed":      { label:"Seeds",      color:"#ca8a04" },
  "Legume":    { label:"Legumes",    color:"#0077cc" },
  "Lentil":    { label:"Lentils",    color:"#7c3aed" },
  "Grain":     { label:"Grains",     color:"#0891b2" },
  "Cereal":    { label:"Cereals",    color:"#db2777" },
};

// ── Chart group config — maps group name to plot div ID, nutrient grid ID, palette, axis label ──
const CHART_GROUPS = [
  { key:"macro",   plotId:"plot-macro",   ngId:"ng-macro",   palette:PALETTES.macro,   ctId:"ctMacro",   yLabel:"g per 100g",       calGroup:false },
  { key:"vitamins",plotId:"plot-vitamin", ngId:"ng-vitamin", palette:PALETTES.vitamin, ctId:"ctVitamin", yLabel:"mg/mcg per 100g",   calGroup:false },
  { key:"minerals",plotId:"plot-mineral", ngId:"ng-mineral", palette:PALETTES.mineral, ctId:"ctMineral", yLabel:"mg per 100g",       calGroup:false },
  { key:"amino",   plotId:"plot-amino",   ngId:"ng-amino",   palette:PALETTES.amino,   ctId:"ctAmino",   yLabel:"mg per 100g",       calGroup:false },
  { key:"fats",    plotId:"plot-fat",     ngId:"ng-fat",     palette:PALETTES.fat,     ctId:"ctFat",     yLabel:"g per 100g",        calGroup:false },
  { key:"calories",plotId:"plot-calories",ngId:"ng-calories",palette:PALETTES.calories,ctId:"ctCalories",yLabel:"kcal per 100g",     calGroup:true  },
];

// ── Load Pyodide and fetch foods_v2.py from assets ──
async function loadNutritionPy() {
  let pyodide;
  if (window.pyodideInstance) {
    pyodide = window.pyodideInstance;
  } else {
    pyodide = await loadPyodide();
    window.pyodideInstance = pyodide;
  }

  // Fetch and execute the food database file — defines FOODS and get_chart_data()
  const foodsCode = await fetch('{{ "/assets/py/foods_v2.py" | relative_url }}').then(r => r.text());
  await pyodide.runPythonAsync(foodsCode);

  // Pull FOODS into JS to build the food selector grid
  const foodsMap = pyodide.globals.get('FOODS').toJs();
  buildFoodGrid(foodsMap);

  // Fetch the nutrient key lists from Python (preserves order)
  const first = foodsMap.values().next().value;
  buildNutrientGrid("ng-macro",    Array.from(first.get("macro").keys()),    "#0077cc");
  buildNutrientGrid("ng-vitamin",  Array.from(first.get("vitamins").keys()), "#7c3aed");
  buildNutrientGrid("ng-mineral",  Array.from(first.get("minerals").keys()), "#0891b2");
  buildNutrientGrid("ng-amino",    Array.from(first.get("amino").keys()),    "#16a34a");
  buildNutrientGrid("ng-fat",      Array.from(first.get("fats").keys()),     "#ca8a04");
  buildNutrientGrid("ng-calories", ["Calories (kcal)"],                      "#dc2626");

  document.getElementById("nutrition-status").textContent = "Python ready — select foods and click Plot";
  return pyodide;
}

// ── Build food selector grid grouped by category, alphabetical within group ──
function buildFoodGrid(foodsMap) {
  const container = document.getElementById("food-grid");
  const groups = {};
  foodsMap.forEach((data, name) => {
    const cat = data.get("category");
    if (!groups[cat]) groups[cat] = [];
    groups[cat].push(name);
  });
  Object.keys(CATEGORY_CONFIG).forEach(cat => {
    if (!groups[cat]) return;
    const cfg = CATEGORY_CONFIG[cat];
    const hdr = document.createElement("div");
    hdr.style.cssText = `font-size:0.78rem; font-weight:600; color:${cfg.color}; margin:0.6rem 0 0.3rem;`;
    hdr.textContent = cfg.label;
    container.appendChild(hdr);
    const row = document.createElement("div");
    row.style.cssText = "display:flex; flex-wrap:wrap; gap:0.35rem; margin-bottom:0.2rem;";
    groups[cat].sort().forEach(name => {
      const cell = document.createElement("div");
      cell.className = "food-cell";
      cell.dataset.food = name;
      cell.style.cssText = `padding:0.35rem 0.7rem; border:2px solid #ccc; border-radius:4px;
        cursor:pointer; background:#f8f9fa; color:#555; font-size:0.82rem; font-weight:600; user-select:none;`;
      cell.textContent = name;
      cell.addEventListener("click", () => toggleCell(cell, cfg.color));
      row.appendChild(cell);
    });
    container.appendChild(row);
  });
}

// ── Build a nutrient selector grid — all cells start selected ──
function buildNutrientGrid(containerId, keys, accentColor) {
  const container = document.getElementById(containerId);
  keys.forEach(key => {
    const cell = document.createElement("div");
    cell.className = "nutrient-cell";
    cell.dataset.nutrient = key;
    cell.classList.add("selected");
    cell.style.cssText = `padding:0.28rem 0.6rem; border:2px solid ${accentColor}; border-radius:4px;
      cursor:pointer; background:#f0f4ff; color:${accentColor}; font-size:0.78rem; font-weight:600; user-select:none;`;
    cell.textContent = key;
    cell.addEventListener("click", () => {
      if (cell.classList.contains("selected")) {
        cell.classList.remove("selected");
        cell.style.border = "2px solid #ccc";
        cell.style.background = "#f8f9fa";
        cell.style.color = "#aaa";
      } else {
        cell.classList.add("selected");
        cell.style.border = `2px solid ${accentColor}`;
        cell.style.background = "#f0f4ff";
        cell.style.color = accentColor;
      }
    });
    container.appendChild(cell);
  });
}

// ── Generic cell toggle helper ──
function toggleCell(cell, accentColor) {
  if (cell.classList.contains("selected")) {
    cell.classList.remove("selected");
    cell.style.border = "2px solid #ccc";
    cell.style.background = "#f8f9fa";
    cell.style.color = "#555";
  } else {
    cell.classList.add("selected");
    cell.style.border = `2px solid ${accentColor}`;
    cell.style.background = "#e8f4ff";
    cell.style.color = accentColor;
  }
}

// ── Get selected nutrient keys from a nutrient grid ──
function getSelectedNutrients(ngId) {
  return [...document.querySelectorAll(`#${ngId} .nutrient-cell.selected`)].map(c => c.dataset.nutrient);
}

// ── Build Plotly traces — horizontal bar or line ──
// barPad: extra spacing between food groups on y-axis via offset trick
function makeTraces(keys, dataObj, foods, chartType, palette) {
  return keys.map((k, i) => {
    const color = palette[i % palette.length];
    if (chartType === "bar") {
      return {
        name:        k,
        // Horizontal bar: x=values, y=foods reversed so first food is at top
        x:           dataObj[k],
        y:           [...foods].reverse(),
        type:        "bar",
        orientation: "h",
        marker:      { color: color, opacity: 0.85 },
        // Offset each trace slightly so grouped bars don't bleed into each other
      };
    } else {
      return {
        name:   k,
        x:      foods,
        y:      dataObj[k],
        type:   "scatter",
        mode:   "lines+markers",
        marker: { color: color, size: 7 },
        line:   { color: color, width: 2 },
      };
    }
  });
}

// ── Build Plotly layout ──
// barHeight: px per food item — larger = more vertical space between foods
function makeLayout(xLabel, chartType, numFoods, numTraces) {
  const BAR_HEIGHT_PER_FOOD = 42; // px per food — increase this for more spacing
  const totalBarH = Math.max(260, numFoods * BAR_HEIGHT_PER_FOOD * Math.max(1, numTraces * 0.5) + 160);
  if (chartType === "bar") {
    return {
      height:        totalBarH,
      barmode:       "group",
      bargap:        0.25,       // gap between food groups (0=no gap, 1=all gap)
      bargroupgap:   0.08,       // gap between bars within a group
      xaxis:         { title: xLabel, automargin: true },
      yaxis:         { automargin: true, tickfont: { size: 11 } },
      legend:        { orientation: "h", y: -0.18, font: { size: 11 } },
      paper_bgcolor: "#f8f9fa",
      plot_bgcolor:  "#f8f9fa",
      margin:        { t: 20, b: 100, l: 160, r: 20 },
    };
  } else {
    return {
      height:        380,
      xaxis:         { title: "Food", tickangle: -35, automargin: true },
      yaxis:         { title: xLabel },
      legend:        { orientation: "h", y: -0.4, font: { size: 11 } },
      paper_bgcolor: "#f8f9fa",
      plot_bgcolor:  "#f8f9fa",
      margin:        { t: 20, b: 160, l: 55, r: 20 },
    };
  }
}

let nutritionPyodideReady = loadNutritionPy();

// ── Main plot function ──
async function plotNutrition() {
  const debug  = document.getElementById("nutrition-debug");
  const status = document.getElementById("nutrition-status");
  try {
    const pyodide = await nutritionPyodideReady;

    // Get selected foods
    const selected = [...document.querySelectorAll(".food-cell.selected")].map(c => c.dataset.food);
    if (selected.length === 0) { debug.textContent = "Please select at least one food."; return; }

    debug.textContent  = "";
    status.textContent = "Calculating...";

    // Call Python get_chart_data() — returns full data for all groups
    const raw = await pyodide.runPythonAsync(`get_chart_data(${JSON.stringify(selected)})`);
    const d   = JSON.parse(raw);
    const numFoods = d.foods.length;

    // ── Render each chart group ──
    CHART_GROUPS.forEach(grp => {
      const plotEl  = document.getElementById(grp.plotId);
      const ct      = document.getElementById(grp.ctId).value;
      const selKeys = getSelectedNutrients(grp.ngId);

      if (selKeys.length === 0) {
        // Nothing selected for this group: show placeholder
        plotEl.style.height = "60px";
        plotEl.innerHTML = `<p style="color:#aaa; font-size:0.82rem; padding:0.5rem 0;">No nutrients selected for this group.</p>`;
        return;
      }

      let traces;
      if (grp.calGroup) {
        // Calories: single trace from d.calories array
        traces = [{
          name:        "Calories (kcal)",
          x:           d.calories,
          y:           [...d.foods].reverse(),
          type:        "bar",
          orientation: ct === "bar" ? "h" : undefined,
          mode:        ct === "line" ? "lines+markers" : undefined,
          marker:      { color: "#dc2626", opacity: 0.85 },
        }];
        if (ct === "line") {
          traces = [{ name:"Calories (kcal)", x:d.foods, y:d.calories,
            type:"scatter", mode:"lines+markers",
            marker:{ color:"#dc2626", size:7 }, line:{ color:"#dc2626", width:2 } }];
        }
      } else {
        // Filter to only selected nutrient keys and their data
        const dataObj = {};
        selKeys.forEach(k => { if (d[grp.key] && d[grp.key][k] !== undefined) dataObj[k] = d[grp.key][k]; });
        traces = makeTraces(selKeys, dataObj, d.foods, ct, grp.palette);
      }

      const layout = makeLayout(grp.yLabel, ct, numFoods, selKeys.length);
      plotEl.style.height = "";  // let Plotly use the layout height
      Plotly.newPlot(grp.plotId, traces, layout, { responsive: true });
    });

    // ── Build summary data table with all nutrient groups ──
    const allCols = [
      ...d.macro_keys, ...d.vitamin_keys, ...d.mineral_keys,
      ...d.amino_keys, ...d.fat_keys, "Calories (kcal)"
    ];
    // Group headers for the table
    const colGroups = [
      { label:"Macros",         count:d.macro_keys.length,   color:"#0077cc" },
      { label:"Vitamins",       count:d.vitamin_keys.length, color:"#7c3aed" },
      { label:"Minerals",       count:d.mineral_keys.length, color:"#0891b2" },
      { label:"Amino Acids",    count:d.amino_keys.length,   color:"#16a34a" },
      { label:"Fatty Acids",    count:d.fat_keys.length,     color:"#ca8a04" },
      { label:"Energy",         count:1,                     color:"#dc2626" },
    ];
    let html = `<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
      <thead>
        <tr>
          <th style="padding:0.3rem 0.5rem; background:#374151; color:white; text-align:left;">Food</th>`;
    colGroups.forEach(g => {
      html += `<th colspan="${g.count}" style="padding:0.3rem 0.5rem; background:${g.color}; color:white; text-align:center;">${g.label}</th>`;
    });
    html += `</tr><tr style="background:#1e3a5f; color:white;">
      <th style="padding:0.3rem 0.5rem; text-align:left; position:sticky; left:0; background:#1e3a5f;">Food</th>`;
    allCols.forEach(n => { html += `<th style="padding:0.3rem 0.5rem; white-space:nowrap;">${n}</th>`; });
    html += `</tr></thead><tbody>`;

    d.foods.forEach((food, i) => {
      const bg = i % 2 === 0 ? "#ffffff" : "#f0f4f8";
      html += `<tr style="background:${bg};">
        <td style="padding:0.3rem 0.5rem; font-weight:600; white-space:nowrap; position:sticky; left:0; background:${bg};">${food}</td>`;
      d.macro_keys.forEach(n   => { html += `<td style="padding:0.3rem 0.5rem; text-align:center;">${d.macro[n][i]}</td>`; });
      d.vitamin_keys.forEach(n => { html += `<td style="padding:0.3rem 0.5rem; text-align:center;">${d.vitamins[n][i]}</td>`; });
      d.mineral_keys.forEach(n => { html += `<td style="padding:0.3rem 0.5rem; text-align:center;">${d.minerals[n][i]}</td>`; });
      d.amino_keys.forEach(n   => { html += `<td style="padding:0.3rem 0.5rem; text-align:center;">${d.amino[n][i]}</td>`; });
      d.fat_keys.forEach(n     => { html += `<td style="padding:0.3rem 0.5rem; text-align:center;">${d.fats[n][i]}</td>`; });
      html += `<td style="padding:0.3rem 0.5rem; text-align:center;">${d.calories[i]}</td></tr>`;
    });
    html += `</tbody></table>`;
    document.getElementById("nutrition-table").innerHTML = html;

    status.textContent = `Showing all nutrients per 100g for ${selected.length} food(s)`;
  } catch(e) {
    debug.textContent = "Error: " + e.message;
    console.error(e);
  }
}
</script>
{% raw %}