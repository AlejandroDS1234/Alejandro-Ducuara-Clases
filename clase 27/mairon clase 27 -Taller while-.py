print("Taller while\n")
#1

"""print("1) Suma hasta cero")
suma=[]
while True:
    try:
        anum=int(input("Ingrese un numero entero para sumar. Ingrese 0 para ver el resultado: "))
        suma.append(anum)
        if anum==0:
            print(f"El resultado de la suma es: {sum(suma)}\n")
            suma.clear()
            adesicion=input("Desea volver a iniciar?(si/no)").lower()
            if adesicion!="si":
                print("\nOk hasta luego\n\n")
                break
    except ValueError:
        print("Ese no es un numero, vuelva a intentar")

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
        print("\nContraseña correcta!!\n\n")
        bcontar=0
        break

#3
print("Lista de compras")
cproductos=[]
while True:
    cproducto=input("Ingrese un producto (Escriba 'fin' para terminar): ")
    cproductos.append(cproducto)
    if cproducto=="fin":
        cproductos.remove("fin")
        print(f"\nSus productos son:\n{cproductos}\n\n")
        cproductos.clear()
        cdesicion=input("Desea volver a iniciar?(si/no)").lower()
        if cdesicion!="si":
            print("Ok hasta luego\n\n")
            break

#4
print("Contador de pare e impares")
dcontador=0
dpares=[]
dimpares=[]
while True:
    while dcontador<10:
        try:
            dnum=int(input("Ingrese un numero entero: "))
            if dnum%2==0:
                dpares.append(dnum)
            else:
                dimpares.append(dnum)
            dcontador+=1
        except ValueError:
            print("Ese no es un numero entero, intente de nuevo")
    if dpares==0:
        print("No ingreso ningun numero par")
    else:
        print(f"Ingreso {len(dpares)} numero pares, y son:\n {dpares}")
    if dimpares==0:
        print("No ingreso ningun numero impar")
    else:
        print(f"Ingreso {len(dimpares)} numero impares, y son:\n {dimpares}")
    dpares.clear()
    dimpares.clear()
    dcontador=0
    ddesicion=input("Desea volver a iniciar?(si/no)").lower()
    if ddesicion!="si":
        print("Ok hasta luego\n\n")
        break

#5
print("5) Promedio de calificaciones")
enotas=[]
while True:

    enota=input("Ingrese una nota de 0 a 5 (Escriba 'salir' para salir): ").lower()
    enotas.append(enota)
    if enota=="salir":
        cannota=len(enotas)-1
        while cannota>=0:
            try:
                enotas[cannota]=float(enotas[cannota])
                cannota-=1
            except ValueError:
                enotas.remove(enotas[cannota])
                cannota-=1
        print(f"Su promedio de notas es: {(sum(enotas))/len(enotas)}")
        enotas.clear()
        edesicion=input("Desea volver a iniciar? (si/no): ").lower()
        if edesicion!="si":
            print("Ok hasta luego\n\n")
            break

#6
print("Tabla de multiplicar interactiva")
while True:
    try:
        fnum=int(input("Ingrese el numero entero para hacer su tabla de multiplicar: "))
        fcontador=1
        print(f"Tabla del {fnum}:")
        while fcontador<=10:
            fop=fnum*fcontador
            print(f"{fnum}*{fcontador}={fop}")
            fcontador+=1
        fdesicion=input("Desea volver a iniciar?(si/no): ").lower()
        if fdesicion!="si":
            print("Ok hasta luego\n\n")
            break   
    except ValueError:
        print("Ese no es un numero entero, intentelo de nuevo")
        
#7
print("7) Adivina el numero")
gnumsecret=37
while True:
    try:
        gnum=int(input("Adivine el numero entero: "))
        if gnum>gnumsecret:
            print("El numero es menor que ese")
        elif gnum<gnumsecret:
            print("El numero es mayor que ese")
        else:
            print("Felicidades!! encontro el numero")
            break
    except ValueError:
        print("Ese no es un numero entero, vuelva a intentar")

#8
print("8) Tupla de frutas")  
hfrutas=("mango","piña","kiwi","cereza","papaya")
while True:
    hfruta=input("Adivine una de las frutas: ").lower()
    if hfruta in hfrutas:
        print("Felicidades!! encontro una de las frutas")
        break
    else:
        print("Esa fruta no esta en la tupla")"""

#9
print("9) Diccionario de traduccion")
ipalabras={"hola":"hello","adios":"bye","gato":"cat","silla":"chair","camaleon":"chameleon"}
print(f"Palabras disponibles: \n{ipalabras.keys()}")
while True:
    try:
        ipalabra=input("Ingrese una palabra de las que estan para traducir: ")
        print(f"La traduccion de {ipalabra} es {ipalabras[ipalabra]}")
    except KeyError:
        print("Esa palabra no esta disponible para traduccion, intente otra")        
