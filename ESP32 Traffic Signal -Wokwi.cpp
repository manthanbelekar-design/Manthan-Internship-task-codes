int red[]    = {23, 19, 17, 2};
int yellow[] = {22, 18, 16, 15};
int green[]  = {21, 5, 4, 13};

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(red[i], OUTPUT);
    pinMode(yellow[i], OUTPUT);
    pinMode(green[i], OUTPUT);
  }
}

void allRed() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(red[i], HIGH);
    digitalWrite(yellow[i], LOW);
    digitalWrite(green[i], LOW);
  }
}

void runLane(int lane) {
  allRed();

  digitalWrite(red[lane], LOW);
  digitalWrite(green[lane], HIGH);
  delay(5000);

  digitalWrite(green[lane], LOW);
  digitalWrite(yellow[lane], HIGH);
  delay(2000);

  digitalWrite(yellow[lane], LOW);
  digitalWrite(red[lane], HIGH);
}

void loop() {
  runLane(0);
  runLane(1);
  runLane(2);
  runLane(3);
}