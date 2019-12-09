 int trigpin1 = 10;
 int echopin1 = 9;
 int trigpin2 = 8;
 int echopin2 = 7;
 int trigpin3 = 6;
 int echopin3 = 5;
 //int trigpin ,echopin;
 int d_r,d_f,d_l;
void setup() {
  // put your setup code here, to run once:
    
     Serial.begin(9600);
     pinMode(trigpin1,OUTPUT);
     pinMode(trigpin2 ,OUTPUT);
     pinMode(trigpin3,OUTPUT);
     pinMode(echopin1,INPUT);
     pinMode(echopin2,INPUT);
     pinMode(echopin3,INPUT);
     //declaration of pins is done 
     
}


void loop() {
         d_r = dis(trigpin2,echopin2);
         d_f = dis(trigpin1,echopin1);
         
         d_l = dis(trigpin3,echopin3);
         Serial.print(d_f);
        // Serial.print("\t");
         //Serial.print(d_r);
        // Serial.print("\t");
         Serial.println(d_l);
}


int dis(int trigpin,int echopin)
{
   // put your main code here, to run repeatedly:
   long duration ;
   float distance ;
   digitalWrite(trigpin,HIGH);
   delayMicroseconds(100);
   digitalWrite(trigpin,LOW);
   duration = pulseIn(echopin,HIGH);
   distance = (duration/2)/29.1;
  // Serial.println(distance);
   return distance;
   //prints the distnce
   //delay(10);
}
