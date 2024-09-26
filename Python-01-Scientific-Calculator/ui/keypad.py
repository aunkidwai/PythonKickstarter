from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import Qt

class Keypad(QWidget):
    def __init__(self, button_clicked_callback):
        super().__init__()
        self.button_clicked_callback = button_clicked_callback
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '(', ')', '^',
            'sin', 'cos', 'tan', 'sqrt',
            'log', 'ln', 'π', 'e'
        ]

        positions = [(i, j) for i in range(7) for j in range(4)]

        for position, button in zip(positions, buttons):
            btn = QPushButton(button)
            btn.clicked.connect(lambda checked, text=button: self.button_clicked_callback(text))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    border: 1px solid #999;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
                QPushButton:pressed {
                    background-color: #d0d0d0;
                }
            """)
            grid.addWidget(btn, *position)

    def keyPressEvent(self, event):
        key = event.text()
        if key in '0123456789.+-*/()^':
            self.button_clicked_callback(key)
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.button_clicked_callback('=')
        elif event.key() == Qt.Key_Backspace:
            self.button_clicked_callback('C')
        else:
            super().keyPressEvent(event)
