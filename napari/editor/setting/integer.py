from .setting import Setting


class Integer(Setting):
    def __init__(self, value: int):
        super().__init__()

        self.value: int = value
