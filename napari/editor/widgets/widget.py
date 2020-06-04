from qtpy.QtWidgets import QWidget, QVBoxLayout

from .view import View
from .scene import Scene


class Widget(QWidget):
    scene: 'Scene'
    view: 'View'

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
