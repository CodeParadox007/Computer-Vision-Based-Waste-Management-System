#include <ESP32Servo.h>

Servo myservo_1;
Servo myservo_2; // create servo object to control a servo


int pos = 0;    // variable to store the servo position

void setup() {
  myservo_1.attach(13);
  myservo_2.attach(16);

  myservo_1.write(125);
  delay(1000);
  myservo_2.write(100);
  delay(2000);

  Serial.begin(9600);
    // attaches the servo on pin 9 to the servo object
}


void s1(){

myservo_1.write(60);
delay(3000);
myservo_1.write(125);
delay(2000);

}

void loop() {
  char c;

  if (Serial.available()){

    c=Serial.read();

    if (c=='C'){ // Battery
      
  myservo_2.write(100);
  delay(2000);
  s1();

  myservo_2.write(100);
  delay(2000);


    }

    if (c=='B'){ //Metal
      myservo_2.write(30);
      delay(2000);
      s1();
      myservo_2.write(100);
      delay(2000);
    }
    
    if (c=='A'){ //Plastic
      myservo_2.write(155);
      delay(2000);
      s1();
      myservo_2.write(100);
      delay(2000);
    }
    
  }

}
