from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from variables import SMALL_FONT_SIZE

class EquationInfo(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.set_style()

    
    def set_style(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)