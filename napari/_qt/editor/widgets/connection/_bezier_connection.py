from math import fabs

from qtpy.QtCore import QPointF
from qtpy.QtGui import QPainterPath

from ._connection_graphics_path_item import ConnectionGraphicsPathItem


class BezierConnection(ConnectionGraphicsPathItem):
    def __init__(self, connection: 'Connection', roundness=100):
        super().__init__(connection)

        self.source = connection.source
        self.destination = connection.destination

        self.roundness = roundness

        self._painter_path = QPainterPath()

    @property
    def painter_path(self) -> 'QPainterPath':
        source = self.posSource
        destination = self.posDestination

        distance = (destination[0] - source[0]) * 0.5

        source_x = +distance
        destination_x = -distance

        source_y = 0
        destination_y = 0

        if self.source is not None:
            x_source = source[0] < destination[0] and self.source.is_x
            y_source = source[0] > destination[0] and self.source.is_y

            if x_source or y_source:
                source_x *= -1
                destination_x *= -1

                source_y = source[1]
                destination_y = destination[1]

                if (source_y - destination_y) != 0:
                    k = source_y - destination_y
                else:
                    k = 0.00001

                destination_y = (source_y - destination_y) / fabs(k)

                if (destination_y - source_y) != 0:
                    k = destination_y - source_y
                else:
                    k = 0.00001

                source_y = (destination_y - source_y) / fabs(k)

                source_y *= self.roundness
                destination_y *= self.roundness

        source_point = QPointF(self.posSource[0], self.posSource[1])

        self._painter_path = QPainterPath(source_point)

        self._painter_path.cubicTo(
            source[0] + source_x,
            source[1] + source_y,
            destination[0] + destination_x,
            destination[1] + destination_y,
            self.posDestination[0],
            self.posDestination[1],
        )

        return self._painter_path
