from .node import Node
from ..socket.layer.image_socket import ImageSocket

from skimage.filters import median

from ...layers import Image


class MedianNode(Node):
    def __init__(self):
        super().__init__('Median')

        self.x_socket = ImageSocket(self.id)
        self.y_socket = ImageSocket(self.id)

    @property
    def options(self) -> ['Option']:
        return []

    @property
    def x(self) -> ['Socket']:
        return [self.x_socket]

    @property
    def y(self) -> ['Socket']:
        return self._y

    def evaluate(self):
        self.y_socket.data = Image(median(self.x_socket.data.data))
