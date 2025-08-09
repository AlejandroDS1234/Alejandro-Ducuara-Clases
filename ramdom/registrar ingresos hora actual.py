from datetime import date, timedelta, datetime

a=datetime.now().year
año=date(day=1,month=1,year=a)
año_siguiente=date(day=1,month=1,year=a+1)
dias=[]
dias_={}
while año<año_siguiente:
    dias.append(año)
    año+=timedelta(days=1)
for dia in dias:
    dias_[dia]=([],[],[])
    #print(str(dia))
personas=[]
dia_actual=datetime.now().day
dia_siguiente=datetime.now().day+1
fecha_actual=date(day=datetime.now().day,month=datetime.now().month,year=datetime.now().year)
def dia__():
    dia_actual=datetime.now().day
    dia_siguiente=datetime.now().day+1
    fecha_actual=date(day=datetime.now().day,month=datetime.now().month,year=datetime.now().year)
while True:
    dia_actual_2=datetime.now().day

    print("OPCIONES:\n1.Agregar persona\n2.Registrar Ingreso\n3.Consultar ingresos\n4.Eliminar persona\n5.Ver personas ingresadas\n6. Salir del programa")
    accion=input("Ingrese la accion que va a realizar: ")
    if dia_actual_2==dia_siguiente:
        dia__()
        conjunto_dia_temprano=set(dias_[fecha_actual-timedelta(days=1)][0])
        conjunto_dia_tarde=set(dias_[fecha_actual-timedelta(days=1)][1])
        conjunto_personas=set(personas)
        temprano=conjunto_personas-conjunto_dia_temprano
        tarde=conjunto_personas-conjunto_dia_tarde
        no_llego=tarde|temprano
        no_llego=list(no_llego)
        for person in no_llego:
            dias_[fecha_actual-timedelta(days=1)][2].append(person)
    if accion=="1":
        while True:
            persona=input("Ingrese la nueva persona: ")
            if persona in personas:
                print("Esta persona ya esta ingresada")
                continue
            else:
                personas.append(persona)
                print("Persona registrada con exito")
                break
    elif accion=="2":
        persona_ingresar=input("Ingrese la persona que ingresa: ")
        hora_llegada=datetime.now().hour+(datetime.now().minute/100)
        if persona_ingresar in personas:
            if float(hora_llegada)<=8:
                print(hora_llegada)
                print("Su llegada ha sido registrada")
                dias_[fecha_actual][0].append(persona_ingresar)
            elif float(hora_llegada)>8:
                print(hora_llegada)
                print("Ha llegado tarde, llegada registrada")
                dias_[fecha_actual][1].append(persona_ingresar)
        else:
            print("Persona no ingresada")
    elif accion=="3":
        print("Este es el registro de los dias trabajados hasta la fecha: ")
        for dia in dias_:
            if dias_[dia][0] or dias_[dia][1] or dias_[dia][2]:
                print(f"Fecha: {dia}")
                print("Puntuales")
                for trabajador in dias_[dia][0]:
                    print(trabajador)
                print("Inpuntuales")
                for trabajador in dias_[dia][1]:
                    print(trabajador)
                print("No llegaron")
                for trabajador in dias_[dia][2]:
                    print(trabajador)
    elif accion=="4":
        print("Personas registradas:")
        for persona in personas:
            print(f"- {persona}\n")
        persona_eliminar=input("Ingrese la persona ")
        if persona_eliminar in personas:
            personas.remove(persona_eliminar)
            print("Persona eliminada con exito")
        else:
            print("Esta persona no esta ingresada")
    elif accion=="5":
        print("Las personas ingresadas son: ")
        for persona in personas:
            print(f"- {persona}\n")
    elif accion=="6":
        print("Programa finalizado")
        exit()
    else:
        print("Accion no valida")
        #FIN