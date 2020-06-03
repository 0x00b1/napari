from qtpy.QtWidgets import QMenu

from ._edit_menu_bar import EditMenuBar


class EditorMenu(QMenu):
    def __init__(self):
        super().__init__()

        edit_menu_bar = EditMenuBar()

        self.edit_menu = edit_menu_bar.addMenu('&Edit')
