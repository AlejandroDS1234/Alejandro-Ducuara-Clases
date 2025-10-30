#clase 4
# #ASIGNACION

a="hola",3
print(a)
##ASIGNACION MULTIPLE

x,z,t=6,3,9
print(x)
print(z)
print(t)
##ASIGNAR EL MISMO VALOR A LAS VARIABLES

r=h=q="hola"
print(r,h,q)
##ASIGNACION CON OPERACIONES

ñ=10
ñ=ñ+5
print(ñ)

o=30
o+=2
o*=3
print(o)

name1="hola pepe "
name1+="¿como estas? "
name1+="¿bien?"
name1*=2
print(name1)

##CONCATENACION

tex1="todo el que tiene un porque"
tex2="puede soportar casi cualquier como"
print(tex1+" "+tex2)

##BUSQUEDA

TEXTOmigala="""Debo admitir que no hemos estado escribiendo tan seguido como antes. Me encantaría culpar a nuestros demandantes trabajos, pero el otro día pasé tres horas viendo capítulos de Adventure Time así que, al menos yo, no tengo una excusa de verdad.
De todos modos, me gusta pensar que tantas horas de procrastinación eventualmente servirán de algo, así que hice una compilación con los mejores cortos de ciencia ficción que vi esta semana, espero que ustedes pierdan tanto tiempo como yo viéndolos:"""
palabra=TEXTOmigala.find("gusta pensar")
t=len(TEXTOmigala) #el total de caracteres
print(palabra,t)

##EXTRACCION

print(TEXTOmigala[263:272])


##ACTIVIDAD
#1
Actividad="El conocimiento es poder"
print(Actividad.find("conocimiento"),Actividad.find("poder"))
#2
punto2="la practica hace al maestro"
print(punto2.find("practica"),punto2.find("maestro"))
#3
frase=input("ingrese una frase: ")
pregunta=input("que palabra quieres buscar de tu frase: ")
print(frase.find(pregunta))
#4
texto_de_ejemplo="""Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"""
print(f"la palabra sabia esta en {texto_de_ejemplo.find("Sabia")}")
print(texto_de_ejemplo.find("Caminaba"),texto_de_ejemplo.find("falanges"))
parte=texto_de_ejemplo[459:655]
print(parte)
#5
texto_ejemplo2="""LA LUNA Y LAS ESTRELLA

con mis ojos bañados por el llanto
miraba la luna y las estrellas
amándote y recordándote yo tanto
le pedía a Dios que te mirara en ellas
era tanta la angustia por verte
tanta que este inmenso amor que tengo
me hacia suspirar por tenerte
solo y triste pensando en ti yo me mantengo
es por la ternura que yo siento por ti
las horas pasan y recuerdo tu linda risa
mientras mi alma guarda un amor por ti
en mi rostro todo mi llanto se desliza
es raro el decir que no estoy triste
cuando por tu amor estoy tan triste
si mis ojos están bañados por el llanto
es porque tú eres para mi un lindo encanto"""
print(texto_ejemplo2.find("le"),texto_ejemplo2.find("encanto"))
ext=texto_ejemplo2[123:619]
print(ext)


#MI PRIMER PROGRAMA

print("calcular nota final")
nombre=input("ingrese su nombre: ")
not1=float(input("ingrese nota 1 (20%): "))
not2=float(input("ingrese nota 2 (30%): "))
not3=float(input("ingrese nota 3 (50%): "))
calculo=((not1*20)+(not2*30)+(not3*50))/100
print(f"el estudiante {nombre} tiene una nota final de: {calculo}")