from imageio import imread

from .node import Node
from ..socket.layer.image_socket import ImageSocket
from ...layers import Image


class OpenImageNode(Node):
    def __init__(self):
        super().__init__('Open image')

        self.socket = ImageSocket(self.id)

    @property
    def options(self) -> ['Option']:
        return []

    @property
    def x(self) -> ['Socket']:
        return []

    @property
    def y(self) -> ['Socket']:
        return [self.socket]

    def evaluate(self):
        image = imread(self.path)

        self.socket.data = Image(image)
