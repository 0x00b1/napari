from qtpy.QtWidgets import QAction, QMainWindow, QWidget


class QtEditor(QMainWindow):
    def __init__(self, editor: 'Editor', parent: QWidget = None):
        super().__init__(parent)
