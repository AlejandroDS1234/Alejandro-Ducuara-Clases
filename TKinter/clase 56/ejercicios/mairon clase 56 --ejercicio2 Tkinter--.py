import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x200")

valor=tk.Button(ventana, text="Valor:")
valor.grid(row=100, column=5)

ventana.mainloop()