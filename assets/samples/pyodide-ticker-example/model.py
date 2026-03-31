# Sample: pure math — no DOM, no Plotly.
# JS calls sine_series() once, then animates by index in the browser.

import math


def sine_series(n_points=400, t_max=8.0):
    """Return full (t, y) arrays for y = sin(t)."""
    if n_points < 2:
        n_points = 2
    dt = t_max / (n_points - 1)
    t = [i * dt for i in range(n_points)]
    y = [math.sin(ti) for ti in t]
    return t, y
