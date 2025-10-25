import tkinter as tk
ventana=tk.Tk()
ventana.title("Calcular costos")
elementos=[[],[(1,"Decoración:",1,0),(2,1,1),(1,"Comida:",2,0),(2,2,1),(1,"Musica:",3,0),(2,3,1),(1,"Transporte:",4,0),(2,4,1)]]
for elem in elementos[1]:
    if elem[0]==1: label=tk.Label(ventana, text=elem[1]).grid(row=elem[2], column=elem[3])
    else:
        entry=tk.Entry(ventana)
        entry.grid(row=elem[1], column=elem[2])
        elementos[0].append(entry)
texto_r=tk.Label(ventana, text="Total:")
texto_r.grid(row=6, column=0)
def operacion():
    costos=[[],[entri.get() for entri in elementos[0]]]
    for a in costos[1]: 
        if a=="" or not a.isdigit(): a=0
        costos[0].append(float(a))
    texto_r.config(text=f"Total: ${sum(costos[0])}")
boton=tk.Button(ventana, text="Calcular", command=operacion).grid(row=5, column=0)
ventana.mainloop()