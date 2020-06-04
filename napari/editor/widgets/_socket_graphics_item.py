from qtpy.QtWidgets import QGraphicsItem, QWidget


class SocketGraphicsItem(QGraphicsItem):
    def __init__(self, socket: 'Socket', parent: QWidget = None):
        super().__init__(parent)
