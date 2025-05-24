#1
print("1) Sumar numeros")
ej1num1=int(input("ingrese el primer numero: "))
ej1num2=int(input("ingrese el segundo numero: "))
ej1op=ej1num1+ej1num2
print(f"la suma de {ej1num1}+{ej1num2} da como resultado: {ej1op}")

#2
print("2) Resta de numeros")
ej2num1=int(input("ingrese el primer numero: "))
ej2num2=int(input("ingrese el segundo numero: "))
ej2op=ej2num1-ej2num2
print(f"la resta del numero {ej2num1}-{ej2num2} da como resultado: {ej2op}")

#3
print("3) Multiplicar numeros")
ej3num1=int(input("ingrese el primer numero: "))
ej3num2=int(input("ingrese el segundo numero: "))
ej3op=ej3num1*ej3num2
print(f"el resultado de la multiplicacion de {ej3num1}*{ej3num2} da como resultado: {ej3op}")

#4
print("4) Division de dos numeros")
ej4num1=int(input("ingrese el primer numero: "))
ej4num2=int(input("ingrese el segundo numero: "))
ej4op=ej4num1/ej4num2
print(f"la division de {ej4num1}/{ej4num2} da como resultado: {ej4op}")

#5
print("5) Saludo")
ej5name=input("ingrese su nombre: ")
ej5aplld=input("ingrese su apellido: ")
print(f"Hola, Buenos dias, gusto en verte {ej5name} {ej5aplld}")

#6
print("6) La primera letra de tu nombre")
ej6name=input("ingrese su nombre: ")
print("la primera letra de su nombre es:",ej6name[0:1])

#7
print("7) La ultima letra del nombre")
ej7name=input("ingrese su nombre: ")
print("la ultima letra de su nombre es:",ej7name[-1])

#8
print("8) calcular el area de un rectangulo")
ej8base=int(input("ingrese la base del rectangulo: "))
ej8altura=int(input("ingrese la altura del rectangulo: "))
ej8op=ej8base*ej8altura
print(f"el area de tu rectangulo es: {ej8op}")

#9
print("9) calcular la edad actual")
ej9año=int(input("ingrese su año de nacimiento: "))
ej9añoactual=2025
ej9op=ej9añoactual-ej9año
print(f"actualmente usted tiene {ej9op} años")

#10
print("10) direccion de correo")
ej10name=input("ingrese un nombre de usuario: ")
ej10name+="@gmail.com"
print(f"tu direccion de correo sera: {ej10name}")

#11
print("11) Cuantas letras tiene tu nombre")
ej11name=input("ingresa tu nombre: ")
ej11ctd=len(ej11name)
print(f"el nombre {ej11name} tiene {ej11ctd} letras")

#12
print("12) combinar palabras")
ej12pl1=input("ingrese una palabra: ")
ej12pl2=input("ingrese otra palabra: ")
print(ej12pl1+ej12pl2)

#13
print("13) mostrar la segunda letra")
ej13pl=input("ingrese una palabra: ")
print(f"la segunda letra de la palabra {ej13pl} es {ej13pl[1:2]}")

#14
print("14) Las tres primeras letras de una palabra")
ej14pl=input("ingrese una palabra: ")
print(f"las tres primeras letas de la palabra {ej14pl} son {ej14pl[0:3]}")

#15
print("15) Letras en orden inverso")
ej15pl=input("ingresa una palabra: ")
print(f"la palabra inversa es: {ej15pl[::-1]}")

#16
print("16) suma, resta, multiplicacion y division de dos numeros")
ej16num1=int(input("ingrese el primer numero: "))
ej16num2=int(input("ingrese el segundo numero: "))
ej16opS=ej16num1+ej16num2
ej16opR=ej16num1-ej16num2
ej16opM=ej16num1*ej16num2
ej16opD=ej16num1/ej16num2
print(f"Las operaciones son:\n {ej16num1}+{ej16num2}={ej16opS}\n {ej16num1}-{ej16num2}={ej16opR}\n {ej16num1}*{ej16num2}={ej16opM}\n {ej16num1}/{ej16num2}={ej16opD}")

#17
print("17) El doble del numero")
ej17num=int(input("ingresa un numero: "))
ej17doble=ej17num*2
print(f"el doble del numero {ej17num} es: {ej17doble}")

#18
print("18) La mitad del numero")
ej18num=int(input("ingrese un numero: "))
ej18mitad=ej18num/2
print(f"la mitad del numero {ej18num} es: {ej18mitad}")

#19
print("19) Cuantos caracteres tiene la frase")
ej19frase=input("ingrese una frase: ")
print(f"la frase, {ej19frase}, tiene {len(ej19frase)} caracteres")

#20
print("20) Repetir 3 veces la frase")
ej20pl=input("ingrese una palabra: ")
print(ej20pl+" "+ej20pl+" "+ej20pl)

#21
print("21) 2 primeras y 2 ultimas letras de tu nombre")
ej21name=input("ingresas tu nombre: ")
print(f" las 2 primeras letras del nombre {ej21name} son {ej21name[0:2]} y las 2 ultimas son {ej21name[-2:]}")

#22
print("22) letra de en medio")
ej22pl=input("ingresa una palabra: ")
ej22ln=len(ej22pl)
ej22op=ej22ln//2
print(f"la letra de en medio de la palabra es {ej22pl[ej22op]}")

#23
print("23) los primeros 10 caracteres de una frase")
ej23frase=input("ingresa una frase: ")
print(f"los primeros 10 caracteres son: {ej23frase[0:10]}")

#24
print("24) elevar al cuadrado")
ej24num=int(input("ingresa un numero: "))
ej24op=ej24num*ej24num
print(f"el elevado al cuadrado del numero {ej24num} es ej24op")

#25 -lo hizo una compañera, salome-
print("25) cual numero es mayor")
ej25num1=int(input("ingresa el primer numero: "))
ej25num2=int(input("ingresa el segundo numero: "))
ej25op=ej25num1*(ej25num1>=ej25num2)+ej25num2*(ej25num1<=ej25num2)
print(f"el numero mayor es el: {ej25op}")



#26
print("26) cuantos dias has vivido")
ej26edad=int(input("ingresa tu edad en años: "))
ej26op=ej26edad*365
print(f"has vivido {ej26op} dias")

#27
print("27) mostrar cada letra por separado")
ej27pl=input("ingresa la palabra puerta: ")#6
print(f"{ej27pl[0:1]}\n{ej27pl[1:2]}\n{ej27pl[2:3]}\n{ej27pl[3:4]}\n{ej27pl[4:5]}\n{ej27pl[5:6]}")

#28
print("la palabra tiene mas de 5 letras")
ej28pl=input("ingresa una palabra: ")
print(f"la palabra tiene {len(ej28pl)} letras")

#29
print("29) multiplicar por 10")
ej29num=int(input("ingrese un numero: "))
ej29num*=10
print(f"el numero multiplicado por 10 es: {ej29num}")

#30
print("30) palabra en minuscula y mayusculas")
ej30pl=input("ingrese una palabra: ")
pp=ej30pl.upper()
pp2=ej30pl.lower()
print(pp,pp2)


