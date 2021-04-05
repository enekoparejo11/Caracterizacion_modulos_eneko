import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import statistics as stats
import math
from tabulate import tabulate



tension,bits,bits_temperatura,bits_irradiancia=np.loadtxt('Mediciones/prueba_3.txt',skiprows=0,unpack=True)

#nº de muestras
longitud=len(tension)
#valor de la resistencia shunt
shunt=0.15
#corriente
corriente=[]
for i in range (longitud):
    corriente.append(((bits[i]*1.1/1023)/shunt))
#potencia
potencia=[]
for i in range (longitud):
    potencia.append(tension[i]*corriente[i])
#temperatura e irradiancia
temperatura=[]
irradiancia=[]
for i in range (longitud):
    temperatura.append((bits_temperatura[i]/1023*5000)/10)
    irradiancia.append(bits_irradiancia[i]*1.123)

#EXTRAPOLACIÓN A CONDICIONES cem

#corriente CEM
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
#tension CEM
tension_corregida=[]
Ns=36
beta=-0.29/100
T1=max(temperatura)
T2=25
for i in range (longitud):
    tension_corregida.append(tension[i]-Ns*beta*(T2-T1)+0.4)
#potencia CEM
potencia_corregida=[]
for i in range (longitud):
    potencia_corregida.append(tension_corregida[i]*corriente_corregida[i])



def graficar():
    plt.figure(figsize=(18,10),dpi=72)
    
    #grafica I_V
    plt.subplot(121)
    plt.plot(tension_corregida,corriente_corregida,label="Condiciones CEM")
    plt.plot(tension,corriente,label="Gráfica real")
    #plt.plot(tension_corregida,fun(tension,*coef1),label="Grafica CEM")
    plt.legend(loc='lower left')
    plt.xlabel('Tensión (V)')
    plt.ylabel('Corriente(A)')
#  
    

    #grafica P_V
    plt.subplot(122)
    plt.plot(tension_corregida,potencia_corregida,label="Condiciones CEM")
    plt.plot(tension,potencia,label="Gráfica real")
    
    #plt.plot(tension_corregida,potencia_corregida,label="Grafica CEM")
    plt.legend(loc='upper left')
    plt.xlabel('Tensión (V)')
    plt.ylabel('Potencia (W)')

   
    plt.show()

def datos():


    posicion_max_potencia= int(np.where(potencia==max(potencia))[0])
    posicion_max_potencia_CEM =int(np.where(potencia_corregida==max(potencia_corregida))[0])



    datos= [['Tension de circuito abierto (Voc)', round(max(tension),2)],
         ['Corriente de cortocircuito (Isc)', round(max(corriente),2)],
         ['Potencia máxima (Pmax)', round(max(potencia),2)],
         ['Tension a máxima potencia (Vmpp)', round(tension[posicion_max_potencia],2)],
         ['Corriente a máxima potencia (Impp)', round(corriente[posicion_max_potencia],2)],
         ['Temperatura', round(stats.mean(temperatura),2)],
         ['Irradiancia',round(stats.mean(irradiancia),2)],
         ['Tension de circuito abierto CEM (Voc_CEM)',round(max(tension_corregida),2)],
         ['Corriente de cortocircuito CEM (Isc_CEM)',round(max(corriente_corregida),2)],
         ['Potencia máxima CEM (Pmax_CEM)',round(max(potencia_corregida),2)],
         ['Tension a máxima potencia CEM (Vmpp_CEM)', round(tension_corregida[posicion_max_potencia_CEM],2)],
         ['Corriente a máxima potencia CEM (Impp_CEM)', round(corriente_corregida[posicion_max_potencia_CEM],2)]]


    print(tabulate(datos))

def rendimiento():
    potencia_panel=int(input("Potencia del panel (W): "))
    irradiancia_cem=1000
    superficie=int(input("Superficie del panel (m2):"))

    rendimiento=potencia_panel/(irradiancia_cem*superficie)*100
    print(rendimiento) 




#graficar()
datos()
