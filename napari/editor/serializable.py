from abc import ABC, abstractmethod


class Serializable(ABC):
    def __init__(self):
        self.id: int = id(self)

    @abstractmethod
    def deserialize(
        self,
        serialized: dict,
        callbacks: dict = {},
        deserialized: dict = {},
        restore_id: bool = True,
    ):
        pass

    @abstractmethod
    def serialize(self) -> dict:
        return {}
