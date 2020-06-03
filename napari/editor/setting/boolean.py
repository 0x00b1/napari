from .setting import Setting


class Boolean(Setting):
    def __init__(self, data: bool):
        super().__init__()

        self.data: bool = data
