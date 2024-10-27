from PySide6.QtCharts import QChart, QBarSet, QBarSeries, QValueAxis, QBarCategoryAxis
from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt


class BarChart(QChart):
    def __init__(self):
        super().__init__()

        self.set_0 = QBarSet("Jane")

        self.set_0.append([1, 2, 3])

        self.series = QBarSeries()
        self.series.append(self.set_0)

        self.font1 = QFont()
        self.font1.setFamilies([u"Inter Hewn"])
        self.font1.setPointSize(12)

        self.addSeries(self.series)
        self.setTitle("Аналитика")
        self.setTitleBrush(QColor("#ffffff"))
        self.setTitleFont(self.font1)
        self.setContentsMargins(0, 0, 0, 0)
        self.setAnimationOptions(QChart.SeriesAnimations)

        self.categories = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн"]
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 40)
        self.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_x)

        self.legend().hide()
        self.setBackgroundVisible(False)
