from ..socket import Socket


class ImageSocket(Socket):
    def __init__(self, node_id: int):
        super().__init__(node_id)

    @property
    def data(self) -> 'Image':
        return self._data

    @data.setter
    def data(self, image: 'Image'):
        self._data = image
