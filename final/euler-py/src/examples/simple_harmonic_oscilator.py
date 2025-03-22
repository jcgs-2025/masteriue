import numpy as np
import matplotlib.pyplot as plt
from euler_py.euler import euler_solve  

def simple_harmonic_oscillator(t, y, k, m):
    """
    Simple harmonic oscillator model.
    
    Parameters
    ----------
    t : float
        Time.
    y : array-like
        Array with the current values of x and v.
    k : float
        Spring constant.
    m : float
        Mass.   
        
    Returns
    -------
    array-like
        Array with the derivatives of x and v.
    """
    x, v = y  # y[0] = x, y[1] = v
    dxdt = v
    dvdt = - (k / m) * x
    return [dxdt, dvdt]

# System parameters
k = 2.0  # Spring constant
m = 1.0  # Mass
y0 = [1.0, 0.0]  # Initial conditions: x(0) = 1.0, v(0) = 0.0
ti, tf = 0, 10  # Time interval
h = 0.01  # h value --> (small h value for better accuracy)

# Solve the system
t, y = euler_solve(simple_harmonic_oscillator, y0, ti, tf, h, args=(k, m))

# Plot 
# plt.plot(t, y[:, 0], label="Position x(t)")
# plt.plot(t, y[:, 1], label="Velocity v(t)")
# plt.xlabel("Time (s)")
# plt.ylabel("Magnitude")
# plt.title("Simple Harmonic Oscillator (Euler method)")
# plt.legend()
# plt.grid()
# plt.savefig("output.png")  
