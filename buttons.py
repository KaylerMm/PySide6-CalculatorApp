from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from display import Display
from equation_info import EquationInfo
from main_window import MainWindow
from utils import valid_input, is_special_key
from variables import MEDIUM_FONT_SIZE

class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.config_style()

    def config_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setProperty('cssClass', 'specialButton')

class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, info: EquationInfo, window: \
                 MainWindow, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None
        
        self._make_grid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    # Creates the whole virtual input keyboard
    def _make_grid(self):
        self.display.enter_Triggered.connect(self._eq)
        self.display.del_Triggered.connect(self.display.backspace)
        self.display.esc_Triggered.connect(self._clear)
        self.display.input_Triggered.connect(self._display_input)
        self.display.operator_Triggered.connect(self.set_left_op)

        for i, row in enumerate(self._grid_mask):
            for j, key in enumerate(row):

                # Ignores empty button and expands 0
                if key == '':
                    continue
                elif key == '0':
                    button = Button(key)
                    self.addWidget(button, i, 0, 1, 2)
                    slot = self._make_slot(self._display_input, button)
                    self._connect_button_clicked(button, slot)
                
                # Special buttons
                elif is_special_key(key):
                    button = Button(key)
                    self.addWidget(button, i, j)
                    self._set_special_button(button)

                # Regular buttons
                else:
                    button = Button(key)
                    self.addWidget(button, i, j)

                    slot = self._make_slot(self._display_input, key)
                    self._connect_button_clicked(button, slot)

    def _connect_button_clicked(self, button, slot):
        button.clicked.connect(slot) # type: ignore

    def _set_special_button(self, button):
        text = button.text()

        if text == 'C':
            self._connect_button_clicked(button, self._clear)
        
        elif text in '+-*/^':
            self._connect_button_clicked(
                button,
                 self._make_slot(self.set_left_op, text)
                 )
            
        elif text == '=':
            self._connect_button_clicked(button, self._eq)
            
        elif text == '◀':
            self._connect_button_clicked(button, self.display.backspace)

    def _make_slot(self, function, *args, **kwargs):
        @Slot(bool)
        def real_slot():
            function(*args, **kwargs)
        return real_slot

    @Slot()
    def _display_input(self, text):
        display_text = self.display.text() + text

        if not valid_input(display_text):
            return
        
        self.display.insert(text)

    @Slot()
    def _clear(self):
        self._left = None
        self._op = None
        self._right = None
        self.equation = None
        self.display.clear()
    
    @Slot()
    def set_left_op(self, text):
        display_text = self.display.text()
        self.display.clear()

        if not valid_input(display_text) and self._left is None:
            self._show_error('Você ainda não digitou nada!')
            return
        
        if self._left is None:
            self._left = float(display_text)

        self._op = text
        self.equation = f'{self._left} {self._op} '

    @Slot()
    def _eq(self):
        display_text = self.display.text()

        if not valid_input(display_text):
            self._show_error('Conta incompleta!')
            return
        
        self._right = float(display_text)
        self.equation = f'{self._left} {self._op} {self._right}'

        try:
            if '^' == self.equation:
                result = eval(self.equation.replace('^','**'))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            result = None
            self._show_error('Erro: divisão por zero!')
        except OverflowError:
            result = None
            self._show_error('Não é possível realizar esta conta!')

        # Clears display and shows final equation in 'equation info'
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')

        # Saves last result in first operand side
        self._left = result
        self.right = None

    # Setting QMessageBox
    def _show_error(self, text):
        msg_box = self.window.create_msg_box()
        msg_box.setText(text)
        msg_box.setIcon(msg_box.Icon.Critical)
        msg_box.setStandardButtons(msg_box.StandardButton.Ok)

        msg_box.exec()
