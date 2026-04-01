"""Bohr demo — Pyodide; energies vs n (stub)."""

def run_bohr_plot(n_max=5):
    n_max = int(n_max)
    n_max = max(1, min(n_max, 20))
    ns = list(range(1, n_max + 1))
    E_eV = [-13.6 / (n * n) for n in ns]
    z = [0.0] * len(ns)
    x_range = (0.5, float(n_max) + 0.5)
    y_range = (-16.0, 2.0)
    x_title = "n"
    y_title = "Energy (eV)"
    return ns, E_eV, z, z, x_range, y_range, x_title, y_title
