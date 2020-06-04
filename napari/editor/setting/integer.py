from .setting import Setting


class Integer(Setting):
    def __init__(self, name: str, default: int = None, required: bool = False):
        super().__init__(name, required)

        self.data: int = default
