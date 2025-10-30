#continuacion diccionarios
#actividad del profe para una memoria 
dictionary={"a":1,"e":2}

print(dictionary)
print(f"clave a: {dictionary['a']}")
print(f"clave e: {dictionary['e']}")

dictionary={"numbers":[10,20,20],"groups":{"a":1,"b":2},"z":3}

print(dictionary)
print(f"clave numbers: {dictionary['numbers']}")
print(f"clave groups: {dictionary['groups']}")

print(f"clave numbers: {dictionary['numbers'][1]}")
print(f"clave groups: {dictionary['groups']['b']}")
print(dictionary['z'])