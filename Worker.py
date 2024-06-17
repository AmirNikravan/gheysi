# This Python file uses the following encoding: utf-8
import random
from PySide6.QtCore import QThread, Signal
# from ui_form import Ui_MainWindow
from Arduino import ArduinoSerial
from PySide6.QtCore import QThread, Signal, QMutex, QWaitCondition, QObject
from Server import *
class Worker(QThread):
    gauge_val = Signal(dict)
    bar_val = Signal(dict)
    keys_val = Signal(dict)
    def __init__(self, arduino_serial,engine):
        super().__init__()
        self.arduino_serial = arduino_serial
        self.received_data = []
        self._running = True
        self.mutex = QMutex()
        self.wait_condition = QWaitCondition()
        self.engine = engine
    def run(self):
        while self._running:
            self.msleep(10)
            self.arduino_serial.receive()
            self.server = Server()
            record = self.server.receive_data('sensors')
            self.server.disconnect()
            keys = record[2]['keys']
            name = record[2]['name']
            daste = record[2]['daste']
            lamps = record[2]['lamps']
            rounds = record[2]['rounds']
            pressure = record[2]['pressure']
            temperature = record[2]['temperature']

            if record:
                if len(record) >= 3:
                    bar = {
                        'sea_water_pressure': pressure['p1'],
                    #     'oil_pressure': self.received_data[1],
                    #     'fuel_pressure': self.received_data[2],
                    #     'air_boost_pressure': self.received_data[3],
                    #     'speed': self.received_data[4],
                    #     'exhaust_temperature_a': self.received_data[5],
                    #     'exhaust_temperature_b': self.received_data[6],
                    #     'air_temp_after': self.received_data[7],
                    #     'air_temp_before': self.received_data[8],
                    #     'sea_water_temperature': self.received_data[9],
                    #     'oil_temperature': self.received_data[10],
                    #     'fresh_water_temp_after': self.received_data[11],
                    #     'fresh_water_temp_before': self.received_data[12],
                    #     'fuel_rack_position': self.received_data[13],
                    }
                    gauge = {
                    #     'banka_exhaust': self.received_data[14],
                    #     'bankb_exhaust': self.received_data[15],
                    #     'banka_cooler': self.received_data[16],
                    #     'bankb_cooler': self.received_data[17],
                    #     'fresh_water_before': self.received_data[18],
                    #     'fresh_water_after': self.received_data[19],
                    #     'oil': self.received_data[20],
                    #     'fuel': self.received_data[21],
                    #     'airboost': self.received_data[22],
                    #     'seawater': self.received_data[23]
                    }
                    key={
                    'toolButton_lamptest' :keys['k1'],
                    'toolButton_lop':keys['k2'],
                    'toolButton_mcr':keys['k3'],
                    'toolButton_bridge':keys['k4'],
                    'toolButton_increase_speed':keys['k5'],
                    'toolButton_decrease_speed':keys['k6'],
                    'toolButton_fault_ack':keys['k7'],
                    'toolButton_fault_reset':keys['k8'],
                    'toolButton_ahead':keys['k9'],
                    'toolButton_neurtal':keys['k10'],
                    'toolButton_astern':keys['k11'],
                    'toolButton_start_engine':keys['k12'],
                    'toolButton_stop_engine':keys['k13'],
                    'toolButton_emergency_stop':keys['k14']
                    }

                    self.keys_val.emit(key)
                    self.bar_val.emit(bar)
                    self.gauge_val.emit(gauge)
                    self.received_data = []  # Reset received data for the next cycle

    def stop(self):
        self.mutex.lock()
        self._running = False
        self.wait_condition.wakeOne()
        self.mutex.unlock()

class Sender(QThread):
    def __init__(self, arduino_serial):
        super().__init__()
        self.arduino_serial = arduino_serial
        self.data_to_send = None
        self._running = True
        self.mutex = QMutex()
        self.wait_condition = QWaitCondition()

    def run(self):
        while self._running:
            self.mutex.lock()
            if self.data_to_send:
                self.arduino_serial.send(self.data_to_send)
                self.data_to_send = None
            self.mutex.unlock()
            self.msleep(10)

    def send_data(self, data):
        self.mutex.lock()
        self.data_to_send = data
        self.wait_condition.wakeOne()
        self.mutex.unlock()

    def stop(self):
        self.mutex.lock()
        self._running = False
        self.wait_condition.wakeOne()
        self.mutex.unlock()

class ButtonWorker(QThread):
    clicked = Signal(str)  # Define the signal

    def __init__(self, button_name):
        super().__init__()
        self.button_name = button_name

    def run(self):
        # Simulate a long-running task
        self.msleep(1)
        self.clicked.emit(self.button_name)  # Emit the signal
