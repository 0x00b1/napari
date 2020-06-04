from .graph_controller import GraphController
from napari.editor.widgets.editor_window import EditorWindow
from ..graph import Graph


class EditorController:
    def __init__(self):
        self.graph = Graph()

        self.graph_controller = GraphController()

        self.editor_window = EditorWindow()
