from qtpy.QtWidgets import QGraphicsView, QWidget


class EditorGraphicsView(QGraphicsView):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
