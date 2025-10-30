import tkinter as tk
import os

ventana = tk.Tk()
ventana.geometry("500x300") #tamaño pantalla
#etiqueta = tk.Label(ventana, text="Hola, Mundo!", bg="blue") #donde va a ir, texto para poner
#etiqueta.pack(fill=tk.BOTH, expand=True) #fill es para que ocupe todo el espacio, expand es para que se expanda
def si(hi="pp"):
    etiqueta = tk.Label(ventana, text=f"Hola,{hi} ", bg="blue") #donde va a ir, texto para poner
    etiqueta.pack(fill=tk.BOTH, expand=True) #fill es para que ocu
def rick():
    os.startfile("C:/Users/HP/Desktop/Provicional 2.0/Alejandro-Ducuara-Clases/ramdom/calculadora/pag2.html")

#BOTONES
boton1 = tk.Button(ventana, text="Boton 1", bg="red", command=si)
boton1.pack(side=tk.LEFT, fill=tk.Y)

boton2 = tk.Button(ventana, text="Boton 2", bg="green", command=rick)
boton2.pack(side=tk.RIGHT, fill=tk.Y)


caja_texto = tk.Entry(ventana)
caja_texto.pack(side=tk.TOP, fill=tk.X,)


def imprimir_texto():
    texto = caja_texto.get()
    si(texto)
    

boton3 = tk.Button(ventana, text="Boton 3", bg="blue", command=imprimir_texto)
boton3.pack(side=tk.BOTTOM, fill=tk.X)

# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)   
# boton3.grid(row=2, column=0)

ventana.mainloop()#fill estirar, side poner en un lado