# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtCore import QThread, Signal, Slot,QTimer

from ui_form import Ui_MainWindow
from Worker import *
from Arduino import *
from Engine import *
from Server import *
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #server

        #engin
        self.engine_name = 'Engine one'
        self.engine = Engine(self.engine_name)
        # right side stacked widget buttons
        self.ui.toolButton_up.clicked.connect(lambda: self.change_main_page('up'))
        self.ui.toolButton_down.clicked.connect(lambda: self.change_main_page('down'))
        self.ui.toolButton_p1f.clicked.connect(lambda: self.change_bar_page('forward'))
        self.ui.toolButton_p1b.clicked.connect(lambda: self.change_bar_page('before'))
        self.ui.toolButton_p2b.clicked.connect(lambda: self.change_bar_page('before'))
        self.ui.toolButton_p2f.clicked.connect(lambda: self.change_bar_page('forward'))
        self.ui.toolButton_p3b.clicked.connect(lambda: self.change_bar_page('before'))
        self.ui.toolButton_p3f.clicked.connect(lambda: self.change_bar_page('forward'))

        # thread for receiving data
        self.arduino_serial = ArduinoSerial(self.engine)
        self.thread = Worker(self.arduino_serial, self.engine)
        self.thread.bar_val.connect(self.update_bars)
        self.thread.gauge_val.connect(self.update_gauges)
        self.thread.keys_val.connect(self.update_keys)
        self.thread.start()

        # thread for sending data
        self.sender = Sender(self.arduino_serial)
        self.sender.start()

        self.desgin_gauge()

        # connect tool buttons
        self.ui.toolButton_lamptest.clicked.connect(self.create_button_handler("lamptest"))
        self.ui.toolButton_lop.clicked.connect(self.create_button_handler("lop"))
        self.ui.toolButton_mcr.clicked.connect(self.create_button_handler("mcr"))
        self.ui.toolButton_bridge.clicked.connect(self.create_button_handler("bridge"))
        self.ui.toolButton_ahead.clicked.connect(self.create_button_handler("ahead"))
        self.ui.toolButton_astern.clicked.connect(self.create_button_handler("astern"))
        self.ui.toolButton_decrease_speed.clicked.connect(self.create_button_handler("decrease_speed"))
        # self.ui.toolButton_down.clicked.connect(self.create_button_handler("down"))
        self.ui.toolButton_emergency_stop.clicked.connect(self.create_button_handler("emergency_stop"))
        self.ui.toolButton_fault_ack.clicked.connect(self.create_button_handler("fault_ack"))
        self.ui.toolButton_fault_reset.clicked.connect(self.create_button_handler("fault_reset"))
        self.ui.toolButton_increase_speed.clicked.connect(self.create_button_handler("increase_speed"))
        self.ui.toolButton_neurtal.clicked.connect(self.create_button_handler("neutral"))
        self.ui.toolButton_start_engine.clicked.connect(self.create_button_handler("start"))
        self.ui.toolButton_stop_engine.clicked.connect(self.create_button_handler("stop"))
    def create_button_handler(self, button_name):
        @Slot()
        def handler():
            self.handle_button_click(button_name)
        return handler

    def handle_button_click(self, button_name):
        self.change_color(button_name)

        self.button_worker = ButtonWorker(button_name)
        self.button_worker.clicked.connect(self.on_button_clicked)
        self.button_worker.start()

    @Slot(str)
    def on_button_clicked(self, button_name):
        print(f'ToolButton {button_name} clicked')
        data_to_send = f"Button {button_name} clicked!"
        self.sender.send_data(data_to_send)
    def change_color(self, name):
        button = None
        if name == 'lamptest':
            button = self.ui.toolButton_lamptest
        elif name == 'lop':
            button = self.ui.toolButton_lop
        elif name == 'mcr':
            button = self.ui.toolButton_mcr
        elif name == 'bridge':
            button = self.ui.toolButton_bridge
        elif name == 'ahead':
            button = self.ui.toolButton_ahead
        elif name == 'astern':
            button = self.ui.toolButton_astern
        elif name == 'decrease_speed':
            button = self.ui.toolButton_decrease_speed
        elif name == 'emergency_stop':
            button = self.ui.toolButton_emergency_stop
        elif name == 'fault_ack':
            button = self.ui.toolButton_fault_ack
        elif name == 'fault_reset':
            button = self.ui.toolButton_fault_reset
        elif name == 'increase_speed':
            button = self.ui.toolButton_increase_speed
        elif name == 'neutral':
            button = self.ui.toolButton_neutral
        elif name == 'start':
            button = self.ui.toolButton_start_engine
        elif name == 'stop':
            button = self.ui.toolButton_stop_engine

        if button:
            button.setStyleSheet("background-color: red;")
            QTimer.singleShot(100, lambda: button.setStyleSheet("background-color: rgb(93, 93, 93);"))
    @Slot(dict)
    def update_keys(self, keys):
        button_mappings = {
            'toolButton_lamptest': self.ui.toolButton_lamptest,
            'toolButton_lop': self.ui.toolButton_lop,
            'toolButton_mcr': self.ui.toolButton_mcr,
            'toolButton_bridge': self.ui.toolButton_bridge,
            'toolButton_ahead': self.ui.toolButton_ahead,
            'toolButton_astern': self.ui.toolButton_astern,
            'toolButton_decrease_speed': self.ui.toolButton_decrease_speed,
            'toolButton_emergency_stop': self.ui.toolButton_emergency_stop,
            'toolButton_fault_ack': self.ui.toolButton_fault_ack,
            'toolButton_fault_reset': self.ui.toolButton_fault_reset,
            'toolButton_increase_speed': self.ui.toolButton_increase_speed,
            'toolButton_neurtal': self.ui.toolButton_neurtal,
            'toolButton_start_engine': self.ui.toolButton_start_engine,
            'toolButton_stop_engine': self.ui.toolButton_stop_engine
        }

        for key_name, key_value in keys.items():
            button = button_mappings.get(key_name)
            if button:
                if key_value:
                    button.setStyleSheet("background-color: red;")
                else:
                    button.setStyleSheet("")
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
        pass
        # self.ui.gauge_exhuast_a.value = val['banka_exhaust']
        # self.ui.gauge_exhuast_b.value = val['bankb_exhaust']
        # self.ui.gauge_cooler_a.value = val['banka_cooler']
        # self.ui.gauge_cooler_b.value = val['bankb_cooler']
        # self.ui.gauge_fw_be.value = val['fresh_water_before']
        # self.ui.gauge_fw_af.value = val['fresh_water_after']
        # self.ui.gauge_oil.value = val['oil']
        # self.ui.gauge_airboost.value = val['airboost']
        # self.ui.gauge_fuel.value = val['fuel']
        # self.ui.gauge_seawater.value = val['seawater']
        # # Force repaint to ensure UI updates
        # self.ui.gauge_exhuast_a.repaint()
        # self.ui.gauge_exhuast_b.repaint()
        # self.ui.gauge_cooler_a.repaint()
        # self.ui.gauge_cooler_b.repaint()
        # self.ui.gauge_fw_be.repaint()
        # self.ui.gauge_fw_af.repaint()
        # self.ui.gauge_oil.repaint()
        # self.ui.gauge_airboost.repaint()
        # self.ui.gauge_fuel.repaint()
        # self.ui.gauge_seawater.repaint()
    def update_bars(self, val):
        self.ui.sea_water_pressure_bar.setValue(int(val['sea_water_pressure']))
        self.ui.lcdNumber_sea_water_pressure_bar.display(int(val['sea_water_pressure']))
        
        # self.ui.oil_pressuer_bar.setValue(int(val['oil_pressure']))
        # self.ui.lcdNumber_oil_pressuer_bar.display(int(val['oil_pressure']))
        
        # self.ui.fuel_pressure_bar.setValue(int(val['fuel_pressure']))
        # self.ui.lcdNumber_fuel_pressure_bar.display(int(val['fuel_pressure']))
        
        # self.ui.air_boost_pressure_bar.setValue(int(val['air_boost_pressure']))
        # self.ui.lcdNumber_air_boost_pressure_bar.display(int(val['air_boost_pressure']))
        
        # self.ui.speed_bar.setValue(int(val['speed']))
        # self.ui.lcdNumber_speed_bar.display(int(val['speed']))
        
        # self.ui.exhuast_temp_abar.setValue(int(val['exhaust_temperature_a']))
        # self.ui.lcdNumber_exhuast_temp_abar.display(int(val['exhaust_temperature_a']))
        
        # self.ui.exhaust_temp_bbar.setValue(int(val['exhaust_temperature_b']))
        # self.ui.lcdNumber_exhaust_temp_bbar.display(int(val['exhaust_temperature_b']))
        
        # self.ui.air_temp_afbar.setValue(int(val['air_temp_after']))
        # self.ui.lcdNumber_air_temp_afbar.display(int(val['air_temp_after']))
        
        # self.ui.air_temp_bebar.setValue(int(val['air_temp_before']))
        # self.ui.lcdNumber_air_temp_bebar.display(int(val['air_temp_before']))
        
        # self.ui.sea_water_tempbar.setValue(int(val['sea_water_temperature']))
        # self.ui.lcdNumber_sea_water_tempbar.display(int(val['sea_water_temperature']))
        
        # self.ui.oil_temperessure_bar.setValue(int(val['oil_temperature']))
        # self.ui.lcdNumber_oil_temperessure_bar.display(int(val['oil_temperature']))
        
        # self.ui.water_temp_bebar.setValue(int(val['fresh_water_temp_after']))
        # self.ui.lcdNumber_water_temp_bebar.display(int(val['fresh_water_temp_after']))
        
        # self.ui.water_temp_afbar.setValue(int(val['fresh_water_temp_before']))
        # self.ui.lcdNumber_water_temp_afbar.display(int(val['fresh_water_temp_before']))
        
        # self.ui.fuel_rack_posbar.setValue(int(val['fuel_rack_position']))
        # self.ui.lcdNumber_fuel_rack_posbar.display(int(val['fuel_rack_position']))



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
