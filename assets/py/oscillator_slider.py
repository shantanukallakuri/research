import math

def run_calc_slider(gamma):
    n = 300
    t = [i * 0.1 for i in range(n)]

    if gamma < 1.0:
        # underdamped
        omega_d = math.sqrt(1.0 - gamma**2)
        y = [math.exp(-gamma * ti) * math.cos(omega_d * ti) for ti in t]
    elif abs(gamma - 1.0) < 1e-9:
        # critically damped (simple normalized form)
        y = [math.exp(-ti) * (1.0 + ti) for ti in t]
    else:
        # overdamped
        s = math.sqrt(gamma**2 - 1.0)
        y = [math.exp(-gamma * ti) * math.cosh(s * ti) for ti in t]

    ep = [math.exp(-gamma * ti) for ti in t]
    en = [-math.exp(-gamma * ti) for ti in t]
    return t, y, ep, en