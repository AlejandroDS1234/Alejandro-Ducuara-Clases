package biblioteca_java;

public class admin extends usuarios {
    public admin() {
        super("Alejo", "123321");
    }
    

    public void cerrar_pagina() {
        System.out.println("Cerrando");
        System.exit(0);
    }
}