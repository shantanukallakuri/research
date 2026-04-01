#### Damped oscillator

<div class="demo-section physics-demos">
<div class="physics-plot-aligned">
<div class="physics-plot-column">
<div class="physics-plot-formula">
\[
x(t)=e^{-\gamma t}(A\cos\omega_d t+B\sin\omega_d t),\quad \omega_d=\sqrt{1-\gamma^2}\ (\gamma&lt;1)
\]
</div>
<div class="physics-plot-frame"><div id="slider-pyplot" class="physics-plot-inner" style="height:280px;"></div></div>
<div class="physics-slider-stack">
<div class="physics-slider-row">
<div class="physics-slider-caption">\(t_{\mathrm{end}}\), value = <span id="slider-tmaxVal" class="physics-val">30.0</span></div>
<input id="slider-tmaxInput" class="physics-hslider" type="range" min="5" max="60" step="0.5" value="30" oninput="document.getElementById('slider-tmaxVal').textContent=parseFloat(this.value).toFixed(1); sliderDebouncePlot();">
</div>
<div class="physics-slider-row">
<div class="physics-slider-caption">γ, value = <span id="slider-gammaVal" class="physics-val">0.10</span></div>
<input id="slider-gammaInput" class="physics-hslider" type="range" min="0.01" max="1.99" step="0.01" value="0.10" oninput="document.getElementById('slider-gammaVal').textContent=parseFloat(this.value).toFixed(2); sliderDebouncePlot();">
</div>
</div>
</div>
</div>
<div id="slider-pyout" class="physics-status">Loading…</div>
<div id="slider-debug" class="physics-debug"></div>
</div>
