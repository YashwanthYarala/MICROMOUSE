 int trigpin = 10;
 int echopin = 9;
void setup() {
  // put your setup code here, to run once:
    
     Serial.begin(9600);
     pinMode(trigpin,OUTPUT);
     pinMode(echopin,INPUT);
     //declaration of pins is done 
     
}

void loop() {
  // put your main code here, to run repeatedly:
   long duration , distance ;
   digitalWrite(trigpin,HIGH);
   delayMicroseconds(1000);
   digitalWrite(trigpin,LOW);
   duration = pulseIn(echopin,HIGH);
   distance = (duration/2)/29.1;
   Serial.println(distance);  //prints the distnce
   //delay(10);
}
