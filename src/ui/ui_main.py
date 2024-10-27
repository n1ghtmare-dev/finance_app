# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from src.ui import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1032, 685)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setBaseSize(QSize(1020, 680))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(20, 19, 50);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar_frame = QFrame(self.centralwidget)
        self.menu_bar_frame.setObjectName(u"menu_bar_frame")
        self.menu_bar_frame.setMinimumSize(QSize(150, 0))
        self.menu_bar_frame.setMaximumSize(QSize(150, 16777215))
        self.menu_bar_frame.setStyleSheet(u"background-color: rgb(29, 29, 65);\n"
"border-radius: 20px;\n"
"border-top-left-radius: 0;\n"
"border-bottom-left-radius: 0;")
        self.menu_bar_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_bar_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.menu_bar_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frame_3 = QFrame(self.menu_bar_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"margin: 5px 0;\n"
"background: 0;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Beverley"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_3)

        self.menu_dashboard_frame = QFrame(self.menu_bar_frame)
        self.menu_dashboard_frame.setObjectName(u"menu_dashboard_frame")
        self.menu_dashboard_frame.setMinimumSize(QSize(0, 40))
        self.menu_dashboard_frame.setStyleSheet(u"background-color: rgb(99, 89, 233);\n"
"border-radius: 0;")
        self.menu_dashboard_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_dashboard_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.menu_dashboard_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.menu_dashboard_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon-dashboard.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(18, 18))
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.label_2 = QLabel(self.menu_dashboard_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Inter Hewn"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-left: 5px;")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.menu_dashboard_frame)

        self.menu_settings_frame = QFrame(self.menu_bar_frame)
        self.menu_settings_frame.setObjectName(u"menu_settings_frame")
        self.menu_settings_frame.setMinimumSize(QSize(0, 40))
        self.menu_settings_frame.setStyleSheet(u"border-radius: 0;")
        self.menu_settings_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_settings_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.menu_settings_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.pushButton = QPushButton(self.menu_settings_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/Icon-settings.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.label_4 = QLabel(self.menu_settings_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin-left: 5px;")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.menu_settings_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.menu_bar_frame)

        self.short_menu_bar_frame = QFrame(self.centralwidget)
        self.short_menu_bar_frame.setObjectName(u"short_menu_bar_frame")
        self.short_menu_bar_frame.setEnabled(True)
        self.short_menu_bar_frame.setMinimumSize(QSize(50, 0))
        self.short_menu_bar_frame.setMaximumSize(QSize(50, 16777215))
        self.short_menu_bar_frame.setStyleSheet(u"background-color: rgb(29, 29, 65);\n"
"border-radius: 20px;\n"
"border-top-left-radius: 0;\n"
"border-bottom-left-radius: 0;")
        self.short_menu_bar_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.short_menu_bar_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.short_menu_bar_frame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, -1)
        self.frame_38 = QFrame(self.short_menu_bar_frame)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"margin: 5px 0;\n"
"background: 0;")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_30)

        self.label_33 = QLabel(self.frame_38)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)
        self.label_33.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_27.addWidget(self.label_33)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_31)


        self.verticalLayout_14.addWidget(self.frame_38)

        self.menu_dashboard_frame_2 = QFrame(self.short_menu_bar_frame)
        self.menu_dashboard_frame_2.setObjectName(u"menu_dashboard_frame_2")
        self.menu_dashboard_frame_2.setMinimumSize(QSize(0, 40))
        self.menu_dashboard_frame_2.setStyleSheet(u"background-color: rgb(99, 89, 233);\n"
"border-radius: 0;")
        self.menu_dashboard_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_dashboard_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.menu_dashboard_frame_2)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_32)

        self.pushButton_4 = QPushButton(self.menu_dashboard_frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(18, 18))
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)

        self.horizontalLayout_28.addWidget(self.pushButton_4)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_33)


        self.verticalLayout_14.addWidget(self.menu_dashboard_frame_2)

        self.menu_settings_frame_2 = QFrame(self.short_menu_bar_frame)
        self.menu_settings_frame_2.setObjectName(u"menu_settings_frame_2")
        self.menu_settings_frame_2.setMinimumSize(QSize(0, 40))
        self.menu_settings_frame_2.setStyleSheet(u"border-radius: 0;")
        self.menu_settings_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_settings_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.menu_settings_frame_2)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_34)

        self.pushButton_5 = QPushButton(self.menu_settings_frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(18, 18))

        self.horizontalLayout_29.addWidget(self.pushButton_5)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_35)


        self.verticalLayout_14.addWidget(self.menu_settings_frame_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.short_menu_bar_frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background: none;")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, -1, -1)
        self.frame_35 = QFrame(self.frame_2)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(50, 40))
        self.frame_36.setMaximumSize(QSize(50, 40))
        self.frame_36.setStyleSheet(u"background-color: rgb(29, 29, 65);\n"
"border: 0;\n"
"border-radius: 15px;\n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 0;")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_36)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.menu_btn = QPushButton(self.frame_36)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_btn.setStyleSheet(u"border: none;\n"
"background: none;\n"
"padding: 15px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/menu-icon.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.menu_btn.setIcon(icon2)

        self.verticalLayout_13.addWidget(self.menu_btn)


        self.horizontalLayout_26.addWidget(self.frame_36)

        self.frame_12 = QFrame(self.frame_35)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(600, 40))
        self.frame_12.setMaximumSize(QSize(923293, 40))
        self.frame_12.setStyleSheet(u"background-color: rgb(29, 29, 65);\n"
"border: 0;\n"
"border-radius: 20px;\n"
"border-top-left-radius: 0;\n"
"border-top-right-radius: 0;")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(200, 16777215))
        self.frame_13.setStyleSheet(u"background: 0;\n"
"border-radius: 0;")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.time_label = QLabel(self.frame_13)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setFont(font1)
        self.time_label.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_7.addWidget(self.time_label)

        self.date_label = QLabel(self.frame_13)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setFont(font1)
        self.date_label.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_7.addWidget(self.date_label)


        self.horizontalLayout_9.addWidget(self.frame_13)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(200, 16777215))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamilies([u"Inter Hewn"])
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.voice_control = QRadioButton(self.frame_14)
        self.voice_control.setObjectName(u"voice_control")
        self.voice_control.setMinimumSize(QSize(40, 22))
        self.voice_control.setMaximumSize(QSize(30, 16777215))
        self.voice_control.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.voice_control.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(99, 89, 233);\n"
"	border-radius: 11px;\n"
"	padding: 4px;\n"
"}\n"
"QRadioButton::indicator{\n"
"	border-radius: 8px;\n"
"}\n"
"QRadioButton::indicator::unchecked{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton::indicator::checked{\n"
"	background-color: rgb(90, 255, 173);\n"
"}")
        self.voice_control.setChecked(False)

        self.horizontalLayout_8.addWidget(self.voice_control)


        self.horizontalLayout_9.addWidget(self.frame_14)


        self.horizontalLayout_26.addWidget(self.frame_12)


        self.verticalLayout_3.addWidget(self.frame_35)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setSizeIncrement(QSize(0, 0))
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_10)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_9)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(185, 95))
        self.frame_4.setStyleSheet(u"background-color: rgb(29, 29, 65);\n"
"border: 0;\n"
"border-radius: 20px")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_16 = QFrame(self.frame_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(55, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setFamilies([u"Inter Hewn"])
        font3.setPointSize(9)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.horizontalSpacer_9 = QSpacerItem(54, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)


        self.verticalLayout_5.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.label_10 = QLabel(self.frame_15)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(30, 30))
        self.label_10.setMaximumSize(QSize(30, 30))
        self.label_10.setSizeIncrement(QSize(1, 1))
        self.label_10.setPixmap(QPixmap(u":/icons/icons/box-arrow-down.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.total_income_label = QLabel(self.frame_15)
        self.total_income_label.setObjectName(u"total_income_label")
        font4 = QFont()
        font4.setFamilies([u"Inter Hewn"])
        font4.setPointSize(12)
        self.total_income_label.setFont(font4)
        self.total_income_label.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_11.addWidget(self.total_income_label)

        self.label_12 = QLabel(self.frame_15)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u":/icons/icons/R.png"))
        self.label_12.setScaledContents(False)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.verticalLayout_5.addWidget(self.frame_15)

        self.frame_17 = QFrame(self.frame_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(134, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        font5 = QFont()
        font5.setPointSize(8)
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"background-color: rgba(2, 177, 90, 15);\n"
"color: rgb(2, 177, 90);\n"
"border-radius: 5px;\n"
"padding: 2px 5px;")

        self.horizontalLayout_12.addWidget(self.label_14)


        self.verticalLayout_5.addWidget(self.frame_17)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(185, 95))
        self.frame_5.setStyleSheet(u"background-color: rgb(29, 29, 65);\n"
"border: 0;\n"
"border-radius: 20px")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_18 = QFrame(self.frame_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_13 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.horizontalSpacer_14 = QSpacerItem(56, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)


        self.verticalLayout_6.addWidget(self.frame_18)

        self.frame_20 = QFrame(self.frame_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setSpacing(8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.label_16 = QLabel(self.frame_20)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(30, 30))
        self.label_16.setMaximumSize(QSize(30, 30))
        self.label_16.setSizeIncrement(QSize(1, 1))
        self.label_16.setPixmap(QPixmap(u":/icons/icons/box-arrow-up.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_16)

        self.total_outcome_label = QLabel(self.frame_20)
        self.total_outcome_label.setObjectName(u"total_outcome_label")
        self.total_outcome_label.setFont(font4)
        self.total_outcome_label.setStyleSheet(u"color: #fff;")

        self.horizontalLayout_15.addWidget(self.total_outcome_label)

        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setPixmap(QPixmap(u":/icons/icons/R.png"))
        self.label_18.setScaledContents(False)

        self.horizontalLayout_15.addWidget(self.label_18)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)


        self.verticalLayout_6.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)

        self.label_15 = QLabel(self.frame_19)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"background-color: rgba(235, 0, 27, 15);\n"
"color: rgb(235, 0, 27);\n"
"border-radius: 5px;\n"
"padding: 2px 5px;")

        self.horizontalLayout_14.addWidget(self.label_15)


        self.verticalLayout_6.addWidget(self.frame_19)


        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(380, 218))
        self.frame_6.setStyleSheet(u"background-color: rgb(29, 29, 65);\n"
"border: 0;\n"
"border-radius: 20px")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.bar_chart = QChartView(self.frame_6)
        self.bar_chart.setObjectName(u"bar_chart")

        self.verticalLayout_7.addWidget(self.bar_chart)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(380, 180))
        self.frame_7.setStyleSheet(u"background-color: rgb(29, 29, 65);\n"
"border: 0;\n"
"border-radius: 20px")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_26 = QFrame(self.frame_7)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_26)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_23 = QFrame(self.frame_26)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_23)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)

        self.horizontalLayout_18.addWidget(self.label_19)

        self.horizontalSpacer_21 = QSpacerItem(41, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_21)


        self.verticalLayout_9.addWidget(self.frame_23)

        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_27)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.horizontalLayout_20.addWidget(self.label_21)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_24)

        self.balance_label = QLabel(self.frame_27)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setMaximumSize(QSize(16777215, 35))
        self.balance_label.setFont(font1)
        self.balance_label.setStyleSheet(u"background-color: rgb(99, 89, 233);\n"
"border-radius: 5px;\n"
"padding: 5px 5px;")

        self.horizontalLayout_20.addWidget(self.balance_label)


        self.verticalLayout_9.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_28)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.horizontalLayout_21.addWidget(self.label_23)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_25)

        self.savings_label = QLabel(self.frame_28)
        self.savings_label.setObjectName(u"savings_label")
        self.savings_label.setMaximumSize(QSize(16777215, 35))
        self.savings_label.setFont(font1)
        self.savings_label.setStyleSheet(u"background-color: rgb(99, 89, 233);\n"
"border-radius: 5px;\n"
"padding: 5px 5px;")

        self.horizontalLayout_21.addWidget(self.savings_label)


        self.verticalLayout_9.addWidget(self.frame_28)


        self.horizontalLayout_22.addWidget(self.frame_26)

        self.pie_chart = QChartView(self.frame_7)
        self.pie_chart.setObjectName(u"pie_chart")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(200)
        sizePolicy2.setHeightForWidth(self.pie_chart.sizePolicy().hasHeightForWidth())
        self.pie_chart.setSizePolicy(sizePolicy2)
        self.pie_chart.setStyleSheet(u"color: #fff;")
        self.pie_chart.setTransformationAnchor(QGraphicsView.ViewportAnchor.NoAnchor)

        self.horizontalLayout_22.addWidget(self.pie_chart)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
        self.frame_11.setMinimumSize(QSize(266, 533))
        self.frame_11.setMaximumSize(QSize(320, 16777215))
        self.frame_11.setStyleSheet(u"background-color: rgb(29, 29, 65);\n"
"border: 0;\n"
"border-radius: 20px;\n"
"\n"
"")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.frame_22 = QFrame(self.frame_11)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"margin-bottom: 5px;")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_20)

        self.label_3 = QLabel(self.frame_22)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.label_3)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_19)


        self.verticalLayout_4.addWidget(self.frame_22)

        self.transactions_frame = QFrame(self.frame_11)
        self.transactions_frame.setObjectName(u"transactions_frame")
        self.transactions_frame.setMinimumSize(QSize(0, 60))
        self.transactions_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.transactions_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.transactions_frame)
        self.verticalLayout_12.setSpacing(8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_29 = QFrame(self.transactions_frame)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 30))
        self.frame_29.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_29.setLineWidth(1)
        self.frame_29.setMidLineWidth(0)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_29)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(18, 18))
        self.label_25.setMaximumSize(QSize(18, 18))
        self.label_25.setSizeIncrement(QSize(1, 1))
        self.label_25.setPixmap(QPixmap(u":/icons/icons/icon-plugs.png"))

        self.horizontalLayout_24.addWidget(self.label_25)

        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(30, 0))
        self.frame_30.setMaximumSize(QSize(100, 16777215))
        self.frame_30.setStyleSheet(u"margin-left: 3px;")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_30)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_30)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_30)
        self.label_27.setObjectName(u"label_27")
        font6 = QFont()
        font6.setFamilies([u"GOST type B"])
        self.label_27.setFont(font6)

        self.verticalLayout_10.addWidget(self.label_27)


        self.horizontalLayout_24.addWidget(self.frame_30)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_26)

        self.label_28 = QLabel(self.frame_29)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.horizontalLayout_24.addWidget(self.label_28)


        self.verticalLayout_12.addWidget(self.frame_29)

        self.frame_31 = QFrame(self.transactions_frame)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 30))
        self.frame_31.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_31)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(18, 18))
        self.label_29.setMaximumSize(QSize(18, 18))
        self.label_29.setSizeIncrement(QSize(1, 1))
        self.label_29.setPixmap(QPixmap(u":/icons/icons/icon-finance.png"))

        self.horizontalLayout_23.addWidget(self.label_29)

        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(30, 0))
        self.frame_32.setMaximumSize(QSize(100, 16777215))
        self.frame_32.setStyleSheet(u"margin-left: 3px;")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_32)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_32)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"color: rgb(41, 211, 126);")

        self.verticalLayout_11.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_32)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font6)

        self.verticalLayout_11.addWidget(self.label_31)


        self.horizontalLayout_23.addWidget(self.frame_32)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_27)

        self.label_32 = QLabel(self.frame_31)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)
        self.label_32.setStyleSheet(u"color: rgb(41, 211, 126);")

        self.horizontalLayout_23.addWidget(self.label_32)


        self.verticalLayout_12.addWidget(self.frame_31)

        self.not_found_frame = QFrame(self.transactions_frame)
        self.not_found_frame.setObjectName(u"not_found_frame")
        self.not_found_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.not_found_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.not_found_frame)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_37)

        self.label_34 = QLabel(self.not_found_frame)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)

        self.horizontalLayout_30.addWidget(self.label_34)

        self.horizontalSpacer_36 = QSpacerItem(48, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_36)


        self.verticalLayout_12.addWidget(self.not_found_frame)


        self.verticalLayout_4.addWidget(self.transactions_frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.frame_34 = QFrame(self.frame_11)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_29)

        self.add_transaction_btn = QPushButton(self.frame_34)
        self.add_transaction_btn.setObjectName(u"add_transaction_btn")
        self.add_transaction_btn.setMaximumSize(QSize(125, 16777215))
        self.add_transaction_btn.setFont(font1)
        self.add_transaction_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_transaction_btn.setStyleSheet(u"background-color: rgba(2, 177, 90, 230);\n"
"padding: 10px 20px;\n"
"border-radius: 10px;")

        self.horizontalLayout_25.addWidget(self.add_transaction_btn)

        self.horizontalSpacer_28 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_28)


        self.verticalLayout_4.addWidget(self.frame_34)


        self.horizontalLayout_6.addWidget(self.frame_11)


        self.verticalLayout_3.addWidget(self.frame_10)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Indigo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043d\u0435\u043b\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"20:13", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"19.10.2024", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u043e\u0435 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.voice_control.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0439 \u0434\u043e\u0445\u043e\u0434", None))
        self.total_income_label.setText(QCoreApplication.translate("MainWindow", u"1735.00", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"+1.29%", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0439 \u0440\u0430\u0441\u0445\u043e\u0434", None))
        self.total_outcome_label.setText(QCoreApplication.translate("MainWindow", u"1735.00", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"+1.29%", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.balance_label.setText(QCoreApplication.translate("MainWindow", u"298275.00\u20bd", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043a\u043e\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.savings_label.setText(QCoreApplication.translate("MainWindow", u"2985.00\u20bd", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0434\u0430 \u0432\u043d\u0435 \u0434\u043e\u043c\u0430", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0445\u043e\u0440\u043e\u0448\u043e \u043f\u043e\u043a\u0443\u0448\u0430\u043b", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"-4172 \u20bd", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u0430", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0435\u0431\u043e\u0439", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"+4172 \u20bd", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0439 \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u043e!", None))
        self.add_transaction_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

