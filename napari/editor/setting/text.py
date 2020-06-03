from .setting import Setting


class Text(Setting):
    def __init__(self, value: str):
        super().__init__()

        self.value: str = value
