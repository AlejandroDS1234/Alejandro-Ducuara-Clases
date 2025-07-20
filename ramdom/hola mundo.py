import random
import time

letras_mayuscula={"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "}
letras_minuscula={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "}
letras=letras_mayuscula | letras_minuscula
palabra=list(input("Ingrese la palabra: "))
palabra_decifrar=list("A")
for letra in range(len(palabra)):
    while palabra[letra]!=palabra_decifrar[letra]:
        letra_palabra=random.choice(list(letras))
        palabra_decifrar[letra]=letra_palabra
        time.sleep(0.020)
        print("".join(palabra_decifrar))
    palabra_decifrar.append("_")
    
    