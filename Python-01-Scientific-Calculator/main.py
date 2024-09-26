import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from modules import basic_operations, advanced_operations, trigonometry, statistics
from utils import input_validation

class ScientificCalculator:
    def __init__(self):
        self.basic_ops = basic_operations
        self.advanced_ops = advanced_operations
        self.trig_ops = trigonometry
        self.stats_ops = statistics
        self.validator = input_validation

    def perform_operation(self, operation, *args):
        # Validate input
        if not self.validator.validate_input(*args):
            return "Invalid input"

        # Convert string inputs to float
        converted_args = [float(arg) for arg in args]

        # Perform the requested operation
        if operation == '+':
            return self.basic_ops.add(*converted_args)
        elif operation == '-':
            return self.basic_ops.subtract(*converted_args)
        elif operation == '*':
            return self.basic_ops.multiply(*converted_args)
        elif operation == '/':
            return self.basic_ops.divide(*converted_args)
        elif operation == 'sqrt':
            return self.advanced_ops.square_root(*converted_args)
        else:
            return "Operation not supported"

def main():
    app = QApplication(sys.argv)
    calculator = ScientificCalculator()
    window = MainWindow(calculator)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
