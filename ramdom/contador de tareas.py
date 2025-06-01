#contar cuantas tareas ha hecho
print("Contador De Tareas")
tareas=int(input("Ingrese la cantidad de tareas que tiene: "))
while True:
    boton=input("Si completo una tarea presione enter")
    tareas=tareas-1
    if tareas==0:
        print("Ya no le quedan mas tareas")
        break
    else:
        print(f"le quedan {tareas} tareas")
    

