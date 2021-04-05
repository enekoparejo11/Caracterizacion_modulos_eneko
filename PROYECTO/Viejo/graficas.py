import matplotlib.pyplot as plt
import script_shunt_1
import numpy as np


def graficar():
    tension=script_shunt_1.tension
    corriente=script_shunt_1.corriente()
    potencia=script_shunt_1.potencia()
    
    plt.figure(figsize=(18,10),dpi=72)
    
    #grafica I_V
    plt.subplot(121)
    plt.plot(tension,corriente,label="Gráfica real")
    plt.legen(loc='upper right')
    plt.xlabel('Tensión (V)')
    plt.ylabel('Corriente(A)')
    plt.grid()
    
    #grafica P_V
    plt.subplot(122)
    plt.plot(potencia)
    plt.xlabel('Tensión (V)')
    plt.ylabel('Potencia (W)')
    plt.grid()

    plt.show()    


graficar()