from qtpy.QtWidgets import QGraphicsView, QWidget


class View(QGraphicsView):
    scene: 'Scene'

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
