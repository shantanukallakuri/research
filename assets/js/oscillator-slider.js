// Global variable to store the timer ID for debouncing slider movements
let sliderDebounceTimer = null;

/**
 * Initializes Pyodide, loads the Python environment, 
 * and fetches the required calculation script.
 */
async function sliderLoadPy() {
  let pyodide;
  // Check if Pyodide is already loaded to avoid redundant initialization
  if (window.pyodideInstance) {
    pyodide = window.pyodideInstance;
  } else {
    // Load the Pyodide runtime and store it in a global window property
    pyodide = await loadPyodide();
    window.pyodideInstance = pyodide;
  }

  // Fetch the external Python logic from the assets folder
  const pyCode = await fetch('/assets/py/oscillator_slider.py').then(r => r.text());
  
  // Execute the Python code to define functions like run_calc_slider()
  await pyodide.runPythonAsync(pyCode);
  
  // Update UI to let the user know the environment is ready
  document.getElementById("slider-pyout").textContent = "Python ready — drag the slider";
  
  // Run an initial calculation so the graph isn't empty on load
  sliderRunCalc();
  return pyodide;
}

// Start loading Python immediately; this promise is used by sliderRunCalc
let sliderPyodideReady = sliderLoadPy();

/**
 * Prevents the calculation from running too many times per second
 * while the user is actively dragging the slider.
 */
window.sliderDebouncePlot = function() {
  clearTimeout(sliderDebounceTimer);
  // Only execute the calculation after the user stops moving for 80ms
  sliderDebounceTimer = setTimeout(sliderRunCalc, 80);
};

/**
 * The main bridge function: pulls data from the UI, runs it through Python,
 * and renders the resulting data using Plotly.
 */
async function sliderRunCalc() {
  const debug = document.getElementById("slider-debug");
  const pyout = document.getElementById("slider-pyout");
  
  try {
    // Ensure Python is fully loaded before proceeding
    const pyodide = await sliderPyodideReady;
    
    // Get the damping coefficient (gamma) from the HTML slider
    const gamma = parseFloat(document.getElementById("slider-gammaInput").value);
    
    // Execute the Python function and pass the gamma value
    const result = await pyodide.runPythonAsync(`run_calc_slider(${gamma})`);
    const converted = result.toJs();
    result.destroy?.();

    // Convert Python lists/arrays into a JavaScript array of arrays [t, y, ep, en]
    const [t, y, ep, en] = converted;
    
    // Use Plotly.react for an efficient "partial update" of the graph
    Plotly.react('slider-pyplot', [
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

    // Calculate energy dissipation percentage: (1 - e^(-2*gamma*t)) * 100
    const energy = (1 - Math.exp(-2 * gamma * t[t.length-1])) * 100;
    
    // Update the text display with the current status
    pyout.textContent = `γ = ${gamma.toFixed(2)} | Energy dissipated: ${energy.toFixed(1)}%`;
    debug.textContent = ""; // Clear any previous errors
  } catch(e) {
    // Catch and display any Python or JavaScript errors in the UI
    debug.textContent = "Error: " + e.message;
  }
}