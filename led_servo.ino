#include <Servo.h>
Servo servoku;
int led1 = 13;
int led2 = 12;
int led3 = 11;

void setup() {
  servoku.attach(6);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

void loop() {
  digitalWrite(led1, HIGH);
  digitalWrite(led2, HIGH);
  digitalWrite(led3, HIGH);
  servoku.write(0);
  delay(1000);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  servoku.write(180);
  delay(1000);
}
