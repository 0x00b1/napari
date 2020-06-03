from .setting import Setting


class Path(Setting):
    def __init__(self, data: str):
        super().__init__()

        self.data: str = data
