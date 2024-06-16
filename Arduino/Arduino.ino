void setup() {
  Serial.begin(9600); // Initialize serial communication with baud rate 9600
  randomSeed(analogRead(0)); // Initialize random number generator with analog pin 0 value
}

void loop() {
  // Create sensor values
  int temperatureValues[5];
  int pressureValues[5];
  bool keysValues[14];
  bool lampsValues[5];
  int roundsValues[5];
  int dasteValues[5];

  // Generate sensor values
  Temperature(temperatureValues);
  Pressure(pressureValues);
  Keys(keysValues);
  Lamps(lampsValues);
  Rounds(roundsValues);
  Daste(dasteValues);

  // Merge sensor values into a single string
  String data = "";

  // Add temperature values to data string
  for (int i = 0; i < 5; ++i) {
    data += String(temperatureValues[i]);
    data += ",";
  }

  // Add pressure values to data string
  for (int i = 0; i < 5; ++i) {
    data += String(pressureValues[i]);
    data += ",";
  }

  // Add keys values to data string
  for (int i = 0; i < 14; ++i) {
    data += String(keysValues[i]);
    data += ",";
  }

  // Add lamps values to data string
  for (int i = 0; i < 5; ++i) {
    data += String(lampsValues[i]);
    data += ",";
  }

  // Add rounds values to data string
  for (int i = 0; i < 5; ++i) {
    data += String(roundsValues[i]);
    data += ",";
  }

  // Add daste values to data string
  for (int i = 0; i < 5; ++i) {
    data += String(dasteValues[i]);
    if (i < 4) {
      data += ",";
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

void Keys(bool values[]) {
  // Generate random keys values (true/false)
  values[0] = false;
  values[1] = false;
  values[2] = false;
  values[3] = false;
  values[4] = false;
  values[5] = false;
  values[6] = false;
  values[7] = false;
  values[8] = false;
  values[9] = false;
  values[10] = false;
  values[11] = false;
  values[12] = false;
  values[13] = false;


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
