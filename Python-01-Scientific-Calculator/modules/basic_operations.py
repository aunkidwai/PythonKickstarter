def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulo(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b

def floor_division(a, b):
    """Perform floor division of a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b

def negate(a):
    """Return the negation of a number."""
    return -a

def absolute(a):
    """Return the absolute value of a number."""
    return abs(a)
