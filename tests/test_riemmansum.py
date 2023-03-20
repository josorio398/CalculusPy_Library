from CalculusPy.RiemannSums import plot_riemann_sum
import pytest
from sympy import * 


x = Symbol("x")

def test_plot_riemann_sum():
    f = sin(x)
    a = 0
    b = pi
    n_max = 10
    method = 'left'
    plot_riemann_sum(f, a, b, n_max, method)

    assert plot_riemann_sum(f, 0, 2, 10, method="left") == None
    assert plot_riemann_sum(f, 0, 2, 20, method="right") == None
    assert plot_riemann_sum(f, 0, 2, 30, method="middle") == None

test_plot_riemann_sum()