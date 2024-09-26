from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from .display import Display
from .keypad import Keypad

class MainWindow(QMainWindow):
    def __init__(self, calculator):
        super().__init__()
        self.calculator = calculator
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Scientific Calculator')
        self.setGeometry(100, 100, 300, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.display = Display()
        layout.addWidget(self.display)

        self.keypad = Keypad(self.on_button_click)
        layout.addWidget(self.keypad)

    def on_button_click(self, button_text):
        if button_text == '=':
            self.calculate()
        elif button_text == 'C':
            self.display.clear()
        else:
            self.display.append(button_text)

    def calculate(self):
        expression = self.display.text()
        try:
            # Remove any spaces from the expression
            expression = expression.replace(' ', '')
            
            if expression.startswith('sqrt(') and expression.endswith(')'):
                # Handle square root
                number = expression[5:-1]  # Extract the number inside sqrt()
                result = self.calculator.perform_operation('sqrt', number)
            else:
                # Handle other operations as before
                for op in ['+', '-', '*', '/']:
                    if op in expression:
                        parts = expression.split(op)
                        if len(parts) == 2:
                            a, b = parts
                            result = self.calculator.perform_operation(op, a, b)
                            break
                else:
                    raise ValueError("Invalid expression")
            
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText('Error: ' + str(e))
