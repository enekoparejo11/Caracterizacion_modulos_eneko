import numpy as np 
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import statistics as stats

tension,corriente,corriente_rectificada=np.loadtxt('datos.txt',skiprows=0,unpack=True)

#print(tension)

'''plt.plot(tension)'''

corriente_buena=np.array(corriente_rectificada)

#plt.plot(corriente)

#plt.plot(corriente)
#plt.plot(corriente_rectificada[18:])

pos_max=np.where(corriente_rectificada == np.amax(corriente_rectificada))

posicion=pos_max[0]
posicion_buena=posicion[0]

print(posicion_buena)

corriente_rectificada_nueva=corriente_rectificada

for i in range (47):
    corriente_rectificada_nueva[i]=corriente_rectificada[posicion_buena]
    
'''pos_min=np.where(corriente_rectificada == np.amin(corriente_rectificada))


posicion_min=pos_min[0]
posicion_min_buena=posicion_min[0]'''

array_media=corriente_rectificada_nueva[124:181]


media=stats.mean(array_media)
media=round(media,2)

print(media)




    
array_el_bueno=corriente_rectificada_nueva[18:]

array_concatenado=[]


for i in range(18):
   array_concatenado.append(media)
    
print(array_concatenado)

#array_el_bueno.concatenate(array_concatenado)

#array_definitivo=array_el_bueno+array_concatenado

array_definitivo=np.concatenate((array_el_bueno,array_concatenado))

for i in range(124,199):
    array_definitivo[i]=media
    
salto=media/75
print(salto)


for i in range (125,200):
    array_definitivo[i]=array_definitivo[i-1]-salto
    
    if(array_definitivo[i]<0):
        array_definitivo[i]=0
    

for i in range (125,200):
    array_definitivo[i]=round(array_definitivo[i],3)
    
    
    
print(array_definitivo)
#plt.plot(tension,array_definitivo)

potencia=[]

for i in range(0,199):
    
    potencia.append(tension[i]*array_definitivo[i])
    

print(array_definitivo)

#plt.plot(tension,corriente)
#plt.plot(tension,corriente_rectificada)
plt.plot(tension,array_definitivo)
#plt.plot(potencia,'r*')



pos_max_potencia=int(np.where(potencia == max(potencia))[0])

print(pos_max_potencia)

print(max(potencia))
print(tension[pos_max_potencia],array_definitivo[pos_max_potencia])
plt.plot(tension[pos_max_potencia],array_definitivo[pos_max_potencia],'r*')


plt.show()
    
