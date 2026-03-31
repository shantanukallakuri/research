<!--
  SAMPLE ONLY — not a Jekyll page by itself.
  Copy the HTML + script block into a real page that already includes:
    {% include sk/head/plotly_head.html %}
    {% include sk/head/pyodide_head.html %}
-->

### Ticker sample (copy into your page)

**Roles:** `.md` = text + HTML shell · `model.py` = numbers · `ticker.js` = Pyodide load + time loop + Plotly

<div class="demo-section">
  <p style="font-size:0.9rem;">Index <code>i</code>: <span id="ticker-i">0</span>
    &nbsp;|&nbsp;
    <button type="button" onclick="tickerPause()">Pause</button>
    <button type="button" onclick="tickerPlay()">Play</button>
  </p>
  <div id="ticker-plot" style="width:100%; max-width:560px; height:280px;"></div>
  <p id="ticker-status" style="font-size:0.85rem; color:#555;">Loading…</p>
</div>

Paste this **after** the HTML block (same page as the includes for Plotly + Pyodide):

    <script>
      window.__TICKER_MODEL_PY__ = "{{ '/assets/samples/pyodide-ticker-example/model.py' | relative_url }}";
    </script>
    <script src="{{ '/assets/samples/pyodide-ticker-example/ticker.js' | relative_url }}"></script>

(Use a real layout with Plotly + Pyodide in `<head>`, same as `learning/physics`.)
