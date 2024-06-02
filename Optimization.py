import sympy as sp

# Define the variable and functions
q = sp.symbols('q')
p = 50 - 0.5 * q  # Price-demand function
C = 100 + 10 * q  # Cost function
Revenue = p * q  # Revenue function
Profit = Revenue - C  # Profit function

# Calculate the derivative of the Profit function
dProfit = sp.diff(Profit, q)

# Solve for the quantity that maximizes profit
critical_points = sp.solve(dProfit, q)

# Evaluate the second derivative test
second_deriv = sp.diff(dProfit, q)
concavity = [second_deriv.subs(q, cp) for cp in critical_points]

# Display results
print(f"Profit function: {Profit}")
print(f"First Derivative (set to zero): {dProfit}")
print(f"Critical Points: {critical_points}")
for cp, conc in zip(critical_points, concavity):
    if conc < 0:
        print(f"Maximum Profit at q = {cp}:")
        print(f"Profit = {Profit.subs(q, cp)}")
    elif conc > 0:
        print(f"Minimum at q = {cp}")
    else:
        print(f"No conclusion can be drawn at q = {cp}")
