<<<<<<< HEAD
from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt6.QtCore import Qt

class DrumPad(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(10)

        for row in range(2):
            for col in range(4):
                ##naming pads
                btn = QPushButton("Pad" + str(row * 4 + col + 1))
                btn.setFixedSize(100, 100)
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #2c3e50;
                        color: white;
                        border-radius: 8px;
                        font-size: 14px;
                    }
                    QPushButton:hover {
                        background-color: #34495e;
                    }
                    QPushButton:pressed {
                        background-color: #1abc9c;
                    }
                """)
                #calls the pad_clicked() function.
                #which button number it was.
                btn.clicked.connect(lambda _, b=row * 4 + col + 1: self.pad_clicked(b))
                layout.addWidget(btn, row, col)

        self.setLayout(layout)

    def pad_clicked(self, pad_number):
        print("Pad" + str(pad_number) + "clicked!")
=======
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QMenu
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor
import sys

class Pad(QPushButton):
    def __init__(self, number = None, path = None, parent = None):
        self.path = path
        self.pad_num = number
        super().__init__(parent)
        self.setFixedSize(150, 150)
        self.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:pressed {
                background-color: #1abc9c;
            }
        """)
        if self.pad_num is not None:
            self.setText("Pad {num}".format(num = self.pad_num))

    def contextMenuEvent(self, a0): ## a0 -> event if its not working
        menu = QMenu(self)
        pad_modify = menu.addAction("Modify")
        pad_reset = menu.addAction("Reset")
        action = menu.exec(a0.globalPos())
        if action == pad_modify:
            self.modifyMusicFile()
        elif action == pad_reset:
            self.resetMusicFile()
    def modifyMusicFile():
        return 0 ##TBD
    def resetMusicFile():
        return 0 ##tbd

class DrumPad(QWidget):
    pads = []
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

        self.pads = []
    
    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(10)
        for row in range(4):
            for col in range(4):
                pad_num = row * 4 + col + 1
                pad = Pad(pad_num)
                layout.addWidget(pad, row, col)
                self.pads.append([pad, pad_num])

        self.setLayout(layout)
>>>>>>> 67c4a372e52771258c89c7606741397f6ab93653
