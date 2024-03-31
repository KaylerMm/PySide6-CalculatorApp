import sys

from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from PySide6.QtGui import QIcon
from display import Display
from equation_info import EquationInfo
from buttons import ButtonsGrid
from styles import set_theme
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    # Creates the application
    app = QApplication(sys.argv)
    window = MainWindow()

    # Sets application theme
    theme = set_theme()
    app.setStyleSheet(theme)

    # Sets window icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Equation info
    info = EquationInfo('')
    window.add_widget_to_v_layout(info)

    # Display
    display = Display()
    window.add_widget_to_v_layout(display)

    # Buttons grid
    buttons_grid = ButtonsGrid(display, info, window)
    window.vertical_layout.addLayout(buttons_grid)

    # Runs application
    window.adjust_fixed_size()
    window.show()
    app.exec()
