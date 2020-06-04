from .setting import Setting


class BooleanSetting(Setting):
    def __init__(self, name: str, default: bool = None, required: bool = False):
        super().__init__(name, required)

        self.data: bool = default
