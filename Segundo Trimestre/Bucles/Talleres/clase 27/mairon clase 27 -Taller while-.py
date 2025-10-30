print("Taller while\n")

#1
print("1) Suma hasta cero")
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
print("3) Lista de compras")
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
            print("\nOk hasta luego\n\n")
            break

#4
print("4) Contador de pares e impares")
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
        print("\nOk hasta luego\n\n")
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
        if len(enotas)!=0:
            print(f"Su promedio de notas es: {(sum(enotas))/len(enotas)}")
            enotas.clear()
            edesicion=input("Desea volver a iniciar? (si/no): ").lower()
            if edesicion!="si":
                print("\nOk hasta luego\n\n")
                break
        else:
            print("no ha ingresado ninguna nota")
            edesicion=input("Desea volver a iniciar? (si/no): ").lower()
            if edesicion!="si":
                print("\nOk hasta luego\n\n")
                break

#6
print("6) Tabla de multiplicar interactiva")
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
            print("\nOk hasta luego\n\n")
            break   
    except ValueError:
        print("Ese no es un numero entero, intentelo de nuevo")
        
#7
print("7) Adivina el numero")
gnumsecret= 37
while True:
    try:
        gnum=int(input("Adivine el numero entero: "))
        if gnum>gnumsecret:
            print("El numero es menor que ese")
        elif gnum<gnumsecret:
            print("El numero es mayor que ese")
        else:
            print("\nFelicidades!! encontró el número\n\n")
            break
    except ValueError:
        print("Ese no es un numero entero, vuelva a intentar")

#8
print("8) Tupla de frutas")  
hfrutas=("mango","piña","kiwi","cereza","papaya")
while True:
    hfruta=input("Adivine una de las frutas: ").lower()
    if hfruta in hfrutas:
        print("\nFelicidades!! encontro una de las frutas\n\n")
        break
    else:
        print("Esa fruta no esta en la tupla")

#9
print("9) Diccionario de traduccion")
ipalabras={"hola":"hello","adios":"bye","gato":"cat","silla":"chair","camaleon":"chameleon"}
print(f"Palabras disponibles: \n{ipalabras.keys()}")
while True:
    try:
        ipalabra=input("Ingrese una palabra de las que estan para traducir: ")
        print(f"La traduccion de {ipalabra} es {ipalabras[ipalabra]}")
        idesicion=input("Desea intentar otra palabra? (si/no): ")
        if idesicion!="si":
            print("\nOk hasta luego\n\n")
            break
    except KeyError:
        print("Esa palabra no esta disponible para traduccion, intente otra")
        
#10
print("10) Calculadora basica")
while True:
    print("\nOperaciones disponibles:\nSuma=1\nResta=2\nMultiplicacion=3\nDivision=4\nSalir=5")
    try:
        iopelg=int(input("ingrese el numero de la operacion que desea realizar: "))
        try:
            if iopelg==1:
                icoun=0
                while icoun==0:
                    try:
                        iopnum1=float(input("Ingrese el numero para sumar:"))
                        iopnum2=float(input("Ingrese el segundo numero para sumar:"))
                        iop=iopnum1+iopnum2
                        print(f"El resultado de {iopnum1}+{iopnum2} es {iop}")
                        icoun=1
                    except ValueError:
                        print("Ese no es un numero, intentelo de nuevo")
            elif iopelg==2:
                icoun=0
                while icoun==0:
                    try:
                        iopnum1=float(input("Ingrese el numero para restar:"))
                        iopnum2=float(input("Ingrese el segundo numero para restar:"))
                        iop=iopnum1-iopnum2
                        print(f"El resultado de {iopnum1}-{iopnum2} es {iop}")
                        icoun=1
                    except ValueError:
                        print("Ese no es un numero, intentelo de nuevo")
            elif iopelg==3:
                icoun=0
                while icoun==0:
                    try:
                        iopnum1=float(input("Ingrese el numero para multiplicar:"))
                        iopnum2=float(input("Ingrese el segundo numero para multiplicar:"))
                        iop=iopnum1*iopnum2
                        print(f"El resultado de {iopnum1}*{iopnum2} es {iop}")
                        icoun=1
                    except ValueError:
                        print("Ese no es un numero, intentelo de nuevo")
            elif iopelg==4:
                icoun=0
                while icoun==0:
                    try:
                        iopnum1=float(input("Ingrese el numero para dividir:"))
                        iopnum2=float(input("Ingrese el segundo numero para dividir:"))
                        iop=round(iopnum1/iopnum2,3)
                        print(f"El resultado de {iopnum1}/{iopnum2} es {iop} aprox")
                        icoun=1
                    except ValueError:
                        print("Ese no es un numero, intentelo de nuevo")
            elif iopelg==5:
                print("\nOk hasta luego\n\n")
                break
            else:
                print("Operacion no disponible")
            idesicion=input("Desea hacer otra operacion? (si/no)").lower()
            if idesicion!="si":
                print("\nOk hasta luego\n\n")
                break
        except ValueError:
            print("Ese no es un numero, intente de nuevo")
    except ValueError:
        print("opcion no disponible")

#11
print("11) Registro de edades")
while True:
    kdatos={}
    kcontador=1
    while True:
        kdatos[f"nombre{kcontador}"]=input(f"Ingrese el nombre {kcontador} (Escriba 'salir' para no ingresar mas): ")
        if kdatos[f"nombre{kcontador}"]=="salir":
            del(kdatos[f"nombre{kcontador}"])
            print(f"Estos son los nombres y edades ingresados:\n{kdatos}")
            kdesicion=input("Desea volver a ingresar datos?(si/no): ").lower()
            kdatos.clear()
            if kdesicion!="si":
                print("\nOk hasta luego\n\n")
                kstop=1
                break
            else:
                break
        kcoun=0
        while kcoun==0:
            try:
                kdatos[f"edad{kcontador}"]=int(input(f"Ingrese la edad {kcontador}: "))
                kcoun=1
            except ValueError:
                print("Edad no valida, vuelva a intantar")
        print("\n")
        kcontador+=1
    try:
        if kstop==1:
            break
    except NameError:
        print(end="")

#12
print("12) Buscar en lista")  
lcolores=["azul","rojo","verde","amarillo","rosado"]
while True:
    lcolor=input("Adivine uno de los colores: ").lower()
    if lcolor in lcolores:
        print("Felicidades!! encontro uno de los colores\n\n")
        break
    else:
        print("Ese color no esta en la lista")

#13
print("13) Potencias de un numero")
while True:
    mcontador=0
    while mcontador!=1:
        try:
            mnum=int(input("Ingrese un numero para mostrar sus potencias: "))
            mcontador=1
        except ValueError:
            print("Ese no es un numero, intentelo de nuevo")
    while mcontador<=5:
        mop=mnum**mcontador
        print(f"el resultado de: {mnum}**{mcontador} es: {mop}")
        mcontador+=1
    mdesicion=input("Desea saber las potencias de otro numero?(si/no): ").lower()
    if mdesicion!="si":
        print("\nOk hasta luego\n\n")
        break

#14
print("14) Lista de cuadrados")
ncontador=1
nnumeros=[]
while True:
    while ncontador<=5:
        try:
            nnum=int(input(f"Ingrese el #{ncontador} numero entero para saber su cuadrado: "))
            nop=nnum**2
            nnumeros.append(nop)
            ncontador+=1
        except ValueError:
            print("Ese no es un numero, intentelo de nuevo")
    print(f"El cuadrado de los numero que ingreso son:\n{nnumeros}\n")
    ndesicion=input("Desea saber e cuadrado de otros numeros?(si/no): ").lower()
    if ndesicion!="si":
        print("\nOk hasta luego\n\n")
        break
    nnumeros.clear()
    ncontador=1

#15
print("15) Diccionario de estudiantes")
while True:
    odatos={}
    ocontador=1
    while True:
        odatos[f"nombre{ocontador}"]=input(f"Ingrese el nombre {ocontador} (Escriba 'fin' para no ingresar mas): ")
        if odatos[f"nombre{ocontador}"]=="fin":
            del(odatos[f"nombre{ocontador}"])
            print(f"Estos son los nombres y edades ingresados:\n{odatos}")
            odesicion=input("Desea volver a ingresar datos?(si/no): ").lower()
            odatos.clear()
            if odesicion!="si":
                print("\nOk hasta luego\n\n")
                ostop=1
                break
            else:
                break
        ocoun=0
        while ocoun==0:
            try:
                odatos[f"nota{ocontador}"]=float(input(f"Ingrese la nota final {ocontador}: "))
                ocoun=1
            except ValueError:
                print("Edad no valida, vuelva a intantar")
        print("\n")
        ocontador+=1
    try:
        if ostop==1:
            break
    except NameError:
        print(end="")

#fin
print("Programa finalizado")
#taller
#terminado
#completo
#el mañana de hoy
#Completo 200%