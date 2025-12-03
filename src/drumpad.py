from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QMenu
from PyQt6.QtCore import QUrl, pyqtSignal, QTimer
from audio import AudioPlayer
import tkinter
from gpiozero import Button
from tkinter import filedialog
from topbar import TopBar
import os

matrix_size = 2

def getProjectBPM():
    return TopBar().bpmslider.value()

class Pad(QPushButton):
    def __init__(self, number = None, path = None, parent = None, state = 'trigger', bpm = 120):
        super().__init__(parent)
        self.path = path
        self.pad_num = number
        self.state = state

        self.bpm = int(bpm)
        self.audio = AudioPlayer(path = None, bpm = self.bpm)

        self.gpio = Button(self.pad_num + 1)

        self.setFixedSize(150, 150) ## panna drumpad style style sisse
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

        self.clicked.connect(self.playAudio)

    def set_bpm(self, bpm):
        self.bpm = int(bpm)
        self.audio.set_bpm(self.bpm)

    def playAudio(self):
        if self.path:
            self.audio.play(self.path, loop=(self.state == 'loop'))
        else:
            pass

    def contextMenuEvent(self, a0): ## a0 -> event if its not working
        menu = QMenu(self)
        
        pad_changeState = menu.addMenu("Pad state")
        pad_modify = menu.addAction("Modify")
        pad_reset = menu.addAction("Reset")

        trigger_state = pad_changeState.addAction("Trigger")
        loop_state = pad_changeState.addAction("Loop")

        action = menu.exec(a0.globalPos())

        if action == pad_modify:
            self.modifyMusicFile()
        elif action == pad_reset:
            self.resetMusicFile()

        ##submenu actions
        if action == trigger_state:
            self.changeStateTrigger()
        elif action == loop_state:
            self.changeStateLoop()

    def changeStateTrigger(self):
        self.state = 'trigger'
        print(self.state)
    def changeStateLoop(self):
        self.state = 'loop'
        print(self.state)

    def modifyMusicFile(self):
        tkinter.Tk().withdraw()
        self.path = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .mp3"),   ("All Files", "*.*")))
        if self.path != "":
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
        for row in range(matrix_size):
            for col in range(matrix_size):
                pad_num = row * matrix_size + col + 1
                pad = Pad(pad_num)
                layout.addWidget(pad, row, col)
                self.pads.append([pad, pad_num])

        self.setLayout(layout)
