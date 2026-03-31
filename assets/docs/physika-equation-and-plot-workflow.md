# Physika: equations, interactive plots, and layout conventions

Applies to `_pages/physika.md`, `assets/js/learning-physics.js`, `assets/py/*.py`, and `_sass/_custom.scss` (`.topic-article .page__content` physics blocks).

---

## Aligned block (`physics-plot-aligned` + `physics-plot-column`)

Wrap each interactive figure in **`physics-plot-aligned`**: an **`inline-flex`** row so the block **shrink-wraps** — **`physics-plot-column`** (equation + plot + sliders) and optional **`physics-controls-beside`** sit **next to each other** as one group, left-aligned in the article (no huge gap pushing readouts to the far right). Plot column width is capped with **`max-width: 100%`** (see `_custom.scss`, default **`35rem`**).

All parameter sliders are **horizontal**, **below the plot**, **full width of the column**, and **stacked** in a **`physics-slider-stack`**. Each **`physics-slider-row`** has a centered **`physics-slider-caption`** line: parameter label, comma, **`value =`** and a **`<span id="…" class="physics-val">`** for the live value, then the range input on the next line.

```html
<div class="demo-section physics-demos">
<div class="physics-plot-aligned">
<div class="physics-plot-column">
<div class="physics-plot-formula">\[ \text{Your LaTeX here} \]</div>
<div class="physics-plot-frame"><div id="my-plot" class="physics-plot-inner"></div></div>
<div class="physics-slider-stack">
  <div class="physics-slider-row">
    <div class="physics-slider-caption">\(t_{\mathrm{end}}\), value = <span id="my-tmaxVal" class="physics-val">30.0</span></div>
    <input class="physics-hslider" type="range" …>
  </div>
  <!-- more rows -->
</div>
</div>
<div class="physics-controls-beside">…</div>
</div>
</div>
```

To change the plot stack width, edit **`width`** / **`max-width`** on `.physics-plot-column` in `_sass/_custom.scss` (default **`35rem`**).

- Use **`\[` … `\]`** so MathJax typesets in HTML (same delimiters as elsewhere with MathJax 3).
- In raw HTML/Jekyll, escape `<` as **`&lt;`** when it would otherwise be parsed as a tag (e.g. `\gamma&lt;1`).
- **Do not** duplicate the same display equation as a separate `$$` block immediately above the demo unless you want it in prose twice; the title line is the copy next to the figure.
- **Plotly** chart titles are left **empty** in `learning-physics.js` (`title: ""`) so the equation in the page is the single prominent title; top margin is reduced (`margin.t` ≈ 12).

---

## Control layout: beside vs below

| Location | What goes here |
|----------|----------------|
| **`physics-controls-beside`** (right of plot) | **Non-slider** choices (e.g. ψ / r²\|ψ\|² radios). Optional extra readouts if you keep them out of the slider stack. |
| **`physics-slider-stack`** (inside `physics-plot-column`, under the plot) | One or more **`physics-slider-row`** blocks: **`physics-slider-caption`** (label + `value =` + span), then the horizontal range. |

CSS classes live under `.topic-article .page__content` in `_sass/_custom.scss`.

---

## Numbered equation rows (`sk/components/eqs.html`)

Unchanged: use `{% include sk/components/eqs.html %}` with `id`, `eq`, `num`, optional `fontsize`, `leader`. Spacing uses `.sk-eqs-row`.

---

## Python + Pyodide

- Scripts listed in `window.__PHYSICS_PY_URLS__` at the bottom of the page load into Pyodide before plotting.
- Entry functions must match `learning-physics.js` (e.g. `run_calc_slider(gamma)`, `hydrogen_radial(...)`, `hydrogen_orbital_slice(...)`).

---

## New demo (mydemo) templates

Private templates under `private-notes/mydemo/` mirror the same HTML/CSS pattern (`physics-plot-formula`, beside, `physics-slider-stack`). Copy `mydemo.py` to `assets/py/`, merge the JS snippet into `learning-physics.js`, register the URL, and add `mydemoRunCalc()` to `pyReady.then` when `#mydemo-pyout` exists.

---

## Files

| Role | Path |
|------|------|
| Page | `_pages/physika.md` |
| MathJax | `_includes/sk/head/math_head.html` |
| Plot wiring | `assets/js/learning-physics.js` |
| Oscillator | `assets/py/oscillator_slider.py` |
| Hydrogen | `assets/py/hydrogen.py` |
| Physics demo styles | `_sass/_custom.scss` (search `physics-`) |
