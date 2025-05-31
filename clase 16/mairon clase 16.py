#Controladores de flujo (condicionales)(if)
#if  y else
"""print("If y Else")
edad=30
if edad>=18:
    print("Es adulto")
else:
    print("No se cumple la condicion")

#multiples if
print("Multiples if\nEjemplo 1:")
x=25
if x>10:
    print("Por encima de 10")
    if x>20:
        print("y tambien por encima de 20!")
    else:
        print("Pero no por enciama de 20")

#sentencia elif
print("Elif")
c=int(input("Ingrese un numero: "))
b=int(input("ingrese otro numero: "))
a=b*c
print(a)
if a>100000:
    print("sus numeros son enormes")
elif a>300:
    print("sus numeros son grandes")
else:
    print("sus numeros son pequeños")"""

#ACTIVIDAD

año=int(input("iNGRESE SU AÑO DE NACIMIENTO: "))
if año<=1940 and año>=1920:
    print("Usted es de la generacion silenciosa")
elif año<=1964:
    print("Usted es de la generacion Boomer")
elif año<=1979:
    print("Usted es de la generacion X")
elif año<=2000:
    print("Usted es de la generacion Y")
elif año<=2010:
    print("Usted es de la generacion Z")
else:
    print("Su año no tiene generacion")



#