from skimage.morphology import disk

from ..node import Node
from ...setting.integer_setting import IntegerSetting
from ...socket.layer.image_socket import ImageSocket
from ....layers import Image


class Disk(Node):
    def __init__(self):
        super().__init__("Disk")

        self.radius = IntegerSetting("Radius", required=True)

        self.socket = ImageSocket("Disk", self.id)

    @property
    def options(self) -> ['Setting']:
        return [self.radius]

    @property
    def x(self) -> ['Socket']:
        return []

    @property
    def y(self) -> ['Socket']:
        return [self.socket]

    def evaluate(self):
        data = disk(radius=self.radius.data)

        self.socket.data = Image(data)
