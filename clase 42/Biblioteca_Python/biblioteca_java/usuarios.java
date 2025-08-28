package biblioteca_java;
import java.util.ArrayList;
import java.util.Scanner;


public class usuarios {

    String nombre;
    String identificacion;
    
    public usuarios(String nombre, String identificacion) {

        this.nombre = nombre;
        this.identificacion = identificacion;
    }

    public void subir_libro(int s,admin admin, usuarios usuarios, biblioteca biblioteca) {

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
        if (s==1) {
            biblioteca.interfazAdmin(admin, usuarios, biblioteca);
        } else {
            biblioteca.interfaz2(admin, usuarios, biblioteca);
        }
        
    }

    public void descargar_libro(int d,admin admin,usuarios usuarios,biblioteca biblioteca) {
        System.out.print("Ingrese el codigo del libro (Si no lo tiene dirijase en el menu a buscar libro, puede regresar dejando en blonco): ");
        Scanner cdg = new Scanner(System.in);
        var cdg_ = cdg.nextLine();
        if (cdg_.equals("")) {
            if (d==1) {
                biblioteca.interfazAdmin(admin, usuarios, biblioteca);
            } else {
                biblioteca.interfaz2(admin, usuarios, biblioteca);
            }
        } else {
            var IDsss = new ArrayList<String>();
            for (var libro: biblioteca.Libross) {
                IDsss.add(libro.codigo);
                if (IDsss.contains(cdg_)) {
                    var idxx = IDsss.indexOf(cdg_);


                }
            }
        }

    }




    
}
