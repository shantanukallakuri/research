### 2.2 Hydrogen demos

<div class="demo-section physics-demos">
<div class="physics-panel">
<div class="physics-plot-aligned">
<div class="physics-plot-column">
<div class="physics-plot-formula">
\[
\text{Radial:}\quad R_{n\ell}(r),\quad r^2|R_{n\ell}(r)|^2
\]
</div>
<div class="physics-plot-frame"><div id="wf-pyplot" class="physics-plot-inner" style="height:300px;"></div></div>
<div class="physics-slider-stack">
<div class="physics-slider-row">
<div class="physics-slider-caption">\(n\), value = <span id="wf-nVal-rad" class="physics-val">1</span></div>
<input id="wf-nInput-rad" class="physics-hslider" type="range" min="1" max="4" step="1" value="1" oninput="wfOnN('rad',this.value)">
</div>
<div class="physics-slider-row">
<div class="physics-slider-caption">ℓ, value = <span id="wf-lVal-rad" class="physics-val">0</span></div>
<input id="wf-lInput-rad" class="physics-hslider" type="range" min="0" max="3" step="1" value="0" oninput="wfOnL('rad',this.value)">
</div>
</div>
</div>
<div class="physics-controls-beside">
<div class="physics-wf-radios">
<label><input type="radio" name="wf-plottype" value="psi" checked onchange="wfDebouncePlot()"> ψ(r)</label>
<label><input type="radio" name="wf-plottype" value="prob" onchange="wfDebouncePlot()"> r²|ψ|²</label>
</div>
</div>
</div>
</div>
<div class="physics-panel">
<div class="physics-plot-aligned">
<div class="physics-plot-column">
<div class="physics-plot-formula">
\[
\text{Orbital slice }(xz)\text{:}\quad |\psi_{n\ell}(x,z)|^2
\]
</div>
<div class="physics-plot-frame"><div id="wf-orbital" class="physics-plot-inner" style="height:300px;"></div></div>
<div class="physics-slider-stack">
<div class="physics-slider-row">
<div class="physics-slider-caption">\(n\), value = <span id="wf-nVal-orb" class="physics-val">1</span></div>
<input id="wf-nInput-orb" class="physics-hslider" type="range" min="1" max="4" step="1" value="1" oninput="wfOnN('orb',this.value)">
</div>
<div class="physics-slider-row">
<div class="physics-slider-caption">ℓ, value = <span id="wf-lVal-orb" class="physics-val">0</span></div>
<input id="wf-lInput-orb" class="physics-hslider" type="range" min="0" max="3" step="1" value="0" oninput="wfOnL('orb',this.value)">
</div>
</div>
</div>
</div>
</div>
<div id="wf-pyout" class="physics-status physics-status--spaced">Loading…</div>
<div id="wf-debug" class="physics-debug"></div>
</div>
