from PySide6.QtGui import QColor, QTextCharFormat, QTextCursor

from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name


class HighlightSlot:
    def __init__(self, widget):
        self._widget = widget

    def widget(self):
        return self._widget

    def _create_format(self, token_style):
        text_format = QTextCharFormat()

        color = token_style["color"]
        if color:
            text_format.setForeground(QColor(f"#{color}"))

        background = token_style["bgcolor"]
        if background:
            text_format.setBackground(QColor(f"#{background}"))

        if token_style["bold"]:
            text_format.setFontWeight(700)

        if token_style["italic"]:
            text_format.setFontItalic(True)

        if token_style["underline"]:
            text_format.setFontUnderline(True)

        return text_format

    def execute(self):
        document = self.widget().document()
        lexer = get_lexer_by_name(
            self.widget().syntax(),
            stripnl=False,
            ensurenl=False,
        )
        style = get_style_by_name(self.widget().theme())
        text = self.widget().toPlainText()

        selections = []
        position = 0

        for token_type, value in lex(text, lexer):
            token_length = len(value)
            if token_length == 0:
                continue

            token_style = style.style_for_token(token_type)
            if not any(token_style[key] for key in ("color", "bgcolor", "bold", "italic", "underline")):
                position += token_length
                continue

            cursor = QTextCursor(document)
            cursor.setPosition(position)
            cursor.setPosition(position + token_length, QTextCursor.KeepAnchor)

            selection = self.widget().ExtraSelection()
            selection.cursor = cursor
            selection.format = self._create_format(token_style)
            selections.append(selection)

            position += token_length

        self.widget().setExtraSelections(selections)
