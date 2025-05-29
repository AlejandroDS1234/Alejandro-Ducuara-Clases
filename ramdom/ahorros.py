#ingresar una cantidad
#poderretirar la cantidad
us="AlejandroDS"
cnt=246810
dinero=[0]
while True:
    print("SISTEMA DE AHORROS")
    usuario=input("ingrese su usuario: ")
    contraseña=int(input("Ingrese su contraseña numerica:"))
    while usuario==us and contraseña==cnt:
        pregunta=input("¿Ahorrar o retirar?: ")
        if pregunta=="ahorrar":
            cantidad=float(input("Ingrese la cantidad que va a ahorrar: "))
            op=dinero[0]+cantidad
            dinero[0]=op
            print(f"La cantidad da dinero actual es de: {dinero}")
            break
        if pregunta=="retirar":
            menoscantidad=float(input("Ingrese la cantidad a retirar: "))
            if menoscantidad>dinero[0]:
                print("Fondos Insuficientes")
                break
            else:
                menosop=dinero[0]-menoscantidad
                dinero[0]=menosop
                print(f"Cantidad de dinero retirada: {menoscantidad} Cantidad actual de dinero ahorrado: {dinero}")
                break
        else:
            print("comando no atmitido")
    else:
        print("usuario o contraseña incorrectos, vuelva a intentar")

