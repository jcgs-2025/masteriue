def factorial(n):
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)