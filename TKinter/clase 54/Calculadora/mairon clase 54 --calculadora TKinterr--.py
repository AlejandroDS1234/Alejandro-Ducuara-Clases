import tkinter as tk
ventana=tk.Tk()
operacion=tk.Label(ventana, text="", background="blue", width=20, justify="right")
operacion.grid(row=0, column=0, columnspan=4)
espacio=tk.Label(ventana, text="",)
espacio.grid(row=1, column=0, columnspan=4)
resul=False

botones=[
    ('7', 2, 2), ('8', 2, 1), ('9', 2, 0), ('/', 2, 3),
    ('4', 3, 2), ('5', 3, 1), ('6', 3, 0), ('*', 3, 3),
    ('1', 4, 2), ('2', 4, 1), ('3', 4, 0), ('-', 4, 3),
    ('0', 5, 1), ('.', 5, 2), ('+', 5, 0)]

for boton in botones:
    tk.Button(ventana, text=boton[0], width=5, height=2, command=lambda num=boton[0]: escribir(num)).grid(row=boton[1], column=boton[2])

def escribir (num):
    if resul and not operacion["text"].strip().isdigit():
        operacion["text"]=""
  
   
        
    if operacion["text"].strip() !="":
        if operacion["text"][len(operacion["text"])-1] in "+-*/.":
            if num.isdigit():
                operacion["text"]+=str(num)
        else:
            operacion["text"]+=str(num)
    else:
        if num.isdigit():
            operacion["text"]+=str(num)
            
def borrar():
    operacion["text"]=operacion["text"][0:-1]    

def igual():
    if operacion["text"].strip() !="":
        if operacion["text"][-1] in "+-*/.":
            operacion["text"]=operacion["text"][0:-1]
            operacion["text"]=str(eval(operacion["text"]))
        else:
            operacion["text"]=str(eval(operacion["text"]))
        resul=True
            
            
botonigual=tk.Button(ventana, text="=", width=5, height=2, command=igual)
botonigual.grid(row=5, column=3)
botonmen=tk.Button(ventana, text="<--", width=5, height=2, command=borrar)
botonmen.grid(row=5, column=0)
ventana.mainloop()
