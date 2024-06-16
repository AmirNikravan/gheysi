import serial
from Engine import Engine  # Assuming Engine class is defined in engine.py
import time

class ArduinoSerial:
    def __init__(self, engine):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)  # Open serial port (adjust port name as needed)
        self.ser.flushInput()  # Flush input buffer to start fresh
        self.engine = engine  # Instantiate Engine object

    def receive(self):
        while True:
            if self.ser.in_waiting > 0:
                try:
                    data = self.ser.readline().decode('utf-8', errors='ignore').strip()  # Read and decode raw bytes from serial
                    # Assuming the Arduino sends data in a comma-separated format
                    data_list = data.split(',')
                    if len(data_list) == 30:
                        # Update Engine object with received data
                        self.engine.update_engine(data_list)
                        break  # Exit the loop after receiving and storing one complete set of data

                except Exception as e:
                    print(f'Error: {e}')

    # def process_data(self, data_list):
    #     # Split the data into respective sensor groups

    #     # Assuming your Engine class has a method `update_engine`
    #     self.engine.update_engine({
    #         'temperatures': temperatures,
    #         'pressures': pressures,
    #         'keys': keys,
    #         'lamps': lamps,
    #         'rounds': rounds,
    #         'daste': daste
    #     })

    def send(self, data):
        try:
            self.ser.write(data.encode('utf-8'))  # Send data to Arduino
            print(f'Sent to Arduino: {data}')
        except Exception as e:
            print(f'Error: {e}')

    def close(self):
        self.ser.close()

# Usage example (assuming you have an Engine class to handle the data):
# engine = Engine()
# arduino_serial = ArduinoSerial(engine)
# arduino_serial.receive()
