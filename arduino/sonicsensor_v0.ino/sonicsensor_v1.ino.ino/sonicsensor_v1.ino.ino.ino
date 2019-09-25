#include "SoftwareSerial.h"
SoftwareSerial serial_connection(13, 12);//Create a serial connection with TX and RX on these pins
#define BUFFER_SIZE 64//This will prevent buffer overruns.
char inData[BUFFER_SIZE];//This is a character buffer where the data sent by the python script will go.
char inChar=-1;//Initialie the first character as nothing
int count=0;//This is the number of lines sent in from the python script
int i=0;//Arduinos are not the most capable chips in the world so I just create the looping variable once
int msg[2];

// defines pins numbers
const int sensorOneTrigPin = 6;
const int sensorOneEchoPin = 7;
const int sensorTwoTrigPin = 9;
const int sensorTwoEchoPin = 10;


// defines variables
long durationOne, durationTwo;
int distanceOne, distanceTwo;

void setup() {
  pinMode(sensorOneTrigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(sensorOneEchoPin, INPUT); // Sets the echoPin as an Input
  pinMode(sensorTwoTrigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(sensorTwoEchoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
  serial_connection.begin(9600);//Initialize communications with the bluetooth module
  serial_connection.println("Ready!!!");//Send something to just start comms. This will never be seen.
  Serial.println("Started");//Tell the serial monitor that the sketch has started.
}

void loop() {
  // Clears the trigPin
  digitalWrite(sensorOneTrigPin, LOW);
  delayMicroseconds(2);


  //   Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(sensorOneTrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sensorOneTrigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  durationOne = pulseIn(sensorOneEchoPin, HIGH);

  // Calculating the distance
  distanceOne= durationOne*0.034/2;

  // Clears the trigPin
  digitalWrite(sensorTwoTrigPin, LOW);
  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(sensorTwoTrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sensorTwoTrigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  durationTwo = pulseIn(sensorTwoEchoPin, HIGH);

  // Calculating the distance
  distanceTwo= durationTwo*0.034/2;

  // Prints the distance on the Serial Monitor
  Serial.print("Sensor One Distance: ");
  Serial.print(distanceOne);
  Serial.print("       Sensor Two Distance: ");
  Serial.println(distanceTwo);
  msg[0]=distanceOne;
  msg[1]=distanceTwo;
  serial_connection.println(String(msg[0])+','+String(msg[1]));//Then send an incrmented string back to the python scripy

  
}
