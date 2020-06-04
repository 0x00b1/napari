from qtpy.QtWidgets import QAction, QMenuBar


class EditMenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        edit_menu_bar = self.menuBar()

        self.edit_menu = edit_menu_bar.addMenu('&Edit')

        self.edit_menu.addAction(QAction(
            parent=self,
            shortcut='Ctrl+Z',
            statusTip="Undo last operation",
            text='&Undo',
            triggered=self.editor.on_undo,
        ))

        self.edit_menu.addAction(QAction(
            parent=self,
            shortcut='Ctrl+Shift+Z',
            statusTip="Redo last operation",
            text='&Redo',
            triggered=self.editor.on_redo,
        ))

        self.addSeparator()

        self.addAction()

        self.edit_menu.addAction(QAction(
            parent=self,
            shortcut='Ctrl+X',
            statusTip="Cut to clipboard",
            text='Cu&t',
            triggered=self.editor.on_cut,
        ))

        self.addAction()

        self.edit_menu.addAction(QAction(
            parent=self,
            shortcut='Ctrl+C',
            statusTip="Copy to clipboard",
            text='&Copy',
            triggered=self.editor.on_copy,
        ))

        self.addAction()

        self.edit_menu.addAction(QAction(
            parent=self,
            shortcut='Ctrl+V',
            statusTip="Paste from clipboard",
            text='&Paste',
            triggered=self.editor.on_paste,
        ))

        self.addAction()

        self.edit_menu.addAction(QAction(
            parent=self,
            shortcut='Del',
            statusTip="Delete selected items",
            text='&Delete',
            triggered=self.editor.on_delete,
        ))

        self.addAction()

