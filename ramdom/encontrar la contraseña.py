import time
import random

letras_mayuscula={"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "}
letras_minuscula={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "}
numeros={"1","2","3","4","5","6","7","8","9","0"}
letras=letras_mayuscula | letras_minuscula #| numeros

encontrar=""
contraseña=list("eternocleidomastoideo")
inicio=time.time()
while encontrar!=contraseña:
   # encontrar=["".join(random.choice(list(numeros))) for _ in range(len(contraseña))]
  #  encontrar=["".join(random.choice(list(letras_mayuscula))) for _ in range(12)]
   # encontrar=["".join(random.choice(list(letras_minuscula))) for _ in range(12)]
    encontrar=["".join(random.choice(list(letras))) for _ in range(len(contraseña))]
    print(encontrar)
fin=time.time()
print(f"Contraseña encontrada!! \n En {fin-inicio} segundos")
    

    

        





