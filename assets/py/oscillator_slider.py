import math

# Fixed axes: edit OSCILLATOR_* only
OSCILLATOR_X_RANGE = (0.0, 60.0)
OSCILLATOR_Y_RANGE = (-1.25, 1.25)
OSCILLATOR_X_AXIS_TITLE = "Time (dimensionless), t"
OSCILLATOR_Y_AXIS_TITLE = "Displacement (dimensionless), x"


def run_calc_slider(gamma, t_max=30.0):
    n = 300
    dt = t_max / max(n - 1, 1)
    t = [i * dt for i in range(n)]
    if gamma < 1.0:
        wd = math.sqrt(1.0 - gamma**2)
        y = [math.exp(-gamma * ti) * math.cos(wd * ti) for ti in t]
    elif abs(gamma - 1.0) < 1e-9:
        y = [math.exp(-ti) * (1.0 + ti) for ti in t]
    else:
        s = math.sqrt(gamma**2 - 1.0)
        y = [math.exp(-gamma * ti) * math.cosh(s * ti) for ti in t]
    ep = [math.exp(-gamma * ti) for ti in t]
    en = [-math.exp(-gamma * ti) for ti in t]
    return t, y, ep, en, OSCILLATOR_X_RANGE, OSCILLATOR_Y_RANGE, OSCILLATOR_X_AXIS_TITLE, OSCILLATOR_Y_AXIS_TITLE
