from abc import abstractmethod
from typing import Optional

from napari.editor.serializable import Serializable


class Node(Serializable):
    invalidated: bool = False

    modified: bool = False

    def __init__(
        self,
        name: str,
        version: str,
        settings: Optional['Setting'] = None,
        x: Optional['Socket'] = None,
        y: Optional['Socket'] = None,
    ):
        super().__init__()

        if not x:
            x = []

        if not y:
            y = []

        if not settings:
            settings = []

        self.kind = self.__class__.__name__

        self.name = name

        self.version = version

        self._settings = settings

        self._x = x
        self._y = y

    @property
    @abstractmethod
    def settings(self) -> ['Setting']:
        return self._settings

    @settings.setter
    @abstractmethod
    def settings(self, value: ['Setting']):
        self._settings = value

    @property
    @abstractmethod
    def x(self) -> ['Socket']:
        return self._x

    @x.setter
    @abstractmethod
    def x(self, value: ['Socket']) -> None:
        self._x = value

    @property
    @abstractmethod
    def y(self) -> ['Socket']:
        return self._y

    @y.setter
    @abstractmethod
    def y(self, value: ['Socket']) -> None:
        self._y = value

    def children(self) -> ['Node']:
        if not self.y:
            return []

        nodes: ['Node'] = []

        for socket in self.y:
            for edge in socket.connections:
                nodes += [edge.spouse(socket).node]

        return nodes

    def deserialize(
        self,
        serialized: dict,
        callbacks: dict = {},
        deserialized: dict = {},
        restore_id: bool = True,
    ):
        if restore_id:
            self.id = serialized['id']

        deserialized[serialized['id']] = self

        self.name = serialized['name']

        def key(item: 'Socket'):
            return item['index'] + item['position'] * 10000

        serialized['x'].sort(key=key)
        serialized['y'].sort(key=key)

        for serialized_x_socket in serialized['x']:
            existing_x_socket: Optional['Socket'] = None

            for socket in self.x:
                if socket.index == serialized_x_socket['index']:
                    existing_x_socket = socket

                    break

            if existing_x_socket is None:
                existing_x_socket = serialized_x_socket["kind"](self)

                self.x += [existing_x_socket]

            existing_x_socket.deserialize(
                callbacks=callbacks,
                deserialized=deserialized,
                restore_id=restore_id,
                serialized=serialized_x_socket,
            )

        for serialized_y_socket in serialized['y']:
            existing_y_socket: Optional['Socket'] = None

            for socket in self.y:
                if socket.index == serialized_y_socket['index']:
                    existing_y_socket = socket

                    break

            if existing_y_socket is None:
                existing_y_socket = serialized_y_socket["kind"](self)

                self.y += [existing_y_socket]

            existing_y_socket.deserialize(
                callbacks=callbacks,
                deserialized=deserialized,
                restore_id=restore_id,
                serialized=serialized_y_socket,
            )

    def modify(self, modified: bool = True):
        self.modified = modified

        if self.modified:
            self.on_modify()

    def modify_children(self, modified: bool = True):
        for child in self.children():
            child.node.modify(modified)

    def modify_grandchildren(self, modified: bool = True):
        for child in self.children():
            child.node.modify(modified)

            child.node.modify_children(modified)

    @abstractmethod
    def evaluate(self):
        self.modify(False)

        self.invalidate(False)

    def evaluate_children(self):
        for child in self.children():
            child.node.evaluate()

    def invalidate(self, invalidated: bool = True):
        self.invalidated = invalidated

        if self.invalidated:
            self.on_invalidate()

    def invalidate_children(self, invalidated: bool = True):
        for child in self.children():
            child.node.invalidate(invalidated)

    def invalidate_grandchildren(self, invalidated: bool = True):
        for child in self.children():
            child.node.invalidate(invalidated)

            child.node.invalidate_children(invalidated)

    def on_modify(self):
        pass

    def on_invalidate(self):
        pass

    def on_update_input(self):
        self.modify()

        self.modify_grandchildren()

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "kind": self.kind,
            "name": self.name,
            "version": self.version,
            "x": [socket.serialize() for socket in self.x],
            "y": [socket.serialize() for socket in self.y],
        }
