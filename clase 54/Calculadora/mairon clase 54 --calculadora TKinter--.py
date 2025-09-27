import tkinter as tk

ventana=tk.Tk() #crea la ventana principal

ventana.title("Silksong") #Asisgna el titulo de la ventana
ventana.geometry("300x400")

entrada= tk.Entry(ventana, width=20, font=("Arial", 18), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones=[
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)]

#
def click(numero): #funcion que se ejecuta cuando se presiona un boton
    actual=entrada.get() #se obtiene el texto que ya esta escrito
    entrada.delete(0, tk.END) #se borra el contenido actualk de la entrada
    entrada.insert(0, actual+str(numero)) #se inserta nuevamente  el texto anterior mas el numero nuevo
    
def borrar(): #se define la funcion borrar 
    entrada.delete(0, tk.END) #borra el contenido de la caja de entrada

def calcular(): #evalua lo escrito en la caja de texto
    try:
        resultado=eval(entrada.get()) #evalua lo escrito en la caja de entrada como operacion matematica
        entrada.delete(0, tk.END) 
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")