import tkinter as tk
ventana=tk.Tk()
ventana.title("Calcular costos")
ventana.geometry("300x200")

elementos=[(1,"Decoración:",1,0),(1,"Comida:",2,0),(1,"Musica:",3,0),(1,"Transporte:",4,0),(2,1,1),(2,1,2),(3,1,2),(4,1,2)]
elementoss=[]
for elem in elementos:
    if elem[3]==1:
        label=tk.Label(ventana, text=elem[0])
        label.grid(row=elem[1], column=elem[2])
    else:
        entry=tk.Entry(ventana)
        entry.grid(row=elem[1], column=elem[2])
        elementoss.append(entry)
        

# titulo=tk.Label(ventana, text="Calcular costos de productos")
# titulo.grid(row=0, column=0, columnspan=2)
# texto_d=tk.Label(ventana, text="Decoración:")
# texto_d.grid(row=1, column=0)
# decoracion=tk.Entry(ventana)
# decoracion.grid(row=1, column=1)
# texto_c=tk.Label(ventana, text="Comida:")
# texto_c.grid(row=2, column=0)
# comida=tk.Entry(ventana)
# comida.grid(row=2, column=1)
# texto_m=tk.Label(ventana, text="Musica:")
# texto_m.grid(row=3, column=0)
# musica=tk.Entry(ventana)
# musica.grid(row=3, column=1)
# texto_t=tk.Label(ventana, text="Transporte:")
# texto_t.grid(row=4, column=0)
# transporte=tk.Entry(ventana)
# transporte.grid(row=4, column=1)
texto_r=tk.Label(ventana, text="Total:")
texto_r.grid(row=6, column=0)
def operacion():
    costos=[entry.get() for entry in elementoss]
    resultado=[]
    for a in costos:
        if a=="" or not a.isdigit():
            a=0
        resultado.append(float(a))
    fin=sum(resultado)
    texto_r.config(text=f"Total: ${fin}")
boton=tk.Button(ventana, text="Calcular", command=operacion)
boton.grid(row=5, column=0)
ventana.mainloop()