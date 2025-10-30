#uno
print("PRIMERO:")
p1num=(1,2,3,4,5)
print(f"En {p1num} el primer elemento es: {p1num[0]} y el ultimo es: {p1num[-1]}\n")
#dos
print("SEGUNDO:")
p2num=[1.1,2.1,3.1,4.1,5.1]
print(f"En {p2num} el segundo elemento es: {p2num[1]} y el cuarto es: {p2num[3]}\n")
#tres
print("TERCERO:")
p3vr1=1
p3vr2=2
p3vr3=3
p3tp=(p3vr1,p3vr2,p3vr3)           #PREGUNTAR
print(f"tupla: {p3tp}\n")
#cuatro
print("CUARTO:")
p4num=[2,4,6,8,10]
p4suma=p4num[0]+p4num[1]+p4num[2]+p4num[3]+p4num[4]
print(f"La suma de los numeros: {p4num} da igual a: {p4suma}\n")
#cinco
print("QUINTO:")
p5num=(2.3,3.4,4.5)
p5pr=(p5num[0]+p5num[1]+p5num[2])/3
print(f"El promedio de: {p5num} es: {p5pr}\n")
#seis
print("SEXTO:")
p6num=[1,3,5,7]
p6vr1=p6num[0]
p6vr2=p6num[1]
p6vr3=p6num[2]
p6vr4=p6num[3]
print(f"{p6vr1} es una variable, {p6vr2} es otra variable, {p6vr3} es otra variable, {p6vr4} es otra variable\n")
#siete
print("SEPTIMO:")
p7num=(2,3)
p7mltc=p7num[0]*p7num[1]
print(f"La multiplicacion de: {p7num} da como resultado: {p7mltc}\n")
#ocho
print("OCTAVO:")
p8ls=["uno","dos","tres"]
p8ls.append("cuatro")
print(f"En la lista: {p8ls} el primer elemento es: {p8ls[0]} y el ultimo es: {p8ls[-1]}\n")
#nueve
print("NOVENO:")
p9tp=(2,4,6,8)
p9suma=p9tp[0]+p9tp[1]
print(f"La suma de los dos primeros elementos en: {p9tp} da como resultado: {p9suma}\n")
#diez
print("DECIMO:")
p10ls=[8,6,4,2.1]
p10rt=p10ls[1]-p10ls[3]
print(f"El resultado de la resta entre el segundo y el cuarto numero en: {p10ls} da como resultado {p10rt}\n")
#once
print("DECIMO PRIMERO")
p11num=(2,4,6,8,10)
p11mltc=p11num[0]*p11num[-1]
print(f"La multiplicacion del primer y ultimo elemento en: {p11num} da: {p11mltc}\n")
#doce
print("DECIMO SEGUNDO")
p12num=[6,4,2]
p12dv=p12num[0]/p12num[2]
print(f"La division entre el primer y el tercer numero en: {p12num} da: {p12dv}\n")
#trece
print("DECIMO TERCERO")
p13tp=(1,2,3,4)
print(f"El tercer elemento en {p13tp} es: {p13tp[2]}\n")
#catorce
print("DECIMO CUARTO")
p14ls=[1.2,2.3,3.4,4.5,5.6]
p12suma=p14ls[0]+p14ls[1]+p14ls[2]+p14ls[3]+p14ls[4]
print(f"La suma de todos los elementos de: {p14ls} da: {p12suma}\n")
#quince
print("DECIMO QUINTO:")
p15lis=[1,2,3,4]
p15tp=tuple(p15lis)
print(f"Tupla: {p15tp}\n")
#diezyseis
print("DECIMO SEXTO:")
p16tp=(1,2,3)
p16lis=list(p16tp)
p16lis.append(4)
print(f"Lista: {p16lis}\n")
#diezysiete
print("DECIMO SEPTIMO:")
p17lis=[5,4,3,2,1]
p17tp=tuple(p17lis)
print(f"El tercer elemento de la tupla: {p17tp} es: {p17tp[2]}\n")
#diezyocho
print("DECIMO OCTAVO:")
p18tp=(2,3,4)
p18lis=list(p18tp)
p18lis[1]=input("Ingrese un nuevo elemento: ")
print(f"Lista: {p18lis}\n")
#diezynueve
print("DECIMO NOVENO:")
p19lis=[5,4,3,2]
p19tp=tuple(p19lis)
print(f"La cantidad de elementos en la tupla {p19tp} es: {len(p19tp)}\n")
#veinte
print("VEINTEAVO:")
p20tp=("cinco","cuatro","tres","dos","uno")
p20lis=list(p20tp)
p20lis.remove(p20lis[-1])
print(f"la lista sin el ultimo elemento: {p20lis}")




