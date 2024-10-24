import time

from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QMainWindow, QApplication
from src.services.mainWindow import MainWindowController
from src.ui.ui_main import Ui_MainWindow
from PySide6 import QtCore
from src.database.database import Database as Database

db = Database('database/database.db')


class MathWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, controller: MainWindowController):
        super(MathWindow, self).__init__()
        self.setupUi(self)
        self.__controller = controller
        self.__init()
        self.triggers_connect()

    def __init(self):
        self.new_thread = QThreadPool()
        self.toggle_menu_frame()
        self.clean_transactions()
        self.show_transactions()

    @QtCore.Slot()
    def triggers_connect(self) -> None:
        self.menu_btn.clicked.connect(self.toggle_menu_frame)

    def toggle_menu_frame(self) -> None:
        if self.menu_bar_frame.isVisible():
            self.short_menu_bar_frame.setVisible(True)
            self.menu_bar_frame.setVisible(False)
        else:
            self.short_menu_bar_frame.setVisible(False)
            self.menu_bar_frame.setVisible(True)

    def clean_transactions(self) -> None:
        for frame in self.transactions_frame.children():
            frame.deleteLater()

    def show_transactions(self) -> None:
        db.get_all_transactions()
        res = db.get_result()
        print(res)



def start_app():
    import sys
    app = QApplication(sys.argv)

    main_window_controller = MainWindowController()
    main_window = MathWindow(main_window_controller)
    main_window.show()

    sys.exit(app.exec())
