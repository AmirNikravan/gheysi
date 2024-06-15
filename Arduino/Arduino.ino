void setup() {
  Serial.begin(9600); // Initialize serial communication with baud rate 9600
  randomSeed(analogRead(0)); // Initialize random number generator with analog pin 0 value
}

void loop() {
  int randomNumbers[14]; // Array to store 14 random numbers
  
  // Generate 2 random numbers between 0 and 124
  for (int i = 0; i < 2; ++i) {
    randomNumbers[i] = random(120); // Generates numbers from 0 to 124
  }
  
  // Generate 5 random numbers between 234 and 956
  for (int i = 2; i < 7; ++i) {
    randomNumbers[i] = random(120); // Generates numbers from 234 to 956
  }
  
  // Generate remaining 7 random numbers (adjust ranges as needed)
  for (int i = 7; i < 14; ++i) {
    randomNumbers[i] = random(120); // Generates numbers from 0 to 999 (adjust range as needed)
  }

  // Send all 14 numbers as a single comma-separated string
  for (int i = 0; i < 24; ++i) {
    Serial.print(randomNumbers[i]);
    if (i < 23) {
      Serial.print(","); // Add comma between numbers
    }
  }
  Serial.println(); // Newline to indicate end of transmission

  delay(100); // Delay for 2 seconds before repeating
}
