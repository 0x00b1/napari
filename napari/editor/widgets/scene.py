from math import ceil, floor

from qtpy.QtCore import QLine
from qtpy.QtGui import QColor, QPen
from qtpy.QtWidgets import QGraphicsScene


class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.size = 20
        self.squares = 5

        self._background_color = QColor("#393939")

        self._a_color = QColor("#2f2f2f")
        self._b_color = QColor("#292929")

        self._a_pen = QPen(self._a_color)
        self._b_pen = QPen(self._b_color)

        self._a_pen.setWidth(1)
        self._b_pen.setWidth(2)

        self.setBackgroundBrush(self._background_color)

    def drawBackground(self, painter: 'QPainter', rect: 'QRectF'):
        super().drawBackground(painter, rect)

        # here we create our grid
        left = int(floor(rect.left()))
        right = int(ceil(rect.right()))
        top = int(floor(rect.top()))
        bottom = int(ceil(rect.bottom()))

        first_left = left - (left % self.size)
        first_top = top - (top % self.size)

        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.size):
            if x % (self.size * self.squares) != 0:
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.size):
            if y % (self.size * self.squares) != 0:
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

        painter.setPen(self._a_pen)
        painter.drawLines(*lines_light)

        painter.setPen(self._b_pen)
        painter.drawLines(*lines_dark)
