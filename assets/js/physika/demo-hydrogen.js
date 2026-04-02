/**
 * Hydrogen radial + orbital demos — embedded Python + Plotly wiring (edit PYTHON below).
 */
(function () {
  var R = window.PhysikaRuntime;
  if (!R) return;

  var PYTHON =
    'import math\n\n\
RADIAL_X_RANGE = (0.0, 55.0)\n\
RADIAL_Y_RANGE_PSI = (-0.55, 0.55)\n\
RADIAL_Y_RANGE_PROB = (0.0, 0.20)\n\
RADIAL_X_AXIS_TITLE = "Radius (Bohr radii), r"\n\
RADIAL_Y_AXIS_TITLE_PSI = "Radial factor (a0^{-3/2}), R_nl"\n\
RADIAL_Y_AXIS_TITLE_PROB = "Radial density (1/a0), r^2|R_nl|^2"\n\
ORBITAL_AXIS_RANGE = (-52.0, 52.0)\n\
ORBITAL_X_AXIS_TITLE = "Position (Bohr radii), x"\n\
ORBITAL_Z_AXIS_TITLE = "Position (Bohr radii), z"\n\n\
def laguerre_assoc(n, alpha, x):\n\
    if n == 0:\n\
        return 1.0\n\
    if n == 1:\n\
        return 1.0 + alpha - x\n\
    L2, L1 = 1.0, 1.0 + alpha - x\n\
    for k in range(2, n + 1):\n\
        L_curr = ((2 * k - 1 + alpha - x) * L1 - (k - 1 + alpha) * L2) / k\n\
        L2, L1 = L1, L_curr\n\
    return L1\n\n\
def legendre_assoc(l, m, x):\n\
    m = abs(m)\n\
    pmm = 1.0\n\
    if m > 0:\n\
        somx2 = math.sqrt(max(0.0, 1.0 - x * x))\n\
        fact = 1.0\n\
        for _ in range(m):\n\
            pmm *= -fact * somx2\n\
            fact += 2.0\n\
    if l == m:\n\
        return pmm\n\
    pmmp1 = x * (2 * m + 1) * pmm\n\
    if l == m + 1:\n\
        return pmmp1\n\
    for ll in range(m + 2, l + 1):\n\
        pll = (x * (2 * ll - 1) * pmmp1 - (ll + m - 1) * pmm) / (ll - m)\n\
        pmm = pmmp1\n\
        pmmp1 = pll\n\
    return pmmp1\n\n\
def R_nl(n, l, r):\n\
    nr = n - l - 1\n\
    if nr < 0:\n\
        return 0.0\n\
    rho = 2.0 * r / n\n\
    norm = (2.0 / n) ** 1.5 * math.sqrt(math.factorial(nr) / (2.0 * n * math.factorial(n + l)))\n\
    return norm * math.exp(-rho / 2.0) * (rho ** l) * laguerre_assoc(nr, 2 * l + 1, rho)\n\n\
def hydrogen_radial(n, l, plot_type="psi"):\n\
    r_max = max(4 * n * (n + 1), 30)\n\
    num = 600\n\
    dr = r_max / num\n\
    r_vals = [dr * i for i in range(1, num + 1)]\n\
    psi_vals = [R_nl(n, l, r) for r in r_vals]\n\
    if plot_type == "prob":\n\
        y_vals = [r**2 * p**2 for r, p in zip(r_vals, psi_vals)]\n\
    else:\n\
        y_vals = psi_vals\n\
    return (\n\
        r_vals,\n\
        y_vals,\n\
        n - l - 1,\n\
        -1.0 / n**2,\n\
        RADIAL_X_RANGE,\n\
        RADIAL_Y_RANGE_PSI,\n\
        RADIAL_Y_RANGE_PROB,\n\
        RADIAL_X_AXIS_TITLE,\n\
        RADIAL_Y_AXIS_TITLE_PSI,\n\
        RADIAL_Y_AXIS_TITLE_PROB,\n\
    )\n\n\
def hydrogen_orbital_slice(n, l):\n\
    grid = 80\n\
    r_max = max(4 * n * (n + 1), 30)\n\
    coords = [r_max * (-1 + 2 * k / (grid - 1)) for k in range(grid)]\n\
    names = ["s", "p", "d", "f"]\n\
    label = str(n) + (names[l] if l < len(names) else "?")\n\
    psi2 = []\n\
    for zi in coords:\n\
        row = []\n\
        for xi in coords:\n\
            r = math.sqrt(xi**2 + zi**2)\n\
            if r < 1e-8:\n\
                row.append(0.0)\n\
                continue\n\
            cos_theta = zi / r\n\
            R = R_nl(n, l, r)\n\
            norm_Y = math.sqrt((2 * l + 1) / (4 * math.pi))\n\
            Y = norm_Y * legendre_assoc(l, 0, cos_theta)\n\
            row.append((R * Y) ** 2)\n\
        psi2.append(row)\n\
    return coords, coords, psi2, label, ORBITAL_AXIS_RANGE, ORBITAL_X_AXIS_TITLE, ORBITAL_Z_AXIS_TITLE\n';

  var pyReady = R.loadPythonModule(PYTHON);
  R.onPyodideError(pyReady, "wf-debug");

  var debouncedWfRun = R.debounce(wfRunCalc, 80);
  window.wfDebouncePlot = function () {
    debouncedWfRun();
  };

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
    window.wfDebouncePlot();
  };
  window.wfOnL = function (side, v) {
    document.getElementById("wf-lVal-" + side).textContent = String(parseInt(v, 10));
    window.wfDebouncePlot();
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

      var res = await py.runPythonAsync("hydrogen_radial(" + nR + ", " + lR + ', "' + pt + '")');
      var Rr = res.toJs();
      res.destroy?.();
      var xR = Array.from(Rr[4]);
      var yR = Array.from(prob ? Rr[6] : Rr[5]);
      var yT = String(prob ? Rr[9] : Rr[8]);
      var traces = [
        {
          x: Rr[0],
          y: Rr[1],
          name: prob ? "prob" : "R_nl",
          type: "scatter",
          line: { color: prob ? "#9333ea" : "#0077cc", width: 2 },
        },
      ];
      if (!prob) traces.push({ x: [xR[0], xR[1]], y: [0, 0], type: "scatter", mode: "lines", line: { color: "#ccc", width: 1, dash: "dot" }, showlegend: false });
      Plotly.react(
        "wf-pyplot",
        traces,
        R.physLayout({
          title: "",
          xaxis: { title: String(Rr[7]), range: xR, autorange: false },
          yaxis: { title: yT, range: yR, autorange: false },
          margin: { t: 12, l: 50, r: 20, b: 50 },
        }),
        R.PHYS_PLOTLY_CONFIG
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
        R.physLayout({
          title: "",
          xaxis: { title: String(O[5]), range: ax, autorange: false, scaleanchor: "y", scaleratio: 1 },
          yaxis: { title: String(O[6]), range: ax, autorange: false },
          margin: { t: 12, l: 50, r: 60, b: 50 },
        }),
        R.PHYS_PLOTLY_CONFIG
      );

      var nm = ["s", "p", "d", "f"];
      out.textContent =
        "Radial n=" + nR + " l=" + lR + " E=" + Number(Rr[3]).toFixed(4) + " Ry nodes=" + Rr[2] +
        " | Orbital n=" + nO + " l=" + lO + " " + nO + (nm[lO] || "?");
      if (dbg) dbg.textContent = "";
    } catch (e) {
      if (dbg) dbg.textContent = e.message;
    }
  }

  pyReady.then(function () {
    var b = document.getElementById("wf-pyout");
    if (b) {
      b.textContent = "Ready.";
      wfRunCalc();
    }
    var nr = document.getElementById("wf-nInput-rad");
    if (nr) wfClampLForN(document.getElementById("wf-lInput-rad"), document.getElementById("wf-lVal-rad"), parseInt(nr.value, 10));
    var no = document.getElementById("wf-nInput-orb");
    if (no) wfClampLForN(document.getElementById("wf-lInput-orb"), document.getElementById("wf-lVal-orb"), parseInt(no.value, 10));
  });
})();
