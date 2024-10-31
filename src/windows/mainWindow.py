from PySide6.QtCore import QThreadPool, QSize
from PySide6.QtGui import QPixmap, QFont, QColor, QPainter
from PySide6.QtWidgets import (QMainWindow, QSpacerItem, QSizePolicy, QApplication, QFrame, QLabel, QHBoxLayout,
                               QVBoxLayout)
from src.services.mainWindow import MainWindowController
from src.ui.ui_main import Ui_MainWindow
from PySide6 import QtCore
from src.windows.pieChart import PieChart
from src.windows.barChart import BarChart
from collections import namedtuple

Data = namedtuple('Data', ['name', 'value', 'primary_color', 'secondary_color'])

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, controller: MainWindowController):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.__controller = controller
        self.__init()
        self.triggers_connect()

    def __init(self):
        self.pages_dict = {'panel': [self.page_panel, [self.open_panel_btn, self.open_panel_btn_1]],
                           'edit': [self.page_edit, [self.open_edit_btn, self.open_edit_btn_1, self.add_transaction_btn]],
                           'settings': [self.page_settings, [self.open_settings_btn, self.open_settings_btn_1]]}
        self.current_page = self.pages_dict['panel'][0]
        self.new_thread = QThreadPool()
        self.toggle_menu_frame()
        self.clean_transactions()
        self.show_transactions()
        self.update_main_info()
        self.draw_pie_chart()
        self.draw_bar_chart()

    @QtCore.Slot()
    def triggers_connect(self) -> None:
        self.menu_btn.clicked.connect(self.toggle_menu_frame)
        for k, v in self.pages_dict.items():
            for btn in v[1]:
                btn.clicked.connect(getattr(self, f"toggle_page_to_{k}"))

    def toggle_page_to_panel(self) -> None:
        self.main_pages_widget.setCurrentWidget(self.page_panel)
        self.draw_bar_chart()
        self.draw_pie_chart()

    def toggle_page_to_edit(self) -> None:
        self.main_pages_widget.setCurrentWidget(self.page_edit)

    def toggle_page_to_settings(self) -> None:
        self.main_pages_widget.setCurrentWidget(self.page_settings)

    def update_main_info(self):
        self.__controller.update_info()
        self.balance_label.setText(f"{self.__controller.balance:.1f}")
        self.savings_label.setText(f"{self.__controller.savings:.1f}")
        self.total_income_label.setText(f"{self.__controller.total_income:.2f}")
        self.total_outcome_label.setText(f"{self.__controller.total_outcome:.2f}")

    def draw_bar_chart(self):
        chart = BarChart()
        self.bar_chart.setChart(chart)
        self.bar_chart.setRenderHint(QPainter.RenderHint.Antialiasing)

    def draw_pie_chart(self):
        self.__controller.db.get_all_outcome()
        self.__controller.db.get_all_transaction_types()
        transactions = self.__controller.db.get_result()
        types = self.__controller.db.get_result()
        datas = list()
        color_types = dict()
        types_dict = {}

        for i in types:
            color_types[i[1]] = [i[3], i[4]]

        for i in transactions:
            if i[2] in list(types_dict):
                types_dict[i[2]][0] = types_dict[i[2]][0] + i[5]
            else:
                types_dict[i[2]] = [i[5], color_types[i[2]][0], color_types[i[2]][1]]
        print(types_dict)

        for k, v in types_dict.items():
            datas.append(Data(v[2], v[0], QColor(f"#{v[1]}"), QColor(f"#{v[1]}")))
        print(datas)

        chart = PieChart(datas)
        chart.setBackgroundVisible(False)

        self.pie_chart.setChart(chart)
        self.pie_chart.setRenderHint(QPainter.RenderHint.Antialiasing)


    def toggle_menu_frame(self) -> None:
        if self.menu_bar_frame.isVisible():
            self.short_menu_bar_frame.setVisible(True)
            self.menu_bar_frame.setVisible(False)
        else:
            self.short_menu_bar_frame.setVisible(False)
            self.menu_bar_frame.setVisible(True)

    def clean_transactions(self) -> None:
        for frame in self.transactions_frame.children():
            if frame.objectName() == "verticalLayout_12":
                continue
            elif frame.objectName() == "not_found_frame":
                frame.setVisible(False)
                continue
            frame.deleteLater()

    def show_transactions(self) -> None:
        self.__controller.db.get_all_transactions()
        res = self.__controller.db.get_result()
        font_i = QFont()
        font_i.setFamilies([u"Inter Hewn"])
        font_g = QFont()
        font_g.setFamilies([u"GOST type B"])
        if len(res) <= 0:
            self.not_found_frame.setVisible(True)
        else:
            i = 0
            for tr in res:
                # TODO: add graphicshadow
                self.__controller.db.get_transaction_type(tr[2])
                transaction_type_info = self.__controller.db.get_result()
                name = f"transaction_frame_{i}"
                setattr(self, name, QFrame(self.transactions_frame))
                transaction_frame: QFrame = getattr(self, name)
                transaction_frame.setObjectName(name)
                # transaction_frame.setStyleSheet("border: 1px solid #ffffff")
                transaction_frame.setMinimumSize(QSize(0, 30))
                transaction_frame.setFrameShape(QFrame.Shape.NoFrame)
                transaction_frame.setFrameShadow(QFrame.Shadow.Raised)

                name = f"tr_{i}_qhboxlayout"
                setattr(self, name, QHBoxLayout(transaction_frame))
                transaction_hbox: QHBoxLayout = getattr(self, name)
                transaction_hbox.setObjectName(name)
                transaction_hbox.setContentsMargins(0, 0, 0, 0)

                name = f"tr_{i}_img"
                setattr(self, name, QLabel(transaction_frame))
                transaction_image: QLabel = getattr(self, name)
                transaction_image.setObjectName(name)
                transaction_image.setMinimumSize(QSize(18, 18))
                transaction_image.setMaximumSize(QSize(18, 18))
                transaction_image.setPixmap(QPixmap(f":/icons/icons/{transaction_type_info[2]}"))

                transaction_hbox.addWidget(transaction_image)

                name = f"transaction_{i}_vbox"
                setattr(self, name, QFrame(transaction_frame))
                transaction_vbox: QFrame = getattr(self, name)
                transaction_vbox.setObjectName(name)
                transaction_vbox.setMinimumSize(QSize(30, 0))
                transaction_vbox.setMaximumSize(QSize(100, 16777215))
                transaction_vbox.setStyleSheet("margin-left: 3px;")
                transaction_vbox.setFrameShape(QFrame.Shape.NoFrame)
                transaction_vbox.setFrameShadow(QFrame.Shadow.Raised)

                name = f"transaction_{i}_vbox_vl"
                setattr(self, name, QVBoxLayout(transaction_vbox))
                transaction_vbox_vl: QVBoxLayout = getattr(self, name)
                transaction_vbox_vl.setObjectName(name)
                transaction_vbox_vl.setSpacing(0)
                transaction_vbox_vl.setContentsMargins(0, 0, 0, 0)

                name = f"transaction_{i}_title"
                setattr(self, name, QLabel(transaction_vbox))
                transaction_title: QLabel = getattr(self, name)
                transaction_title.setObjectName(name)
                transaction_title.setFont(font_i)
                transaction_title.setText(str(tr[3]))
                transaction_title.setMinimumSize(QSize(200, 0))


                transaction_vbox_vl.addWidget(transaction_title)

                name = f"transaction_{i}_description"
                setattr(self, name, QLabel(transaction_vbox))
                transaction_desc: QLabel = getattr(self, name)
                transaction_desc.setObjectName(name)
                transaction_desc.setText(str(tr[4]))
                transaction_desc.setFont(font_g)

                transaction_vbox_vl.addWidget(transaction_desc)

                transaction_hbox.addWidget(transaction_vbox)

                name = f"transaction_{i}_hspacer"
                setattr(self, name, QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
                transaction_hbox.addItem(getattr(self, name))

                name = f"transaction_{i}_amount"
                setattr(self, name, QLabel(transaction_frame))
                transaction_amount: QLabel = getattr(self, name)
                transaction_amount.setObjectName(name)
                transaction_amount.setText(str(tr[5])+" ₽")
                transaction_amount.setFont(font_i)

                transaction_hbox.addWidget(transaction_amount)

                self.verticalLayout_12.addWidget(transaction_frame)

                i += 1



def start_app():
    import sys
    app = QApplication(sys.argv)

    main_window_controller = MainWindowController()
    main_window = MainWindow(main_window_controller)
    main_window.show()

    sys.exit(app.exec())
