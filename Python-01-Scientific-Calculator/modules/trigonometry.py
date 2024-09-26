import math
from typing import Union

Number = Union[int, float]

def sin(angle: Number, use_degrees: bool = True) -> float:
    """Calculate the sine of an angle."""
    if use_degrees:
        angle = math.radians(angle)
    return math.sin(angle)

def cos(angle: Number, use_degrees: bool = True) -> float:
    """Calculate the cosine of an angle."""
    if use_degrees:
        angle = math.radians(angle)
    return math.cos(angle)

def tan(angle: Number, use_degrees: bool = True) -> float:
    """Calculate the tangent of an angle."""
    if use_degrees:
        angle = math.radians(angle)
    return math.tan(angle)

def asin(value: Number) -> float:
    """Calculate the arcsine (inverse sine) of a value."""
    return math.degrees(math.asin(value))

def acos(value: Number) -> float:
    """Calculate the arccosine (inverse cosine) of a value."""
    return math.degrees(math.acos(value))

def atan(value: Number) -> float:
    """Calculate the arctangent (inverse tangent) of a value."""
    return math.degrees(math.atan(value))

def atan2(y: Number, x: Number) -> float:
    """Calculate the arctangent of y/x, considering the quadrant."""
    return math.degrees(math.atan2(y, x))

def sinh(x: Number) -> float:
    """Calculate the hyperbolic sine of x."""
    return math.sinh(x)

def cosh(x: Number) -> float:
    """Calculate the hyperbolic cosine of x."""
    return math.cosh(x)

def tanh(x: Number) -> float:
    """Calculate the hyperbolic tangent of x."""
    return math.tanh(x)

def degrees_to_radians(degrees: Number) -> float:
    """Convert degrees to radians."""
    return math.radians(degrees)

def radians_to_degrees(radians: Number) -> float:
    """Convert radians to degrees."""
    return math.degrees(radians)
