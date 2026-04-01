### 1.1 The Bohr model

<div class="demo-section physics-demos">
<div class="physics-plot-aligned">
<div class="physics-plot-column">
<div class="physics-plot-formula">\[ E_n = -\dfrac{13.6\ \mathrm{eV}}{n^2}\quad (\text{hydrogen-like stub}) \]</div>
<div class="physics-plot-frame"><div id="bohr-pyplot" class="physics-plot-inner" style="height:280px;"></div></div>
<div class="physics-slider-stack">
<div class="physics-slider-row">
<div class="physics-slider-caption">\(n_{\max}\), value = <span id="bohr-nmaxVal" class="physics-val">5</span></div>
<input id="bohr-nmaxInput" class="physics-hslider" type="range" min="1" max="20" step="1" value="5" oninput="document.getElementById('bohr-nmaxVal').textContent=parseInt(this.value,10); bohrDebouncePlot();">
</div>
</div>
</div>
</div>
<div id="bohr-pyout" class="physics-status">Loading…</div>
<div id="bohr-debug" class="physics-debug"></div>
</div>
