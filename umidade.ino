#define SensorPin A0

float sensorValue = 0;
void setup() {
  Serial.begin(9600);
}

void loop(){
  for (int i = 0; i <=100; i++){
    sensorValue += analogRead(SensorPin);
    delay(5);
  }
  sensorValue /= 100;
  Serial.println(map(sensorValue, 200, 1043, 100, 0));
  delay(50);
}
