#TALLER 1
print("TALLER 1")
print("Ingrese la siguiente informacion:")
nmpt=input("Ingrese el nombre del producto: ")
prcpt=float(input("Ingrese el precio por unidad: "))
cdpt=int(input("Ingrese la cantidad comprada: "))
tupla=(nmpt,prcpt)
lista=[tupla,cdpt]
diccionario={"producto":lista}
op=cdpt*prcpt
print(f"El nombre, el precio y la cantidad comprada son: {diccionario}")
print(f"El costo total de la compra del producto es de: {op}")
#TALLER 2
print("TALLER 2\nFactura\nProducto 1:")
pd1nm=input("Ingrese el nombre del primer producto: ")
pd1pu=float(input("Ingrese el precio del producto: "))
pd1cd=int(input("Ingrese la cantidad del producto comprada: "))
print("Producto 2:")
pd2nm=input("Ingrese el nombre del segundo producto: ")
pd2pu=float(input("Ingrese el precio del producto: "))
pd2cd=int(input("Ingrese la cantidad del producto comprada: "))
print("Producto 3:")
pd3nm=input("Ingrese el nombre del tercer producto: ")
pd3pu=float(input("Ingrese el precio del producto: "))
pd3cd=int(input("Ingrese la cantidad del producto comprada: "))
tuplapd1=(pd1nm,pd1pu)
tuplapd2=(pd2nm,pd2pu)
tuplapd3=(pd3nm,pd3pu)
listapd1=[tuplapd1,pd1cd]
listapd2=[tuplapd2,pd2cd]
listapd3=[tuplapd3,pd3cd]
dcc={"producto1":listapd1,"producto2":listapd2,"producto3":listapd3}
ptpd1=pd1pu*pd1cd
ptpd2=pd2pu*pd2cd
ptpd3=pd3pu*pd3cd
pt=ptpd1+ptpd2+ptpd3
print("FACTURA")
print(f"Producto, cantidad y precio 1: {dcc["producto1"]}")
print(f"Total: {ptpd1}")
print(f"Producto, cantidad y precio 2: {dcc["producto2"]}")
print(f"Total: {ptpd2}")
print(f"Producto, cantidad y precio 3: {dcc["producto3"]}")
print(f"Total: {ptpd3}")
print(f"Total a pagar: {pt}")
#TALLER 3
print("TALLER 3\nRegistro de notas\nIngrese los siguientes datos:")
t3nm=input("Ingrese el nombre de un estudiante: ")
print("Ingrese las asignatura que cursa: ")
t3as1=input("Asignatura 1: ")
t3as2=input("Asignatura 2: ")
t3as3=input("Asignatura 3: ")
print(f"Ingrese las notas de {t3as1}")
t31nt1=float(input("Ingrese la primera nota: "))
t31nt2=float(input("Ingrese la segunda nota: "))
print(f"Ingrese las notas de {t3as2}")
t32nt1=float(input("Ingrese la primera nota: "))
t32nt2=float(input("Ingrese la segunda nota: "))
print(f"Ingrese las notas de {t3as3}")
t33nt1=float(input("Ingrese la primera nota: "))
t33nt2=float(input("Ingrese la segunda nota: "))
t3tupla1=(t3as1,(t31nt1+t31nt2)/2)
t3tupla2=(t3as2,(t32nt1+t32nt2)/2)
t3tupla3=(t3as3,(t33nt1+t33nt2)/2)
t3lista1=[t3tupla1,t31nt1,t31nt2]
t3lista2=[t3tupla2,t32nt1,t32nt2]
t3lista3=[t3tupla3,t33nt1,t33nt2]
t3lista=[t3lista1,t3lista2,t3lista3]
t3dcc={"nombre":t3nm,"materias":t3lista}
clclo=(t3tupla1[1]+t3tupla2[1]+t3tupla3[1])/3
print("BOLETIN:")
print(f"La nota final en {t3as1} es de: {t3tupla1[1]}")
print(f"La nota final en {t3as2} es de: {t3tupla2[1]}")
print(f"La nota final en {t3as3} es de: {t3tupla3[1]}")
print(f"El promedio final del estudiante es de: {clclo}")
