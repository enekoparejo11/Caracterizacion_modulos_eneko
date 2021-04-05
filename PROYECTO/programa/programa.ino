
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SD.h>

LiquidCrystal_I2C lcd(0x27,16,2);
File myFile;

const int inputPin=2;
const int relay=10;
const int tension_max=40;
int state=0;
const int CS_pin=9;
float sensibility = 0.100;
float shunt = 0.2;

const int muestras=300;
 
int  voltaje[muestras];
int  corriente[muestras];
int  temperatura[muestras];
int  irradiancia[muestras];
int i=0;
unsigned long tiempo1;
unsigned long   tiempo2;
int delta; 
int valor=1;
float Y=0.0;
float alpha=0.05;
float S=Y;
int R=1; //ohmios


void setup()

{
 analogReference(INTERNAL1V1); 
 digitalWrite(relay,HIGH);
 delay(1000);
 lcd.init();
 lcd.backlight();

 Serial.begin(9600);
 pinMode(inputPin,INPUT);
 pinMode(relay,OUTPUT);


//Comprobación de que la tarjeta SD está bien conectada
 initialition_checking();
 delete_file_SD();

 //Mensaje de inicio
 //Comprobación de que la tarjeta SD está bien conectada (hay que programarlo)
 //lcd.println("---------------------------------------------------");
 //lcd.println("Pulse el boton iniciar para comenzar la medición: ");
 //lcd.println("---------------------------------------------------"); 
  lcd.setCursor(0,0);
  lcd.print("Pulse el boton ");
  lcd.setCursor(0,1);
  lcd.print("para comenzar");
  delay(1000);

    
    
  }


 
void loop() 

{


state=digitalRead(inputPin);

if(state == HIGH)



  {
    lcd.clear();
    digitalWrite(relay,LOW);
   
    tiempo1=micros();
    
   
    for(i=0;i<muestras;i++)
    {
      voltaje[i]=analogRead(A2);
      corriente[i]=analogRead(A1);
      //delayMicroseconds(1000);
    }
    digitalWrite(relay,HIGH);



   
    tiempo2=micros();

    //IMPRIMIR MEDIDAS
    
    analogReference(DEFAULT);
    int temperatura_buena=analogRead(A4);
    int irradiancia_buena=analogRead(A5);
    for(i=0;i<muestras;i++)
    {
     Serial.print(float(tension_max)*voltaje[i]/1023);
     //Serial.print(voltaje[i]);
     Serial.print(" ");
     //float Corriente=(abs(((corriente[i]*5.0/1023)-2.5)/sensibility));
     //Serial.print((abs(((corriente[i]*5.0/1023)-2.5)/sensibility)),8);
     //S=(alpha*Corriente)+((1-alpha)*S);
       Serial.print((corriente[i]*1.1/1023)/shunt);
     Serial.print(" ");
     Serial.print(temperatura_buena);
     Serial.print(" ");
     Serial.print(irradiancia_buena);
     Serial.println(" ");
     //Serial.print(S);
     //Serial.println(" ");
     //Serial.print(temperatura[i],8); 
     //Serial.print(" ");
     //Serial.println(irradiancia[i],8); 
    }
 
    Serial.print("Tiempo de medición  (ms): ");
    Serial.println(((tiempo2-tiempo1)/1000));
    Serial.println("---------------------------------------------------"); 

    lcd.setCursor(0,0);
    lcd.print("Medicion");
    lcd.setCursor(0,1);
    lcd.print("finalaizada");
    delay(3000);
    lcd.clear();
    float maximo_tension=max(voltaje[0],voltaje[muestras-1]);
    float maximo_corriente=max(corriente[0],corriente[muestras-1]);
    float voc=float(tension_max)*maximo_tension/1023;
    float isc=(maximo_corriente*1.1/1023)/shunt;
    float pmax=voc*isc;
    float irradiancia_final=irradiancia_buena*1.123;
    
    
    lcd.setCursor(0,0);
    lcd.print("V:");
    lcd.setCursor(2,0);
    //lcd.print(float(tension_max)*maximo_tension/1023);
    lcd.print(voc);
    lcd.setCursor(9,0);
    lcd.print("I:");
    lcd.setCursor(11,0);
    //lcd.print((maximo_corriente*1.1/1023)/shunt);
    lcd.print(isc);
    lcd.setCursor(0,1);
    lcd.print("P:");
    lcd.setCursor(2,1);
    lcd.print(pmax);
    lcd.setCursor(9,1);
    lcd.print("E:");
    lcd.setCursor(11,1);
    lcd.print(irradiancia_final);


    //escritura tarjeta SD

          myFile.print(tension);
          myFile.print(" ");
          myFile.print(corriente,2);
          myFile.print(" ");
          myFile.print(humedad);
          myFile.print(" ");
          myFile.println(temperatura);
          myFile.print(" ");
          myFile.close();

    

}



 

}


    //RUTINA COMPROBACIÓN

    float initialition_checking()
    {

      if (!SD.begin(CS_pin)) //se le ha definido el puerto CS de la tarjeta SD al pin 9, sería recomendable definirlo como constante
      {
        lcd.println("No se pudo");
        lcd.setCursor(0,1);
        lcd.print("Inicializar tarjeta SD");
        //return;
      }

    lcd.print("inicializacion");
    lcd.setCursor(0,1);
    lcd.print("correcta");
    delay(2000);
    lcd.clear();
    lcd.setCursor(0,0);

    }

  //RUTINA BORRADO FICHERO TARJETA SD

    float delete_file_SD()

    {

          if (SD.exists("datos.txt")) 
    
      {
        SD.remove("datos.txt");
        lcd.print("Eliminando");
        lcd.setCursor(0,1);
        lcd.print("archivo");
        delay(3000);
      }

    }
   
