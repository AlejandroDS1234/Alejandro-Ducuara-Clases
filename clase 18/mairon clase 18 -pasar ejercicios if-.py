#1
#aprobar credito bancario
print("Solicitar Credito Bancario")
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese la edad: "))
if edad>=18:
    print(f"Continue {nombre}")
    credito=float(input("Ingrese la cantidad de credito solicitada: "))
    salario=float(input("Ingrese su salario mensual: "))
    if salario*6<credito:
        print("Credito denegado, no puede pagar\n\n")
    else:
        print(f"Felicidades {nombre} su credito ha sido aprobado\n\n")
else:
    print("No puedes continuar, eres menor de edad\n\n")

#2
#precio de entrada a un local
print("Precio de entrada")
Edad=int(input("Ingrese su edad: "))
if Edad<4:
    print("Entra gratis\n\n")
elif Edad<=18:
    print("Paga 5 euros\n\n")
elif Edad>18:
    print("Paga 18 euros\n\n")
else:
    print("Edad mal ingresada\n\n")
    
#3
#Calculadora
print("Calculadora")
print("Operaciones:\nSuma(s)\nResta(r)\nMultiplicacion(m)\nDivision(d)")
op=input("Ingrese la letra de la operacion que va a realizar: ").lower()
if op=="s":
    sumnum1=float(input("Ingrese el primer numero para sumar: "))
    sumnum2=float(input("Ingrese el segundo numero para sumar: "))
    sum=sumnum1+sumnum2
    print(f"El resultado de la suma: {sumnum1}+{sumnum2} es {sum}\n\n")
elif op=="r":
    resnum1=float(input("Ingrese el primer numero para restar: "))
    resnum2=float(input("Ingrese el segundo numero para restar: "))
    res=resnum1-resnum2
    print(f"El resultado de la resta: {resnum1}-{resnum2} es {res}\n\n")
elif op=="m":
    mulnum1=float(input("Ingrese el primer numero para multiplicar: "))
    mulnum2=float(input("Ingrese el segundo numero para multiplicar: "))
    mul=mulnum1*mulnum2
    print(f"El resultado de la multiplicacion: {mulnum1}*{mulnum2} es {mul}\n\n")
elif op=="d":
    divinum1=float(input("Ingrese el primer numero para dividir: "))
    divinum2=float(input("Ingrese el segundo numero para dividir: "))
    divi=divinum1/divinum2
    print(f"El resultado de la division: {divinum1}/{divinum2} es {divi}\n\n")
else:
    print("Operacion mal escrita o invalida\n\n")