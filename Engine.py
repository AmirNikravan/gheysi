import re
import time

class Engine:
    def __init__(self, name):
        self.data = {}
        self.name = name  # Initialize a name attribute

    def update_engine(self, data_list):
        print(data_list)
        # Update the single dictionary with sensor data
        self.data = {
            'name': self.name,
            'temperature': {f't{i+1}': int(data_list[i]) for i in range(5)},
            'pressure': {f'p{i+1}': int(data_list[5 + i]) for i in range(5)},
            'keys': {f'k{i+1}': bool(int(data_list[10 + i])) for i in range(14)},  # Convert 0/1 to boolean
            'lamps': {f'l{i+1}': bool(int(data_list[15 + i])) for i in range(5)},  # Convert 0/1 to boolean
            'rounds': {f'r{i+1}': int(data_list[20 + i]) for i in range(5)},
            'daste': {f'd{i+1}': int(data_list[25 + i]) for i in range(5)}
        }

        # Print the updated dictionary (for debugging)
        print(f'Sensor Data: {self.data}')

# Example usage:
# engine = Engine("Engine1")
# data_list = [
#     '10', '20', '30', '40', '50',  # Temperature
#     '60', '70', '80', '90', '100',  # Pressure
