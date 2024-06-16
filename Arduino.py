import serial

class ArduinoSerial:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)  # Open serial port (adjust port name as needed)
        self.ser.flushInput()  # Flush input buffer to start fresh

    def receive(self):
        data_dict = {}  # Dictionary to store the received integers
        while True:
            if self.ser.in_waiting > 0:
                try:
                    data = self.ser.readline().decode('utf-8', errors='ignore').strip()  # Read and decode raw bytes from serial
                    # Assuming the Arduino sends data in a comma-separated format
                    data_list = data.split(',')
                    if len(data_list) == 24:
                        # Store integers in a dictionary with keys from 1 to 24
                        data_dict = {f"number_{i+1}": int(data_list[i]) for i in range(24)}
                        print(f'Stored data in dictionary: {data_dict}')
                        break  # Exit the loop after receiving and storing one complete set of data
                except Exception as e:
                    print(f'Error: {e}')
        return data_dict

    def send(self, data):
        try:
            self.ser.write(data.encode('utf-8'))  # Send data to Arduino
            print(f'Sent to Arduino: {data}')
        except Exception as e:
            print(f'Error: {e}')

    def close(self):
        self.ser.close()  # Close serial port when done
