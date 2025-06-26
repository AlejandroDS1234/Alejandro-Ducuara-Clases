print("Taller while\n")
#1
"""print("1) Suma hasta cero")
suma=[]
while True:
    try:
        anum=int(input("Ingrese un numero entero para sumar. Ingrese 0 para ver el resultado: "))
        suma.append(anum)
        if anum==0:
            print(f"El resultado de la suma es: {sum(suma)}")
            suma.clear()
            break
    except ValueError:
        print("Ese no es un numero, vuelva a intentar")"""

#2
print("2) Contraseña secreta")
bcontraseña="python123"
bcontar=0
while True:
    ingcontra=input("Ingrese la contraseña: ")
    bcontar+=1
    if bcontar==3:
        print("Pista: Un lenguaje de programacion de alto nivel y los tres primeros numeros enteros positivos")
        bcontar=0
    if ingcontra==bcontraseña:
        print("Contraseña correcta!!")
        bcontar=0
        break
    