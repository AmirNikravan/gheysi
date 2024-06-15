# This Python file uses the following encoding: utf-8
import random
from PySide6.QtCore import QThread, Signal
# from ui_form import Ui_MainWindow
from Arduino import ArduinoSerial
class Worker(QThread):
    gauge_val = Signal(dict)
    bar_val = Signal(dict)

    def __init__(self, arduino_serial):
        super().__init__()
        self.arduino_serial = arduino_serial
        self.received_data = []

    def run(self):
        while True:
            self.msleep(1000)
            data = self.arduino_serial.receive()
            if data:
                self.received_data.extend(data.values())  # Append the list of numbers directly
                if len(self.received_data) >= 14:
                    # Ensure we only take the first 14 numbers
                    self.received_data = self.received_data[:14]
                    bar = {
                        'sea_water_pressure': self.received_data[0],
                        'oil_pressure': self.received_data[1],
                        'fuel_pressure': self.received_data[2],
                        'air_boost_pressure': self.received_data[3],
                        'speed': self.received_data[4],
                        'exhaust_temperature_a': self.received_data[5],
                        'exhaust_temperature_b': self.received_data[6],
                        'air_temp_after': self.received_data[7],
                        'air_temp_before': self.received_data[8],
                        'sea_water_temperature': self.received_data[9],
                        'oil_temperature': self.received_data[10],
                        'fresh_water_temp_after': self.received_data[11],
                        'fresh_water_temp_before': self.received_data[12],
                        'fuel_rack_position': self.received_data[13],
                    }
                    gauge = {
                        'banka_exhaust': random.randint(0, 1000),
                        'bankb_exhaust': random.randint(0, 1000),
                        'banka_cooler': random.randint(0, 1000),
                        'bankb_cooler': random.randint(0, 1000),
                        'fresh_water_before': random.randint(0, 120),
                        'fresh_water_after': random.randint(0, 120),
                        'oil': random.randint(0, 120),
                        'fuel': random.randint(0, 1000),
                        'airboost': random.randint(0, 4),
                        'seawater': random.randint(0, 120)
                    }
                    self.bar_val.emit(bar)
                    self.gauge_val.emit(gauge)
                    self.received_data = []  # Reset received data for the next cycle
class ButtonWorker(QThread):
    clicked = Signal(str)

    def __init__(self, button_name):
        super().__init__()
        self.button_name = button_name

    def run(self):
        # Simulate a long-running task
        self.msleep(1)
        self.clicked.emit(self.button_name)

