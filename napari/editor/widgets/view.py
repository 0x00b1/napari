from qtpy.QtGui import QPainter
from qtpy.QtWidgets import QGraphicsView, QWidget
from qtpy.QtCore import Qt


class View(QGraphicsView):
    scene: 'Scene'

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.RubberBandDrag)

        self.setAcceptDrops(True)
