// ════════════════════════════════════════════════════════════════════════
// nutrition.js — v9
// Changes from v8:
//   - Each nutrient gets a unique color AND a unique fill pattern
//     (hatch lines, dots, crosses, etc.) for double visual distinction
//   - Save options: PNG/JPG (Plotly built-in), Excel (SheetJS), table PNG
//   - Updated unit label: "mg or mcg per 100g" explained in axis title
// ════════════════════════════════════════════════════════════════════════

// ── Food category display config ──
const FOOD_CATEGORIES = {
  "Fruit":         { color: "#e05c00" },
  "Vegetable":     { color: "#16a34a" },
  "Nut":           { color: "#92400e" },
  "Seed":          { color: "#ca8a04" },
  "Legume":        { color: "#0077cc" },
  "Lentil":        { color: "#7c3aed" },
  "Grain":         { color: "#0891b2" },
  "Cereal":        { color: "#db2777" },
  "Tropical Fruit":{ color: "#f59e0b" },
  "Dried Fruit":   { color: "#b45309" },
  "Mushroom":      { color: "#6b7280" },
  "Seaweed":       { color: "#065f46" },
  "Dairy":         { color: "#2563eb" },
  "Egg":           { color: "#d97706" },
  "Meat & Fish":   { color: "#dc2626" },
  "Herb & Spice":  { color: "#7c3aed" },
  "Fermented":     { color: "#059669" },
};

// ── Nutrient category display config ──
const NUTRIENT_CATEGORIES = {
  "Macro":    { color: "#0077cc", keys: [] },
  "Vitamins": { color: "#7c3aed", keys: [] },
  "Minerals": { color: "#0891b2", keys: [] },
  "Amino":    { color: "#16a34a", keys: [] },
  "Fats":     { color: "#ca8a04", keys: [] },
  "Calories": { color: "#dc2626", keys: ["Calories (kcal)"] },
};

// ── Plotly fill patterns — cycled across nutrients ──
// shape: '', '/', '\', 'x', '-', '|', '+', '.'
const PATTERNS = [
  { shape: '/',  size: 4  },
  { shape: '\\', size: 4  },
  { shape: 'x',  size: 4  },
  { shape: '-',  size: 4  },
  { shape: '|',  size: 4  },
  { shape: '+',  size: 4  },
  { shape: '.',  size: 4  },
  { shape: '/',  size: 10 },
  { shape: '\\', size: 10 },
  { shape: 'x',  size: 10 },
  { shape: '-',  size: 10 },
  { shape: '|',  size: 10 },
];

// ── Global per-nutrient maps: colour and pattern, keyed by nutrient name ──
const NUTRIENT_COLOR_MAP   = {};
const NUTRIENT_PATTERN_MAP = {};

function buildNutrientMaps(allKeys) {
  const goldenAngle    = 137.508;
  const lightnessBands = [38, 52, 44, 58, 34, 48];
  const saturation     = 72;
  allKeys.forEach((k, i) => {
    const hue       = (i * goldenAngle) % 360;
    const lightness = lightnessBands[i % lightnessBands.length];
    NUTRIENT_COLOR_MAP[k]   = `hsl(${hue.toFixed(1)}, ${saturation}%, ${lightness}%)`;
    NUTRIENT_PATTERN_MAP[k] = PATTERNS[i % PATTERNS.length];
  });
}

// ── Food table: per-row colour stepping within category hue ──
function rowColor(baseColor, index, total) {
  const hex = baseColor.replace('#', '');
  const r   = parseInt(hex.slice(0, 2), 16);
  const g   = parseInt(hex.slice(2, 4), 16);
  const b   = parseInt(hex.slice(4, 6), 16);
  const fac = 0.55 + (index / Math.max(total - 1, 1)) * 0.4;
  const mix = 0.3;
  const rr  = Math.min(255, Math.round(r * fac + 255 * (1 - fac) * mix));
  const gg  = Math.min(255, Math.round(g * fac + 255 * (1 - fac) * mix));
  const bb  = Math.min(255, Math.round(b * fac + 255 * (1 - fac) * mix));
  return `rgb(${rr},${gg},${bb})`;
}

// ── Build food selection table ──
function buildFoodTable(foodsMap) {
  const catOrder = Object.keys(FOOD_CATEGORIES);
  const groups   = {};
  catOrder.forEach(c => (groups[c] = []));
  foodsMap.forEach((data, name) => {
    const cat = data.get("category");
    if (groups[cat]) groups[cat].push(name);
    else { groups[cat] = [name]; } // handle new categories not in config
  });
  catOrder.forEach(c => { if (groups[c]) groups[c].sort(); });

  // Also add any categories from data not in config
  foodsMap.forEach((data, name) => {
    const cat = data.get("category");
    if (!FOOD_CATEGORIES[cat]) {
      FOOD_CATEGORIES[cat] = { color: "#6b7280" };
      if (!groups[cat]) groups[cat] = [];
      if (!groups[cat].includes(name)) groups[cat].push(name);
    }
  });

  const allCats = Object.keys(groups).filter(c => groups[c].length > 0);
  const maxRows = Math.max(...allCats.map(c => groups[c].length));
  const table   = document.getElementById("food-table");

  const thead = document.createElement("thead");
  const htr   = document.createElement("tr");
  allCats.forEach(cat => {
    const th = document.createElement("th");
    th.textContent = cat;
    th.dataset.cat = cat;
    th.title = "Click to select / deselect all";
    th.style.cssText = `
      padding:0.3rem 0.4rem;
      background:${(FOOD_CATEGORIES[cat]||{color:"#6b7280"}).color};
      color:white; font-weight:700; text-align:center; cursor:pointer;
      border:1px solid rgba(0,0,0,0.12); white-space:nowrap;
      min-width:80px; font-size:0.68rem;`;
    th.addEventListener("click", () => toggleFoodColumn(cat));
    htr.appendChild(th);
  });
  thead.appendChild(htr);
  table.appendChild(thead);

  const tbody = document.createElement("tbody");
  for (let r = 0; r < maxRows; r++) {
    const tr = document.createElement("tr");
    allCats.forEach(cat => {
      const td    = document.createElement("td");
      const foods = groups[cat] || [];
      if (r < foods.length) {
        const name = foods[r];
        const bg   = rowColor((FOOD_CATEGORIES[cat]||{color:"#6b7280"}).color, r, foods.length);
        td.textContent    = name;
        td.className      = "food-row";
        td.dataset.food   = name;
        td.dataset.cat    = cat;
        td.dataset.baseBg = bg;
        td.style.cssText  = `
          padding:0.25rem 0.4rem; cursor:pointer;
          border:1px solid rgba(0,0,0,0.07);
          background:${bg}; color:#222;
          font-size:0.68rem; white-space:nowrap;
          opacity:0.35; text-decoration:line-through;`;
        td.addEventListener("click", () => toggleFoodRow(td));
      } else {
        td.style.cssText = "border:1px solid rgba(0,0,0,0.04); background:#fafafa;";
      }
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  }
  table.appendChild(tbody);
}

// ── Build nutrient selection table ──
function buildNutrientTable(keys) {
  NUTRIENT_CATEGORIES["Macro"].keys    = keys.gram_keys;
  NUTRIENT_CATEGORIES["Vitamins"].keys = keys.vitamin_keys;
  NUTRIENT_CATEGORIES["Minerals"].keys = keys.mineral_keys;
  NUTRIENT_CATEGORIES["Amino"].keys    = keys.amino_keys;
  NUTRIENT_CATEGORIES["Fats"].keys     = keys.fat_keys;

  // Build colour + pattern maps across ALL nutrient keys in order
  const allKeys = [
    ...keys.gram_keys, ...keys.vitamin_keys, ...keys.mineral_keys,
    ...keys.amino_keys, ...keys.fat_keys, "Calories (kcal)",
  ];
  buildNutrientMaps(allKeys);

  const catOrder = Object.keys(NUTRIENT_CATEGORIES);
  const maxRows  = Math.max(...catOrder.map(c => NUTRIENT_CATEGORIES[c].keys.length));
  const table    = document.getElementById("nutrient-table");
  table.innerHTML = "";

  const thead = document.createElement("thead");
  const htr   = document.createElement("tr");
  catOrder.forEach(cat => {
    const th = document.createElement("th");
    th.textContent = cat;
    th.dataset.cat = cat;
    th.title = "Click to select / deselect all";
    th.style.cssText = `
      padding:0.28rem 0.4rem;
      background:${NUTRIENT_CATEGORIES[cat].color};
      color:white; font-weight:700; text-align:center; cursor:pointer;
      border:1px solid rgba(0,0,0,0.12); white-space:nowrap;
      min-width:95px; font-size:0.62rem;`;
    th.addEventListener("click", () => toggleNutrientColumn(cat));
    htr.appendChild(th);
  });
  thead.appendChild(htr);
  table.appendChild(thead);

  const tbody = document.createElement("tbody");
  for (let r = 0; r < maxRows; r++) {
    const tr = document.createElement("tr");
    catOrder.forEach(cat => {
      const td   = document.createElement("td");
      const kArr = NUTRIENT_CATEGORIES[cat].keys;
      if (r < kArr.length) {
        const name    = kArr[r];
        const bg      = NUTRIENT_COLOR_MAP[name]   || '#aaa';
        const pattern = NUTRIENT_PATTERN_MAP[name] || { shape:'', size:0 };
        td.textContent      = name;
        td.className        = "nutrient-row selected";
        td.dataset.nutrient = name;
        td.dataset.cat      = cat;
        td.dataset.baseBg   = bg;
        // Show pattern hint visually in cell using CSS border styles
        const patternStyle  = patternToBorderStyle(pattern.shape);
        td.style.cssText    = `
          padding:0.2rem 0.4rem; cursor:pointer;
          border:2px ${patternStyle} rgba(255,255,255,0.7);
          background:${bg}; color:white;
          white-space:nowrap; font-weight:600;
          font-size:0.6rem;`;
        td.addEventListener("click", () => toggleNutrientRow(td));
      } else {
        td.style.cssText = "border:1px solid rgba(0,0,0,0.04); background:#fafafa;";
      }
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  }
  table.appendChild(tbody);
}

// Map pattern shape to a CSS border style for visual hint in the table cell
function patternToBorderStyle(shape) {
  switch(shape) {
    case '/':  return 'dashed';
    case '\\': return 'dotted';
    case 'x':  return 'double';
    case '-':  return 'dashed';
    case '|':  return 'dotted';
    case '+':  return 'double';
    case '.':  return 'dotted';
    default:   return 'solid';
  }
}

// ── Toggle helpers — food ──
function toggleFoodRow(td) {
  if (td.classList.contains("selected")) {
    td.classList.remove("selected");
    td.style.opacity        = "0.35";
    td.style.textDecoration = "line-through";
  } else {
    td.classList.add("selected");
    td.style.opacity        = "1";
    td.style.textDecoration = "none";
  }
}
function toggleFoodColumn(cat) {
  const cells       = document.querySelectorAll(`.food-row[data-cat="${cat}"]`);
  const allSelected = [...cells].every(c => c.classList.contains("selected"));
  cells.forEach(c => {
    if (allSelected) {
      c.classList.remove("selected");
      c.style.opacity = "0.35"; c.style.textDecoration = "line-through";
    } else {
      c.classList.add("selected");
      c.style.opacity = "1"; c.style.textDecoration = "none";
    }
  });
}

// ── Toggle helpers — nutrient ──
function toggleNutrientRow(td) {
  if (td.classList.contains("selected")) {
    td.classList.remove("selected");
    td.style.opacity        = "0.35";
    td.style.textDecoration = "line-through";
  } else {
    td.classList.add("selected");
    td.style.opacity        = "1";
    td.style.textDecoration = "none";
  }
}
function toggleNutrientColumn(cat) {
  const cells       = document.querySelectorAll(`.nutrient-row[data-cat="${cat}"]`);
  const allSelected = [...cells].every(c => c.classList.contains("selected"));
  cells.forEach(c => {
    if (allSelected) {
      c.classList.remove("selected");
      c.style.opacity = "0.35"; c.style.textDecoration = "line-through";
    } else {
      c.classList.add("selected");
      c.style.opacity = "1"; c.style.textDecoration = "none";
    }
  });
}

// ── Load Pyodide and fetch foods_v3.py ──
async function loadNutritionPy() {
  let pyodide;
  if (window.pyodideInstance) {
    pyodide = window.pyodideInstance;
  } else {
    pyodide = await loadPyodide();
    window.pyodideInstance = pyodide;
  }

  const resp = await fetch('/assets/py/foods_v3.py');
  if (!resp.ok) throw new Error('Could not load foods_v3.py: ' + resp.status + ' ' + resp.url);
  await pyodide.runPythonAsync(await resp.text());

  const foodsMap = pyodide.globals.get('FOODS').toJs();
  buildFoodTable(foodsMap);

  const firstFood = foodsMap.values().next().value;
  buildNutrientTable({
    gram_keys:    Array.from(firstFood.get("macro").keys()),
    vitamin_keys: Array.from(firstFood.get("vitamins").keys()),
    mineral_keys: Array.from(firstFood.get("minerals").keys()),
    amino_keys:   Array.from(firstFood.get("amino").keys()),
    fat_keys:     Array.from(firstFood.get("fats").keys()),
  });

  document.getElementById("nutrition-status").textContent =
    "Python ready — select foods and click Plot";
  return pyodide;
}

let nutritionPyodideReady = loadNutritionPy();

// ── Get colour + pattern for a nutrient ──
function getNutrientColor(k)   { return NUTRIENT_COLOR_MAP[k]   || '#aaa'; }
function getNutrientPattern(k) { return NUTRIENT_PATTERN_MAP[k] || { shape:'', size:0 }; }

// ── Main plot function ──
async function plotNutrition() {
  const debug  = document.getElementById("nutrition-debug");
  const status = document.getElementById("nutrition-status");
  try {
    const pyodide = await nutritionPyodideReady;

    const selectedFoods = [...document.querySelectorAll(".food-row.selected")]
      .map(c => c.dataset.food);
    if (selectedFoods.length === 0) {
      debug.textContent = "Please select at least one food."; return;
    }

    const selectedNutrients = new Set(
      [...document.querySelectorAll(".nutrient-row.selected")].map(c => c.dataset.nutrient)
    );
    if (selectedNutrients.size === 0) {
      debug.textContent = "Please select at least one nutrient."; return;
    }

    debug.textContent  = "";
    status.textContent = "Calculating...";

    const raw = await pyodide.runPythonAsync(
      `get_chart_data(${JSON.stringify(selectedFoods)})`
    );
    const d = JSON.parse(raw);

    // Partition nutrients by scale
    const largeKeys = [...d.gram_keys, ...d.fat_keys, "Calories (kcal)"]
      .filter(k => selectedNutrients.has(k));
    const smallKeys = [...d.vitamin_keys, ...d.mineral_keys, ...d.amino_keys]
      .filter(k => selectedNutrients.has(k));

    const traces = [];

    // ── Large scale bars (grams/kcal) — bottom x-axis ──
    largeKeys.forEach(k => {
      let vals;
      if      (k === "Calories (kcal)")          vals = d.calories;
      else if (d.macro   && d.macro[k]   != null) vals = d.macro[k];
      else if (d.fats    && d.fats[k]    != null) vals = d.fats[k];
      if (!vals) return;
      const pat = getNutrientPattern(k);
      traces.push({
        name:          k,
        y:             d.foods,
        x:             vals,
        type:          'bar',
        orientation:   'h',
        xaxis:         'x',
        offsetgroup:   'large',
        // Color + pattern together
        marker: {
          color:   getNutrientColor(k),
          pattern: {
            shape:    pat.shape,
            size:     pat.size,
            fillmode: 'overlay',
            fgcolor:  'rgba(255,255,255,0.6)',
            bgcolor:  getNutrientColor(k),
            fgopacity: 0.8,
          },
          line: { color: 'rgba(0,0,0,0.2)', width: 0.5 },
        },
        hovertemplate: `${k}: %{x}<extra></extra>`,
      });
    });

    // ── Small scale bars (mg/mcg) — top x-axis ──
    smallKeys.forEach(k => {
      let vals;
      if      (d.vitamins && d.vitamins[k] != null) vals = d.vitamins[k];
      else if (d.minerals && d.minerals[k] != null) vals = d.minerals[k];
      else if (d.amino    && d.amino[k]    != null) vals = d.amino[k];
      if (!vals) return;
      const pat = getNutrientPattern(k);
      traces.push({
        name:          k,
        y:             d.foods,
        x:             vals,
        type:          'bar',
        orientation:   'h',
        xaxis:         'x2',
        offsetgroup:   'small',
        marker: {
          color:   getNutrientColor(k),
          pattern: {
            shape:    pat.shape,
            size:     pat.size,
            fillmode: 'overlay',
            fgcolor:  'rgba(255,255,255,0.6)',
            bgcolor:  getNutrientColor(k),
            fgopacity: 0.8,
          },
          line: { color: 'rgba(0,0,0,0.2)', width: 0.5 },
        },
        hovertemplate: `${k}: %{x} mg/mcg<extra></extra>`,
      });
    });

    const barH = Math.max(400, d.foods.length * 70 + 160);
    document.getElementById("nutrition-plot").style.height = barH + "px";

    Plotly.newPlot('nutrition-plot', traces, {
      barmode: 'stack',
      height:  barH,
      legend: {
        x: -0.42, y: 1,
        xanchor: 'left', yanchor: 'top',
        orientation: 'v',
        font: { size: 9 },
        bgcolor: 'rgba(248,249,250,0.97)',
        bordercolor: '#ddd', borderwidth: 1,
      },
      xaxis: {
        title: 'g or kcal per 100g',
        side: 'bottom', showgrid: true, zeroline: false,
      },
      xaxis2: {
        title: 'mg or mcg per 100g  (vitamins, minerals, amino acids)',
        side: 'top', overlaying: 'x',
        showgrid: false, zeroline: false, color: '#7c3aed',
      },
      yaxis: { automargin: true, tickfont: { size: 11 } },
      paper_bgcolor: '#f8f9fa',
      plot_bgcolor:  '#f8f9fa',
      margin: { t: 60, b: 60, l: 10, r: 20 },
    }, {
      responsive: true,
      // ── Plotly built-in save buttons ──
      modeBarButtonsToAdd: [
        {
          name: 'Save PNG',
          icon: Plotly.Icons.camera,
          click: function(gd) {
            Plotly.downloadImage(gd, { format: 'png', filename: 'nutrition_chart', scale: 2 });
          }
        },
        {
          name: 'Save JPG',
          icon: Plotly.Icons.camera,
          click: function(gd) {
            Plotly.downloadImage(gd, { format: 'jpeg', filename: 'nutrition_chart', scale: 2 });
          }
        },
        {
          name: 'Save SVG',
          icon: Plotly.Icons.camera,
          click: function(gd) {
            Plotly.downloadImage(gd, { format: 'svg', filename: 'nutrition_chart' });
          }
        },
      ],
      modeBarButtonsToRemove: [],
    });

    // ── Store current data for Excel export ──
    window._nutritionData = d;
    window._nutritionSelectedNutrients = selectedNutrients;

    // ── Summary table ──
    const allCols   = [...d.gram_keys, ...d.vitamin_keys, ...d.mineral_keys,
                        ...d.amino_keys, ...d.fat_keys, 'Calories (kcal)'];
    const shownCols = allCols.filter(k => selectedNutrients.has(k));

    let html = `<div style="margin-bottom:0.5rem; display:flex; gap:0.5rem; flex-wrap:wrap;">
      <button class="btn" onclick="exportExcel()" style="font-size:0.78rem; padding:0.3rem 0.8rem;">
        ⬇ Download Excel</button>
      <button class="btn" onclick="exportTablePNG()" style="font-size:0.78rem; padding:0.3rem 0.8rem; background:#16a34a;">
        ⬇ Save Table as PNG</button>
    </div>`;
    html += `<table id="nutrition-data-table" style="width:100%; border-collapse:collapse; font-size:0.75rem;">
      <thead><tr style="background:#0077cc; color:white;">
        <th style="padding:0.3rem 0.5rem; text-align:left; white-space:nowrap;">Food</th>`;
    shownCols.forEach(n => {
      html += `<th style="padding:0.3rem 0.5rem; white-space:nowrap;">${n}</th>`;
    });
    html += `</tr></thead><tbody>`;

    d.foods.forEach((food, i) => {
      const bg = i % 2 === 0 ? '#ffffff' : '#f0f4f8';
      html += `<tr style="background:${bg};">
        <td style="padding:0.3rem 0.5rem; font-weight:600; white-space:nowrap;">${food}</td>`;
      shownCols.forEach(n => {
        let val = '—';
        if      (n === 'Calories (kcal)')     val = d.calories[i];
        else if (d.macro    && d.macro[n])    val = d.macro[n][i];
        else if (d.vitamins && d.vitamins[n]) val = d.vitamins[n][i];
        else if (d.minerals && d.minerals[n]) val = d.minerals[n][i];
        else if (d.amino    && d.amino[n])    val = d.amino[n][i];
        else if (d.fats     && d.fats[n])     val = d.fats[n][i];
        html += `<td style="padding:0.3rem 0.5rem; text-align:center;">${val}</td>`;
      });
      html += `</tr>`;
    });
    html += `</tbody></table>`;
    document.getElementById("nutrition-table").innerHTML = html;

    status.textContent =
      `Showing ${selectedNutrients.size} nutrients for ${selectedFoods.length} food(s)`;
  } catch (e) {
    debug.textContent = "Error: " + e.message;
    console.error(e);
  }
}

// ── Export table to Excel using SheetJS (loaded from CDN) ──
function exportExcel() {
  const d   = window._nutritionData;
  const sel = window._nutritionSelectedNutrients;
  if (!d || !sel) { alert("Plot first to generate data."); return; }

  // Dynamically load SheetJS if not present
  if (typeof XLSX === 'undefined') {
    const s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js';
    s.onload = () => _doExportExcel(d, sel);
    document.head.appendChild(s);
  } else {
    _doExportExcel(d, sel);
  }
}

function _doExportExcel(d, sel) {
  const allCols   = [...d.gram_keys, ...d.vitamin_keys, ...d.mineral_keys,
                      ...d.amino_keys, ...d.fat_keys, 'Calories (kcal)'];
  const shownCols = allCols.filter(k => sel.has(k));

  // Build array of arrays: header row + data rows
  const rows = [['Food', ...shownCols]];
  d.foods.forEach((food, i) => {
    const row = [food];
    shownCols.forEach(n => {
      let val = '';
      if      (n === 'Calories (kcal)')     val = d.calories[i];
      else if (d.macro    && d.macro[n])    val = d.macro[n][i];
      else if (d.vitamins && d.vitamins[n]) val = d.vitamins[n][i];
      else if (d.minerals && d.minerals[n]) val = d.minerals[n][i];
      else if (d.amino    && d.amino[n])    val = d.amino[n][i];
      else if (d.fats     && d.fats[n])     val = d.fats[n][i];
      row.push(val);
    });
    rows.push(row);
  });

  const ws = XLSX.utils.aoa_to_sheet(rows);
  // Auto-width columns
  ws['!cols'] = rows[0].map((_, ci) => ({
    wch: Math.max(...rows.map(r => String(r[ci]||'').length), 10)
  }));
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, "Nutrition");
  XLSX.writeFile(wb, "nutrition_data.xlsx");
}

// ── Export the HTML table as PNG using html2canvas ──
function exportTablePNG() {
  const tableEl = document.getElementById("nutrition-data-table");
  if (!tableEl) { alert("Plot first to generate table."); return; }

  if (typeof html2canvas === 'undefined') {
    const s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js';
    s.onload = () => _doTablePNG(tableEl);
    document.head.appendChild(s);
  } else {
    _doTablePNG(tableEl);
  }
}

function _doTablePNG(el) {
  html2canvas(el, { scale: 2, backgroundColor: '#ffffff' }).then(canvas => {
    const a = document.createElement('a');
    a.download = 'nutrition_table.png';
    a.href = canvas.toDataURL('image/png');
    a.click();
  });
}