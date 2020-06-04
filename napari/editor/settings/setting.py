from napari.editor.serializable import Serializable


class Setting(Serializable):
    data: any

    def __init__(self, name: str, required: bool = False):
        super().__init__()

        self.kind: str = self.__class__.__name__

        self.metadata: dict = {}

        self.name = name

        self.required: bool = required

    def deserialize(
        self,
        serialized: dict,
        callbacks: dict = {},
        deserialized: dict = {},
        restore_id: bool = True,
    ):
        pass

    def serialize(self) -> dict:
        return {
            "data": self.data,
            "kind": self.kind,
            "metadata": self.metadata,
            "name": self.name,
            "required": self.required,
        }
