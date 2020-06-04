from qtpy.QtCore import Qt
from qtpy.QtGui import QColor, QPen
from qtpy.QtWidgets import QGraphicsItem, QGraphicsPathItem, QWidget


class ConnectionGraphicsPathItem(QGraphicsPathItem):
    hover: bool = False

    _source_position: (int, int)
    _destination_position: (int, int)

    def __init__(self, connection: 'Connection', parent: QWidget = None):
        super().__init__(parent)

        self.connection = connection

        self._color = self._default_color = QColor("#001000")
        self._color_hover = QColor("#FF37A6FF")
        self._color_select = QColor("#00ff00")

        self._pen = QPen(self._color)
        self._pen.setWidthF(3.0)

        self._pen_drag = QPen(self._color)
        self._pen_drag.setStyle(Qt.DashLine)
        self._pen_drag.setWidthF(3.0)

        self._pen_select = QPen(self._color_select)
        self._pen_select.setWidthF(3.0)

        self._pen_hover = QPen(self._color_hover)
        self._pen_hover.setWidthF(5.0)

        self.setAcceptHoverEvents(True)

        self.setFlag(QGraphicsItem.ItemIsSelectable)

        self.setZValue(-1)

    @property
    def destination_position(self) -> (int, int):
        if self._destination_position:
            return self._destination_position

    @destination_position.setter
    def destination_position(self, position: (int, int)):
        self._destination_position = position

    @property
    def source_position(self) -> (int, int):
        if self._source_position:
            return self._source_position

    @source_position.setter
    def source_position(self, position: (int, int)):
        self._source_position = position

    def disable_selectable(self):
        self.setAcceptHoverEvents(False)

        self.setFlag(QGraphicsItem.ItemIsSelectable, False)

    def on_select(self):
        pass

    def boundingRect(self) -> 'QRectF':
        return self.shape().boundingRect()

    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent'):
        super().mouseReleaseEvent(event)

    def shape(self) -> 'QPainterPath':
        return self.painter_path

    def paint(self, painter: 'QPainter', **kwargs):
        self.setPath(self.painter_path)

        painter.setBrush(Qt.NoBrush)

        if self.edge.y and self.hover:
            painter.setPen(self._pen_hover)

            painter.drawPath(self.path())

        if self.edge.y:
            if self.isSelected():
                painter.setPen(self._pen_select)
            else:
                painter.setPen(self._pen)
        else:
            painter.setPen(self._pen_drag)

        painter.drawPath(self.path())
