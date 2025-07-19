import numpy as np
import pytest
from euler_py.euler import euler_solve
from src.examples.epidemic_model import sir_model

def test_sir_model_shape():
    """Verifica que la función sir_model devuelva un array de 3 elementos.
    """
    y0 = np.array([990, 10, 0])  # Condiciones iniciales
    dydt = sir_model(0, y0)
    assert isinstance(dydt, np.ndarray), "La salida no es un array de numpy"
    assert dydt.shape == (3,), "La salida debe tener 3 elementos (S, I, R)"

def test_sir_model_dynamics():
    """Verifica que los valores de S, I y R evolucionen de forma esperada."""
    S0, I0, R0 = 990, 10, 0
    y0 = np.array([S0, I0, R0])
    ti, tf, h = 0, 50, 1

    t, y = euler_solve(sir_model, y0, ti, tf, h)

    assert y[0, 0] == S0, "El primer valor de S debe ser igual a S0"
    assert y[0, 1] == I0, "El primer valor de I debe ser igual a I0"
    assert y[0, 2] == R0, "El primer valor de R debe ser igual a R0"

    # Al final del periodo, S debería haber disminuido y R debería haber aumentado
    assert y[-1, 0] < S0, "S debe haber disminuido con el tiempo"
    assert y[-1, 2] > R0, "R debe haber aumentado con el tiempo"
