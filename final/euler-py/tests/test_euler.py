import numpy as np
import pytest
from euler_py.euler import euler_solve  # Importar la función que vamos a probar
from src.examples.epidemic_model import sir_model

# Función simple: dy/dt = y (Crecimiento exponencial)
def exponential_growth(t, y):
    return y

# Prueba 1: Verificar que la solución de Euler para dy/dt = y sea razonable
def test_euler_exponential():
    y0 = [1]  # Condición inicial
    ti, tf, h = 0, 1, 0.01  # Intervalo de tiempo y paso
    t, y = euler_solve(exponential_growth, y0, ti, tf, h)

    # Comparamos con la solución exacta: y = e^t
    y_exact = np.exp(t)
    assert np.allclose(y.flatten(), y_exact, atol=0.05), "Euler no se aproxima bien a e^t"

# Prueba 2: Verificar que la función retorna el número correcto de pasos
def test_euler_step_count():
    y0 = [1]
    ti, tf, h = 0, 2, 0.2
    t, y = euler_solve(exponential_growth, y0, ti, tf, h)

    expected_steps = int((tf - ti) / h) + 1
    assert len(t) == expected_steps, "Número incorrecto de pasos"

# Prueba 3: Verificar que funciona con múltiples ecuaciones diferenciales (sistemas)
def test_euler_system():
    def system(t, y):
        return np.array([-y[0], y[1]])  # Sistema con dos ecuaciones

    y0 = [1, 0]
    ti, tf, h = 0, 1, 0.1
    t, y = euler_solve(system, y0, ti, tf, h)

    assert y.shape == (len(t), 2), "La forma de salida no es correcta para sistemas"
    
def test_sir_model_shape():
    """Verifica que la función del modelo SIR retorne un array de la forma correcta."""
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

if __name__ == "__main__":
    pytest.main()
