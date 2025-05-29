#INPUT
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

#codigo actividades potenciacion #clase 3
#1) 4**6/4**3
bc=4
ex1=6
ex2=3
ps1=bc**ex1
ps2=bc**ex2
rs=ps1/ps2
print(f"El resultado de {ps1}*{ps2} es {rs}")

#2) 12**4/12**2
abc=12
aex1=4
aex2=2
aps1=abc**aex1
aps2=abc**aex2
ars=aps1/aps2
print(f"El resultado de {aps1}/{aps2} es {ars}")

#3) 5**5*5**2
bbc=5
bex=2
bps1=bbc**bbc
bps2=bbc**bex
brs=bps1*bps2
print(f"El resultado de {bps1}*{bps2} es {brs}")

#4) 10**1*10**3
cbc=10
cex1=1
cex2=3
cps1=cbc**cex1
cps2=cbc**cex2
crs=cps1*cps2
print(f"El resultado de {cps1}*{cps2} es {crs}")
    
#Indexacion de cadenas de caracteres -- Extraccion
letra="python"
print(letra[3])