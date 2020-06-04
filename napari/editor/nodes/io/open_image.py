from imageio import imread

from napari.editor.node import Node
from ...setting.path_setting import PathSetting
from ...socket.layer.image_socket import ImageSocket
from ....layers import Image


class OpenImage(Node):
    def __init__(self):
        super().__init__('Open image', "1.0.0")

        self.path = PathSetting("Path", required=True)

        self.image = ImageSocket("Image", self.id)

    @property
    def settings(self) -> ['Option']:
        return [self.path]

    @property
    def x(self) -> ['Socket']:
        return []

    @property
    def y(self) -> ['Socket']:
        return [self.image]

    def evaluate(self):
        data = imread(self.path)

        self.image.data = Image(data)
