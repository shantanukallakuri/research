/**
 * Shared helpers for Physika demo scripts: one Pyodide instance, Plotly layout, debounce.
 * Load before per-demo bundles (demo-bohr.js, demo-oscillator.js, demo-hydrogen.js).
 */
(function () {
  async function ensurePyodide() {
    if (window.pyodideInstance) return window.pyodideInstance;
    var p = await loadPyodide();
    window.pyodideInstance = p;
    return p;
  }

  function debounce(fn, ms) {
    var t;
    return function () {
      clearTimeout(t);
      t = setTimeout(fn, ms);
    };
  }

  var PHYS_PLOTLY_CONFIG = { displayModeBar: true, displaylogo: false, scrollZoom: true };
  function physLayout(o) {
    return Object.assign(
      { dragmode: "zoom", paper_bgcolor: "#f8f9fa", plot_bgcolor: "#f8f9fa" },
      o
    );
  }

  /**
   * Run embedded Python once and resolve to the shared Pyodide instance.
   * Demos pass their PYTHON string; no duplicate loadPyodide / runPythonAsync boilerplate.
   */
  function loadPythonModule(source) {
    return (async function () {
      var py = await ensurePyodide();
      await py.runPythonAsync(source);
      return py;
    })();
  }

  /** Wire pyReady.catch to a debug element id (same message shape for every demo). */
  function onPyodideError(pyReady, debugElementId) {
    pyReady.catch(function (e) {
      var el = document.getElementById(debugElementId);
      if (el) el.textContent = "Python: " + e.message;
    });
  }

  window.PhysikaRuntime = {
    ensurePyodide: ensurePyodide,
    loadPythonModule: loadPythonModule,
    onPyodideError: onPyodideError,
    debounce: debounce,
    physLayout: physLayout,
    PHYS_PLOTLY_CONFIG: PHYS_PLOTLY_CONFIG,
  };
})();
