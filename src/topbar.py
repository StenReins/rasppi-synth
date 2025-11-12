from PyQt6.QtWidgets import QToolBar, QBoxLayout, QWidget, QLabel, QSizePolicy
from PyQt6.QtGui import QFont
from styles import topbar


class TopBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setMovable(False)
        self.setStyleSheet(topbar)

        title = QLabel("rasppy")
        self.addWidget(title)

        drumpadview_button = self.addAction("drumpad")
        drumpadview_button.setToolTip("Drumpad")

