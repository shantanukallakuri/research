import math

def run_calc(gamma):
    n = 300
    omega_d = math.sqrt(max(1.0 - gamma**2, 1e-10))
    t  = [i * 0.1 for i in range(n)]
    y  = [math.exp(-gamma * ti) * math.cos(omega_d * ti) for ti in t]
    ep = [ math.exp(-gamma * ti) for ti in t]
    en = [-math.exp(-gamma * ti) for ti in t]
    return t, y, ep, en