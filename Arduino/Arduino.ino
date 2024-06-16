void setup() {
  Serial.begin(9600); // Initialize serial communication with baud rate 9600
  randomSeed(analogRead(0)); // Initialize random number generator with analog pin 0 value
}

void loop() {
  // Create sensor values
  int temperatureValues[5];
  Temperature(temperatureValues);

  int pressureValues[5];
  Pressure(pressureValues);

  bool keysValues[5];
  generateKeys(keysValues);

  bool lampsValues[5];
  Lamps(lampsValues);

  int roundsValues[5];
  Rounds(roundsValues);

  int dasteValues[5];
  Daste(dasteValues);

  // Send sensor values over serial communication as a single string
  Serial.print("temp=[");
  printArray(temperatureValues, 5);
  Serial.print("],press=[");
  printArray(pressureValues, 5);
  Serial.print("],keys=[");
  printBooleanArray(keysValues, 5);
  Serial.print("],lamps=[");
  printBooleanArray(lampsValues, 5);
  Serial.print("],rounds=[");
  printArray(roundsValues, 5);
  Serial.print("],daste=[");
  printArray(dasteValues, 5);
  Serial.println("]");

  delay(100); // Delay for 100 milliseconds before repeating
}

void Temperature(int values[]) {
  // Generate random temperature values between 0 and 100
  for (int i = 0; i < 5; ++i) {
    values[i] = random(0, 101);
  }
}

void Pressure(int values[]) {
  // Generate random pressure values between 0 and 100
  for (int i = 0; i < 5; ++i) {
    values[i] = random(0, 101);
  }
}

void generateKeys(bool values[]) {
  // Generate random keys values (true/false)
  for (int i = 0; i < 5; ++i) {
    values[i] = random(0, 2); // Generate either 0 (false) or 1 (true)
  }
}

void Lamps(bool values[]) {
  // Generate random lamps values (true/false)
  for (int i = 0; i < 5; ++i) {
    values[i] = random(0, 2) == 0 ? false : true; // Generate random boolean values
  }
}

void Rounds(int values[]) {
  // Generate random rounds values between 0 and 100
  for (int i = 0; i < 5; ++i) {
    values[i] = random(0, 101);
  }
}

void Daste(int values[]) {
  // Generate random daste values between 0 and 100
  for (int i = 0; i < 5; ++i) {
    values[i] = random(0, 101);
  }
}

void printArray(int values[], int length) {
  for (int i = 0; i < length; ++i) {
    Serial.print(values[i]);
    if (i < length - 1) {
      Serial.print(",");
    }
  }
}

void printBooleanArray(bool values[], int length) {
  for (int i = 0; i < length; ++i) {
    Serial.print(values[i] ? "true" : "false"); // Convert boolean to string representation
    if (i < length - 1) {
      Serial.print(",");
    }
  }
}
