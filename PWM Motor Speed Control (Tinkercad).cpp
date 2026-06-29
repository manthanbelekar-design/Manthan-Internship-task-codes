int motorSpeedPin = 9;
int motorPin1 = 7;
int motorPin2 = 8;
int potPin = A0;

int potValue = 0;
int speedValue = 0;

void setup() {

    pinMode(motorSpeedPin, OUTPUT);
    pinMode(motorPin1, OUTPUT);
    pinMode(motorPin2, OUTPUT);

    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
}

void loop() {

    potValue = analogRead(potPin);

    speedValue = map(potValue, 0, 1023, 0, 255);

    analogWrite(motorSpeedPin, speedValue);
}