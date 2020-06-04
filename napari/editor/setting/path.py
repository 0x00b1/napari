from .setting import Setting


class Path(Setting):
    def __init__(self, name: str, default: str = None, required: bool = False):
        super().__init__(name, required)

        self.data: str = default
