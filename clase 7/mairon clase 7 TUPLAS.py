tupla=(1,2,3,4)
tupla2=("hola","como","estas")
tupla3=(1,"hola",2,"como",3.5)
#print(len(tupla3))
tupla4=(1,2,1,3,1,4,1,5)
#print(tupla4.count(1),tupla2.index("estas"))


#Convertir tuplas --> listas

Tupla=(2,4,6,8)
Lista=list(Tupla)
Lista.append("hola") #algo
#print(Lista)

#Convertir listas --> tuplas

lista=["hola","como","estas"]
TTupla=tuple(lista)
#print(TTupla)


#Ejercicio

dias=("LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO")
print(dias[2])
print(dias.count("LUNES"))
print(dias.index("JUEVES"))



#EJERCICIOS
print("1) crear tupla")
num=(1,2,3,4,5)
print("2) acceder a un elemento")
print(num[1])
print("3) Longitud de la tupla")
print(len(num))
print("4) Posicion del numero 4")
print(num.index(4))
print("5) Cuantas veces aparece el numero 2")
print(num.count(2))
print("6) datos mesclados")
tpmescla=("hola pepe",2,2.5)
print("7 tuplas anidadas")
mzc=(-3,-2,-1,0,num)
print(mzc[4][0])