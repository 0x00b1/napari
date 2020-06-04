from collections.abc import MutableMapping
from typing import Iterator, Optional

from napari.editor.serializable import Serializable


class Graph(MutableMapping, Serializable):
    connections: ['Connection'] = []

    nodes: ['Node'] = []

    _index: int = 0

    def __init__(self):
        super().__init__()

    def __delitem__(self, node: 'Node') -> None:
        if node in self.nodes:
            self.nodes.remove(node)

    def __getitem__(self, node_id: int) -> 'Node':
        for node in self.nodes:
            if node.id == node_id:
                return node

    def __iter__(self) -> Iterator['Node']:
        return self

    def __next__(self) -> 'Node':
        try:
            node = self.nodes[self._index]
        except IndexError:
            raise StopIteration

        self._index += 1

        return node

    def __setitem__(self, node_id: int, node: 'Node') -> None:
        self[node_id] = node

    def __len__(self) -> int:
        return len(self.nodes)

    def connect(self, connection: 'Connection'):
        self.connections += [connection]

    def deserialize(
        self,
        serialized: dict,
        callbacks: dict = {},
        deserialized: dict = {},
        restore_id: bool = True,
    ):
        if restore_id:
            self.id = serialized['id']

        nodes: ['Node'] = self.nodes.copy()

        for serialized_node in serialized['nodes']:
            existing: 'Node' = None

            for node in nodes:
                if node.id == serialized_node['id']:
                    existing = node

                    break

            if existing:
                existing.deserialize(
                    callbacks=callbacks,
                    deserialized=deserialized,
                    restore_id=restore_id,
                    serialized=serialized_node,
                )

                nodes.remove(existing)
            else:
                node = serialized_node["kind"](serialized_node)(self)

                node.deserialize(
                    callbacks=callbacks,
                    deserialized=deserialized,
                    restore_id=restore_id,
                    serialized=serialized_node,
                )

            node_callback = callbacks["on_deserialized_node"]

            if node_callback:
                node_callback(serialized_node)

        while nodes:
            node = nodes.pop()

            node.remove()

        connections: ['Connection'] = self.connections.copy()

        for serialized_connection in serialized['connections']:
            existing_connection: Optional['Connection'] = None

            for connection in connections:
                if connection.id == serialized_connection['id']:
                    existing_connection = connection

                    break

            if existing_connection:
                existing_connection.deserialize(
                    callbacks=callbacks,
                    deserialized=deserialized,
                    restore_id=restore_id,
                    serialized=serialized_connection,
                )

                connections.remove(existing_connection)

            connection_callback = callbacks["on_deserialized_connection"]

            if connection_callback:
                connection_callback(serialized_connection)

        while connections:
            connection = connections.pop()

            connection.remove()

    def disconnect(self, connection: 'Connection'):
        if connection in self.connections:
            self.connections.remove(connection)

    def serialize(self) -> dict:
        serialized = {
            "connections": [],
            "id": self.id,
            "nodes": [],
        }

        for node in self.nodes:
            serialized["nodes"] += [node.serialize()]

        for connection in self.connections:
            serialized["connections"] += [connection.serialize()]

        return serialized
