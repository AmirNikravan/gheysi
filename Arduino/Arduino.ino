// Global arrays to keep track of key states
bool keysValues[14];

void setup() {
  Serial.begin(9600); // Initialize serial communication with baud rate 9600
  randomSeed(analogRead(0)); // Initialize random number generator with analog pin 0 value

  // Initialize all key values to false
  for (int i = 0; i < 14; ++i) {
    keysValues[i] = false;
  }
}

void loop() {
  // Check for incoming serial data
  if (Serial.available() > 0) {
    String incomingData = Serial.readStringUntil('\n'); // Read the incoming data until newline character
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
  bool lampsValues[5];
  int roundsValues[5];
  int dasteValues[5];

  // Generate sensor values
  Temperature(temperatureValues);
  Pressure(pressureValues);
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

    // Take actions based on the button name and toggle the corresponding key
    if (buttonName == "lamptest") {//1
      keysValues[0] = !keysValues[0];
    } else if (buttonName == "lop") {//2
      keysValues[1] = !keysValues[1];
    } else if (buttonName == "mcr") {//3
      keysValues[2] = !keysValues[2];
    } else if (buttonName == "bridge"){//4
      keysValues[3] = !keysValues[3];
    } else if (buttonName == "increase_speed") {//5
      keysValues[4] = !keysValues[4];
    } else if (buttonName == "decrease_speed") {//6
      keysValues[5] = !keysValues[5];
    } else if (buttonName == "fault_ack") {//7
      keysValues[6] = !keysValues[6];
    } else if (buttonName == "fault_reset") {//8
      keysValues[7] = !keysValues[7];
    } else if (buttonName == "ahead") {//9
      keysValues[8] = !keysValues[8];
    } else if (buttonName == "neurtal") {//10
      keysValues[9] = !keysValues[9];
    } else if (buttonName == "astern") {//1
      keysValues[10] = !keysValues[10];
    } else if (buttonName == "start") {
      keysValues[11] = !keysValues[11];
    } else if (buttonName == "stop") {
      keysValues[12] = !keysValues[12];
    } else if (buttonName == "emergency_stop") {
      keysValues[13] = !keysValues[13];
    }
    // Add more conditions for other buttons as needed
  }
}
