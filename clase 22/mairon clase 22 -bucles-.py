#bucles
contador=int(input("Ingrese un numero: "))
while contador>0:
    print(f"contador: {contador}")
    contador-=1
print("Termino el contador")

contador2=1
while contador2<=100:
    print(f"contador: {contador2}")
    contador2+=1
    
#while True:
while True:
    texto=input("Escribe algo (o 'salir' para terminar): ").lower()
    if texto=="salir":
        break
    print(f"Escribiste {texto}")