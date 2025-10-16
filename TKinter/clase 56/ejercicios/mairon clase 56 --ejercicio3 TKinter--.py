import tkinter as tk
ventana=tk.Tk()
ventana.geometry("500x500")
tar=tk.Label(ventana, text="Ingrese la tarea:")
tar.grid(row=0, column=0, columnspan=2)

espacio=tk.Label(ventana, text=""   )
espacio.grid(row=1, column=0)

lista=tk.Listbox(ventana, width=25)
lista.grid(row=2, column=4, columnspan=5)

tarea=tk.Entry(ventana, text="0", width=50)
tarea.grid(row=0, column=2, columnspan=3)

mensaje=tk.Label(ventana)
mensaje.grid(row=4, column=4, columnspan=3)

def agregar():
    tarea_=tarea.get()

    if tarea_.strip() != "":
        mensaje.configure(text="Tarea agregada con exito")
        lista.insert(tk.END, f"{tarea_}")
        tarea.delete(0, tk.END)
    else:
        mensaje.configure(text="No ingreso ninguna tarea")
        
def eliminar():
    if lista.size() != 0:
        tarea_=tarea.get()
        if tarea_.strip() != "":
            indices=lista.get(0, tk.END)
            if tarea_ in indices:
                indice=indices.index(tarea_)
                lista.delete(indice)
                mensaje.configure(text="Tarea eliminada con exito")
                tarea.delete(0, tk.END)
            else:
                mensaje.configure(text="La tarea no se encuentra en la lista")
                tarea.delete(0, tk.END)
            
        else:
            mensaje.configure(text="Ingrese la tarea a eliminar")
    else:
        mensaje.configure(text="No hay tareas para eliminar")
        
        
agregar=tk.Button(ventana, text="Agregar tarea", command=agregar)
agregar.grid(row=2, column=0, sticky="n")

eliminar=tk.Button(ventana, text="Eliminar tarea", command=eliminar)
eliminar.grid(row=2, column=1, sticky="n")
        


ventana.mainloop()