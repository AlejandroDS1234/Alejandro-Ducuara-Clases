a=list(input("Ingrese una contraseña: "))
b=list(input("Ingrese su contraseña: "))
if a==b:
    print("correcto")
else:
    c=len(a)-1
    d=len(b)-1
    e=[]
    
    while c>=d:
        if a[c]!=b[d]:
            e.append(b[d])
            d=d-1
            c=c-1
            if d<0 or c<0:
                break
        else:
            print("no")
            break
    print(b)
    print((e[::-1]))
    