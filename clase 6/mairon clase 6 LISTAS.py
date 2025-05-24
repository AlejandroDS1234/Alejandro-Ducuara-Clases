#listas Ej normal
a=[1,2,4,4,5,"hola"]
a[2]=3
print(a)

#Sumar numeros
print("SUMAR NUMEROS")
numero=[int(input("Ingrese un numero a sumar: ")),int(input("Ingrese otro numero a sumar: "))]
suma=numero[0]+numero[1]
print(f"El resultado de la suma es: {suma}")

#agregar datos a la lista con .append()  Actividad
#1
print("LISTA DE PRODUCTOS")
productos=[]
productos.append(input("Ingresa un producto: "))
productos.append(input("Ingresa otro producto: "))
productos.append(input("Ingresa otro producto: "))
print(f"Tu lista de productos tiene:\n{productos}")

#2
print("PRECIO DE TRES ARTICULOS")
precios=[]
precios.append(float(input("Ingresa el precio del primer producto: ")))
precios.append(float(input("Ingresa el precio del segundo producto: ")))
precios.append(float(input("Ingresa el precio del tercer producto: ")))
op=precios[0]+precios[1]+precios[2]
print(f"La suma de los precios es: {op}")

#3 utilizar el max() y el min()
print("NUMEROS MAYOR Y MENOR")
numeros=[]
numeros.append(int(input("Ingresa el primer numero: ")))
numeros.append(int(input("Ingresa el segundo numero: ")))
numeros.append(int(input("Ingresa el tercer numero: ")))
numeros.append(int(input("Ingresa el cuarto numero: ")))
print(f"El numero mayor fue: {max(numeros)} y el menor: {min(numeros)}")

