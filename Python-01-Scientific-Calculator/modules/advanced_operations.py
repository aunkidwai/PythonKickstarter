import math

def power(base, exponent):
    """Raise base to the power of exponent."""
    return math.pow(base, exponent)

def square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(number)

def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def logarithm(number, base=10):
    """Calculate the logarithm of a number with a specified base (default is 10)."""
    if number <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid input for logarithm")
    return math.log(number, base)

def natural_logarithm(number):
    """Calculate the natural logarithm (base e) of a number."""
    if number <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers")
    return math.log(number)

def exponential(x):
    """Calculate e raised to the power of x."""
    return math.exp(x)

def absolute_value(number):
    """Return the absolute value of a number."""
    return abs(number)

def floor(number):
    """Return the largest integer less than or equal to the given number."""
    return math.floor(number)

def ceiling(number):
    """Return the smallest integer greater than or equal to the given number."""
    return math.ceil(number)
