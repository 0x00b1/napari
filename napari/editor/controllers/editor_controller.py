from .graph_controller import GraphController
from napari.editor.widgets.editor_window import EditorWindow
from ..graph import Graph


class EditorController:
    editor_window: 'EditorWindow'

    def __init__(self):
        self.graph = Graph()

        self.graph_controller = GraphController()

    def open(self, parent):
        self.editor_window = EditorWindow(parent)

        self.editor_window.show()
