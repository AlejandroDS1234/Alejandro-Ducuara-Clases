package biblioteca_java;

import java.util.Scanner;


public class usuarios {

    String nombre;
    String identificacion;
    
    public usuarios(String nombre, String identificacion) {

        this.nombre = nombre;
        this.identificacion = identificacion;
    }

    public void subir_libro(biblioteca biblioteca) {

        System.out.println("SUBIR UN LIBRO");
        System.out.print("Ingrese el nombre del libro: ");
        Scanner nm_l = new Scanner(System.in);
        var nm_ll = nm_l.nextLine();
        System.out.print("Ingrese el autor del libro: ");
        Scanner au_l = new Scanner(System.in);
        var au_ll = au_l.nextLine();
        System.out.print("Ingrese el genero del libro: ");
        Scanner gn_l = new Scanner(System.in);
        var gn_ll = gn_l.nextLine();
        String id="";
        int limiteInferior=1;
        int limiteSuperior=9;
        for (int ñ=0; ñ<9; ñ+=1) {
            int numeroAleatorio=(int) (limiteInferior+(limiteSuperior-limiteInferior+1)*Math.random());
            id+=numeroAleatorio;
        }

        var nuevo_libro = new libros(nm_ll, au_ll, gn_ll, id);
        biblioteca.Libross.add(nuevo_libro);
        System.out.println("Libro Agregado!!!");
        
    }

    public void descargar_libro() {

    }




    
}
