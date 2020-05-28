from qtpy.QtWidgets import QGraphicsItem, QWidget


class NodeWidget(QGraphicsItem):
    def __init__(self, node: 'Node', parent: QWidget = None):
        super().__init__(parent)
