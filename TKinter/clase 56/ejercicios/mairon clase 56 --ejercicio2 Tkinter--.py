import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x200")

valorr=tk.Label(ventana, text="Valor:")
valorr.grid(row=0, column=0)

valor=tk.Entry(ventana, text="0", width=50)
valor.grid(row=0, column=1, columnspan=3)


espacio=tk.Label(ventana, text=""   )
espacio.grid(row=1, column=0)

texto_=tk.Label(ventana)
texto_.grid(row=4, column=1, columnspan=3)

def escribir(cos, val, can):
    if cos == 1:
        tem = "Celsius"
        a="°F"
    else:
        tem = "Farenheit"
        a="°C"
    espacio2=tk.Label(ventana, text=""   )
    
    texto_.configure( text=" "   )
    texto_.configure( text=f"El valor en {tem} de {can}{a} es: {val}"  )
   
    
    
    
def farenheit(num):
    valo=valor.get()
    if valo == "": valo = 0
    farenheit= (float(valo) * 1.8) + 32
    escribir(2, farenheit, valo)

def celcius(num):
    valo=valor.get()
    if valo == "": valo = 0
    celcius= (float(valo) - 32)/1.8
    escribir(1, celcius, valo)

pre=tk.Label(ventana, text="La temperatura que ingreso esta en: ", )
pre.grid(row=2, column=0, columnspan=2)

faren=tk.Button(ventana, text="Farenheit", command=lambda: celcius(2))
faren.grid(row=2, column=2)

cel=tk.Button(ventana, text="Celsius", command=lambda: farenheit(1))
cel.grid(row=2, column=3)

ventana.mainloop()