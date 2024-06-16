import re
import time
class Engine:
    def __init__(self):
        self.temperature = {}
        self.pressure = {}
        self.keys = {}
        self.lamps = {}
        self.rounds = {}
        self.daste = {}
    def update_engine(self, data_list):
        # Assign sensor data to corresponding dictionaries
        self.temperature = {f't{i+1}': int(data_list[i]) for i in range(5)}
        self.pressure = {f'p{i+1}': int(data_list[5 + i]) for i in range(5)}
        self.keys = {f'k{i+1}': bool(int(data_list[10 + i])) for i in range(5)}  # Convert 0/1 to boolean
        self.lamps = {f'l{i+1}': bool(int(data_list[15 + i])) for i in range(5)}  # Convert 0/1 to boolean
        self.rounds = {f'r{i+1}': int(data_list[20 + i]) for i in range(5)}
        self.daste = {f'd{i+1}': int(data_list[25 + i]) for i in range(5)}

        # Print the updated dictionaries (for debugging)
        print(f'Temperature: {self.temperature}')
        print(f'Pressure: {self.pressure}')
        print(f'Keys: {self.keys}')
        print(f'Lamps: {self.lamps}')
        print(f'Rounds: {self.rounds}')
        print(f'Daste: {self.daste}')
