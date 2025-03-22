import numpy as np

def euler_solve(f, y0, ti, tf, h, args=()):
    n_steps = int((tf - ti) / h) + 1
    
    y0 = np.array(y0, dtype=float)
    scalar_input = False
    if y0.ndim == 0:
        y0 = y0.reshape(1)
        scalar_input = True
    
    y = np.zeros((n_steps, len(y0)))
    t = np.linspace(ti, tf, n_steps)

    y[0] = y0 
    for i in range(n_steps - 1):
        y[i + 1] = y[i] + h * np.array(f(t[i], y[i], *args))  # Euler method

    if scalar_input:
        y = y.flatten()

    return t, y
