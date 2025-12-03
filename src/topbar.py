from PyQt6.QtWidgets import QToolBar, QWidget, QLabel, QSlider, QSizePolicy
from PyQt6.QtGui import QFont, QAction, QActionGroup, QIcon
from PyQt6.QtCore import Qt, pyqtSignal, QRect, pyqtSlot
from styles import topbar

class TopBar(QToolBar):
    navigationRequested = pyqtSignal(str)
    themeToggleRequested = pyqtSignal()

    volumeChanged = pyqtSignal(int)
    project_BPM = 120

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setMovable(False)
        self.setStyleSheet(topbar)

        title = QLabel("rasppy")
        title.setFont(QFont("Arial", 14))
        self.addWidget(title)

        self.pageswitches = QActionGroup(self)
        self.pageswitches.setExclusive(True)

        self.drumpad_btn = QAction("Drumpad", self)
        self.drumpad_btn.setCheckable(True)
        self.drumpad_btn.setChecked(True)
        self.drumpad_btn.triggered.connect(lambda checked, p='Drumpad': self.navigationRequested.emit(p))
        self.pageswitches.addAction(self.drumpad_btn)
        self.addAction(self.drumpad_btn)

        self.record_btn = QAction("Record", self)
        self.record_btn.setIcon(QIcon("src/resources/icons/record-icon.svg"))
        self.record_btn.setCheckable(True)
        self.pageswitches.addAction(self.record_btn)
        self.addAction(self.record_btn)

        ##Slider for setting project BPM
        self.bpmslider = QSlider()
        self.bpmslider.setToolTip("BPM")
        self.bpmslider.setGeometry(QRect(0,0,80,16))
        self.bpmslider.setOrientation(Qt.Orientation.Horizontal)
        self.bpmslider.setRange(0,300)
        self.bpmslider.setValue(120)
        self.bpmslider.setSingleStep(1)
        self.bpmslider.setPageStep(10)

        self.bpmslider.valueChanged.connect(self.setBPMValue)

        self.bpmlabel = QLabel(f"BPM:{self.project_BPM}")
        self.addWidget(self.bpmlabel)
        self.addWidget(self.bpmslider)


        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.addWidget(spacer)

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(90)
        self.volume_slider.setFixedWidth(120)
        self.volume_slider.valueChanged.connect(self._emitVolume)
        self.addWidget(self.volume_slider)

        theme_button = self.addAction("Theme")
        theme_button.triggered.connect(self._handle_theme_toggle)

        close_button = self.addAction("x")
        close_button.setToolTip("Close")
        close_button.triggered.connect(self._handle_close)

    def _handle_close(self):
        if self.parent is not None:
            self.parent.close()

    def _handle_theme_toggle(self):
        self.themeToggleRequested.emit()

    def _emitVolume(self, value):
        self.volumeChanged.emit(value)
    def setBPMValue(self, value):
        self.project_BPM = value
        self.bpmlabel.setText(f"BPM:{self.project_BPM}")
