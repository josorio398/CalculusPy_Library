import numpy as np
import plotly.graph_objs as go
from sympy.utilities.lambdify import lambdify
from ipywidgets import interact



def plot_riemann_sum(f, a, b, n_max, method="right"):
    """
    Crea una visualización de las sumas de Riemann de una función dada f
    en el intervalo [a, b] con n rectángulos utilizando el método especificado.

    Parámetros:
    f (función de sympy): La función para la que se calcularán las sumas de Riemann.
    a (float): El límite inferior del intervalo de integración.
    b (float): El límite superior del intervalo de integración.
    method (str): El método de aproximación a utilizar ('left', 'right', o 'middle').
    n_max (int): El número máximo de rectángulos a utilizar.

    Retorna:
    None: muestra una visualización interactiva con deslizador para controlar n.
    """
    
    @interact(n=(1, n_max))
    def interactive_plot(n):
        # Convierte la función sympy en una función Python utilizando lambdify
        x = f.free_symbols.pop()
        f_np = lambdify(x,f,'numpy')

        # Crea una lista con n + 1 puntos equidistantes en el intervalo [a,b]
        x_vals = np.linspace(a,b,n+1)

        # Crea una lista con puntos suavizados para graficar la funcion
        x_smooth = np.linspace(a,b,100)
        y_smooth = [f_np(x) for x in x_smooth]

        # Calcula el ancho dx del rectangulo
        dx = (b-a)/n

        # Calcula las alturas y_vals del rectangulo
        if method == 'left':
            y_vals = [f_np(x_vals[i]) for i in range(n)]
        elif method == 'right':
            y_vals = [f_np(x_vals[i]) for i in range(1,n+1)]
        else:
            x_mid = [(x_vals[i]+x_vals[i+1])/2 for i in range(n)]
            y_vals = [f_np(x_mid[i]) for i in range(n)]

         # Calcula el area total bajo los rectangulos
        area = round(sum([y_vals[i]*dx for i in range(n)]),6)

         # Muestra el resultado en consola
        #print(f"El área aproximada bajo la curva es {area:.4f}")

        # Crea una figura Plotly y agrega los datos
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_smooth,y=y_smooth,
                                 name='f(x)',line=dict(color='blue')))
        for i in range(n):
            x0 = x_vals[i]
            x1 = x_vals[i+1]
            y0 = 0
            y1 = y_vals[i]
            fig.add_shape(type='rect',x0=x0,y0=y0,x1=x1,y1=y1,
                          line=dict(color='red'),fillcolor='red',opacity=0.4)
        
        fig.update_layout(title={'text':f'{method.capitalize()} Riemann Sums, Rectangles = {n}, Area = {area}','x':0.5,'y':0.9,},
                          xaxis_title='x',yaxis_title='y')
        
        fig.update_layout(width=800, height=600)

        fig.show()




