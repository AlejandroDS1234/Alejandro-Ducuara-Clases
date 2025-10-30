#Datos guardados en el sistema
cnt=246810
dinero=1000000

#cajero
print("\n\n|---|Cajero|---|\n\n")
while True:
    contar1=1
    while contar1==1:
        try:
            contraseña=int(input("Ingrese su contraseña numerica:"))
            contar1=0
        except ValueError:
            print("\n!!!Debe ser una contraseña numerica, intentelo de nuevo!!!\n")
    while contraseña==cnt:
        print(f"\n\n---Saldo: {dinero}---\n\n")
        coun=1
        while coun==1:
            try:
                retirar=float(input("Ingrese la cantidad a retirar: "))
                if retirar<0:
                	print("\n!!!La cantidad a retirar debe ser positiva, intente de nuevo!!!\n")
                else:
                	coun=0
            except ValueError:
            	print("\n!!!Ingrese una cantidad valida!!!\n")
        if retirar>dinero:
            print("\n---Fondos Insuficientes---\n")
            contar2=1
            while contar2==1:
                try:
                    salir=int(input("\n\nIngrese 1 para retirar otra cantidad o 0 para salir: "))

                    if salir==0:
                        print("\n---Hasta luego---\n")
                        print("---------------------")
                        contar3=0
                        contar2=0
                        print("\n\n|---|Cajero|---|\n\n")
                    elif salir==1:
                        contar2=0
                        continue
                    elif salir!=0 or salir!=1:
                        print("\n!!!Debe ingresar 0 o 1, vuelva a intentar!!!\n")
                except ValueError:
                    print("\n!!!Ese no es un digito valido, vuelva a intentar!!!\n")
        else:
            dinero-=retirar
            print(f"\n---Cantidad de dinero retirada: {retirar}---\n---Cantidad actual de dinero ahorrado: {dinero}---\n")
            contar2=1
            while contar2==1:
                try:
                    salir=int(input("\n\nIngrese 1 para retirar otra cantidad o 0 para salir: "))
                    if salir==0:
                        print("\n---Hasta luego---\n")
                        print("---------------------")
                        contar3=0
                        contar2=0
                        print("\n\n|---|Cajero|---|\n\n")
                    elif salir==1:
                        contar2=0
                        continue
                    elif salir!=0 or salir!=1:
                        print("\n!!!Debe ingresar 0 o 1, vuelva a intentar!!!\n")
                except ValueError:
                    print("\n!!!ese no es un digito valido!!!\n")
        try:
            if contar3==0:
                contar3=1
                break
                
        except NameError:
            print("\n")
    else:
        print("\n!!!contraseña incorrecta, vuelva a intentar!!!\n")