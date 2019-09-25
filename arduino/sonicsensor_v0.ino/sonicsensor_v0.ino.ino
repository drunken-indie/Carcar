/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*
* by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/

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
}

void loop() {
// Clears the trigPin
digitalWrite(sensorOneTrigPin, LOW);
delayMicroseconds(2);


// Sets the trigPin on HIGH state for 10 micro seconds
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
Serial.println(distanceOne);
Serial.print("Sensor Two Distance: ");
Serial.println(distanceTwo);
}
