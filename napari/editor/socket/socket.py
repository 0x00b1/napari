from abc import abstractmethod

from napari.editor.serializable import Serializable


class Socket(Serializable):
    connections: ['Connection'] = []

    def __init__(self, name: str, node_id: int):
        super().__init__()

        self.name = name

        self.node_id = node_id

        self._data = None

    @property
    @abstractmethod
    def data(self):
        return self.data

    @data.setter
    @abstractmethod
    def data(self, value):
        self._data = value

    def connect(self, connection: 'Connection'):
        self.connections += [connection]

    def connected(self, connection: 'Connection') -> bool:
        return connection in self.connections

    def deserialize(
        self,
        serialized: dict,
        callbacks: dict = {},
        deserialized: dict = {},
        restore_id: bool = True,
    ):
        pass

    def disconnect(self, connection: 'Connection'):
        if connection in self.connections:
            self.connections.remove(connection)

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'kind': self.__class__.__name__,
            'name': self.name,
            'node_id': self.node_id,
        }
