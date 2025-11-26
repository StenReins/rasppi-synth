from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QMenu
import tkinter
from tkinter import filedialog
from gpiozero import *
from gpiozero import Button
import time
import os


class Pad(QPushButton):
    states = {
    'triggered': 0,
    'held': 1,
    'looped':2
    }
    def __init__(self, number = None, path = None, parent = None, state = states[0]):
        self.path = path
        self.pad_num = number
        self.state = state
        self.pad_button = Button(number)
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
            self.setText(f"Pad {self.pad_num}")

    def contextMenuEvent(self, a0): ## a0 -> event if its not working
        menu = QMenu(self)
        pad_modify = menu.addAction("Modify")
        pad_reset = menu.addAction("Reset")
        action = menu.exec(a0.globalPos())
        if action == pad_modify:
            self.modifyMusicFile()
        elif action == pad_reset:
            self.resetMusicFile()
    def modifyMusicFile(self):
        tkinter.Tk().withdraw()
        self.path = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .mp3"),   ("All Files", "*.*")))
        if self.path is not "":
            file_name = os.path.split(self.path)[1]
            self.setText(file_name)
    def resetMusicFile(self):
        if self.path is not None:
            self.path = None
            self.setText(f"Pad {self.pad_num}")

class DrumPad(QWidget):
    pads = []
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

        self.pads = []
    
    def initUI(self):
        layout = QGridLayout()
        layout.setSpacing(10) 
        for row in range(3):
            for col in range(3):
                pad_num = row * 4 + col + 1
                pad = Pad(pad_num)
                layout.addWidget(pad, row, col)
                self.pads.append([pad, pad_num])

        self.setLayout(layout)