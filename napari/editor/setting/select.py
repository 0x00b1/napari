from .setting import Setting


class Select(Setting):
    def __init__(self, name: str, default: [str] = None, required: bool = False):
        super().__init__(name, required)

        self.data: [str] = default
