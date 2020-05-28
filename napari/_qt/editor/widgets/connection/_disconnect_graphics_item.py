from qtpy.QtWidgets import QGraphicsItem, QWidget


class DisconnectGraphicsItem(QGraphicsItem):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
