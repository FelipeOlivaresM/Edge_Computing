
/*
  Por si hay errores al usar el Com0 en Linux: sudo chmod a+rw /dev/ttyACM0
  
  -------------------------- Conexiones de AD8232 a Arduino Uno:

  -------------------- Alimentacion:

  Tierra: GND a GND.              <-------- cable negro.
  Alimentacion: 3.3v a 3.3v.      <-------- cable rojo.

  -------------------- Datos:

  Salida: OUTPUT a puerto analogo A0 (La señal de frecuencia cardíaca totalmente acondicionada está presente en esta salida).       <-------- cable amarillo (pierna derecha).
  Diodo de entrada: LO + a puerto digital       6 <-------- cable cafe (brazo izquierdo o derecho).
  Diodo de salida: LO - a puerto digital        7 <-------- cable naranja (brazo izquierdo o derecho).

  Se usan las conexiones LO- y LO+ para monitorear la impedancia piel-electron entre los diodos (Measurement of skin-electrode impedance),
  si la impedancia supera cietos parametros la señal de ecg captada no es confiable, esto debido a que la impedancia supera la impedancia
  minima necesaria para tomar una medida de ecg confiable.

*/

int pinLo1 = 6;       // LO - a puerto digital 6 <-------- cable naranja.
int pinLo2 = 7;       // LO + a puerto digital 7 <-------- cable cafe.
int Output = A0;      // Output a puerto analogo A0 <-------- cable naranja.

void setup() {
  Serial.begin(9600);
  pinMode(pinLo1, INPUT);
  pinMode(pinLo2, INPUT);
}

void loop() {
  if ((digitalRead(pinLo1) == 1) || (digitalRead(pinLo2) == 1)) {  // Validacion de la impedancia piel-electron.
    Serial.println('!');
  }
  else {  // Impresion de la señal de ecg si la impedancia piel-electron es aceptable.
    Serial.println(analogRead(Output));
  }
  delay(1);  //  Se hace una pequeña espera para no saturar el puerto serial.
}
