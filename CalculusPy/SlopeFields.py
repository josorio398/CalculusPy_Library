import numpy as np
import plotly.graph_objects as go
from sympy import *

def slope_fields(dydx, n=25, lengthSlope=0.2, xMin=-5, xMax=5, yMin=-5, yMax=5, ics=None):
    x = symbols('x', real=True)
    y = Function('y', real=True)
    dydx_func = lambdify((x, y(x)), dydx, 'numpy')

    def calcPointsFromPointAndSlope(x, y, slope, length):
        deltaX = length / np.sqrt(1 + slope**2)
        deltaY = slope * deltaX
        return [(x - deltaX/2, y - deltaY/2), (x + deltaX/2, y + deltaY/2)]

    x_vals = np.linspace(xMin, xMax, n)
    y_vals = np.linspace(yMin, yMax, n)

    fig = go.Figure()

    for x_val in x_vals:
        for y_val in y_vals:
            slope = dydx_func(x_val, y_val)
            if np.isfinite(slope):
                line_points = calcPointsFromPointAndSlope(x_val, y_val, slope, lengthSlope)
                x_line = [point[0] for point in line_points]
                y_line = [point[1] for point in line_points]
                fig.add_trace(go.Scatter(x=x_line, y=y_line, mode='lines', showlegend=False, line=dict(color='black', width=1)))

    if ics != None:
        name_x,name_y = tuple(ics.items())[0][0], tuple(ics.items())[0][1]
        edo = Eq(diff(y(x),x),dydx)
        sol = dsolve(edo, ics=ics)
        # Lambdify the solution using numpy
        sol_lambdified = lambdify(x, sol.rhs, 'numpy')

        x_vals = np.linspace(xMin, xMax, 1000)

        # Calculate the y values using the lambdified solution
        with np.errstate(invalid='ignore', divide='ignore'):
            y_vals = np.array([sol_lambdified(xi) for xi in x_vals])

        # Remove any invalid values
        valid_indices = np.isfinite(y_vals)
        x_vals = x_vals[valid_indices]
        y_vals = y_vals[valid_indices]

        # Suppress the warnings
        np.warnings.filterwarnings('ignore')


        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Particular Solution,  ' + str(name_x) + "="+str(name_y), line=dict(color='blue', width=2)))

    fig.update_layout(
        title='<b>Slope Field</b>',  # Encerrar el título entre etiquetas <b> para negrita
        title_font=dict(size=24, family='Arial'), 
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(range=[xMin, xMax]),
        yaxis=dict(range=[yMin, yMax]),
        legend_title="dy/dx = "+str(dydx).replace('*', '').replace('(x)',""),
        plot_bgcolor='white',
        width=800,  # Establecer el ancho de la gráfica
        height=600  # Establecer la altura de la gráfica

    )

    fig.show()