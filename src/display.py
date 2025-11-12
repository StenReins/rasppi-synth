from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit

class Display(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        self.top = QLineEdit()

        self.bottom = QLineEdit()

        layout.addWidget(self.top)
        layout.addWidget(self.bottom)

        self.setLayout(layout)
        self.setGeometry(0,0,)
        
