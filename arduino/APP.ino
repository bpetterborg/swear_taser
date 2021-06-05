/*
 * Put this on the Arduino that you're using
 * Should work on most Uno-compatible boards
 * Gets serial data to know when to shock you
 */

int incomingData;
int TIME_ON = 5000;
const int TOKEN = 123;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); // this is set to internal led just for testing

  digitalWrite(13, HIGH);
  delay(1000);
  Serial.write("CONNECTED \n");
  Serial.write(TOKEN);
}

void loop() {
  
  while (Serial.available()) {
    incomingData = Serial.read();
    
    if (incomingData == TOKEN) {
      
      digitalWrite(13, HIGH);
      Serial.write("STARTING \n");
      delay(TIME_ON);
      
      digitalWrite(13, LOW);
      Serial.write("STOPPING \n");
    }
  }
}
