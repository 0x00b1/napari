from napari._qt.editor.widgets.connection._connection_graphics_path_item import (
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
