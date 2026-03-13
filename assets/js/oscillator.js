async function loadPy() {
  let pyodide;
  if (window.pyodideInstance) {
    pyodide = window.pyodideInstance;
  } else {
    pyodide = await loadPyodide();
    window.pyodideInstance = pyodide;
  }
  const pyCode = await fetch('/assets/py/oscillator.py').then(r => r.text());
  await pyodide.runPythonAsync(pyCode);
  document.getElementById("pyout").textContent = "Python ready — click Calculate";
  return pyodide;
}
let pyodideReady = loadPy();
async function runCalc() {
  const debug = document.getElementById("debug");
  const pyout = document.getElementById("pyout");
  try {
    const pyodide = await pyodideReady;
    const gamma = parseFloat(document.getElementById("gammaInput").value);
    debug.textContent = "Running Python...";
    const result = await pyodide.runPythonAsync(`run_calc(${gamma})`);
    const [t, y, ep, en] = result.toJs();
    Plotly.newPlot('pyplot', [
      { x: t, y: y,  name: 'x(t)',      type: 'scatter', line: { color: '#0077cc' } },
      { x: t, y: ep, name: '+envelope', type: 'scatter', line: { color: '#e05c00', dash: 'dash' } },
      { x: t, y: en, name: '-envelope', type: 'scatter', line: { color: '#e05c00', dash: 'dash' } }
    ], {
      title: `Damped Oscillator (γ=${gamma.toFixed(2)})`,
      xaxis: { title: 'Time' },
      yaxis: { title: 'Amplitude' },
      paper_bgcolor: '#f8f9fa',
      plot_bgcolor: '#f8f9fa'
    });
    const energy = (1 - Math.exp(-2 * gamma * t[t.length-1])) * 100;
    pyout.textContent = `γ = ${gamma.toFixed(2)} | Energy dissipated: ${energy.toFixed(1)}%`;
    debug.textContent = "";
  } catch(e) {
    debug.textContent = "Error: " + e.message;
  }
}