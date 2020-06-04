from ..graph import Graph
from ..widgets.editor_window import EditorWindow
from ..widgets.scene import Scene
from ..widgets.view import View
from ..widgets.widget import Widget
from .graph_controller import GraphController


class EditorController:
    scene: 'Scene'
    view: 'View'
    widget: 'Widget'
    window: 'EditorWindow'

    def __init__(self):
        self.graph = Graph()

        self.graph_controller = GraphController()

    def open(self, parent):
        self.window = EditorWindow(parent)

        self.scene = Scene()

        self.view = View(self.scene)
        self.view.scene = self.scene
        self.view.setScene(self.scene)

        self.widget = Widget()

        self.widget.layout.addWidget(self.view)

        self.window.show()
