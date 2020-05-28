from napari.editor.option.option import Option


class Path(Option):
    def __init__(self, path):
        super().__init__()

        self.data = path
