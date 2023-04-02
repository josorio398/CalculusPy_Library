from sympy import symbols, Eq
from sympy.printing.mathml import mathml
from IPython.display import display, Math

x, y = symbols('x y')
eq = Eq(x**2 + y**2, 1)

# Convertir la ecuación a MathML
eq_mathml = mathml(eq)

# Agregar etiquetas MathML para que sea HTML válido
eq_html = f"<math xmlns='http://www.w3.org/1998/Math/MathML'>{eq_mathml}</math>"

# Mostrar la ecuación en HTML
print(display(Math(eq_html)))