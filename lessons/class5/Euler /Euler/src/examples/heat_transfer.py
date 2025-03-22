import numpy as np
import matplotlib.pyplot as plt
from euler.euler import euler_solve

def heat_transfer_ode(t, T):
    """
    Function that defines the ODE for heat transfer.
    
    Args:
        t (float): The time.
        x (ndarray): The temperature.
        
    Returns:
        ndarray: The derivative of the temperature.
    """
    k = 0.1
    T_env = 20
    
    dT_dt = k*(T_env - T)
    
    return np.array([dT_dt])

def analytical_solution(t, T0=100):
    """
    Function that defines the analytical solution for the heat transfer ODE.
    
    Args:
        t (float): The time.
        
    Returns:
        float: The analytical solution.
    """
    k = 0.1
    T_env = 20
    T0 = 100
    
    return T_env + (T0 - T_env)*np.exp(-k*t)

t, T_euler = euler_solve(heat_transfer_ode, y0 = 100, ti = 0, tf = 50, h = 10)
T_analytical = analytical_solution(t, 100)

plt.figure(figsize=(10, 6))
plt.plot(t, T_euler,'o-', label="Numerical solution")
plt.plot(t, T_analytical, 'x-', label="Analytical solution")

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Heat transfer")
plt.grid(True)
plt.legend()
plt.show()