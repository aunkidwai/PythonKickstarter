# Scientific Calculator

A comprehensive scientific calculator application built with Python and PyQt5.

![Calculator UI Screenshot](placeholder_for_screenshot.png)

## Features

- Basic arithmetic operations
- Advanced mathematical functions
- Trigonometric calculations
- Statistical operations
- User-friendly graphical interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/scientific-calculator.git
   cd scientific-calculator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the calculator:
```bash
python main.py
```

## Main Functionalities

### Basic Operations

Perform basic arithmetic calculations:

```
python
from modules.basic_operations import add, subtract, multiply, divide
result = add(5, 3) # 8
result = subtract(10, 4) # 6
result = multiply(3, 7) # 21
result = divide(15, 3) # 5.0
```

### Advanced Operations

Access advanced mathematical functions:

```
from modules.advanced_operations import square_root, power, factorial

result = square_root(16)  # 4.0
result = power(2, 3)  # 8.0
result = factorial(5)  # 120
```

### Trigonometric Functions

Perform trigonometric calculations:

```
from modules.trigonometry import sin, cos, tan

result = sin(30)  # Sine of 30 degrees
result = cos(60)  # Cosine of 60 degrees
result = tan(45)  # Tangent of 45 degrees
```

### Statistical Operations

Compute statistical values:

```
from modules.statistics import mean, median, standard_deviation

data = [1, 2, 3, 4, 5]
result = mean(data)  # 3.0
result = median(data)  # 3.0
result = standard_deviation(data)  # ~1.58
```

## UI Components

The calculator's UI is built using PyQt5 and consists of three main components:

1. Display: Shows the input and results
2. Keypad: Provides buttons for input and operations
3. Main Window: Combines the display and keypad

```python:ui/main_window.py
startLine: 5
endLine: 33
```

## Testing

Run the test suite:

```
pytest -v
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
