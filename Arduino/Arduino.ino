void setup() {
  Serial.begin(9600); // Initialize serial communication with baud rate 9600
  randomSeed(analogRead(0)); // Initialize random number generator with analog pin 0 value
}

void loop() {
  // Create sensor values
  int temperatureValues[5];
  int pressureValues[5];
  bool keysValues[5];
  bool lampsValues[5];
  int roundsValues[5];
  int dasteValues[5];

  // Generate sensor values
  Temperature(temperatureValues);
  Pressure(pressureValues);
  generateKeys(keysValues);
  Lamps(lampsValues);
  Rounds(roundsValues);
  Daste(dasteValues);

  // Merge sensor values into a single string
  String data = "";
  for (int i = 0; i < 5; ++i) {
    data += String(temperatureValues[i]) + "," + String(pressureValues[i]) + "," + 
            String(keysValues[i]) + "," + String(lampsValues[i]) + "," + 
            String(roundsValues[i]) + "," + String(dasteValues[i]);
    if (i < 4) {
      data += ","; // Add comma between sets of values
    }
  }

  // Send data over serial
  Serial.println(data);

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
