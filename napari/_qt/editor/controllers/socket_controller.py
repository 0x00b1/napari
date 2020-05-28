from napari._qt.editor.widgets._socket_graphics_item import SocketGraphicsItem
from napari.editor.socket.socket import Socket


class SocketController:
    def __init__(self, node_controller: 'NodeController'):
        self.node_controller = node_controller

        self.node = self.node_controller.node

        self.graph_controller = self.node_controller.graph_controller
        self.graph_widget = self.graph_controller.graph_widget

        self.socket = Socket(self.node.id)

        self.socket_widget = SocketGraphicsItem(self.socket)

    def destroy_socket(self):
        self.socket_widget.setParentItem(None)

        self.graph_widget.removeItem(self.socket_widget)

        del self.socket_widget
