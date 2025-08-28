package biblioteca_java;

public class inicio {

    public static void main(String[] args) {

        var libro1xdefecto = new libros("El principito", "Antoine de Saint", "Novela", "842909348");
        var libro2xdefecto = new libros("Metamorfosis", "Franz Kafka", "Novela", "349090878");
        var libro3xdefecto = new libros("El gato negro", "Edgar Allan Poe", "Cuento", "054983232");
        
        var Biblioteca_virtual = new biblioteca();

        Biblioteca_virtual.Libross.add(libro1xdefecto);
        Biblioteca_virtual.Libross.add(libro2xdefecto);
        Biblioteca_virtual.Libross.add(libro3xdefecto);

        var Alejo = new admin();

       
        Biblioteca_virtual.interfaz1(Alejo, Biblioteca_virtual);


        
    }

    
}