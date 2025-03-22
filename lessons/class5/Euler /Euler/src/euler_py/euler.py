import numpy as np

def euler_solve(f, y0, ti, tf, h):
    """
    Function to solve an ODE using Euler's method.
    
    Args:
        f (function): The function that defines the ODE.
        y0 (float or ndarray): The initial value of the ODE.
        ti (float): The initial time.
        tf (float): The final time.
        h (float): The step size.
        
    Returns:
        tuple: A tuple with the time and the solution of the ODE.
        
    Raises:
        ValueError: If the final time is less than the initial time.
        ValueError: If the step size is less than or equal to zero.   
    """
    n_steps = int((tf - ti) / h) +1 
    y = np.zeros(n_steps + 1)
    t = np.linspace(ti, tf, n_steps)

    y0 = np.array(y0, dtype=float)
        
    scalar_input = False
    if y0.ndim == 0:
        y0 = y0.reshape(1)
        scalar_input = True
        
    y = np.zeros((n_steps, len(y0)))
    t = np.linspace(ti, tf, n_steps)
        
    y[0] = y0
    t[0] = ti
    
    for i in range(0,n_steps-1):
        y[i+1] = y[i] + h * f(t[i], y[i])
        
    return t, y