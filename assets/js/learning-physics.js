async function ensurePyodide() {
  if (window.pyodideInstance) return window.pyodideInstance;
  var p = await loadPyodide();
  window.pyodideInstance = p;
  return p;
}
async function loadPythonFromUrl(pyodide, url) {
  var res = await fetch(url);
  if (!res.ok) throw new Error("load " + url + ": " + res.status);
  await pyodide.runPythonAsync(await res.text());
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

var pyReady = (async function () {
  var pyodide = await ensurePyodide();
  var urls = window.__PHYSICS_PY_URLS__ || [];
  for (var i = 0; i < urls.length; i++) await loadPythonFromUrl(pyodide, urls[i]);
  return pyodide;
})();

function setPhysicsErr(msg) {
  var a = document.getElementById("slider-debug");
  var b = document.getElementById("wf-debug");
  if (a) a.textContent = msg;
  if (b) b.textContent = msg;
}
pyReady.catch(function (e) {
  setPhysicsErr("Python: " + e.message);
});
pyReady.then(function () {
  var a = document.getElementById("slider-pyout");
  var b = document.getElementById("wf-pyout");
  if (a) a.textContent = "Ready.";
  if (b) b.textContent = "Ready.";
  sliderRunCalc();
  wfRunCalc();
  var nr = document.getElementById("wf-nInput-rad");
  if (nr) wfClampLForN(document.getElementById("wf-lInput-rad"), document.getElementById("wf-lVal-rad"), parseInt(nr.value, 10));
  var no = document.getElementById("wf-nInput-orb");
  if (no) wfClampLForN(document.getElementById("wf-lInput-orb"), document.getElementById("wf-lVal-orb"), parseInt(no.value, 10));
  var bo = document.getElementById("bohr-pyout");
  if (bo) {
    bo.textContent = "Ready.";
    bohrRunCalc();
  }
});


var debouncedSliderRun = debounce(sliderRunCalc, 80);
var debouncedWfRun = debounce(wfRunCalc, 80);
window.sliderDebouncePlot = function () {
  debouncedSliderRun();
};
window.wfDebouncePlot = function () {
  debouncedWfRun();
};

var debouncedBohrRun = debounce(bohrRunCalc, 80);
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
      physLayout({
        title: "",
        margin: { t: 12, l: 52, r: 12, b: 48 },
        xaxis: { title: String(c[6]), range: xR, autorange: false },
        yaxis: { title: String(c[7]), range: yR, autorange: false },
      }),
      PHYS_PLOTLY_CONFIG
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
      physLayout({
        title: "",
        margin: { t: 12, l: 52, r: 12, b: 48 },
        xaxis: { title: String(c[6]), range: xR, autorange: false },
        yaxis: { title: String(c[7]), range: yR, autorange: false },
      }),
      PHYS_PLOTLY_CONFIG
    );
    var t = c[0];
    var pct = (1 - Math.exp(-2 * g * t[t.length - 1])) * 100;
    out.textContent = "gamma=" + g.toFixed(2) + " dissipated ~" + pct.toFixed(1) + "%";
    if (dbg) dbg.textContent = "";
  } catch (e) {
    if (dbg) dbg.textContent = e.message;
  }
}

function wfClampLForN(lIn, lVal, n) {
  lIn.max = n - 1;
  var l = parseInt(lIn.value, 10);
  if (l > n - 1) {
    l = n - 1;
    lIn.value = String(l);
  }
  lVal.textContent = String(l);
}
window.wfOnN = function (side, v) {
  var n = parseInt(v, 10);
  document.getElementById("wf-nVal-" + side).textContent = String(n);
  wfClampLForN(document.getElementById("wf-lInput-" + side), document.getElementById("wf-lVal-" + side), n);
  wfDebouncePlot();
};
window.wfOnL = function (side, v) {
  document.getElementById("wf-lVal-" + side).textContent = String(parseInt(v, 10));
  wfDebouncePlot();
};

async function wfRunCalc() {
  var dbg = document.getElementById("wf-debug");
  var out = document.getElementById("wf-pyout");
  if (!out) return;
  try {
    var py = await pyReady;
    var nR = parseInt(document.getElementById("wf-nInput-rad").value, 10);
    var lR = parseInt(document.getElementById("wf-lInput-rad").value, 10);
    var nO = parseInt(document.getElementById("wf-nInput-orb").value, 10);
    var lO = parseInt(document.getElementById("wf-lInput-orb").value, 10);
    var pt = document.querySelector('input[name="wf-plottype"]:checked').value;
    var prob = pt === "prob";

    var res = await py.runPythonAsync("hydrogen_radial(" + nR + ", " + lR + ", \"" + pt + "\")");
    var R = res.toJs();
    res.destroy?.();
    var xR = Array.from(R[4]);
    var yR = Array.from(prob ? R[6] : R[5]);
    var yT = String(prob ? R[9] : R[8]);
    var traces = [
      {
        x: R[0],
        y: R[1],
        name: prob ? "prob" : "R_nl",
        type: "scatter",
        line: { color: prob ? "#9333ea" : "#0077cc", width: 2 },
      },
    ];
    if (!prob) traces.push({ x: [xR[0], xR[1]], y: [0, 0], type: "scatter", mode: "lines", line: { color: "#ccc", width: 1, dash: "dot" }, showlegend: false });
    Plotly.react(
      "wf-pyplot",
      traces,
      physLayout({
        title: "",
        xaxis: { title: String(R[7]), range: xR, autorange: false },
        yaxis: { title: yT, range: yR, autorange: false },
        margin: { t: 12, l: 50, r: 20, b: 50 },
      }),
      PHYS_PLOTLY_CONFIG
    );

    var res2 = await py.runPythonAsync("hydrogen_orbital_slice(" + nO + ", " + lO + ")");
    var O = res2.toJs();
    res2.destroy?.();
    var ax = Array.from(O[4]);
    var psi = Array.from(O[2]).map(function (row) {
      return Array.from(row);
    });
    Plotly.react(
      "wf-orbital",
      [
        {
          x: Array.from(O[0]),
          y: Array.from(O[1]),
          z: psi,
          type: "heatmap",
          colorscale: "RdBu",
          zmid: 0,
          colorbar: { title: "|psi|^2", thickness: 12 },
        },
      ],
      physLayout({
        title: "",
        xaxis: { title: String(O[5]), range: ax, autorange: false, scaleanchor: "y", scaleratio: 1 },
        yaxis: { title: String(O[6]), range: ax, autorange: false },
        margin: { t: 12, l: 50, r: 60, b: 50 },
      }),
      PHYS_PLOTLY_CONFIG
    );

    var nm = ["s", "p", "d", "f"];
    out.textContent =
      "Radial n=" + nR + " l=" + lR + " E=" + Number(R[3]).toFixed(4) + " Ry nodes=" + R[2] +
      " | Orbital n=" + nO + " l=" + lO + " " + nO + (nm[lO] || "?");
    if (dbg) dbg.textContent = "";
  } catch (e) {
    if (dbg) dbg.textContent = e.message;
  }
}
