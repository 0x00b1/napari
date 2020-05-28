from qtpy.QtCore import QPointF
from qtpy.QtGui import QPainterPath

from ._connection_graphics_path_item import ConnectionGraphicsPathItem


class DirectConnection(ConnectionGraphicsPathItem):
    def __init__(self, connection: 'Connection'):
        super().__init__(connection)

        self._painter_path = QPainterPath()

    @property
    def painter_path(self) -> 'QPainterPath':
        source = QPointF(self.posSource[0], self.posSource[1])

        destination = QPointF(self.posDestination[0], self.posDestination[1])

        self._painter_path = QPainterPath(source)

        self._painter_path.lineTo(destination)

        return self._painter_path
