from .setting import Setting


class Boolean(Setting):
    def __init__(self, value: bool):
        super().__init__()

        self.value: bool = value
