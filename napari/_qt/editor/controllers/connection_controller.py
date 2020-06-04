from napari.editor.widgets import (
    ConnectionGraphicsPathItem,
)
from ....editor.connection import Connection


class ConnectionController:
    def __init__(
        self, source: 'SocketController', destination: 'SocketController'
    ):
        self.connection = Connection(
            source=source.socket, destination=destination.socket,
        )

        self.connection_widget = ConnectionGraphicsPathItem(self.connection)

    def disconnect(self):
        pass
