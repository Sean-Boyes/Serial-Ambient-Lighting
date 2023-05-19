
#define BLUE 3
#define GREEN 5
#define RED 6

int numb;
int val1 = 0;
int val2 = 0;
int val3 = 0;
int rnd = 1;
int iInt;
int inVal = 1;
int R;
int G;
int B;
void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ;
  }
//  Serial.println("Initiated");
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  digitalWrite(RED, HIGH);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);
}

void loop() {
  while (Serial.available() >0){    
    iInt = Serial.read();
//    delay(500);
    if (rnd == 3 && iInt != 10) {
      val3 = iInt;
      rnd += 1;
    }
    if (rnd == 2 && iInt != 10) {
      val2 = iInt;
      rnd += 1;
    }
//    delay(100);
    if (rnd == 1 && iInt != 10) {
      val1 = iInt;
      rnd += 1;
    }
//    delay(100);
    if (iInt == 10) {
//      Serial.println("numb:");
      if (val1 != 0) {
        val1 -= 48;
      }
      if (val2 != 0) {
        val2 -= 48;
      }
      if (val3 != 0) {
        val3 -= 48;
      }
      numb = (val1*100)+(val2*10)+(val3);
      if (rnd == 3) {
        numb /= 10;
      }
      if (rnd == 2) {
        numb /= 100;
      }
//      Serial.println(numb);
//      Serial.println("round:");
//      Serial.println(rnd);
      if (inVal == 3) {
        B = numb;
        inVal += 1;
      }
      if (inVal == 2) {
        G = numb;
        inVal += 1;
      }
      if (inVal == 1) {
        R = numb;
        inVal += 1;
      }
      if (inVal == 4) {
//        Serial.println(R);
//        Serial.println(G);
//        Serial.println(B);
        analogWrite(RED, R);
        analogWrite(GREEN, G);
        analogWrite(BLUE, B);
        inVal = 1;
      }
      rnd = 1;
      val1 = 0;
      val2 = 0;
      val3 = 0;
    }
  }
}
