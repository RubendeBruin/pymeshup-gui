from PySide6.QtGui import QColor, QSyntaxHighlighter, QTextCharFormat

from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name


class PygmentsHighlighter(QSyntaxHighlighter):
    """
    Syntax highlighter backed by Pygments, implemented as a QSyntaxHighlighter.

    Pygments lexes the entire document at once (required for correct multi-line
    token handling, e.g. triple-quoted strings).  The resulting token stream is
    converted into a per-block format cache so that Qt's highlightBlock() callback
    can apply formats with simple setFormat() calls — no ExtraSelections needed.
    """

    def __init__(self, document, syntax="Python", theme="solarized-light"):
        # Initialise fields *before* super().__init__ because Qt may call
        # highlightBlock() during the parent constructor via rehighlight().
        self._syntax = syntax
        self._theme = theme
        self._block_formats: dict[int, list] = {}  # block_num -> [(start, len, fmt)]
        self._rehighlighting = False

        super().__init__(document)

        document.contentsChange.connect(self._on_contents_change)
        self._rebuild_block_formats()

    # ------------------------------------------------------------------
    # Public API (mirrors the old widget.setSyntax / setTheme interface)
    # ------------------------------------------------------------------

    def setSyntax(self, syntax: str) -> None:
        self._syntax = syntax
        self._rebuild_block_formats()
        self._full_rehighlight()

    def setTheme(self, theme: str) -> None:
        self._theme = theme
        self._rebuild_block_formats()
        self._full_rehighlight()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _on_contents_change(self, position: int, removed: int, added: int) -> None:
        """Triggered by real text edits; rebuilds the format cache and repaints."""
        if self._rehighlighting:
            return
        self._rebuild_block_formats()
        # Pygments needs global context, so all blocks must be re-highlighted
        # (not just the locally-dirty ones that Qt would normally repaint).
        self._full_rehighlight()

    def _full_rehighlight(self) -> None:
        self._rehighlighting = True
        try:
            self.rehighlight()
        finally:
            self._rehighlighting = False

    @staticmethod
    def _create_format(token_style: dict) -> QTextCharFormat:
        fmt = QTextCharFormat()
        if token_style["color"]:
            fmt.setForeground(QColor(f"#{token_style['color']}"))
        if token_style["bgcolor"]:
            fmt.setBackground(QColor(f"#{token_style['bgcolor']}"))
        if token_style["bold"]:
            fmt.setFontWeight(700)
        if token_style["italic"]:
            fmt.setFontItalic(True)
        if token_style["underline"]:
            fmt.setFontUnderline(True)
        return fmt

    def _rebuild_block_formats(self) -> None:
        """Lex the full document with pygments and build a per-block format map."""
        doc = self.document()
        if doc is None:
            self._block_formats = {}
            return

        text = doc.toPlainText()
        try:
            lexer = get_lexer_by_name(self._syntax, stripnl=False, ensurenl=False)
        except Exception:
            self._block_formats = {}
            return

        style = get_style_by_name(self._theme)
        block_formats: dict[int, list] = {}
        abs_pos = 0

        for token_type, value in lex(text, lexer):
            token_len = len(value)
            if not token_len:
                continue

            token_style = style.style_for_token(token_type)
            has_style = any(
                token_style[k] for k in ("color", "bgcolor", "bold", "italic", "underline")
            )

            if has_style:
                fmt = self._create_format(token_style)

                # A single pygments token can span multiple blocks (e.g. a
                # triple-quoted string).  Walk through the blocks it covers and
                # record a format run for each block, excluding block separators.
                remaining_start = abs_pos
                remaining_len = token_len

                while remaining_len > 0:
                    block = doc.findBlock(remaining_start)
                    if not block.isValid():
                        break

                    block_num = block.blockNumber()
                    block_start = block.position()
                    # block.length() includes the trailing newline; subtract it
                    # so we never colour the block separator itself.
                    text_end = block_start + max(block.length() - 1, 0)

                    if remaining_start >= text_end:
                        # We are sitting on the block separator — skip it.
                        remaining_start += 1
                        remaining_len -= 1
                        continue

                    chars_in_block = min(remaining_len, text_end - remaining_start)
                    rel_start = remaining_start - block_start

                    block_formats.setdefault(block_num, []).append(
                        (rel_start, chars_in_block, fmt)
                    )

                    remaining_start += chars_in_block
                    remaining_len -= chars_in_block

                    # Advance past the newline separator to reach the next block.
                    if remaining_len > 0 and remaining_start == text_end:
                        remaining_start += 1
                        remaining_len -= 1

            abs_pos += token_len

        self._block_formats = block_formats

    # ------------------------------------------------------------------
    # QSyntaxHighlighter override
    # ------------------------------------------------------------------

    def highlightBlock(self, text: str) -> None:
        block_num = self.currentBlock().blockNumber()
        for rel_start, length, fmt in self._block_formats.get(block_num, []):
            self.setFormat(rel_start, length, fmt)
