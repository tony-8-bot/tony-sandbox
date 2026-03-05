"""Simple math utilities for tony-sandbox."""


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of two numbers."""
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
