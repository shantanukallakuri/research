let wfDebounceTimer = null;

async function wfLoadPy() {
  let pyodide;
  if (window.pyodideInstance) {
    pyodide = window.pyodideInstance;
  } else {
    pyodide = await loadPyodide();
    window.pyodideInstance = pyodide;
  }
  const pyCode = await fetch('/assets/py/hydrogen.py').then(r => r.text());
  await pyodide.runPythonAsync(pyCode);
  document.getElementById("wf-pyout").textContent = "Python ready — drag the sliders";
  wfRunCalc();
  return pyodide;
}

let wfPyodideReady = wfLoadPy();

// called when n slider moves — update n display, clamp l max, then plot
function wfOnN(val) {
  const n = parseInt(val);
  document.getElementById("wf-nVal").textContent = n;

  // update l slider max to n-1
  const lSlider = document.getElementById("wf-lInput");
  lSlider.max = n - 1;

  // if current l exceeds new max, pull it down
  const l = parseInt(lSlider.value);
  if (l > n - 1) {
    lSlider.value = n - 1;
    document.getElementById("wf-lVal").textContent = n - 1;
  }

  wfDebouncePlot();
}

// called when l slider moves — just update display and plot
function wfOnL(val) {
  document.getElementById("wf-lVal").textContent = parseInt(val);
  wfDebouncePlot();
}

function wfDebouncePlot() {
  clearTimeout(wfDebounceTimer);
  wfDebounceTimer = setTimeout(wfRunCalc, 80);
}

async function wfRunCalc() {
  const debug = document.getElementById("wf-debug");
  const pyout = document.getElementById("wf-pyout");
  try {
    const pyodide  = await wfPyodideReady;
    const n        = parseInt(document.getElementById("wf-nInput").value);
    const l        = parseInt(document.getElementById("wf-lInput").value);
    const plotType = document.querySelector('input[name="wf-plottype"]:checked').value;

    // --- radial plot ---
    const result = await pyodide.runPythonAsync(
      `hydrogen_radial(${n}, ${l}, "${plotType}")`
    );
    const [r, y, nodeCount, energy] = result.toJs();

    const isProb  = plotType === "prob";
    const yLabel  = isProb ? "r²|ψ(r)|²" : "ψ(r)";
    const color   = isProb ? "#9333ea" : "#0077cc";
    const radTitle = `n=${n}, ℓ=${l}  —  ${isProb ? "Radial Probability Density" : "Radial Wave Function"}`;

    const radTraces = [
      { x: r, y: y, name: yLabel, type: 'scatter',
        line: { color: color, width: 2 } }
    ];
    if (!isProb) {
      radTraces.push({
        x: [r[0], r[r.length-1]], y: [0, 0],
        type: 'scatter', mode: 'lines',
        line: { color: '#ccc', width: 1, dash: 'dot' },
        showlegend: false
      });
    }

    Plotly.react('wf-pyplot', radTraces, {
      title: radTitle,
      xaxis: { title: 'r / a₀' },
      yaxis: { title: yLabel },
      paper_bgcolor: '#f8f9fa',
      plot_bgcolor:  '#f8f9fa',
      margin: { t: 45, l: 50, r: 20, b: 50 }
    });

    // --- orbital shape plot ---
    const orbResult = await pyodide.runPythonAsync(
      `hydrogen_orbital_slice(${n}, ${l})`
    );
    const [xGrid, zGrid, psiGrid, orbLabel] = orbResult.toJs();

    // flatten nested JS maps from .toJs() into plain 2D arrays
    const xArr = Array.from(xGrid);
    const zArr = Array.from(zGrid);
    const psiArr = Array.from(psiGrid).map(row => Array.from(row));

    Plotly.react('wf-orbital', [{
      x: xArr, z: zArr,
      z: psiArr,
      type: 'heatmap',
      colorscale: 'RdBu',
      zmid: 0,
      colorbar: { title: '|ψ|²', thickness: 12 }
    }], {
      title: `${orbLabel} orbital  (xz slice)`,
      xaxis: { title: 'x / a₀', scaleanchor: 'y' },
      yaxis: { title: 'z / a₀' },
      paper_bgcolor: '#f8f9fa',
      plot_bgcolor:  '#f8f9fa',
      margin: { t: 45, l: 50, r: 60, b: 50 }
    });

    const names   = ['s','p','d','f'];
    const orbName = (n + (names[l] || '?'));
    const nodeStr = nodeCount === 1 ? "1 radial node" : `${nodeCount} radial nodes`;
    pyout.textContent = `${orbName} orbital | E = ${energy.toFixed(4)} Ry | ${nodeStr} | ℓ=${l} → ${names[l] || '?'} symmetry`;
    debug.textContent = "";

  } catch(e) {
    debug.textContent = "Error: " + e.message;
  }
}