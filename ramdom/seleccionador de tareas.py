import random
import time
while True:
    print("\n\n","ORGANIZADOR PARA HACER TAREAS".center(40,"="),"\n\n")
    tareas=[]
    tareas_saltadas=[]
    contador=1
    while True:
        tarea=input("Ingrese una nuevo tarea (Enter para continuar): ")
        if tarea!="":
            print("Tarea agregada\n")
            tareas.append(tarea)
            continue
        else:
            if len(tareas)==0:
                print("No ha ingresado ninguna tarea")
            else:
                print("\n","TAREAS".center(20,"-"),"\n")
                while len(tareas)!=0:
                    tarea_hacer=random.choice(tareas)
                    if len(tareas)==1:
                        print("Ultima tarea")
                        print(f"La ultima tarea es:")
                        time.sleep(2)
                        print(f"\n{tarea_hacer}\n")
                        input("Ingrese enter o escriba algo para continuar: ")
                        tareas.remove(tarea_hacer)
                    else:
                        if tarea_hacer in tareas_saltadas:
                            if tareas==tareas_saltadas:
                                print(f"Tiene {len(tareas)} tareas")
                                print(f"La tarea numero {contador} a realizar es:")
                                time.sleep(2)
                                print(f"\n{tarea_hacer}\n")
                                continuar=input("Presione enter para continuar o escriba algo para saltar la tarea: ")
                                if continuar!="":
                                    print("Tarea saltada\n")
                                    continue
                                contador+=1
                                tareas.remove(tarea_hacer)
                                tareas_saltadas.remove(tarea_hacer)
                                   
                        else:

                            print(f"Tiene {len(tareas)} tareas")
                            print(f"La tarea numero {contador} a realizar es:")
                            time.sleep(2)
                            print(f"\n{tarea_hacer}\n")
                            continuar=input("Presione enter para continuar o escriba algo para saltar la tarea: ")
                            if continuar!="":
                                print("Tarea saltada\n")
                                tareas_saltadas.append(tarea_hacer)
                                continue
                            contador+=1
                            tareas.remove(tarea_hacer)
                print("\n¡¡¡Ya no tiene mas tareas!!!\n")
                break

