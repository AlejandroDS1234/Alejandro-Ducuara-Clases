#Taller condicionales
#Operaciones matematicas
#1
print("1) Numero positivo negativo o cero")
anum=int(input("Ingrese un numero: "))
if anum>0:
    print(f"El numero {anum} es positivo\n")
elif anum<0:
    print(f"El numero {anum} es negativo\n")
else:
    print("Su numero es 0\n")

#2
print("2) Calcular el mayor")
bnum1=int(input("Ingrese el primer numero: "))
bnum2=int(input("Ingrese un segundo numero: "))
if bnum1>bnum2:
    print(f"El numero {bnum1} es el mayor\n")
elif bnum1<bnum2:
    print(f"El numero {bnum2} es el mayor\n")
else:
    print("Los numeros son iguales\n")

#3
print("3) Par o Impar")
cnum=int(input("Ingrese un numero: "))
if cnum/2==cnum//2+0.00:
    print(f"El numero {cnum} es par\n")
else:
    print(f"El numero {cnum} es impar\n")
        
#4
print("4) El numero esta entre 10 y 20?")
dnum=int(input("Ingrese un numero: "))
if dnum>10 and dnum<20:
    print(f"El numero {dnum} esta entre 10 y 20\n")
else:
    print(f"El numero {dnum} no esta en el rango de 10 y 20\n")

#5
print("5) Encontrar el numero mayor")
enum1=int(input("Ingrese el primer numero: "))
enum2=int(input("Ingrese el segundo numero: "))
enum3=int(input("Ingrese el tercero numero: "))
if enum1>enum2 and enum1>enum3:
    print(f"El numero mayor es: {enum1}\n")
elif enum2>enum1 and enum2>enum3:
    print(f"El numero mayor es: {enum2}\n")
elif enum3>enum1 and enum3>enum2:
    print(f"El numero mayor es: {enum3}\n")
else:
    print(f"Los numeros nos iguales\n")

#6
print("6) precio final")
fnum=float(input("Ingrese el precio final: "))
if fnum>100:
    fop=fnum-((fnum*10)/100)
    print(f"Se le aplico un descuento del 10% por superar los 100$, su total es de: {fop}\n")
else:
    print(f"El precio a pagar es {fnum}\n")

#7
print("7) votar")
gedad=int(input("Ingrese su edad: "))
if gedad>=18:
    print("Usted puede votar\n")
else:
    print("Usted no puede votar\n")     

#8
print("8) descuento VIP")
htipo=input("Ingrese el tipo de cliente (VIP o normal): ").lower()
hprecio=float(input("Ingrese el precio a pagar: "))
if htipo=="vip":
    hop=hprecio-((hprecio*20)/100)
    print(f"Se le aplico un descuento del 20% por ser cliente VIP, total a pagar: {hop}\n")
else:
    print(f"total a pagar {hprecio}\n")
    
#9
print("9) Multiplo de 5 y 3")
inum=int(input("Ingrese un numero: "))
if inum/5==inum//5+0.0 and inum/3==inum//3+0.0:
    print(f"El numero {inum} es multiplo de 3 y 5\n")
else:
    print("El numero no es multiplo de 3 y 5\n")

#10
print("10) Numero divisible entre 2 numeros dados")
jnum1=int(input("Ingrese un numero: "))
jnum2=int(input("Ingrese el primer divisor: "))
jnum3=int(input("Ingrese el segundo divisaor: "))
if jnum1/jnum2==jnum1//jnum2+0.0 and jnum1/jnum3==jnum1//jnum3+0.0:
    print(f"El numero {jnum1} es divisible entre {jnum2} y {jnum3}\n")
else:
    print(f"El numero {jnum1} no es divisible entre {jnum2} y {jnum3}\n")

#11
print("11) tercero mayor que 10")
knum=[int(input("ingresa un primer numero: ")),int(input("ingresa un segundo numero: ")),int(input("ingresa un tercer numero: ")),int(input("ingresa un cuarto numero: ")),int(input("ingresa un quinto numero: "))]
print(f"Lista: {knum}")
if knum[2]>10:
    print(f"{knum[2]} es mayor que 10\n")
else:
    print("El tercer elemento no es mayor que 10\n")
    
#12
print("12) 7 esta en la lista?")
lnum=[3,5,7,9]
print(lnum)
if lnum.count(7)==0:
    print("No esta en la lista\n")
else:
    print("Esta en la lista\n")

#13
print("13) sumar los dos primeros elementos de la lista")
mnum=[4,6,2,8]
mop=mnum[0]+mnum[1]
print(mnum)
if mop>10:
    print("Suma alta\n")
else:
    print("Suma baja\n")
    
#14
print("14) Ultimo nombre")
nname=["Ana","Luis","Pedro","Marta"]
print(nname)
print(f"El ultimo nombre es: {nname[-1]}")
if nname[-1]=="Marta":
    print("Nombre correcto\n")
else:
    print("Nombre diferente\n")

#15
print("15) cambiar color azul")
ocolor=[input("Ingresa un color: ").lower(),input("Ingresa un segundo color: ").lower(),input("Ingresa un tercer color: ").lower()]
print(ocolor)
if ocolor[1]=="azul":
    ocolor[1]=input("Cambia el color: ")
    print(f"Lista actualizada: {ocolor}\n")
else:
    print("Esta es la lista\n")
    
#16
print("16) orden segun el mayor")
pnum=(5,8,12,20)
if pnum[0]<pnum[-1]:
    print(f"Tupla ordenada ascendente: {sorted(pnum)}\n")
else:
    print(f"Tupla orden descendente: {sorted(pnum, reverse=True)}\n")

#17
print("17) El segundo valor mayor a 30")
qnum=(25, 32, 28)
if qnum[1]>30:
    print("Edad mayor a 30\n")
else:
    print("Edad menor o igual a 30\n")

#18
print("18) convertir tuplas y listas")
rnum=(1,2,3)
rlis=list(rnum)
if rlis[1]==2:
    rlis[1]=9
rtupla=tuple(rlis)
print(rtupla,"\n")

#19
print("19) coordenadas")
snum=(4, 9)
print(snum)
if snum[1]>5:
    print("Coordenada alta\n")
else:
    print("Coordenada baja\n")

#20
print("20) Tuplas iguales")
tnum1=(3,4)
tnum2=(3,5)
print(tnum1,"\n",tnum2)
if tnum1==tnum2:
    print("Tuplas iguales\n")
else:
    print("Tuplas diferentes\n")

#21
print("21) Mayor o menor de edad")
unum={"nombre":"Juan","edad":17}
if unum["edad"]>=18:
    print("Adulto\n")
else:
    print("Menor de edad\n")

#22
print("22) Cambiar edad")
vnum={"nombre":"Lucia","edad":20}
if vnum["edad"]>18:
    vnum["edad"]=21
print(vnum,"\n")

#23
print("23) agregar ciudad")
wnum={"nombre":"Carlos"}
if wnum.get("ciudad")==None:
    wnum["ciudad"]="Bogota"
print(f"{wnum}\n")

#24
print("24) mirar si precio existe")
xnum={"producto":"pan","precio":1200}
if xnum.get("precio")!=None:
    print(f"precio: {xnum["precio"]}\n")
else:
    print("No hay precio\n")

#25
print("25) precio de pan")
ynum={"pan":1200,"leche":2000}
if ynum.get("pan")!=None:
    print(f"pan: {ynum['pan']}\n")
else:
    print("Producto no disponible")
#taller
#Terminado
#FIn