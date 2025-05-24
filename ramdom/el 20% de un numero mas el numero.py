#el 20% de un numero mas ese numero.
p=[float(input("Ingrese el numero para sumar con su 20%: "))]
t=int(input("cuantos numeros necesita?: "))
print(p[0])
while True: 
    i=(p[-1]*20)/100
    n=i+p[-1]
    p.append(n)
    print(p[-1])
    if len(p)==t:
        break