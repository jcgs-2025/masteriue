from stats_lib import statistics
import pytest
from itertools import repeat

def test_functions():
    assert statistics.mean([30,15]) == 22.5 
    assert statistics.median([1, 2, 3]) == 2
    assert statistics.variance([1, 2, 3]) == 1
""
@pytest.mark.parametrize("n", [list(repeat(1, 2*i)) for i in range(1, 10)])
def test_mean(benchmark, n):
    benchmark.pedantic(statistics.mean, args=(n,), iterations=10000, rounds=100)