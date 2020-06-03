from napari.editor.serializable import Serializable


class Setting(Serializable):
    value: any

    def deserialize(
        self,
        serialized: dict,
        callbacks: dict = {},
        deserialized: dict = {},
        restore_id: bool = True,
    ):
        pass

    def serialize(self) -> dict:
        pass
