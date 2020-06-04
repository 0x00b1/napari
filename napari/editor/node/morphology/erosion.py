from skimage.morphology import erosion

from ..node import Node
from ...setting.integer_setting import IntegerSetting
from ...socket.layer.image_socket import ImageSocket
from ....layers import Image


class Erosion(Node):
    def __init__(self):
        super().__init__("Erosion")

        self.radius = IntegerSetting("Radius", required=True)

        self.image = ImageSocket("Image", self.id)

        self.structure = ImageSocket("Structure", self.id)

        self.eroded = ImageSocket("Eroded", self.id)

    @property
    def options(self) -> ['Setting']:
        return [self.radius]

    @property
    def x(self) -> ['Socket']:
        return [self.image, self.structure]

    @property
    def y(self) -> ['Socket']:
        return [self.eroded]

    def evaluate(self):
        data = erosion(self.image.data, self.structure.data)

        self.eroded.data = Image(data)
