print("MULTIPLICA O DIVIDE POTENCIAS")
numero1=int(input("escriba el primer numero: "))
potencia1=int(input("elevado a: "))
operacion=input("Dividido (d) o Multiplicado (m): ")
numero2=int(input("escriba el segundo numero: "))
potencia2=int(input("elevado a: "))
np=numero1**potencia1
np2=numero2**potencia2
if operacion=="m":
    M=np*np2
    print(f"la multiplicacion de {numero1}**{potencia1} por {numero2}**{potencia2} da como resultado: {M}")
elif operacion=="d":
    D=np/np2
    print(f"la divicion de {numero1}**{potencia1} entre {numero2}**{potencia2} da como resultado: {D}")
else:
    print("error")