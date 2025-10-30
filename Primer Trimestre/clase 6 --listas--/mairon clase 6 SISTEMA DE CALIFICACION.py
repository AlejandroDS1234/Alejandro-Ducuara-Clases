print("SISTEMA DE CALIFICACION\n")
print("Este es un sistema de calificacion de notas en las materias:\nTrigonometria\nFisica\nGeometria\nEstadistica\nQuimica\n\nLas notas van de 1-5, la nota minima para pasar es de 3.0.\nDe 3.0 a 3.9 es una nota basica\nDe 4.0 a 4.5 es una nota alta\nDe 4.6 a 5.0 es una nota superior\n")
Name=input("Ingrese su nombre: ")
print("Notas en trigonometria\n")
tnt1=float(input("Ingrese la primera nota: "))
tnt2=float(input("Ingrese la segunda nota: "))
tnt3=float(input("Ingrese la tercera nota: "))
top=(tnt1+tnt2+tnt3)/3
print(f"El promedio final de trigonometria es de: {top}\n")

print("Notas en fisica\n")
fnt1=float(input("Ingrese la primera nota: "))
fnt2=float(input("Ingrese la segunda nota: "))
fnt3=float(input("Ingrese la tercera nota: "))
fop=(fnt1+fnt2+fnt3)/3
print(f"El promedio final de fisica es de: {fop}\n")

print("Notas en geometria\n")
gnt1=float(input("Ingrese la primera nota: "))
gnt2=float(input("Ingrese la segunda nota: "))
gnt3=float(input("Ingrese la tercera nota: "))
gop=(gnt1+gnt2+gnt3)/3
print(f"El promedio final de geometria es de: {gop}\n")

print("Notas en estadistica\n")
ent1=float(input("Ingrese la primera nota: "))
ent2=float(input("Ingrese la segunda nota: "))
ent3=float(input("Ingrese la tercera nota: "))
eop=(ent1+ent2+ent3)/3
print(f"El promedio final de estadistica es de: {eop}\n")

print("Notas en quimica\n")
qnt1=float(input("Ingrese la primera nota: "))
qnt2=float(input("Ingrese la segunda nota: "))
qnt3=float(input("Ingrese la tercera nota: "))
qop=(qnt1+qnt2+qnt3)/3
print(f"El promedio final de quimica es de: {qop}\n")

pt=(top+fop+gop+eop+qop)/5
print(f"El estudiante {Name} tiene las siguientes notas:\nTrigonometria: {top}\nFisica: {fop}\nGeometria: {gop}\nEstadistica: {eop}\nQuimica: {qop}\nObteniendo un promedio total de: {pt}\n\nSi tiene 4.6 o mas, ?¡Felicitaciones!\nSi sacaste de 4.0 a 4.5, vas bien\nSi sacaste 3.0 a 3.9, puedes mejorar\nSi sacaste menos de 3.0, no te rindas, aun puedes recuperar")