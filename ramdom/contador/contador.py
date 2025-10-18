import tkinter as tk
from PIL import Image, ImageTk
import winsound
import time

ventana=tk.Tk()
ventana.geometry("200x50")

contador=0 

def click():
	global contador
	contador+=1
	texto.configure(text=f"Clicks: {contador}")
	if contador==13:
		ventana.destroy()
		ventana2=tk.Tk()
		ventana2.attributes('-fullscreen', True)
		ancho= ventana2.winfo_screenwidth()
		alto=ventana2.winfo_screenheight()
		cosa=Image.open("C:/Users/HP/Desktop/Provicional 2.0/Alejandro-Ducuara-Clases/ramdom/contador/datos/download.jpg")
		cosa2=Image.open("C:/Users/HP/Desktop/Provicional 2.0/Alejandro-Ducuara-Clases/ramdom/contador/datos/ng.png")
		cosa2=cosa2.resize((ancho,alto))
		cosa=cosa.resize((ancho,alto))
		mostrarcosa=ImageTk.PhotoImage(cosa)
		mostrarcosa2=ImageTk.PhotoImage(cosa2)

		estado={"estado":True, "activo":True}
		def a():
			if not estado["activo"]:
				ventana2.destroy()
				return

			if estado["estado"]==True:
				mostrar= tk.Label(ventana2, image=mostrarcosa)
				mostrar.place(x=0, y=0, width=ancho, height=alto)
			else:
				mostrar2=tk.Label(ventana2, image=mostrarcosa2)
				mostrar2.place(x=0, y=0, width=ancho, height=alto)

			estado["estado"]= not estado["estado"]

			ventana2.after(300, a)

		winsound.PlaySound("C:/Users/HP/Desktop/Provicional 2.0/Alejandro-Ducuara-Clases/ramdom/contador/datos/sonido.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
		time.sleep(0.5)
		a()
		ventana2.after(5000, lambda: estado.update({"activo":False}))
		ventana2.mainloop()
		
		

		
	
texto=tk.Label(ventana, text=f"Clicks: ")
texto.grid(row=3, column=2)
	
boton=tk.Button(ventana, text="presioname", command=click, background="chocolate1")
boton.grid(row=2, column=2, columnspan=2)



ventana.mainloop()

