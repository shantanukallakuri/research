/**
 * Damped oscillator demo — embedded Python + Plotly wiring (edit PYTHON below).
 */
(function () {
  var R = window.PhysikaRuntime;
  if (!R) return;

  var PYTHON =
    "import math\n\n\
# Fixed axes: edit OSCILLATOR_* only\n\
OSCILLATOR_X_RANGE = (0.0, 60.0)\n\
OSCILLATOR_Y_RANGE = (-1.25, 1.25)\n\
OSCILLATOR_X_AXIS_TITLE = \"Time (dimensionless), t\"\n\
OSCILLATOR_Y_AXIS_TITLE = \"Displacement (dimensionless), x\"\n\n\
def run_calc_slider(gamma, t_max=30.0):\n\
    n = 300\n\
    dt = t_max / max(n - 1, 1)\n\
    t = [i * dt for i in range(n)]\n\
    if gamma < 1.0:\n\
        wd = math.sqrt(1.0 - gamma**2)\n\
        y = [math.exp(-gamma * ti) * math.cos(wd * ti) for ti in t]\n\
    elif abs(gamma - 1.0) < 1e-9:\n\
        y = [math.exp(-ti) * (1.0 + ti) for ti in t]\n\
    else:\n\
        s = math.sqrt(gamma**2 - 1.0)\n\
        y = [math.exp(-gamma * ti) * math.cosh(s * ti) for ti in t]\n\
    ep = [math.exp(-gamma * ti) for ti in t]\n\
    en = [-math.exp(-gamma * ti) for ti in t]\n\
    return t, y, ep, en, OSCILLATOR_X_RANGE, OSCILLATOR_Y_RANGE, OSCILLATOR_X_AXIS_TITLE, OSCILLATOR_Y_AXIS_TITLE\n";

  var pyReady = R.loadPythonModule(PYTHON);
  R.onPyodideError(pyReady, "slider-debug");

  var debouncedSliderRun = R.debounce(sliderRunCalc, 80);
  window.sliderDebouncePlot = function () {
    debouncedSliderRun();
  };

  async function sliderRunCalc() {
    var dbg = document.getElementById("slider-debug");
    var out = document.getElementById("slider-pyout");
    if (!out) return;
    try {
      var py = await pyReady;
      var g = parseFloat(document.getElementById("slider-gammaInput").value);
      var tm = parseFloat(document.getElementById("slider-tmaxInput").value);
      var res = await py.runPythonAsync("run_calc_slider(" + g + ", " + tm + ")");
      var c = res.toJs();
      res.destroy?.();
      var xR = Array.from(c[4]);
      var yR = Array.from(c[5]);
      Plotly.react(
        "slider-pyplot",
        [
          { x: c[0], y: c[1], name: "x(t)", type: "scatter", line: { color: "#0077cc" } },
          { x: c[0], y: c[2], name: "+env", type: "scatter", line: { color: "#e05c00", dash: "dash" } },
          { x: c[0], y: c[3], name: "-env", type: "scatter", line: { color: "#e05c00", dash: "dash" } },
        ],
        R.physLayout({
          title: "",
          margin: { t: 12, l: 52, r: 12, b: 48 },
          xaxis: { title: String(c[6]), range: xR, autorange: false },
          yaxis: { title: String(c[7]), range: yR, autorange: false },
        }),
        R.PHYS_PLOTLY_CONFIG
      );
      var t = c[0];
      var pct = (1 - Math.exp(-2 * g * t[t.length - 1])) * 100;
      out.textContent = "gamma=" + g.toFixed(2) + " dissipated ~" + pct.toFixed(1) + "%";
      if (dbg) dbg.textContent = "";
    } catch (e) {
      if (dbg) dbg.textContent = e.message;
    }
  }

  pyReady.then(function () {
    var a = document.getElementById("slider-pyout");
    if (a) {
      a.textContent = "Ready.";
      sliderRunCalc();
    }
  });
})();
