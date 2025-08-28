package biblioteca_java;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;

public class biblioteca {

    ArrayList<usuarios> Usuarioss = new ArrayList<>();
    ArrayList<libros> Libross = new ArrayList<>();

    public void interfaz1(admin admin,biblioteca biblioteca) {

        System.out.println("Biblioteca virtual\nEsta es una biblioteca donde podra encontrar libros subidos por la comunidad y descargarlos de manera gratuita\nIngrese 1 para registrarse\nIngrese 2 para inciar secion");
        System.out.print("Ingrese su opcion: ");
        Scanner dsss = new Scanner(System.in);
        var dsss_ = dsss.nextLine();
        
        
        switch (dsss_) {
            case "1":
                biblioteca.agregar_usuario(admin,biblioteca);
                break;
            case "2":
                biblioteca.iniciar_secion(admin,biblioteca);
                break;
            default:
                System.out.println("Opcion no valida");
                biblioteca.interfaz1(admin,biblioteca);
        }
    
    }


    public void interfaz2(admin admin,usuarios usuarios, biblioteca biblioteca) {

        System.out.println("BIBLIOTECA VIRTUAL");
        System.out.println("Hola, ¿que desea hacer?\n1) Buscar Libro\n2) Subir un libro\n3) Descargar libro\n4) Ver algunos libros disponibles\n5) Cerrar secion");
        System.out.print("Ingrese su opcion: ");
        Scanner dss = new Scanner(System.in);
        var dss_ = dss.nextLine();

        switch (dss_) {
            case "1":
                biblioteca.buscar_libro(0,admin,usuarios,biblioteca);
                break;
            case "2":
                usuarios.subir_libro(0,admin,usuarios, biblioteca);
                break;
            case "3":
                usuarios.descargar_libro(0,admin,usuarios, biblioteca);
                break;
            case "5":
                biblioteca.interfaz1(admin,biblioteca);
                break;
            case "4":
                biblioteca.ver_libros(0,admin,usuarios,biblioteca);
                break;
            default:
                System.out.println("Opcion no valida");
                biblioteca.interfaz2(admin,usuarios, biblioteca);
        }
    
    
    
    }

    public void interfazAdmin(admin Alejo,usuarios usuarios, biblioteca biblioteca) {

        System.out.println("BIBLIOTECA VIRTUAL --Admin--");
        System.out.println("Hola, ¿que desea hacer?\n1) Buscar Libro\n2) Subir un libro\n3) Descargar libro\n4) Ver algunos libros disponibles\n5) Cerrar secion\n6) Apagar pagina");
        System.out.print("Ingrese su opcion: ");
        Scanner ds = new Scanner(System.in);
        var ds_ = ds.nextLine();

        switch (ds_) {
            case "1":
                biblioteca.buscar_libro(1,Alejo,Alejo, biblioteca);
                break;
            case "2":
                Alejo.subir_libro(1,Alejo,usuarios,biblioteca);
                break;
            case "3":
                Alejo.descargar_libro(1,Alejo,usuarios, biblioteca);
                break;
            case "4":
                biblioteca.interfaz1(Alejo,biblioteca);
                break;
            case "5":
                biblioteca.ver_libros(1,Alejo,usuarios,biblioteca);
                break;
            case "6":
                Alejo.cerrar_pagina();
                break;
            default:
                System.out.println("Opcion no valida");
                biblioteca.interfazAdmin(Alejo,usuarios, biblioteca);
        }

    }


    public void iniciar_secion(admin admin, biblioteca biblioteca) {

        System.out.println("INICIAR SECION");

        System.out.print("Ingrese su identificacion: ");
        Scanner idr = new Scanner(System.in);
        var idr_ = idr.nextLine();
        var IDs = new ArrayList<String>();
        for (var usuario__: biblioteca.Usuarioss) {
            IDs.add(usuario__.identificacion);
        }

        if (idr_.equals(admin.identificacion)) {
            biblioteca.interfazAdmin(admin,admin, biblioteca);
        } else if (IDs.contains(idr_)) {
            var idx = IDs.indexOf(idr_);
            biblioteca.interfaz2(admin,biblioteca.Usuarioss.get(idx), biblioteca);
        } else {
            System.out.println("Usted no se ha registrado");
        }
    }


    public void agregar_usuario(admin admin,biblioteca biblioteca) {
        System.out.println("REGISTRARSE");
        System.out.print("Ingrese su nombre: ");
        Scanner nm = new Scanner(System.in);
        var nm_ = nm.nextLine();

        System.out.print("Ingrese su identificacion: ");
        Scanner id = new Scanner(System.in);
        var id_ = id.nextLine();

        var IDss = new ArrayList<String>();
        for (var usuario__: biblioteca.Usuarioss) {
            IDss.add(usuario__.identificacion);

        }
        if (IDss.contains(id_)) {
            System.out.println("Este usuario ya esta registrado");
            biblioteca.interfaz1(admin,biblioteca);
        }
        var nuevo_usuario = new usuarios(nm_,id_);
        biblioteca.Usuarioss.add(nuevo_usuario);
        biblioteca.interfaz1(admin, biblioteca);
    }


    public void buscar_libro(int b,admin admin,usuarios usuarios, biblioteca biblioteca) {

        System.out.println("BUSCAR LIBRO");
        System.out.print("Ingrese alguna referencia del libro (nombre, autor, genero, codigo): ");
        Scanner buscar = new Scanner(System.in);
        var buscar_ = buscar.nextLine();
        var a=biblioteca.Libross.size();
        var bl = 0;
        for (var libro: biblioteca.Libross) {
            if (buscar_.equals(libro.titulo) || buscar_.equals(libro.autor) || buscar_.equals(libro.genero) || buscar_.equals(libro.codigo)) {
                System.out.println("-----------------------------------------------------------------------------------------------------");
                System.out.println(String.format("Nombre: %s\nAutor: %s\nGenero: %s\nCodigo: %s", libro.titulo,libro.autor,libro.genero,libro.codigo));
                System.out.println("-----------------------------------------------------------------------------------------------------");
                bl+=1;
                a-=1;
            } else {
                a-=1;
            }

            if (a<=0) {
                if (bl==0) {
                    System.out.println("Libro no encontrado. Por el momento no esta disponible o trate de escribir el nombre correctamente");
                }
                if (b==1) {
                    biblioteca.interfazAdmin(admin, usuarios, biblioteca);
                } else {
                    biblioteca.interfaz2(admin, usuarios, biblioteca);
                }
            }
        }
    }






    public void ver_libros(int v,admin admin,usuarios usuarios,biblioteca biblioteca) {

        System.out.println("Algunos de los libros disponibles son: ");
        System.out.println("Nombre ---- Autor ---- Genero ---- Codigo");
        if (biblioteca.Libross.size()<10) {
            for (var lbo: biblioteca.Libross) {
                System.out.println("-----------------------------------------------------------------------------------------------------");
                System.out.println(String.format("%s -- %s -- %s -- %s", lbo.titulo,lbo.autor,lbo.genero,lbo.codigo));
                System.out.println("-----------------------------------------------------------------------------------------------------");
            }
        } else {
            var ListaCopialibros = new ArrayList<>(biblioteca.Libross);
            Collections.shuffle(ListaCopialibros);
            var librosRandom = ListaCopialibros.subList(0, (int) biblioteca.Libross.size()/2);

            for (var libro_i_:librosRandom) {
                System.out.println("-----------------------------------------------------------------------------------------------------");
                System.out.println(String.format("%s -- %s -- %s -- %s", libro_i_.titulo,libro_i_.autor,libro_i_.genero,libro_i_.codigo));
                System.out.println("-----------------------------------------------------------------------------------------------------");
            }

        }
        if (v==1) {
            biblioteca.interfazAdmin(admin, usuarios, biblioteca);
        } else {
            biblioteca.interfaz2(admin, usuarios, biblioteca);
        }
    }
}


