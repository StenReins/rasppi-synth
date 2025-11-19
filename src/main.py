from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import pyqtSignal
from drumpad import DrumPad
from topbar import TopBar
from styles import STYLESHEET
import sys
from drumpad import DrumPad

page_indices = {
    'drumpad': 0
}

class Raspsynth(QMainWindow):
    navigationRequested = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        try:
            print("Program is working.")
            # window params
            self.setWindowTitle("rasppy v0.0.1")
            ##self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
            self.setStyleSheet(STYLESHEET)
            self.setGeometry(20, 20, 1080, 720)
            # central widget
            self.widget = QStackedWidget()
            self.setCentralWidget(self.widget)

<<<<<<< HEAD
            ##widget inits go here
            self.main = QWidget()
            self.layout = QVBoxLayout(self.main)
=======
            # pages
            drumpad_widget = DrumPad(self)
            self.widget.addWidget(drumpad_widget)
>>>>>>> 67c4a372e52771258c89c7606741397f6ab93653

            # top bar (toolbar)
            self.topbar = TopBar(self)
            self.addToolBar(self.topbar)

<<<<<<< HEAD
            ##GUI components
            try:
                self.layout.addWidget(self.topbar)
            except Exception as e:
                print("TopBar failed:", e)

            self.drum_pad = DrumPad()
            self.layout.addWidget(self.drum_pad)

            self.main.setLayout(self.layout)
            self.setCentralWidget(self.main)

        except:
            print("Something went  during initialization.")
    
=======
            self.topbar.navigationRequested.connect(self.setPage)

            self.setPage('drumpad')
        except Exception as e:
            print("Something went wrong.", e)

    def setPage(self, page_name: str):
        idx = page_indices.get(page_name, 0)
        self.widget.setCurrentIndex(idx)

        
>>>>>>> 67c4a372e52771258c89c7606741397f6ab93653
def main():
    app = QApplication(sys.argv)
    window = Raspsynth()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()