""""
Ejecuta doctests de forma automática.
"""

import doctest
import unittest
from src.doctest_py import math_utils


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(math_utils))
    return tests

if __name__ == "__main__":
    unittest.main()
    
