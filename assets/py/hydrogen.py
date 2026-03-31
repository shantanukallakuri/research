import math

def factorial(k):
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result


def laguerre_assoc(n, alpha, x):
    """
    Associated Laguerre polynomial L^alpha_n(x)
    via three-term recurrence. Stable for all n used here.
    """
    if n == 0:
        return 1.0
    if n == 1:
        return 1.0 + alpha - x
    L_prev2 = 1.0
    L_prev1 = 1.0 + alpha - x
    for k in range(2, n + 1):
        L_curr = ((2*k - 1 + alpha - x) * L_prev1 - (k - 1 + alpha) * L_prev2) / k
        L_prev2 = L_prev1
        L_prev1 = L_curr
    return L_curr


def legendre_assoc(l, m, x):
    """
    Associated Legendre polynomial P^m_l(x) for x in [-1,1].
    Uses standard upward recurrence in l for fixed m >= 0.
    Only m=0 needed for the xz-slice (phi=0) plots.
    """
    m = abs(m)
    # start from P^m_m
    pmm = 1.0
    if m > 0:
        somx2 = math.sqrt(max(0.0, 1.0 - x*x))
        fact = 1.0
        for _ in range(m):
            pmm *= -fact * somx2
            fact += 2.0
    if l == m:
        return pmm
    pmmp1 = x * (2*m + 1) * pmm
    if l == m + 1:
        return pmmp1
    for ll in range(m + 2, l + 1):
        pll = (x * (2*ll - 1) * pmmp1 - (ll + m - 1) * pmm) / (ll - m)
        pmm   = pmmp1
        pmmp1 = pll
    return pmmp1


def R_nl(n, l, r):
    """Radial wave function R_nl(r) at a single r value (a0 units)."""
    nr = n - l - 1
    if nr < 0:
        return 0.0

    rho = 2.0 * r / n

    # Standard hydrogen radial normalization (a0 = 1 units):
    # N = (2/n)^(3/2) * sqrt((n-l-1)! / (2n * (n+l)!))
    norm = (2.0 / n) ** 1.5 * math.sqrt(
        factorial(nr) / (2.0 * n * factorial(n + l))
    )

    return norm * math.exp(-rho / 2.0) * (rho ** l) * laguerre_assoc(nr, 2 * l + 1, rho)


def hydrogen_radial(n, l, plot_type="psi"):
    """
    Returns (r_vals, y_vals, node_count, energy) for the radial part.
    r grid extends to 4*n*(n+1) Bohr radii, 600 points.
    """
    r_max = max(4 * n * (n + 1), 30)
    num   = 600
    dr    = r_max / num
    r_vals = [dr * i for i in range(1, num + 1)]

    psi_vals = [R_nl(n, l, r) for r in r_vals]

    if plot_type == "prob":
        y_vals = [r**2 * p**2 for r, p in zip(r_vals, psi_vals)]
    else:
        y_vals = psi_vals

    return r_vals, y_vals, n - l - 1, -1.0 / n**2


def hydrogen_orbital_slice(n, l):
    """
    Compute |ψ_nlm(x,0,z)|^2 on a 2D xz grid (m=0 gives the
    standard textbook shapes: s sphere, p dumbbell, d cloverleaf).

    Returns (x_1d, z_1d, psi2_2d, orbital_label).
    psi2_2d[i][j] corresponds to z[i], x[j].
    """
    grid   = 80           # 80x80 is fast enough in Pyodide
    r_max  = max(4 * n * (n + 1), 30)
    coords = [r_max * (-1 + 2 * k / (grid - 1)) for k in range(grid)]  # -r_max..+r_max

    names = ['s', 'p', 'd', 'f']
    label = str(n) + (names[l] if l < len(names) else '?')

    psi2 = []
    for zi in coords:               # rows = z axis
        row = []
        for xi in coords:           # cols = x axis
            r = math.sqrt(xi**2 + zi**2)
            if r < 1e-8:
                row.append(0.0)
                continue
            # polar angle theta (from +z axis), phi=0 (xz plane)
            cos_theta = zi / r
            R = R_nl(n, l, r)
            # real spherical harmonic Y_l^0 (m=0) up to normalization
            # Y_l^0 = sqrt((2l+1)/4pi) * P_l^0(cos theta)
            norm_Y = math.sqrt((2*l + 1) / (4 * math.pi))
            Y      = norm_Y * legendre_assoc(l, 0, cos_theta)
            psi2_val = (R * Y) ** 2
            row.append(psi2_val)
        psi2.append(row)

    return coords, coords, psi2, label
