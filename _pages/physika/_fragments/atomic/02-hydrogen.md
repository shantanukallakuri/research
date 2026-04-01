### 1.2 Hydrogen

The hydrogen atom: electron $$\color{blue}{-e}$$, proton $$\color{blue}{+e}$$, Coulomb potential.

{% include sk/components/eqs.html
  id="eq-1.1"
  eq="\color{#000080}E_n = -\tfrac{13.6\text{ eV}}{n^2}"
  fontsize="1.00em"
  num="1.1"
  leader="....."
%}

{% include sk/components/eqs.html
  id="eq-1.2"
  eq="\color{#000080}V(r) = -\tfrac{e^2}{4\pi\epsilon_0 r}"
  fontsize="1.00em"
  num="1.2"
  leader="....."
%}

{% include sk/components/eqs.html
  id="eq-1.3"
  eq="\color{#000080}E_n = -\tfrac{13.6\text{ eV}}{n^2}"
  fontsize="1.00em"
  num="1.3"
  leader="....."
%}

Energy scales as $$1/n^2$$ ([eq. 1.1](#eq-1.1)).

<details class="topic-code-fold">
  <summary>Code</summary>
  {% highlight python %}
  import math
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
  {% endhighlight %}
</details>

{% include sk/components/eqs.html
  id="eq-1.4"
  eq="\color{#000080}\psi_{n\ell m} = R_{n\ell}(r)\,Y_\ell^m(\theta,\phi)"
  fontsize="1.00em"
  num="1.4"
  leader="....."
%}

{% include sk/components/eqs.html
  id="eq-1.5"
  eq="\color{#000080}\left[ -\tfrac{\hbar^2}{2m_e}\nabla^2 + V(r) \right] \psi = E\psi"
  fontsize="1.00em"
  num="1.5"
  leader="....."
%}
