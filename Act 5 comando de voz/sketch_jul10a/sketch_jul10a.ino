int led1 = 25;
int led2 = 26;


void setup() {

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

  Serial.begin(9600);

}


void loop() {


  if(Serial.available()){


    char comando = Serial.read();


    switch(comando){


      case 'A':
        digitalWrite(led1, HIGH);
        break;


      case 'a':
        digitalWrite(led1, LOW);
        break;


      case 'B':
        digitalWrite(led2, HIGH);
        break;


      case 'b':
        digitalWrite(led2, LOW);
        break;
      



      case 'T':
        digitalWrite(led1, HIGH);
        digitalWrite(led2, HIGH);

        break;


      case 't':
        digitalWrite(led1, LOW);
        digitalWrite(led2, LOW);

        break;
     }

  }

}