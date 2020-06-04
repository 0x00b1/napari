from imageio import imread

from napari.editor.node.node import Node
from napari.editor.setting.path import Path
from napari.editor.socket.layer.image_socket import ImageSocket
from napari.layers import Image


class OpenImage(Node):
    def __init__(self):
        super().__init__('Open image')

        self.socket: 'Socket' = ImageSocket(self.id)

        self.path: 'Path' = Path()

    @property
    def options(self) -> ['Option']:
        return [
            self.path
        ]

    @property
    def x(self) -> ['Socket']:
        return []

    @property
    def y(self) -> ['Socket']:
        return [self.socket]

    def evaluate(self):
        image = imread(self.path)

        self.socket.data = Image(image)
