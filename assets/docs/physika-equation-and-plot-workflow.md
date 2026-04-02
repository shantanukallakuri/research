# Physika: equations, interactive plots, and layout conventions

Applies to `_pages/physika.md`, `_pages/physika/_fragments/**/*.md`, `assets/js/physika/*.js`, and `_sass/_custom.scss` (`.topic-article .page__content` physics blocks).

---

## Multi-file Physika content (single URL)

The published page is still **`/physika/`** only (`_pages/physika.md`). Body copy for each subsection lives in **`_pages/physika/_fragments/<section>/`**, e.g. `_fragments/atomic/01-bohr-model.md`. Each fragment **starts with the subsection heading** (`###` or `####`) so the sticky TOC and anchors work.

To add a subsection: create a new `.md` file under `_pages/physika/_fragments/` (e.g. `atomic/05-topic.md`), then add one **`include_relative`** line to `physika.md` in the order you want. The path is **relative to** `_pages/physika.md`, for example: `physika/_fragments/atomic/05-topic.md`. At the bottom of `physika.md`, **`physika-runtime.js`** loads first, then one **combined JS+Python script per demo** (Plotly + Pyodide heads stay in front matter as today).

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
- **Plotly** chart titles are left **empty** in each demo script (`title: ""`) so the equation in the page is the single prominent title; top margin is reduced (`margin.t` ≈ 12).

---

## Control layout: beside vs below

| Location | What goes here |
|----------|----------------|
| **`physics-controls-beside`** (right of plot) | **Non-slider** choices (e.g. ψ / r²\|ψ\|² radios). Optional extra readouts if you keep them out of the slider stack. |
| **`physics-slider-stack`** (inside `physics-plot-column`, under the plot) | One or more **`physics-slider-row`** blocks: **`physics-slider-caption`** (label + `value =` + span), then the horizontal range. |

CSS classes live under `.topic-article .page__content` in `_sass/_custom.scss`.

---

## Numbered equation rows (`sk/components/eqs.html`)

Unchanged: use the Liquid **`include`** tag for `sk/components/eqs.html` with `id`, `eq`, `num`, optional `fontsize`, `leader`. Spacing uses `.sk-eqs-row`.

---

## Python + Pyodide (one file per demo)

- **`assets/js/physika/physika-runtime.js`** — Shared only: single Pyodide instance (`ensurePyodide`), **`loadPythonModule(source)`** (embed → `runPythonAsync`), **`onPyodideError(pyReady, debugElementId)`**, **`debounce`**, **`physLayout`**, **`PHYS_PLOTLY_CONFIG`** (**`window.PhysikaRuntime`**). MathJax / Plotly / Pyodide **script tags** are not in these files; they load once from **`physika.md`** via **`sk/head/math_head.html`**, **`plotly_head.html`**, **`pyodide_head.html`**.
- **`demo-bohr.js`**, **`demo-oscillator.js`**, **`demo-hydrogen.js`** — Each file embeds that demo’s Python as a string and runs **`pyodide.runPythonAsync`** when its bundle loads (no `fetch` of `.py` files). Plotly IDs and Python entry points live together in that file.

Entry function names must match the **`runPythonAsync(...)`** calls in the same file (e.g. `run_calc_slider`, `hydrogen_radial`, `hydrogen_orbital_slice`).

To add a new demo: add **`demo-<name>.js`** (copy a small existing demo as a template), include it in **`physika.md`** after **`physika-runtime.js`**, and add the HTML block in a fragment.

---

## New demo (mydemo) templates

Private templates under `private-notes/mydemo/` mirror the **damped oscillator** block on Physika: `physics-plot-formula`, `physics-plot-frame`, stacked **`physics-slider-stack`** (caption + horizontal ranges), then **`physics-status`** / **`physics-debug`**. Add a new **`demo-mydemo.js`** (embedded Python string + **`mydemoRunCalc`** + **`pyReady.then`**), include it after **`physika-runtime.js`** in **`physika.md`**, starting from **`mydemo-learning-physics-snippet.js`** adapted to use **`window.PhysikaRuntime`**. See `private-notes/mydemo/README.md`.

---

## Files

| Role | Path |
|------|------|
| Page shell | `_pages/physika.md` (includes fragments; sticky TOC uses headings in fragments) |
| Subsection fragments | `_pages/physika/_fragments/atomic/*.md` (add more folders under `_fragments/` as needed) |
| MathJax | `_includes/sk/head/math_head.html` |
| Shared Pyodide + Plotly helpers | `assets/js/physika/physika-runtime.js` |
| Bohr demo (JS + embedded Python) | `assets/js/physika/demo-bohr.js` |
| Oscillator demo (JS + embedded Python) | `assets/js/physika/demo-oscillator.js` |
| Hydrogen demos (JS + embedded Python) | `assets/js/physika/demo-hydrogen.js` |
| Physics demo styles | `_sass/_custom.scss` (search `physics-`) |
