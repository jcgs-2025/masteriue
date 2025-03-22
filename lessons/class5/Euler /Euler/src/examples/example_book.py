import numpy as np
from euler.euler import euler_solve

def f(t, x):
    dX_dt = (1 - 2*t) * x
    return np.array([dX_dt])

def analytical_solution(t):
    return np.exp(1/4 - (1/2-t)**2)

t, y = euler_solve(f, 1, 0, 0.9, 0.3)

print("t = ", t)
print("y = ", y)
print("Analytical solution = ", analytical_solution(t))
print("r2 = ", np.sum((y - analytical_solution(t))**2))
