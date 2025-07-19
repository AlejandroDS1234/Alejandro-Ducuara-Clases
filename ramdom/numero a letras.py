import time

def numeros_letras(numero):
    unidades={1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve"}
    decenas={1:"diez",11:"once",12:"doce",13:"trece",14:"catorce",15:"quice",2:"veinti",3:"treinta",4:"cuarenta",5:"cincuenta",6:"sesenta",7:"setenta",8:"ochenta",9:"noventa"}
    if len(str(numero))>3:
        return "El numero es muy grande"
    else:

        if numero>=1 and numero<=9:
            return f"{unidades[numero]}"
        elif numero>=11 and numero<=15:
            return f"{decenas[numero]}"
        elif numero==10 or numero>=16 and numero<=99:
            numero=str(numero)
            decena=int(numero[0])
            unidad=int(numero[1])
            if unidad==0:
                if decena==2:
                    return "veinte"
                else:
                    return f"{decenas[decena]}"
            else:
                if decena!=2:  
                    return f"{decenas[decena]} y {unidades[unidad]}"
                else:
                    return f"{decenas[decena]}{unidades[unidad]}"
        elif numero>=100 and numero<=999:
            numero=str(numero)
            decena=int(numero[1])
            unidad=int(numero[2])
            centena=int(numero[0])
          #  print(unidad, decena, centena)
            if unidad==0 and decena==0:
                if centena==1:
                    return f"cien"
                else:
                    return f"{unidades[centena]}cientos"
            elif decena==0:
                if centena==1:
                    return f"ciento {unidades[unidad]}"
                else:
                    return f"{unidades[centena]}cientos {unidades[unidad]}"
            elif unidad==0:
                if centena==1:
                    if decena==2:
                        return f"ciento veinte"
                    else:
                        return f"ciento {decenas[decena]}"
                else:
                    if decena==2:
                        return f"{unidades[centena]}cientos veinte"
                    else:
                        return f"{unidades[centena]}cientos {decenas[decena]}"
            else:
                if centena==1:
                    if decena==2:
                        return f"ciento {decenas[decena]}{unidades[unidad]}"
                    else:
                        return f"ciento {decenas[decena]} y {unidades[unidad]}"
                else:
                    return f"{unidades[centena]}cientos {decenas[decena]} y {unidades[unidad]}"

personas=["pepe","papa","poncio"]
contador=1
for persona in personas:
    time.sleep(1)
    print(f"{numeros_letras(contador)}) {persona}")
    contador+=1