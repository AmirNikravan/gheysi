void setup() {
  Serial.begin(9600); // Initialize serial communication with baud rate 9600
  randomSeed(analogRead(0)); // Initialize random number generator with analog pin 0 value
}

void loop() {
  // Check for incoming serial data
  if (Serial.available() > 0) {
    String incomingData = Serial.readStringUntil('\n'); // Read the incoming data until newline character

    // Print the received data for debugging
    Serial.print("Received: ");
    Serial.println(incomingData);

    // Process the received data
    processReceivedData(incomingData);
  } else {
    // Create and send sensor data
    sendSensorData();
  }

  delay(10); // Small delay to allow serial processing
}

void sendSensorData() {
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

  Serial.println(data); // Send data over serial
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

void processReceivedData(String data) {
  // Example function to process the received data
  // This is where you can parse the data string and take actions based on it

  // Assuming the data format is "Button <button_name> clicked!"
  if (data.startsWith("Button ")) {
    int buttonNameStartIndex = 7;
    int buttonNameEndIndex = data.indexOf(" clicked!");
    String buttonName = data.substring(buttonNameStartIndex, buttonNameEndIndex);

    // Print the button name
    Serial.print("Button pressed: ");
    Serial.println(buttonName);

    // Take actions based on the button name
    // For example, if button name is "lamptest", do something
    if (buttonName == "lamptest") {
      // Perform actions for lamptest button press
      // Example: turn on a lamp, activate a relay, etc.
    }
    // Add more conditions for other buttons as needed
  }
}
