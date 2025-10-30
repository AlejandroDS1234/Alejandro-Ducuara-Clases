package java_poo_miniejemplo;

public class animal {// la clase tiene que estar en un archivo con el nombre de la clase

    //atributos animal
    String nombre;
    int edad;
    String especie;

    //constructor  //cosas obligatorias que deba tener
    public animal(String nombre, int edad, String especie) {//definir los parametros

        this.nombre = nombre;
        this.edad = edad;
        this.especie = especie;

    }





    //comportamientos (metodos)
    public void Comer() { //no puede ser estatica
        System.out.println(String.format("El %s esta comiendo", nombre));
        
    }
    
}
