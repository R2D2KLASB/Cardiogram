int const PULSE_SENSOR_PIN = 0;
int Signal;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Signal = analogRead(PULSE_SENSOR_PIN); 
  Serial.println(Signal);               
  delay(1);
}
