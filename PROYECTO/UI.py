from tkinter import *
import tkinter
from PIL import ImageTk, Image
#import principal
from tkinter import filedialog
import shutil as sht

ventana = Tk()
ventana.title ('Trazador de curvas I-V')
ventana.geometry('600x600')
ventana.config(bg='#222831')


mensaje1=Label(ventana,text="Obtención de las características \n de paneles fotovoltaicos")
mensaje1.config(font=("Verdana",12))
mensaje1.place(bordermode=OUTSIDE, height=100, width=100)
mensaje1.pack()

imagen1=ImageTk.PhotoImage(Image.open('imagenes/Logo_EIG_EHU.jpg'))
graficar=ImageTk.PhotoImage(Image.open('imagenes/graficar.jpg').resize((100, 100)))
abrir=ImageTk.PhotoImage(Image.open('imagenes/abrir.png').resize((100,100)))
ehu_logo=Label(image=imagen1)
ehu_logo.pack()


condicion=False

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    destino =r"C:\Users\Eneko\Desktop\PROYECTO"
    #print('Selected:', filename)
    sht.copy(filename,destino)
    condicion=True
    print("fichero copiado")
    print(condicion)
    import main
    print("importado wey")
    boton = Button(image=graficar,command=(lambda: main.graficar()))
    boton.place(x=125,y=125)
    boton.pack(expand=1)


button = Button(image=abrir, command=UploadAction)
button.place(x=300,y=300)
button.place(x=125,y=125)
button.pack(expand=1)




ventana.mainloop()

