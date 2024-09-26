from typing import Any

def validate_input(*args: Any) -> bool:
    """
    Validate the input arguments for calculator operations.
    
    This function attempts to convert string inputs to float,
    then checks if all input arguments are either integers or floats.
    
    Args:
    *args: Variable length argument list of inputs to validate.
    
    Returns:
    bool: True if all inputs are valid (int or float), False otherwise.
    """
    for arg in args:
        try:
            float(arg)
        except ValueError:
            return False
    return True

def validate_expression(expression: str) -> bool:
    """
    Validate a mathematical expression string.
    
    This function checks if the expression contains only valid characters
    and has balanced parentheses.
    
    Args:
    expression (str): The mathematical expression to validate.
    
    Returns:
    bool: True if the expression is valid, False otherwise.
    """
    valid_chars = set('0123456789+-*/()^. ')
    if not all(char in valid_chars for char in expression):
        return False
    
    # Check for balanced parentheses
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0
