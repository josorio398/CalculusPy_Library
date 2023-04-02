from CalculusPy.RiemannSums import plot_riemann_sum
import pytest
from sympy import Symbol, pi,sin


x = Symbol("x")

def test_plot_riemann_sum():
    f = sin(x)
    a = 0
    b = pi
    n_max = 10
    method = 'left'
    plot_riemann_sum(f, a, b, n_max, method)

    assert plot_riemann_sum(f, a, b, n_max, method) == None


#test_plot_riemann_sum()