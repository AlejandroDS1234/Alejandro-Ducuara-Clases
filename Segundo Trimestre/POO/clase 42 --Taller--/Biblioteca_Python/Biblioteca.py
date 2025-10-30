
import random
import os



class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
    

    def subir_libro(self,s, Usuario, biblioteca=None ):
        if biblioteca==None:
            biblioteca=biblioteca_virtual
        print("SUBIR UN LIBRO")
        numeros={"1","2","3","4","5","6","7","8","9","0"}
        nm_l=input("Ingrese el nombre del libro: ")
        au_l=input("Ingrese el autor del libro: ")
        gn_l=input("Ingrese el genero del libro: ")
        id="".join(random.choice(list(numeros)) for _ in range(9))

        nuevo_libro=libro(nm_l, au_l, gn_l, id)
        biblioteca.libros.append(nuevo_libro)
        print("¡Libro Agregado!")
        if s==1:
            biblioteca.interfasAdmin()
        else:
            biblioteca.interfas2(Usuario)

    

    def descargar_libro(self,d, Usuario, biblioteca=None):
        if biblioteca==None:
            biblioteca=biblioteca_virtual
        cdg=input("Ingrese el codigo del libro (Si no lo tiene dirijase en el menu a buscar libro, puede regresar dejando en blonco): ")
        if cdg=="":
            if d==1:
                biblioteca.interfasAdmin()
            else:
                biblioteca.interfas2(Usuario)
        else:
            IDsss=[libro.codigo for libro in biblioteca.libros]
            if cdg in IDsss:
                idxx=IDsss.index(cdg)
                
                direccion_descargas= os.getcwd()
                nombre_txt=f"{biblioteca.libros[idxx].nombre.replace(' ','_')}.txt"
                direccion_completa=os.path.join(direccion_descargas, nombre_txt)
                with open(direccion_completa, "w", encoding="utf-8") as f:
                    f.write("\n")
                    f.write("\n")
                    f.write("\n")
                    f.write(f"\n{biblioteca.libros[idxx].nombre}\n\n")
                    f.write(f"Autor: {biblioteca.libros[idxx].autor}\n")
                    f.write(f"Género: {biblioteca.libros[idxx].genero}\n")
                    f.flush()
                    os.fsync(f.fileno())
                    print("El libro ha sido descargado")
                    if d==1:
                        biblioteca.interfasAdmin()
                    else:
                        biblioteca.interfas2(Usuario)
            else:
                print("Codigo de libro no existente")
                if d==1:
                    biblioteca.interfasAdmin()
                else:
                    biblioteca.interfas2(Usuario)

        

class admin(Usuario):
    def __init__(self):
        super().__init__(nombre="Alejandro",identificacion="123321")


    def cerrarPagina(self):
        print("Cerrando pagina")
        exit()
Alejo=admin()

        
class libro:
    def __init__(self, nombre,autor, genero, codigo):
        self.nombre=nombre
        self.autor=autor
        self.genero=genero
        self.codigo=codigo

libro1xdefecto=libro("El principito", "Antoine de Saint", "Novela", "842909348")
libro2xdefecto=libro("Metamorfosis", "Franz Kafka", "Novela", "349090878")
libro3xdefecto=libro("El gato negro", "Edgar Allan Poe", "Cuento", "054983232")

class biblioteca:
    
    def __init__(self):
        self.libros=[libro1xdefecto,libro2xdefecto,libro3xdefecto]
        self.usuarios=[]

    def interfas1(self, biblioteca=None):
        if biblioteca==None:
            biblioteca=biblioteca_virtual
        print("Biblioteca virtual\nEsta es una biblioteca donde podra encontrar libros subidos por la comunidad y descargarlos de manera gratuita\nIngrese 1 para registrarse\nIngrese 2 para inciar secion")
        dsss=input("Ingrese su opcion: ")
        if dsss=="1":
            biblioteca.agregar_usuario()
        elif dsss=="2":
            biblioteca.iniciar_secion()
        else:
            print("Opcion no valida")
            biblioteca.interfas1()
        

    def interfas2(self, Usuario,biblioteca=None ):
        if biblioteca==None:
            biblioteca=biblioteca_virtual
        print("BIBLIOTECA VIRTUAL")
        print("Hola, ¿que desea hacer?\n1) Buscar Libro\n2) Subir un libro\n3) Descargar libro\n4) Ver algunos libros disponibles\n5) Cerrar secion")
        dss=input("Ingrese su opcion: ")
        if dss=="1":
            biblioteca.buscar_libro(0,Usuario)
        elif dss=="2":
            Usuario.subir_libro(0,Usuario)
        elif dss=="3":
            Usuario.descargar_libro(0,Usuario)
        elif dss=="5":
            biblioteca.interfas1()
        elif dss=="4":
            biblioteca.ver_libros(0,Usuario)
        else:
            print("Opcion no valida")
            biblioteca.interfas2(Usuario)

    def interfasAdmin(self, biblioteca=None):
        if biblioteca==None:
            biblioteca=biblioteca_virtual
        print("ADMIN")
        print("Bienvenido alejandro, ¿que desea hacer?\n1) Buscar Libro\n2) Subir un libro\n3) Descargar libro\n4) Ver algunos libros disponibles\n5) Cerrar secion\n6) Apagar la pagina")
        ds=input("Ingrese su opcion: ")
        if ds=="1":
            biblioteca.buscar_libro(1,Alejo)
        elif ds=="2":
            Alejo.subir_libro(1,Alejo)
        elif ds=="3":
            Alejo.descargar_libro(1,Alejo)
        elif ds=="6":
            Alejo.cerrarPagina()
        elif ds=="5":
            biblioteca.interfas1()
        elif ds=="4":
            biblioteca.ver_libros(1,Alejo)
        else:
            print("Opcion no valida")
            biblioteca.interfasAdmin()
        

    def iniciar_secion(self, biblioteca=None):
        if biblioteca==None:
            biblioteca=biblioteca_virtual
        print("INICIAR SECION")
        idr=input("Ingrese su identificacion: ")
        IDs=[usuario.identificacion for usuario in self.usuarios]

        if idr==Alejo.identificacion:
            biblioteca.interfasAdmin()
        elif idr in IDs:
            idx=IDs.index(idr)
            biblioteca.interfas2(self.usuarios[idx])
        else:
            print("Usted no se ha registrado")
            biblioteca.interfas1()
            

    def agregar_usuario(self,biblioteca=None):
        if biblioteca==None:
            biblioteca=biblioteca_virtual
        print("REGISTRARSE")
        nm=input("Ingrese su nombre: ")
        id=input("Ingrese su identificacion: ")

        
        IDss=[usuario.identificacion for usuario in self.usuarios]
        if id in IDss:
            print("Este usuario ya esta registrado")
            biblioteca.interfas1()
        nuevo_usuario=Usuario(nm,id)
        self.usuarios.append(nuevo_usuario)
        biblioteca.interfas1()

    def buscar_libro(self,b,Usuario, biblioteca=None):
        if biblioteca==None:
            biblioteca=biblioteca_virtual
        print("BUSCAR LIBRO")
        buscar=input("Ingrese alguna referencia del libro (nombre, autor, genero, codigo): ")
        a=len(self.libros)
        bl=0
        for libro in self.libros:
            if libro.nombre==buscar or libro.autor==buscar or libro.genero==buscar or libro.codigo==buscar:
                print("-".center(50,"-"))
                print(f"Nombre: {libro.nombre}\nAutor: {libro.autor}\nGenero: {libro.genero}\nCodigo: {libro.codigo}")
                print("-".center(50,"-"))
                bl+=1
                a-=1
                #print(a)
            else:
                a-=1
                #print(a)
            if a<=0:
                    if bl==0:
                        print("Libro no encontrado. Por el momento no esta disponible o trate de escribir el nombre correctamente")
                    if b==1:
                        biblioteca.interfasAdmin()
                    else:
                        biblioteca.interfas2(Usuario)
    def ver_libros(self,v,Usuario, biblioteca=None):
        if biblioteca==None:
            biblioteca=biblioteca_virtual
        print("Algunas de los libros disponibles son: ")
        print("Nombre ---- Autor ---- Genero ---- Codigo")
        if len(self.libros)<10:
            for lbo in self.libros:
                print("-".center(50,"-"))
                print(f"{lbo.nombre} -- {lbo.autor} -- {lbo.genero} -- {lbo.codigo}")
                print("-".center(50,"-"))
        else:
            lb_ran_=random.sample(self.libros,len(self.libros)//2)
            for lb_ran in lb_ran_:   
                print("-".center(50,"-"))
                print(f"{lb_ran.nombre} -- {lb_ran.autor} -- {lb_ran.genero} -- {lb_ran.codigo}")
                print("-".center(50,"-"))

        if v==1:
            biblioteca.interfasAdmin()
        else:
            biblioteca.interfas2(Usuario)




biblioteca_virtual=biblioteca()
biblioteca_virtual.interfas1()


