int trigpin,echopin;
int trigpin1 = 34;
int trigpin2 = 36;
//int trigpin3 = 40 ;
int echopin1 = 32;
int echopin2 = 38;
//int echopin3 = 42;
int d_r,d_f,d_l;;
void setup() {
   put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trigpin,OUTPUT);
  pinMode(trigpin1,OUTPUT);
 pinMode(trigpin2,OUTPUT);
 pinMode(trigpin3,OUTPUT);
  pinMode(echopin,INPUT);
  pinMode(echopin1,INPUT);
  pinMode(echopin2,INPUT);
  pinMode(echopin3,INPUT);
  
  

}

void loop() {
  // put your main code here, to run repeatedly:
  d_f  = dis(trigpin1,echopin1);
  d_r = dis(trigpin2,echopin2);
 // d_l = dis(trigpin3,echopin3);
  Serial.println(d_f);
  delay(10);
  Serial.println(d_r);
  delay(10);
  Serial.println(d_l);
  delay(10);
  Serial.println("--------------");
  

}
// distance function
int dis(int trigpin,int echopin)
{
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
