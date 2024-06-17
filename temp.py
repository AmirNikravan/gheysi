from PySide6.QtCore import QThread, Signal, QMutex, QWaitCondition, QObject, Slot, QTimer
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # server

        # engine
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
