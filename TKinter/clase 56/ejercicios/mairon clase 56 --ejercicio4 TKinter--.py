import tkinter as tk
ventana=tk.Tk()
ventana.geometry("200x50")

contador=0 

def click():
	global contador
	contador+=1
	texto.configure(text=f"Clicks: {contador}")
	
texto=tk.Label(ventana, text=f"Clicks: ")
texto.grid(row=3, column=2)
	
boton=tk.Button(ventana, text="presioname", command=click, background="chocolate1")
boton.grid(row=2, column=2, columnspan=2)

ventana.mainloop()
