from .setting import Setting


class Text(Setting):
    def __init__(self, data: str):
        super().__init__()

        self.data: str = data
