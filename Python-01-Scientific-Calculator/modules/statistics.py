import math
from typing import List, Union

Number = Union[int, float]

def mean(numbers: List[Number]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)

def median(numbers: List[Number]) -> float:
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of an empty list")
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def mode(numbers: List[Number]) -> List[Number]:
    """Calculate the mode(s) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mode of an empty list")
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    return [num for num, freq in frequency.items() if freq == max_freq]

def variance(numbers: List[Number]) -> float:
    """Calculate the variance of a list of numbers."""
    if len(numbers) < 2:
        raise ValueError("Variance requires at least two numbers")
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)  # Changed from (len(numbers) - 1)

def standard_deviation(numbers: List[Number]) -> float:
    """Calculate the standard deviation of a list of numbers."""
    return math.sqrt(variance(numbers))

def range_stat(numbers: List[Number]) -> float:
    """Calculate the range of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate range of an empty list")
    return max(numbers) - min(numbers)

def covariance(x: List[Number], y: List[Number]) -> float:
    """Calculate the sample covariance between two lists of numbers."""
    if len(x) != len(y):
        raise ValueError("Lists must have the same length")
    if len(x) < 2:
        raise ValueError("Covariance requires at least two pairs of numbers")
    x_mean = mean(x)
    y_mean = mean(y)
    return sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / (len(x) - 1)

def correlation(x: List[Number], y: List[Number]) -> float:
    if len(x) != len(y):
        raise ValueError("Lists must have the same length")
    if len(x) < 2:
        raise ValueError("Correlation requires at least two pairs of numbers")
    
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x_squared = sum(xi ** 2 for xi in x)
    sum_y_squared = sum(yi ** 2 for yi in y)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2))
    
    if denominator == 0:
        return 0  # If denominator is 0, correlation is undefined (or 0)
    
    return numerator / denominator
