from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MIN_WIDTH
from utils import is_empty, is_special_key

class Display(QLineEdit):
    enter_Triggered = Signal()
    del_Triggered = Signal()
    esc_Triggered = Signal()
    input_Triggered = Signal(str)
    operator_Triggered = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_style()

    def set_style(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for i in range(4)])
        self.setMinimumWidth(MIN_WIDTH)
    
    # Keys from keyboard
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        # Enter/Equal key
        if key == KEYS.Key_Enter | KEYS.Key_Return | KEYS.Key_Equal:
            self.enter_Triggered.emit()
            return event.ignore()

        # Backspace key
        elif key == KEYS.Key_Backspace | KEYS.Key_Delete | KEYS.Key_D:
            self.del_Triggered.emit()
            return event.ignore()

        # Escape key
        elif key == KEYS.Key_Escape | KEYS.Key_C:
            self.esc_Triggered.emit()
            return event.ignore()

        # Blank/Function keys
        if is_empty(text):
            return event.ignore()
        
        elif not is_special_key(text):
            self.input_Triggered.emit(text)
            return event.ignore()
        
        if KEYS.Key_Plus | KEYS.Key_Minus | KEYS.Key_Asterisk | KEYS.Key_Slash:
            self.operator_Triggered.emit(text)