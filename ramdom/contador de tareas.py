#contar cuantas tareas ha hecho
"""print("Contador De Tareas")
tareas=int(input("Ingrese la cantidad de tareas que tiene: "))
while True:
    boton=input("Si completo una tarea presione enter")
    tareas=tareas-1
    if tareas==0:
        print("Ya no le quedan mas tareas")
        break
    else:
        print(f"le quedan {tareas} tareas")"""



#tareas mas avanzado
print("Ingrese el nombre de la asignatura en que tiene tareas: ")
materias=[]
numeros=[0]
while True:
    tarea=input("(deje en blanco si no tiene mas tareas) ")
    materias.append(tarea)
    numeros.append(numeros[-1]+1)
    if tarea=="":
        materias.remove("")
        for numero in numeros:
            cantidad=len(materias)-numero
            if cantidad==0:
                print(f"ha finalizado todas las tareas")
                input("presione enter para salir")
                materias.clear()
                numeros.clear()
                numeros.append(0)
                print("Ingrese el nombre de la asignatura en que tiene tareas: ")
                break
            else:
                print(f"le quedan {cantidad} tareas, siga con la tarea de {materias[numero]}")
                input("Presione enter para la siguiente")

            


