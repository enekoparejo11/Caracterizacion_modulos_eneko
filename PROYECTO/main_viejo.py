import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import statistics as stats
import math


#lectura de los datos

tension,bits,bits_temperatura,bits_irradiancia=np.loadtxt('Mediciones/prueba_tejado.txt',skiprows=0,unpack=True)

#longitud del array de las muestras

longitud=len(bits) 

#calculo corriente
shunt=0.2
corriente=[]

for i in range (longitud):
    corriente.append((bits[i]*1.1/1023)/shunt)


#suavizar curva

def fun(x, a, b, c):
    return a * np.cosh(b * x) + c


coef,_ = curve_fit(fun, tension, corriente)


#potencia

potencia=[]

for i in range (longitud):
    potencia.append(tension[i]*corriente[i])

print("Potencia: ",max(potencia))
print("Corriente: ", max(corriente))
print("Tension: ", max(tension))



#temperatura e irradiancia

temperatura=[]
irradiancia=[]

for i in range (longitud):
    temperatura.append((bits_temperatura[i]/1023*5000)/10)
    irradiancia.append(bits_irradiancia[i]*1.123)
    
print("Temperatura: ", stats.mean(temperatura))
print("Irradiancia:", stats.mean(irradiancia))
 


#extrapolación a condiciones estandar CEM+


#extrapolación corriente

corriente_corregida=[]

Isc1=max(corriente)
E2=1000
E1=max(irradiancia)
alpha=-0.086/100
T2=25
T1=max(temperatura)
Isc2=Isc1*(E2/E1)+(alpha*(T2-T1))
deltaI=Isc2-Isc1
for i in range (longitud):
    corriente_corregida.append((corriente[i]*(E2/E1)+(alpha*(T2-T1))))

coef1,_=curve_fit(fun,tension,corriente_corregida)


#extrapolacion tension

tension_corregida=[]

Ns=36
beta=-0.29/100
T1=max(temperatura)
T2=25

for i in range (longitud):
    tension_corregida.append(tension[i]-Ns*beta*(T2-T1))


#extrapolación corriente

potencia_corregida=[]

for i in range (longitud):
    potencia_corregida.append(tension_corregida[i]*corriente_corregida[i])





#graficar
def graficar():
    plt.figure(figsize=(18,10),dpi=72)
    
    #grafica I_V
    plt.subplot(121)
    #plt.plot(tension,corriente)
    plt.plot(tension,fun(tension,*coef),label="Gráfica real")
    #plt.plot(tension_corregida,fun(tension,*coef1),label="Grafica CEM")
    plt.legend(loc='upper right')
    plt.xlabel('Tensión (V)')
    plt.ylabel('Corriente(A)')
    

    
      
    #grafica P_V
    plt.subplot(122)
    plt.plot(tension,potencia,label="Gráfica real")
    #plt.plot(tension_corregida,potencia_corregida,label="Grafica CEM")
    plt.legend(loc='upper left')
    plt.xlabel('Tensión (V)')
    plt.ylabel('Potencia (W)')
   
    plt.show() 


print("Corriente ISC en CEM:", max(corriente_corregida))
print("Tension Voc en CEM:", max(tension_corregida))
print("Potencia CEM:",max(potencia_corregida))


#calculo de error en las mediciones

def error ():
    real=float(input("Introduce el valor real: "))
    teorico=float(input("Introduce el valor teorico: "))
    error=abs(((real-teorico)/teorico)*100)
    print(error)



