import tkinter as tk

ventana=tk.Tk()

nombree=tk.Label(ventana, text="Nombre:")
nombree.grid(row=1, column=0)
nombre=tk.Entry(ventana, text="Nombre")
edadd=tk.Label(ventana, text="Edad:")
edadd.grid(row=2, column=0)
edad=tk.Entry(ventana, text="Edad")
correoo=tk.Label(ventana, text="Correo:")
correoo.grid(row=3, column=0)
correo=tk.Entry(ventana, text="Correo")
nombre.grid(row=1, column=1)
edad.grid(row=2, column=1)
correo.grid(row=3, column=1)

def guardar():
    nombre_=nombre.get()
    edad_=edad.get()
    correo_=correo.get()
    texto_=tk.Label(ventana, text=f"Nombre: {nombre_}, Edad: {edad_}, Correo: {correo_}")
    texto_.grid(row=5, column=1)
guardar=tk.Button(ventana, text="Guardar", command=guardar)
guardar.grid(row=4, column=1)


ventana.geometry("400x200")
ventana.mainloop()