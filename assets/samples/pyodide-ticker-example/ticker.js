/**
 * Sample: load Pyodide once, run Python once for arrays, then animate in JS only.
 * Expects global loadPyodide from pyodide.js (include pyodide_head before this).
 *
 * Set window.__TICKER_MODEL_PY__ to the URL of model.py (e.g. via Liquid relative_url).
 */
(function () {
  const pyUrl = window.__TICKER_MODEL_PY__;
  if (!pyUrl) {
    console.error("Set window.__TICKER_MODEL_PY__ to model.py URL before ticker.js");
    return;
  }

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

  let tFull = [];
  let yFull = [];
  let i = 0;
  let timer = null;
  const stepMs = 40;

  async function init() {
    const out = document.getElementById("ticker-status");
    try {
      const pyodide = await ensurePyodide();
      await loadPythonFromUrl(pyodide, pyUrl);
      const result = await pyodide.runPythonAsync("sine_series()");
      const arr = result.toJs();
      result.destroy?.();
      tFull = Array.from(arr[0]);
      yFull = Array.from(arr[1]);
      if (out) out.textContent = "Ready — " + tFull.length + " points (Python once).";
      drawFrame();
      timer = setInterval(tick, stepMs);
    } catch (e) {
      if (out) out.textContent = "Error: " + e.message;
    }
  }

  function drawFrame() {
    const n = Math.min(i + 1, tFull.length);
    const t = tFull.slice(0, n);
    const y = yFull.slice(0, n);
    Plotly.react("ticker-plot", [{ x: t, y: y, type: "scatter", mode: "lines", line: { color: "#0077cc" } }], {
      title: "sin(t) — drawing by index (JS ticker)",
      xaxis: { title: "t" },
      yaxis: { title: "y", range: [-1.1, 1.1] },
      paper_bgcolor: "#f8f9fa",
      plot_bgcolor: "#f8f9fa"
    });
    const lab = document.getElementById("ticker-i");
    if (lab) lab.textContent = String(i);
  }

  function tick() {
    i += 2;
    if (i >= tFull.length) i = 0;
    drawFrame();
  }

  window.tickerPause = function () {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  };

  window.tickerPlay = function () {
    if (!timer && tFull.length) timer = setInterval(tick, stepMs);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
