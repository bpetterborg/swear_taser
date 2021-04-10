/*  
 *  Put this one on the Arduino you're using
 *  
 *  This gets the serial data from the PC to 
 *  know when to shock you.
 *  
 */

int incomingData;
int TASING_TIME = 1000;

void setup() 
{
    Serial.begin(9600);
    pinMode(11, OUTPUT);    // status led
    pinMode(12, OUTPUT);    // relay (for taser)

    digitalWrite(11, HIGH);
    delay(10);
    Serial.write("Connected to Arduino");
    digitalWrite(11, LOW);
}

void loop() 
{
    while (Serial.available())
    {
        incomingData = Serial.read();
        if (incomingData == 1)
        {
            digitalWrite(12, HIGH);     // taser on
            Serial.write("Tasing...");  
            delay(TASING_TIME);         // wait for TASING_TIME ms
            digitalWrite(12, LOW);      // taser off
        }
    }
}