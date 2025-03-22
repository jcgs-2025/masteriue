import numpy as np
import matplotlib.pyplot as plt
from euler.euler import euler_solve 

def projectile_ode(t, y):
    """
    Function that defines the ODE for projectile motion.
    
    Args:
        t (float): The time.
        y (ndarray): The position and velocity.
        
    Returns:
        ndarray: The derivative of the position and velocity.
    """ 
    x, y, vx, vy = y
    
    k = 0.25 # friction coefficient
    
    dx_dt = vx
    dy_dt = vy
    dvx_dt = 0
    dvy_dt = -9.8 - k*vy
    return np.column_stack([dx_dt, dy_dt, dvx_dt, dvy_dt])

def analytical_solution(t, x0, y0, vx0, vy0):
    """
    Function that defines the analytical solution for the projectile motion ODE.
    
    Args:
        t (float): The time.
        v0 (float): The initial velocity.
        theta (float): The launch angle.
        
    Returns:
        tuple: The analytical solution.
    """
    x = x+vx0*t
    y = y0 + vy0*t - 0.5*9.8*t**2
    vx = vx0 * np.ones_like(t)
    vy = vy0 - 9.8*t
    return x, y, vx, vy

t, y = euler_solve(projectile_ode, y0 = [0, 0, 20, 20], ti = 0, tf = 4, h = 0.5)
y_analytical = analytical_solution(t, 0, 0, 20, 20)

plt.figure(figsize=(12, 10))

plt.subplot(2, 1, 1)
plt.plot(y_euler[:,0], y_euler[:,1], 'o-', label="Numerical solution")
plt.plot(y_analytical[0], y_analytical[1], 'x-', label="Analytical solution")
plt.xlabel("Horizontal distance")
plt.ylabel("Vertical distance")
plt.title("Projectile motion")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, y_euler[:,1], 'o-', label="Numerical solution")
plt.plot(t, y_analytical[1], 'x-', label="Analytical solution")
plt.xlabel("Time")
plt.ylabel("Vertical distance")
plt.title("Projectile motion")
plt.grid(True)
plt.legend()

plt.show()