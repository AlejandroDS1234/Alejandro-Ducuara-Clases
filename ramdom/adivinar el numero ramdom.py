import random
while True:
    num=random.choice(range(-100,100))
    contador=0
    while True:
        n=1
        while n==1:
            try:
                num1=int(input("Adivine el numero: "))
                contador+=1
                n=0
            except ValueError:
                print("Ese no es un numero, intente de nuevo")
        if num1>num:
            print("El numero es menor que ese")
        elif num1<num:
            print("El numero es mayor que ese")
        else:
            print("\nFelicitaciones, ese es el numero\n")
            print(f"En {contador} intentos")
            desicion=input("Desea intentarlo otra vez?(si/no): ").lower()
            if desicion!="si":
                print("Programa finalizado")
                a=0
                break
            else:
                break
    try:
        if a==0:
            break
    except NameError:
        print("\n\n")