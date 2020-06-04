from qtpy.QtCore import QSize
from qtpy.QtWidgets import QMainWindow, QWidget


class EditorWindow(QMainWindow):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

    def sizeHint(self):
        return QSize(800, 600)
