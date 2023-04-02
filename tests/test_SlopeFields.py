import pytest
from CalculusPy.SlopeFields import *
from sympy import symbols,Function

def test_calcPointsFromPointAndSlope():
    x, y = 0, 0
    slope = 1
    length = 2
    points = calcPointsFromPointAndSlope(x, y, slope, length)
    assert points == [(-0.7071067811865475, -0.7071067811865475), (0.7071067811865475,0.7071067811865475)]

def test_slope_fields():
    x = symbols('x', real=True)
    y = Function('y', real=True)
    dydx = x**2 + y(x)
    slope_fields(dydx)
    assert slope_fields(dydx) == None

#test_calcPointsFromPointAndSlope()
#test_slope_fields()