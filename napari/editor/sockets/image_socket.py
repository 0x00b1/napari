from napari.editor.socket import Socket


class ImageSocket(Socket):
    @property
    def data(self) -> 'Image':
        return self._data

    @data.setter
    def data(self, image: 'Image'):
        self._data = image
