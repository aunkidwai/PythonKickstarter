from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Display(QLineEdit):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setAlignment(Qt.AlignRight)
        self.setReadOnly(True)
        self.setMaxLength(50)  # Limit the input length
        
        font = QFont('Arial', 18)
        self.setFont(font)
        
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid gray;
                border-radius: 5px;
                padding: 5px;
                background-color: #f0f0f0;
                color: #333;
            }
        """)

    def append(self, text):
        current_text = self.text()
        self.setText(current_text + text)

    def backspace(self):
        current_text = self.text()
        self.setText(current_text[:-1])

    def clear(self):
        super().clear()
