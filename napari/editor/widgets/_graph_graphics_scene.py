from qtpy.QtWidgets import QGraphicsScene


class GraphGraphicsScene(QGraphicsScene):
    def __init__(self, graph: 'Graph', parent=None):
        super().__init__(parent)
