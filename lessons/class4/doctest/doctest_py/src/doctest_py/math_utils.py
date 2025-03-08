""""
Esto es un modulo que contiene algunas funciones matemáticas con doctest
"""

def factorial(n):
    """Calcula el factorial de un número entero no negativo.
    
    Args:
        n (int): Número entero no negativo.
        
    Returns:
        int: Factorial de n.
        
    Raises:
        ValueError: Si n es un número negativo.
        
    Examples:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: n debe ser un número entero no negativo
    """
    if n < 0:
        raise ValueError("n debe ser un número entero no negativo")
    return 1 if n == 0 else n * factorial(n - 1)

def add(a, b):
    """Suma dos números.
    
    Args:
        a (int): Primer número.
        b (int): Segundo número.
        
    Returns:
        int: Suma de a y b.
        
    Examples:
        >>> add(1, 2)
        3
        >>> add(5, 5)
        10
        >>> add(0, 0)
        0
    """
    return a + b