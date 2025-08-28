package biblioteca_java;

import java.util.ArrayList;
import java.util.Scanner;
import javax.swing.JComponent;

public class biblioteca {

    ArrayList<usuarios> Usuarioss = new ArrayList<>();
    ArrayList<libros> Libross = new ArrayList<>();

    public void interfaz1(biblioteca biblioteca) {

        System.out.println("Biblioteca virtual\\nEsta es una biblioteca donde podra encontrar libros subidos por la comunidad y descargarlos de manera gratuita\\nIngrese 1 para registrarse\\nIngrese 2 para inciar secion");
        System.out.print("Ingrese su opcion: ");
        Scanner dsss = new Scanner(System.in);
        var dsss_ = dsss.nextLine();
        
        
        switch (dsss_) {
            case "1":
                biblioteca.agregar_usuario(biblioteca);
                break;
            case "2":
                biblioteca.iniciar_secion(biblioteca);
                break;
            default:
                System.out.println("Opcion no valida");
                biblioteca.interfaz1(biblioteca);
        }
    
    }


    public void interfaz2(usuarios usuarios, biblioteca biblioteca) {

        System.out.println("BIBLIOTECA VIRTUAL");
        System.out.println("Hola, ¿que desea hacer?\\n1) Buscar Libro\\n2) Subir un libro\\n3) Descargar libro\\n4) Ver algunos libros disponibles\\n5) Cerrar secion");
        System.out.print("Ingrese su opcion: ");
        Scanner dss = new Scanner(System.in);
        var dss_ = dss.nextLine();

        switch (dss_) {
            case "1":
                biblioteca.buscar_libro(usuarios);
                break;
            case "2":
                biblioteca.subir_libro(biblioteca);
                break;
            case "3":
                biblioteca.descargar_libro(biblioteca, usuarios);
                break;
            case "4":
                biblioteca.interfaz1(biblioteca);
                break;
            case "5":
                biblioteca.ver_libros(usuarios);
                break;
            default:
                System.out.println("Opcion no valida");
                biblioteca.interfaz2(usuarios, biblioteca);
        }
    
    
    
    }

    public void interfazAdmin(Admin Alejo, biblioteca biblioteca) {

        System.out.println("BIBLIOTECA VIRTUAL --Admin--");
        System.out.println("Hola, ¿que desea hacer?\\n1) Buscar Libro\\n2) Subir un libro\\n3) Descargar libro\\n4) Ver algunos libros disponibles\\n5) Cerrar secion\\n6) Apagar pagina");
        System.out.print("Ingrese su opcion: ");
        Scanner ds = new Scanner(System.in);
        var ds_ = ds.nextLine();

        switch (ds_) {
            case "1":
                biblioteca.buscar_libro(Alejo);
                break;
            case "2":
                biblioteca.subir_libro(biblioteca);
                break;
            case "3":
                biblioteca.descargar_libro(biblioteca, Alejo);
                break;
            case "4":
                biblioteca.interfaz1(biblioteca);
                break;
            case "5":
                biblioteca.ver_libros(Alejo);
                break;
            case "6":
                Alejo.cerrar_pagina();
                break;
            default:
                System.out.println("Opcion no valida");
                biblioteca.interfazAdmin(Alejo, biblioteca);
        }

    }


    public void iniciar_secion(biblioteca biblioteca) {

        System.out.println("INICIAR SECION");

        System.out.print("Ingrese su identificacion: ");
        Scanner idr = new Scanner(System.in);
        var idr_ = idr.nextLine();
        var IDs = new ArrayList<String>();
        for (var usuario: biblioteca.Usuarioss) {
            IDs.add(usuario.identificacion);
        }

        if (idr.equals(admin.identificacion)) {
            
        }
    }






    
}


