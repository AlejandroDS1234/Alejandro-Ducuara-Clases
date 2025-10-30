#ACTIVIDAD
nbclnts=["mairon","pepe","aurturo","pepe","maximiliano","ligoverto"]
#Agregar a juliana
nbclnts.append("JULIANA")
#La cantidad de elementos
elmt=len(nbclnts)
print(f"hay {elmt} elementos en la lista:\n{nbclnts}")
#Orden alfabeticamente
print(f"El nombre alfabeticamente mayor es: {max(nbclnts)} y el menor es: {min(nbclnts)}")
#Numero intermedio

print(f"juliana esta en la posicion: {nbclnts.index("JULIANA")}")
print(f"La lista resultante es: {nbclnts}")


print("")
#remover ejemplo

numeros=[1,2,3,2]
numeros[3]=4
numeros.remove(4)
print(numeros)
