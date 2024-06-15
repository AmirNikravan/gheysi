import serial

class ArduinoSerial:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 9600)  # Open serial port (adjust port name as needed)
        self.ser.flushInput()  # Flush input buffer to start fresh

    def receive(self):
        self.data_dict = {}  # Dictionary to store the received integers
        while True:
            if self.ser.in_waiting > 0:
                try:
                    data = self.ser.readline().decode('utf-8', errors='ignore').strip()  # Read and decode raw bytes from serial
                    # print(f'Received from Arduino: {data}')

                    # Assuming the Arduino sends data in a comma-separated format
                    data_list = data.split(',')
                    if len(data_list) == 14:
                        # Store integers in a dictionary with keys from 1 to 14
                        self.data_dict = {f"number_{i+1}": int(data_list[i]) for i in range(14)}
                        # print(f'Stored data in dictionary: {self.data_dict}')
                        break  # Exit the loop after receiving and storing one complete set of data
                except Exception as e:
                    print(f'Errord: {e}')
        return self.data_dict

    def close(self):
        self.ser.close()  # Close serial port when done

# Usage example:
# arduino_serial = ArduinoSerial()
# received_data = arduino_serial.receive()
# arduino_serial.close()

# print(received_data)  # Print the received dictionary
