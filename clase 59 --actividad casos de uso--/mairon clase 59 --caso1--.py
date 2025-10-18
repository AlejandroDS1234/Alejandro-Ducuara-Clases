import tkinter as tk
ventana=tk.Tk()
ventana.geometry("400x400")
ventana.title("Lista de productos")
producto=(("Arroz", "2400$", 50), ("Azucar", "2500$", 100), ("Sal", "1700$", 100), ("Aceite", "7200$", 25), ("Leche", "5500$", 70))
lista=tk.Listbox(ventana, width=50)
for item in producto:
    cosa=f"Producto: {item[0]} | Precio: {item[1]} | Cantidad Total: {item[2]}"
    lista.insert(tk.END, cosa)
def mostrar_productos():
    lista.grid(row=1, column=0, columnspan=4)
    boton.config(text="Ocultar productos", command=ocultar_productos)
def ocultar_productos():
    lista.grid_forget()
    boton.config(text="Mostrar lista de productos", command=mostrar_productos)
boton=tk.Button(ventana, text="Mostrar lista de productos", command=mostrar_productos)
boton.grid(row=0, column=0, sticky="nwes")
ventana.mainloop()