print("DATOS DE MASCOTAS")
nm=input("Ingrese el nombre de su mascota: ")
tp=input("Ingrese el tipo de mascota: ")
ed=int(input("Ingrese la edad de su mascota: "))
nmd=input("Ingrese su nombre (el de dueño): ")
cd=input("Ingrese su ciudad: ")
datos={"nombre de la mascota":nm,"tipo de mascota":tp,"edad de la mascota":ed,"nombre del dueño":nmd,"ciudad":cd}
print(f"Los datos de su mascota son: {datos}")