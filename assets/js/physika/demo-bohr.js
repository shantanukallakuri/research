/**
 * Bohr model demo — embedded Python + Plotly wiring (edit PYTHON below).
 */
(function () {
  var R = window.PhysikaRuntime;
  if (!R) return;

  var PYTHON =
    '"""Bohr demo — Pyodide; energies vs n (stub)."""\n\n\
def run_bohr_plot(n_max=5):\n\
    n_max = int(n_max)\n\
    n_max = max(1, min(n_max, 20))\n\
    ns = list(range(1, n_max + 1))\n\
    E_eV = [-13.6 / (n * n) for n in ns]\n\
    z = [0.0] * len(ns)\n\
    x_range = (0.5, float(n_max) + 0.5)\n\
    y_range = (-16.0, 2.0)\n\
    x_title = "n"\n\
    y_title = "Energy (eV)"\n\
    return ns, E_eV, z, z, x_range, y_range, x_title, y_title\n';

  var pyReady = R.loadPythonModule(PYTHON);
  R.onPyodideError(pyReady, "bohr-debug");

  var debouncedBohrRun = R.debounce(bohrRunCalc, 80);
  window.bohrDebouncePlot = function () {
    debouncedBohrRun();
  };

  async function bohrRunCalc() {
    var dbg = document.getElementById("bohr-debug");
    var out = document.getElementById("bohr-pyout");
    var plotEl = document.getElementById("bohr-pyplot");
    if (!out || !plotEl) return;
    try {
      var py = await pyReady;
      var nmax = parseInt(document.getElementById("bohr-nmaxInput").value, 10);
      var res = await py.runPythonAsync("run_bohr_plot(" + nmax + ")");
      var c = res.toJs();
      res.destroy?.();
      var xR = Array.from(c[4]);
      var yR = Array.from(c[5]);
      Plotly.react(
        "bohr-pyplot",
        [{ x: c[0], y: c[1], name: "E_n", type: "scatter", mode: "lines+markers", line: { color: "#0077cc" } }],
        R.physLayout({
          title: "",
          margin: { t: 12, l: 52, r: 12, b: 48 },
          xaxis: { title: String(c[6]), range: xR, autorange: false },
          yaxis: { title: String(c[7]), range: yR, autorange: false },
        }),
        R.PHYS_PLOTLY_CONFIG
      );
      var Ey = c[1];
      var eLast = Ey[Ey.length - 1];
      out.textContent =
        "n_max=" + nmax + "   E(" + nmax + ")=" + eLast.toFixed(3) + " eV";
      if (dbg) dbg.textContent = "";
    } catch (e) {
      if (dbg) dbg.textContent = e.message;
    }
  }

  pyReady.then(function () {
    var bo = document.getElementById("bohr-pyout");
    if (bo) {
      bo.textContent = "Ready.";
      bohrRunCalc();
    }
  });
})();
