#ingresar una cantidad
#poderretirar la cantidad
cnt=246810
dinero=200
while True:
    print("Cajero")
    contar1=1
    while contar1==1:
        try:
            contraseña=int(input("Ingrese su contraseña numerica:"))
            contar1=0
        except ValueError:
            print("Debe ser una contraseña numerica, intentelo de nuevo")
    while contraseña==cnt:
        print(f"Saldo: {dinero}")
        retirar=float(input("Ingrese la cantidad a retirar: "))
        if retirar>dinero:
            print("Fondos Insuficientes")
            contar2=1
            while contar2==1:
                try:
                    salir=int(input("Ingrese 1 para retirar otra cantidad o 0 para salir: "))
                    if salir==0:
                        print("Hasta luego\n\n")
                        contar3=0
                    elif salir==1:
                        contar2=0
                        continue
                    elif salir!=0 or salir!=1:
                        print("Debe ingresar 0 o 1, vuelva a intentar")
                except ValueError:
                    print("Ese no es un digito valido")
        else:
            menosop=dinero-retirar
            dinero=menosop
            print(f"Cantidad de dinero retirada: {retirar} Cantidad actual de dinero ahorrado: {dinero}")
            break
        try:
            if contar3==0:
                break
        except ValueError:
            print("\n")
    else:
        print("contraseña incorrecta, vuelva a intentar")