from .setting import Setting


class Integer(Setting):
    def __init__(self, data: int):
        super().__init__()

        self.data: int = data
