int ldrPin = A0;
int ledPin = 9;

void setup() {
    pinMode(ledPin, OUTPUT);
}

void loop() {
    int ldrValue = analogRead(ldrPin);

    int brightness = map(ldrValue, 0, 1023, 0, 255);

    analogWrite(ledPin, brightness);

    delay(10);
}