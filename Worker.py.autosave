# This Python file uses the following encoding: utf-8
import random
from PySide6.QtCore import QThread, Signal
# from ui_form import Ui_MainWindow

class Worker(QThread):
    bar_val = Signal(dict)
    gauge_val = Signal(dict)
    def run(self):
        while(True):
            self.msleep(1000)
            bar ={
            'sea_water_pressure' : random.randint(0,10),
            'oil_pressure' : random.randint(0,10),
            'fuel_pressure' : random.randint(0,10),
            'air_boost_pressure' : random.randint(0,10),
            'speed' : random.randint(0,2200),
            'exhuast_temperature_a' : random.randint(0,1200),
            'exhuast_temperature_b' : random.randint(0,1200),
            'air_temp_after' : random.randint(0,120),
            'air_temp_before' : random.randint(0,120),
            'sea_water_temperature': random.randint(0,100),
            'oil_temperature' : random.randint(0,100),
            'fresh_water_temp_after' : random.randint(0,100),
            'fresh_water_temp_before' : random.randint(0,100),
            'fuel_rack_position' : random.randint(0,100),
            }
            gauge = {
            'banka_exhuast' : random.randint(0,1000),
            'bankb_exhuast' : random.randint(0,1000),
            'banka_cooler' : random.randint(0,1000),
            'bankb_cooler' : random.randint(0,1000),
            'fresh_water_before' : random.randint(0,120),
            'fresh_water_after' : random.randint(0,120),
            'oil' : random.randint(0,120),
            'fuel' : random.randint(0,1000),
            'airboost' : random.randint(0,4),
            'seawater' : random.randint(0,120)
            }
            self.bar_val.emit(bar)
            self.gauge_val.emit(gauge)


