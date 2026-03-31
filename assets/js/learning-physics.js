/* learning/physics: Pyodide + Plotly. Set window.__PHYSICS_PY_URLS__ in the page before this script. */

async function ensurePyodide() {
  if (window.pyodideInstance) return window.pyodideInstance;
  const pyodide = await loadPyodide();
  window.pyodideInstance = pyodide;
  return pyodide;
}

async function loadPythonFromUrl(pyodide, url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error("Could not load " + url + ": " + res.status);
  await pyodide.runPythonAsync(await res.text());
}

function debounce(fn, delayMs) {
  var t = null;
  return function () {
    clearTimeout(t);
    t = setTimeout(fn, delayMs);
  };
}

var pyReady = (async function () {
  var pyodide = await ensurePyodide();
  var urls = window.__PHYSICS_PY_URLS__ || [];
  for (var u = 0; u < urls.length; u++) {
    await loadPythonFromUrl(pyodide, urls[u]);
  }
  return pyodide;
})();

pyReady.catch(function (err) {
  var msg = "Failed to load Python: " + err.message;
  var s = document.getElementById("slider-debug");
  var w = document.getElementById("wf-debug");
  if (s) s.textContent = msg;
  if (w) w.textContent = msg;
});

pyReady.then(function () {
  var s = document.getElementById("slider-pyout");
  var w = document.getElementById("wf-pyout");
  if (s) s.textContent = "Python ready — drag the slider";
  if (w) w.textContent = "Python ready — drag the sliders";
  sliderRunCalc();
  wfRunCalc();
});

/* --- Damped oscillator --- */

var debouncedSliderRun = debounce(sliderRunCalc, 80);

window.sliderDebouncePlot = function () {
  debouncedSliderRun();
};

async function sliderRunCalc() {
  var debug = document.getElementById("slider-debug");
  var pyout = document.getElementById("slider-pyout");
  if (!pyout) return;

  try {
    var pyodide = await pyReady;
    var gamma = parseFloat(document.getElementById("slider-gammaInput").value);
    var result = await pyodide.runPythonAsync("run_calc_slider(" + gamma + ")");
    var c = result.toJs();
    result.destroy?.();

    var t = c[0];
    var y = c[1];
    var ep = c[2];
    var en = c[3];

    Plotly.react("slider-pyplot", [
      { x: t, y: y, name: "x(t)", type: "scatter", line: { color: "#0077cc" } },
      { x: t, y: ep, name: "+envelope", type: "scatter", line: { color: "#e05c00", dash: "dash" } },
      { x: t, y: en, name: "-envelope", type: "scatter", line: { color: "#e05c00", dash: "dash" } }
    ], {
      title: "Damped Oscillator (γ=" + gamma.toFixed(2) + ")",
      xaxis: { title: "Time" },
      yaxis: { title: "Amplitude" },
      paper_bgcolor: "#f8f9fa",
      plot_bgcolor: "#f8f9fa"
    });

    var energy = (1 - Math.exp(-2 * gamma * t[t.length - 1])) * 100;
    pyout.textContent = "γ = " + gamma.toFixed(2) + " | Energy dissipated: " + energy.toFixed(1) + "%";
    if (debug) debug.textContent = "";
  } catch (e) {
    if (debug) debug.textContent = "Error: " + e.message;
  }
}

/* --- Hydrogen --- */

var wfDebounceTimer = null;

window.wfOnN = function (val) {
  var n = parseInt(val, 10);
  document.getElementById("wf-nVal").textContent = n;
  var lSlider = document.getElementById("wf-lInput");
  lSlider.max = n - 1;
  var l = parseInt(lSlider.value, 10);
  if (l > n - 1) {
    lSlider.value = n - 1;
    document.getElementById("wf-lVal").textContent = n - 1;
  }
  wfDebouncePlot();
};

window.wfOnL = function (val) {
  document.getElementById("wf-lVal").textContent = parseInt(val, 10);
  wfDebouncePlot();
};

window.wfDebouncePlot = function () {
  clearTimeout(wfDebounceTimer);
  wfDebounceTimer = setTimeout(wfRunCalc, 80);
};

async function wfRunCalc() {
  var debug = document.getElementById("wf-debug");
  var pyout = document.getElementById("wf-pyout");
  if (!pyout) return;

  try {
    var pyodide = await pyReady;
    var n = parseInt(document.getElementById("wf-nInput").value, 10);
    var l = parseInt(document.getElementById("wf-lInput").value, 10);
    var plotType = document.querySelector('input[name="wf-plottype"]:checked').value;

    var result = await pyodide.runPythonAsync(
      "hydrogen_radial(" + n + ", " + l + ", \"" + plotType + "\")"
    );
    var radialConverted = result.toJs();
    result.destroy?.();
    var r = radialConverted[0];
    var y = radialConverted[1];
    var nodeCount = radialConverted[2];
    var energy = radialConverted[3];

    var isProb = plotType === "prob";
    var yLabel = isProb ? "r²|ψ(r)|²" : "ψ(r)";
    var color = isProb ? "#9333ea" : "#0077cc";
    var radTitle = "n=" + n + ", ℓ=" + l + "  —  " + (isProb ? "Radial Probability Density" : "Radial Wave Function");

    var radTraces = [
      { x: r, y: y, name: yLabel, type: "scatter", line: { color: color, width: 2 } }
    ];
    if (!isProb) {
      radTraces.push({
        x: [r[0], r[r.length - 1]], y: [0, 0],
        type: "scatter", mode: "lines",
        line: { color: "#ccc", width: 1, dash: "dot" },
        showlegend: false
      });
    }

    Plotly.react("wf-pyplot", radTraces, {
      title: radTitle,
      xaxis: { title: "r / a₀" },
      yaxis: { title: yLabel },
      paper_bgcolor: "#f8f9fa",
      plot_bgcolor: "#f8f9fa",
      margin: { t: 45, l: 50, r: 20, b: 50 }
    });

    var orbResult = await pyodide.runPythonAsync(
      "hydrogen_orbital_slice(" + n + ", " + l + ")"
    );
    var orbitalConverted = orbResult.toJs();
    orbResult.destroy?.();
    var xGrid = orbitalConverted[0];
    var zGrid = orbitalConverted[1];
    var psiGrid = orbitalConverted[2];
    var orbLabel = orbitalConverted[3];

    var xArr = Array.from(xGrid);
    var zArr = Array.from(zGrid);
    var psiArr = Array.from(psiGrid).map(function (row) {
      return Array.from(row);
    });

    Plotly.react("wf-orbital", [{
      x: xArr,
      y: zArr,
      z: psiArr,
      type: "heatmap",
      colorscale: "RdBu",
      zmid: 0,
      colorbar: { title: "|ψ|²", thickness: 12 }
    }], {
      title: orbLabel + " orbital  (xz slice)",
      xaxis: { title: "x / a₀", scaleanchor: "y" },
      yaxis: { title: "z / a₀" },
      paper_bgcolor: "#f8f9fa",
      plot_bgcolor: "#f8f9fa",
      margin: { t: 45, l: 50, r: 60, b: 50 }
    });

    var names = ["s", "p", "d", "f"];
    var orbName = n + (names[l] || "?");
    var nodeStr = nodeCount === 1 ? "1 radial node" : nodeCount + " radial nodes";
    pyout.textContent =
      orbName + " orbital | E = " + energy.toFixed(4) + " Ry | " + nodeStr +
      " | ℓ=" + l + " → " + (names[l] || "?") + " symmetry";
    if (debug) debug.textContent = "";
  } catch (e) {
    if (debug) debug.textContent = "Error: " + e.message;
  }
}
