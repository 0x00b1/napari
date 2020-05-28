from qtpy.QtGui import QFocusEvent
from qtpy.QtWidgets import QTextEdit


class TextSetting(QTextEdit):
    def focusInEvent(self, event: QFocusEvent):
        self.parentWidget().setEditingFlag(True)

        super().focusInEvent(event)

    def focusOutEvent(self, event: QFocusEvent):
        self.parentWidget().setEditingFlag(False)

        super().focusOutEvent(event)
