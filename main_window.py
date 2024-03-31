from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args,**kwargs)

        # Setting basic layout
        self.central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)
        self.setWindowTitle('Calculadora - Kayler')

        # Window title
        self.setCentralWidget(self.central_widget)

    # Sets window size and locks it
    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Adds widgets to vertical layout
    def add_widget_to_v_layout(self, widget: QWidget):
        self.vertical_layout.addWidget(widget)

    def create_msg_box(self):
        return QMessageBox(self)