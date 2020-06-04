from skimage.filters import gaussian

from napari.editor.node import Node
from ...setting.integer_setting import IntegerSetting
from ...socket.layer.image_socket import ImageSocket
from ....layers import Image


class Gaussian(Node):
    def __init__(self):
        super().__init__("Gaussian", "1.0.0")

        self.sigma = IntegerSetting("Radius", default=1)

        self.image = ImageSocket("Image", self.id)

        self.response = ImageSocket("Response", self.id)

    @property
    def settings(self) -> ['Setting']:
        return [self.sigma]

    @property
    def x(self) -> ['Socket']:
        return [self.image]

    @property
    def y(self) -> ['Socket']:
        return [self.response]

    def evaluate(self):
        data = gaussian(self.image.data, sigma=self.sigma.data)

        self.response.data = Image(data)
