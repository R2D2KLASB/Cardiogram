int const PULSE_SENSOR_PIN = 0;
int Signal;
#define USE_ARDUINO_INTERRUPTS false

#include <PulseSensorPlayground.h>
const int OUTPUT_TYPE = SERIAL_PLOTTER;
const int PULSE_INPUT = A0;
const int THRESHOLD = 400;   // Adjust this number to avoid noise when idle
byte samplesUntilReport;
const byte SAMPLES_PER_SERIAL_SAMPLE = 10;
PulseSensorPlayground pulseSensor;
void setup() {
  pulseSensor.analogInput(PULSE_INPUT);
  Serial.begin(9600);
  pulseSensor.setSerial(Serial);
  pulseSensor.setOutputType(OUTPUT_TYPE);
  pulseSensor.setThreshold(THRESHOLD);
}

void loop() {
  String myString = "";
  if (Serial.read()){
    unsigned long starttime = millis();
    while (millis() - starttime < 3000){
      if (pulseSensor.sawNewSample()) {
        myString.concat(analogRead(PULSE_INPUT));
        myString.concat("\r\n");
        delay(1);
      
      }
    }
    Serial.print(myString);
    
  }
  
//  if (pulseSensor.sawNewSample()) {
//    
//    
//      Serial.println(analogRead(PULSE_INPUT));
//      delay(1);
//      
//    }
    
//  Signal = analogRead(PULSE_SENSOR_PIN); 
//  Serial.println(Signal);               
     
}
