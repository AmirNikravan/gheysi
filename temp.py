import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QThread, Signal
import random
class Worker(QThread):
    bar_val = Signal(dict)
    gauge_val = Signal(dict)

    def run(self):
        while True:
            self.msleep(1000)
            bar = {
                'sea_water_pressure': random.randint(0, 10),
                'oil_pressure': random.randint(0, 10),
                'fuel_pressure': random.randint(0, 10),
                'air_boost_pressure': random.randint(0, 10),
                'speed': random.randint(0, 2200),
                'exhaust_temperature_a': random.randint(0, 1200),
                'exhaust_temperature_b': random.randint(0, 1200),
                'air_temp_after': random.randint(0, 120),
                'air_temp_before': random.randint(0, 120),
                'sea_water_temperature': random.randint(0, 100),
                'oil_temperature': random.randint(0, 100),
                'fresh_water_temp_after': random.randint(0, 100),
                'fresh_water_temp_before': random.randint(0, 100),
                'fuel_rack_position': random.randint(0, 100),
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-threaded Button Click Example")

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.buttons = []
        self.threads = []

        for i in range(10):
            button = QPushButton(f"Button {i+1}")
            layout.addWidget(button)
            button.clicked.connect(lambda checked, idx=i: self.on_button_clicked(idx))
            self.buttons.append(button)

            thread = Worker()
            thread.bar_val.connect(self.update_bar)
            thread.gauge_val.connect(self.update_gauge)
            self.threads.append(thread)
            thread.start()

    def on_button_clicked(self, button_id):
        print(f"Button {button_id + 1} clicked.")

    def update_bar(self, bar_values):
        print(f"Bar values updated: {bar_values}")

    def update_gauge(self, gauge_values):
        print(f"Gauge values updated: {gauge_values}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
