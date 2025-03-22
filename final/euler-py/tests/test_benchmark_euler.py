import numpy as np
import pytest
from euler_py.euler import euler_solve

# Definimos una ecuación diferencial simple: dy/dt = -y (Decaimiento exponencial)
def decay_function(t, y):
    return -y

# Benchmark para el método de Euler
@pytest.mark.benchmark(group="euler")
def test_euler_benchmark(benchmark):
    y0 = [1]  # Condición inicial
    ti, tf, h = 0, 10, 0.001  # Intervalo de tiempo y paso pequeño
    result = benchmark(euler_solve, decay_function, y0, ti, tf, h)

    # Verificamos que la solución no tenga valores NaN o Inf
    assert not np.isnan(result[1]).any(), "Euler generó NaN"
    assert not np.isinf(result[1]).any(), "Euler generó Inf"
