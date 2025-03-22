import numpy as np
import matplotlib.pyplot as plt
from euler_py.euler import euler_solve  

# SIR model
def sir_model(t, y):
    """
    SIR model for epidemics.
    
    Parameters
    ----------
    t : float
        Time.
    y : array-like
        Array with the current values of S, I and R.
        
    Returns
    -------
    array-like
        Array with the derivatives of S, I and R.
    """
    S, I, R = y
    beta = 0.3   # Infection rate
    gamma = 0.1  # Recovery rate
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return np.array([dSdt, dIdt, dRdt])

# Initial conditions
S0, I0, R0 = 990, 10, 0
y0 = np.array([S0, I0, R0])

# Time interval and step size
ti, tf, h = 0, 100, 0.01

# Solve the system
t, y = euler_solve(sir_model, y0, ti, tf, h)

print("Time:", t[:10])  # Primeros 10 valores de tiempo
print("S:", y[:10, 0])  # Primeros 10 valores de S
print("I:", y[:10, 1])  # Primeros 10 valores de I
print("R:", y[:10, 2])  # Primeros 10 valores de R


# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, y[:, 0], label="Susceptibles")
plt.plot(t, y[:, 1], label="Infecs")
plt.plot(t, y[:, 2], label="Recovs")
plt.xlabel("Time (days)")
plt.ylabel("Population")
plt.legend()
plt.title("SIR Model (Euler method)")
plt.grid()
plt.savefig("SIR model.png")
plt.show()
