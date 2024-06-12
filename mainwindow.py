# This Python file uses the following encoding: utf-8
import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, Signal, QTimer

from ui_form import Ui_MainWindow
from Worker import Worker

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #right sdie stacked widget buttons
        self.ui.toolButton_up.clicked.connect(lambda: self.change_main_page('up'))
        self.ui.toolButton_down.clicked.connect(lambda: self.change_main_page('down'))
        self.ui.toolButton_p1f.clicked.connect(lambda: self.change_bar_page('forward'))
        self.ui.toolButton_p1b.clicked.connect(lambda: self.change_bar_page('before'))
        self.ui.toolButton_p2b.clicked.connect(lambda: self.change_bar_page('before'))
        self.ui.toolButton_p2f.clicked.connect(lambda: self.change_bar_page('forward'))
        self.ui.toolButton_p3b.clicked.connect(lambda: self.change_bar_page('before'))
        self.ui.toolButton_p3f.clicked.connect(lambda: self.change_bar_page('forward'))
        #thread
        self.thread = Worker()
        self.thread.gauge_val.connect(self.update_gauges)
        self.thread.bar_val.connect(self.update_bars)
        self.desgin_gauge()
        self.start_thread()
    def desgin_gauge(self):
        self.ui.gauge_seawater.minValue = 0
        self.ui.gauge_seawater.maxValue = 120
        self.ui.gauge_oil.minValue = 0
        self.ui.gauge_oil.maxValue = 120
        self.ui.gauge_fw_af.minValue =0
        self.ui.gauge_fw_be.minValue = 0
        self.ui.gauge_fw_af.maxValue = 120
        self.ui.gauge_fw_be.maxValue = 120
        self.ui.gauge_exhuast_a.minValue = 0
        self.ui.gauge_exhuast_b.minValue = 0
        self.ui.gauge_exhuast_a.maxValue = 1200
        self.ui.gauge_exhuast_b.maxValue = 1200
        self.ui.gauge_cooler_a.minValue = 0
        self.ui.gauge_cooler_b.minValue = 0
        self.ui.gauge_cooler_a.maxValue = 120
        self.ui.gauge_cooler_b.maxValue = 120
        self.ui.gauge_airboost.units = 'bar'
        self.ui.gauge_airboost.minValue = 0
        self.ui.gauge_airboost.maxValue = 4
        self.ui.gauge_airboost.scalaCount = 1
        self.ui.gauge_exhuast_a.setMouseTracking(False)
        self.ui.gauge_exhuast_b.setMouseTracking(False)
        self.ui.gauge_cooler_a.setMouseTracking(False)
        self.ui.gauge_cooler_b.setMouseTracking(False)
        self.ui.gauge_fw_be.setMouseTracking(False)
        self.ui.gauge_fw_af.setMouseTracking(False)
        self.ui.gauge_oil.setMouseTracking(False)
        self.ui.gauge_airboost.setMouseTracking(False)
        self.ui.gauge_fuel.setMouseTracking(False)
        self.ui.gauge_seawater.setMouseTracking(False)
        # pass
        # self.ui.gauge_exhuast_b.units = ' celsius'
    def update_gauges(self, val):
        # print(val)
        self.ui.gauge_exhuast_a.value = val['banka_exhuast']
        self.ui.gauge_exhuast_b.value = val['bankb_exhuast']
        self.ui.gauge_cooler_a.value = val['banka_cooler']
        self.ui.gauge_cooler_b.value = val['bankb_cooler']
        self.ui.gauge_fw_be.value = val['fresh_water_before']
        self.ui.gauge_fw_af.value = val['fresh_water_after']
        self.ui.gauge_oil.value = val['oil']
        self.ui.gauge_airboost.value = val['airboost']
        self.ui.gauge_fuel.value = val['fuel']
        self.ui.gauge_seawater.value = val['seawater']
        # Force repaint to ensure UI updates
        self.ui.gauge_exhuast_a.repaint()
        self.ui.gauge_exhuast_b.repaint()
        self.ui.gauge_cooler_a.repaint()
        self.ui.gauge_cooler_b.repaint()
        self.ui.gauge_fw_be.repaint()
        self.ui.gauge_fw_af.repaint()
        self.ui.gauge_oil.repaint()
        self.ui.gauge_airboost.repaint()
        self.ui.gauge_fuel.repaint()
        self.ui.gauge_seawater.repaint()
    def update_bars(self,val):
        self.ui.sea_water_pressure_bar.setValue(val['sea_water_pressure'])
        self.ui.lcdNumber_sea_water_pressure_bar.display(val['sea_water_pressure'])
        self.ui.oil_pressuer_bar.setValue(val['oil_pressure'])
        self.ui.lcdNumber_oil_pressuer_bar.display(val['oil_pressure'])
        self.ui.fuel_pressure_bar.setValue(val['fuel_pressure'])
        self.ui.lcdNumber_fuel_pressure_bar.display(val['fuel_pressure'])
        self.ui.air_boost_pressure_bar.setValue(val['air_boost_pressure'])
        self.ui.lcdNumber_air_boost_pressure_bar.display(val['air_boost_pressure'])
        self.ui.speed_bar.setValue(val['speed'])
        self.ui.lcdNumber_speed_bar.display(val['speed'])
        self.ui.exhuast_temp_abar.setValue(val['exhuast_temperature_a'])
        self.ui.lcdNumber_exhuast_temp_abar.display(val['exhuast_temperature_b'])
        self.ui.exhaust_temp_bbar.setValue(val['exhuast_temperature_a'])
        self.ui.lcdNumber_exhaust_temp_bbar.display(val['exhuast_temperature_b'])
        self.ui.air_temp_afbar.setValue(val['air_temp_after'])
        self.ui.lcdNumber_air_temp_afbar.display(val['air_temp_after'])
        self.ui.air_temp_bebar.setValue(val['air_temp_before'])
        self.ui.lcdNumber_air_temp_bebar.display(val['air_temp_before'])
        self.ui.sea_water_tempbar.setValue(val['sea_water_temperature'])
        self.ui.lcdNumber_sea_water_tempbar.display(val['sea_water_temperature'])
        self.ui.oil_temperessure_bar.setValue(val['oil_temperature'])
        self.ui.lcdNumber_oil_temperessure_bar.display(val['oil_temperature'])
        self.ui.water_temp_bebar.setValue(val['fresh_water_temp_after'])
        self.ui.lcdNumber_water_temp_bebar.display(val['fresh_water_temp_after'])
        self.ui.water_temp_afbar.setValue(val['fresh_water_temp_before'])
        self.ui.lcdNumber_water_temp_afbar.display(val['fresh_water_temp_before'])
        self.ui.fuel_rack_posbar.setValue(val['fuel_rack_position'])
        self.ui.lcdNumber_fuel_rack_posbar.display(val['fuel_rack_position'])




    def start_thread(self):
        self.thread.start()

    def change_bar_page(self, direction):
        max_index = self.ui.stackedWidget_bar.count() - 1
        min_index = 0
        current = self.ui.stackedWidget_bar.currentIndex()
        if direction == 'forward':
            if current == max_index:
                self.ui.stackedWidget_bar.setCurrentIndex(min_index)
            else:
                self.ui.stackedWidget_bar.setCurrentIndex(current + 1)
        elif direction == 'before':
            if current == min_index:
                self.ui.stackedWidget_bar.setCurrentIndex(max_index)
            else:
                self.ui.stackedWidget_bar.setCurrentIndex(current - 1)

    def change_main_page(self, direction):
        max_index = self.ui.stackedWidget.count() - 1
        min_index = 0
        current = self.ui.stackedWidget.currentIndex()
        if direction == 'up':
            if current == max_index:
                self.ui.stackedWidget.setCurrentIndex(min_index)
            else:
                self.ui.stackedWidget.setCurrentIndex(current + 1)
        elif direction == 'down':
            if current == min_index:
                self.ui.stackedWidget.setCurrentIndex(max_index)
            else:
                self.ui.stackedWidget.setCurrentIndex(current - 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
