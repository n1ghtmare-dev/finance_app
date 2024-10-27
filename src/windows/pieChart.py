from functools import partial
from PySide6 import QtCharts
from PySide6.QtCharts import QChart, QPieSeries, QPieSlice
from PySide6.QtGui import QFont, QColor


class PieChart(QChart):

    def __init__(self, datas, parent=None):
        super(PieChart, self).__init__(parent)
        self._datas = datas

        self.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.legend().hide()

        self.font1 = QFont()
        self.font1.setFamilies([u"Inter Hewn"])
        self.font1.setPointSize(12)

        self.series = QPieSeries()
        self.series.setHoleSize(0.3)
        self.inner_series = QPieSeries()
        self.inner_series.setPieSize(0.3)
        self.inner_series.setHoleSize(0.22)
        self.setTitleBrush(QColor("#ffffff"))
        self.setTitleFont(self.font1)

        self.set_series()
        self.set_inner_series()

    def set_series(self):
        slices = list()
        for data in self._datas:
            _slice = QPieSlice(data.name, data.value)
            _slice.setColor(data.primary_color)
            _slice.setBorderWidth(0)
            _slice.setLabelColor(QColor("#ffffff"))
            _slice.setLabelBrush(data.primary_color)
            _slice.setLabelVisible()
            _slice.hovered.connect(partial(self.explode, _slice))
            _slice.setLabelArmLengthFactor(0.1)
            slices.append(_slice)
            self.series.append(_slice)

        for _slice in slices:
            # if _slice.percentage() > 0.2:
            #     _slice.setLabelPosition(QtCharts.QPieSlice.LabelInsideHorizontal)
            label = f"<p align='center' style='color: white'>{_slice.label()} {round(_slice.percentage()*100, 2)}%</p>"
            _slice.setLabel(label)

        self.addSeries(self.series)
        self.setTitle("Расходы")


    def set_inner_series(self):
        for data in self._datas:
            _slice = self.inner_series.append(data.name, data.value)
            _slice.setColor(data.secondary_color)
            _slice.setBorderWidth(0)

        self.addSeries(self.inner_series)

    def explode(self, _slice: QPieSlice, is_hovered) -> None:
        if is_hovered:
            start = _slice.startAngle()
            end = _slice.startAngle()+_slice.angleSpan()
            self.inner_series.setPieStartAngle(end)
            self.inner_series.setPieEndAngle(start+360)
        else:
            self.inner_series.setPieStartAngle(0)
            self.inner_series.setPieEndAngle(360)
        _slice.setExplodeDistanceFactor(0.1)
        _slice.setExploded(is_hovered)
