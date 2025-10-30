class perro:
    especie="Mamifero"
    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
    
    #Metodos
    def ladrar(self):
        return f"{self.nombre} ladra :)"
    
    def mostrarinfo(self):
        return f"Nombre: {self.nombre}\n Raza: {self.raza}\n Edad: {self.edad}\n Especie: {self.especie}"
    
    
    #Programa principal
    
perro1=perro("Simba","Criollo",7)
#print(perro1.ladrar())
#print(perro1.mostrarinfo())

perro2=perro("Luna","Poodle",5)
#print(perro2.ladrar())
#print(perro2.mostrarinfo())

perro3=perro("Max","Bulldog",4)
#print(perro3.ladrar())
#print(perro3.mostrarinfo())

print(perro1)