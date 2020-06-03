from napari.editor.serializable import Serializable


class Setting(Serializable):
    data: any

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
            "kind": self.__class__.__name__
        }
