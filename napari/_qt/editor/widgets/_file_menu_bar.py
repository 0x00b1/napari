from qtpy.QtWidgets import QAction, QMenuBar


class FileMenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        new_action = QAction(
            parent=self,
            shortcut='Ctrl+N',
            statusTip="Create new graph",
            text='&New',
            triggered=self.editor.on_new,
        )

        self.addAction(new_action)

        open_action = QAction(
            parent=self,
            shortcut='Ctrl+O',
            statusTip="Open file",
            text='&Open',
            triggered=self.editor.on_open,
        )

        self.addAction(open_action)

        save_action = QAction(
            parent=self,
            shortcut='Ctrl+S',
            statusTip="Save file",
            text='&Save',
            triggered=self.editor.on_save,
        )

        self.addAction(save_action)

        save_as_action = QAction(
            parent=self,
            shortcut='Ctrl+Shift+S',
            statusTip="Save file as...",
            text='Save &As...',
            triggered=self.editor.on_save_as,
        )

        self.addAction(save_as_action)

        self.addSeparator()

        close_action = QAction(
            parent=self,
            shortcut='Ctrl+Q',
            statusTip="Close",
            text='&Close',
            triggered=self.editor.on_close,
        )

        self.addAction(close_action)
