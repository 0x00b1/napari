from napari.editor.serializable import Serializable


class Connection(Serializable):
    def __init__(self, source: 'Socket', destination: 'Socket'):
        super().__init__()

        self._source = None
        self._destination = None

        self.source = source
        self.destination = destination

    @property
    def destination(self) -> 'Socket':
        return self._destination

    @destination.setter
    def destination(self, socket: 'Socket'):
        if self._destination is not None:
            self._destination.disconnect(self)

        self._destination = socket

        if self.destination is not None:
            self.destination.connect(self)

    @property
    def source(self) -> 'Socket':
        return self._source

    @source.setter
    def source(self, socket: 'Socket'):
        if self._source is not None:
            self._source.disconnect(self)

        self._source = socket

        if self.source is not None:
            self.source.connect(self)

    def deserialize(
        self,
        serialized: dict,
        callbacks: dict = {},
        deserialized: dict = {},
        restore_id: bool = True,
    ):
        if restore_id:
            self.id = serialized['id']

        self.source = deserialized[serialized['source']]

        self.destination = deserialized[serialized['destination']]

    def disconnect(self):
        self.destination = None
        self.source = None

    def reconnect(self, source: 'Socket', destination: 'Socket'):
        if self.source == destination:
            self.source = destination
        elif self.destination == source:
            self.destination = source

    def serialize(self) -> dict:
        serialized = {"destination_id": None, "id": self.id, "source_id": None}

        if self.destination:
            serialized["destination_id"] = self.destination.id

        if self.source:
            serialized["source_id"] = self.source.id

        return serialized

    def spouse(self, socket: 'Socket'):
        if socket == self.destination:
            return self.source
        else:
            return self.destination
