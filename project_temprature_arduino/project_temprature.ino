int temprature_data[10] = {22.3, 22.4, 23.4, 22.4, 19.8, 20.8, 20.2, 22.8, 24.9, 20.78};

int a =0; 

void setup() {
Serial.begin(9600);              //Starting serial communication
}

  
void loop() {
  while(a<10) {
    Serial.println(temprature_data[a]);
    delay(1000);   // give the loop some break
    a++;           // a value increase every loop
  }
}
