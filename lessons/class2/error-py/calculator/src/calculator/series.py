def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Args:
        n (int): The number to compute the factorial of. Must be non-negative.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)