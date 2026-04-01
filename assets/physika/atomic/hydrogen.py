import math

RADIAL_X_RANGE = (0.0, 55.0)
RADIAL_Y_RANGE_PSI = (-0.55, 0.55)
RADIAL_Y_RANGE_PROB = (0.0, 0.20)
RADIAL_X_AXIS_TITLE = "Radius (Bohr radii), r"
RADIAL_Y_AXIS_TITLE_PSI = "Radial factor (a0^{-3/2}), R_nl"
RADIAL_Y_AXIS_TITLE_PROB = "Radial density (1/a0), r^2|R_nl|^2"
ORBITAL_AXIS_RANGE = (-52.0, 52.0)
ORBITAL_X_AXIS_TITLE = "Position (Bohr radii), x"
ORBITAL_Z_AXIS_TITLE = "Position (Bohr radii), z"


def laguerre_assoc(n, alpha, x):
    if n == 0:
        return 1.0
    if n == 1:
        return 1.0 + alpha - x
    L2, L1 = 1.0, 1.0 + alpha - x
    for k in range(2, n + 1):
        L_curr = ((2 * k - 1 + alpha - x) * L1 - (k - 1 + alpha) * L2) / k
        L2, L1 = L1, L_curr
    return L1


def legendre_assoc(l, m, x):
    m = abs(m)
    pmm = 1.0
    if m > 0:
        somx2 = math.sqrt(max(0.0, 1.0 - x * x))
        fact = 1.0
        for _ in range(m):
            pmm *= -fact * somx2
            fact += 2.0
    if l == m:
        return pmm
    pmmp1 = x * (2 * m + 1) * pmm
    if l == m + 1:
        return pmmp1
    for ll in range(m + 2, l + 1):
        pll = (x * (2 * ll - 1) * pmmp1 - (ll + m - 1) * pmm) / (ll - m)
        pmm = pmmp1
        pmmp1 = pll
    return pmmp1


def R_nl(n, l, r):
    nr = n - l - 1
    if nr < 0:
        return 0.0
    rho = 2.0 * r / n
    norm = (2.0 / n) ** 1.5 * math.sqrt(math.factorial(nr) / (2.0 * n * math.factorial(n + l)))
    return norm * math.exp(-rho / 2.0) * (rho ** l) * laguerre_assoc(nr, 2 * l + 1, rho)


def hydrogen_radial(n, l, plot_type="psi"):
    r_max = max(4 * n * (n + 1), 30)
    num = 600
    dr = r_max / num
    r_vals = [dr * i for i in range(1, num + 1)]
    psi_vals = [R_nl(n, l, r) for r in r_vals]
    if plot_type == "prob":
        y_vals = [r**2 * p**2 for r, p in zip(r_vals, psi_vals)]
    else:
        y_vals = psi_vals
    return (
        r_vals,
        y_vals,
        n - l - 1,
        -1.0 / n**2,
        RADIAL_X_RANGE,
        RADIAL_Y_RANGE_PSI,
        RADIAL_Y_RANGE_PROB,
        RADIAL_X_AXIS_TITLE,
        RADIAL_Y_AXIS_TITLE_PSI,
        RADIAL_Y_AXIS_TITLE_PROB,
    )


def hydrogen_orbital_slice(n, l):
    grid = 80
    r_max = max(4 * n * (n + 1), 30)
    coords = [r_max * (-1 + 2 * k / (grid - 1)) for k in range(grid)]
    names = ["s", "p", "d", "f"]
    label = str(n) + (names[l] if l < len(names) else "?")
    psi2 = []
    for zi in coords:
        row = []
        for xi in coords:
            r = math.sqrt(xi**2 + zi**2)
            if r < 1e-8:
                row.append(0.0)
                continue
            cos_theta = zi / r
            R = R_nl(n, l, r)
            norm_Y = math.sqrt((2 * l + 1) / (4 * math.pi))
            Y = norm_Y * legendre_assoc(l, 0, cos_theta)
            row.append((R * Y) ** 2)
        psi2.append(row)
    return coords, coords, psi2, label, ORBITAL_AXIS_RANGE, ORBITAL_X_AXIS_TITLE, ORBITAL_Z_AXIS_TITLE
