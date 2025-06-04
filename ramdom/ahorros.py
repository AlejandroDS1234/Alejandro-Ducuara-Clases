#ingresar una cantidad
#poderretirar la cantidad
us="AlejandroDS"
cnt=246810
dinero=0
while True:
    print("SISTEMA DE AHORROS")
    usuario=input("ingrese su usuario: ")
    contraseña=int(input("Ingrese su contraseña numerica:"))
    while usuario==us and contraseña==cnt:
        print(f"Saldo: {dinero}")
        pregunta=input("¿Ahorrar o retirar?: ").lower()
        if pregunta=="ahorrar":
            cantidad=float(input("Ingrese la cantidad que va a ahorrar: "))
            op=dinero+cantidad
            dinero=op
            print(f"La cantidad da dinero actual es de: {dinero}")
            break
        elif pregunta=="retirar":
            menoscantidad=float(input("Ingrese la cantidad a retirar: "))
            if menoscantidad>dinero:
                print("Fondos Insuficientes")
                break
            else:
                menosop=dinero-menoscantidad
                dinero=menosop
                print(f"Cantidad de dinero retirada: {menoscantidad} Cantidad actual de dinero ahorrado: {dinero}")
                break
        else:
            print("comando no atmitido")
    else:
        print("usuario o contraseña incorrectos, vuelva a intentar")

