from qtpy.QtWidgets import QGraphicsScene


class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
