import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#lectura de los datos

tension,bits=np.loadtxt('datos_shunt3.txt',skiprows=0,unpack=True)


#longitud del array de las muestras

longitud=len(bits) 

#calculo corriente

corriente=[]

for i in range (longitud):
    corriente.append((bits[i]*5/1023))

#suavizar curva

def fun(x, a, b, c):
    return a * np.cosh(b * x) + c


coef,_ = curve_fit(fun, tension, corriente)



#potencia

potencia=[]

for i in range (longitud):
    potencia.append(tension[i]*corriente[i])

print(max(potencia))
print(max(corriente))
print(max(tension))


#extrapolación a condiciones estandar CEM+



plt.plot(tension,corriente)
plt.plot(tension,fun(tension,*coef))













#graficar
def graficar():
    plt.figure(figsize=(18,10),dpi=72)
    
    #grafica I_V
    plt.subplot(121)
    plt.plot(tension,fun(tension,*coef),label="Gráfica real")
    plt.legend(loc='upper right')
    plt.xlabel('Tensión (V)')
    plt.ylabel('Corriente(A)')
    plt.grid()
    
#grafica P_V
    '''plt.subplot(122)
    plt.plot(potencia)
    plt.xlabel('Tensión (V)')
    plt.ylabel('Potencia (W)')
    plt.grid()'''

   
    plt.show()    
    

    
    

