import tkinter as tk
ventana=tk.Tk()
ventana.geometry("165x257")
ventana.config(background="gray32")
calculadora=tk.Frame(ventana, background="gray32")
calculadora.grid(row=0, column=0, pady=5)
teclado=tk.Frame(calculadora, background="gray32")
teclado.grid(row=2, column=0, padx=3, pady=10)
operacion=tk.Label(calculadora, text="", background="SteelBlue1", width=20, height=-2 ,anchor="e", highlightthickness=5, highlightcolor="dark slate gray", highlightbackground="dark slate gray")
operacion.grid(row=0, column=0, columnspan=4, sticky="s")


estado={"resul":False}


botones=[
    ('7', 3, 2), ('8', 3, 1), ('9', 3, 0), ('/', 2, 3),
    ('4', 4, 2), ('5', 4, 1), ('6', 4, 0), ('*', 2, 2),
    ('1', 5, 2), ('2', 5, 1), ('3', 5, 0), ('-', 2, 1),
    ('0', 6, 1), ('.', 6, 0), ('+', 2, 0)]

for boton in botones:
    tk.Button(teclado, text=boton[0], width=4, height=2,background="gray64",command=lambda num=boton[0]: escribir(num)).grid(row=boton[1], column=boton[2], padx=1)

def escribir (num):
    global resul
    
    if estado["resul"] and  (True!=(eval(operacion["text"])==int or eval(operacion["text"])==float)):
        borrarall()
        
    if operacion["text"] !="":
        if operacion["text"][len(operacion["text"])-1] in "+-*/.":
            if num.isdigit():
                operacion["text"]+=str(num)
        else:
            operacion["text"]+=str(num)
    else:
        if num.isdigit():
            operacion["text"]+=str(num)
    
    estado["resul"]=False
    
    
            
def borrar():
    operacion["text"]=operacion["text"][0:-1]    

def igual():
    if operacion["text"].strip() !="":
        try:
            if operacion["text"][-1] in "+-*/.":
                operacion["text"]=operacion["text"][0:-1]
                operacion["text"]=str(eval(operacion["text"]))
            else:
                operacion["text"]=str(eval(operacion["text"]))
        except:
            operacion["text"]="Error"
        estado["resul"]=True

def borrarall():
    operacion["text"]=""
            
            
botonigual=tk.Button(teclado, text="=", width=4, height=2,background="gray64", command=igual)
botonigual.grid(row=6, column=2)
botonmen=tk.Button(teclado, text="<--", width=4, height=2,background="gray64" ,command=borrar)
botonmen.grid(row=4, column=3)
botonmen=tk.Button(teclado, text="AC", width=4, height=2,background="gray64" ,command=borrarall)
botonmen.grid(row=3, column=3)
ventana.mainloop()
