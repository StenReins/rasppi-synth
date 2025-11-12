from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
from topbar import TopBar
from styles import STYLESHEET
import sys

class Raspsynth(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            print("Program is working.")
            ##window params
            self.setWindowTitle("rasppy v0.0.1")
            self.setStyleSheet(STYLESHEET)
            self.setMinimumSize(600,600)
            self.setMaximumSize(600,600)
            self.setContentsMargins(20,10,20,20)

            ##widget inits go here
            self.main = QWidget()

            ##class inits for other GUI elements go here
            self.addToolBar(TopBar(self))

        except:
            print("Something went  during initialization.")
    
def main():
    app = QApplication(sys.argv)
    window = Raspsynth()
    window.show()
    app.exec()
main()