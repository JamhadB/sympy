import sympy as sp

t = sp.symbols('t')
x = sp.Function('x')(t)
omega_0 = sp.symbols('omega_0', real=True, positive=True)
gamma = sp.symbols('gamma', real=True, positive=True)

# Define the differential equation
# Example: damped harmonic oscillator
eq = sp.Eq(x.diff(t, t) + 2 * gamma * x.diff(t) + omega_0**2 * x, 0)

# Solve the differential equation
solution = sp.dsolve(eq, x)

print("The solution to the differential equation is:")
print(solution)
