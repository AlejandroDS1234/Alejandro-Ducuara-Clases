#include <iostream>

int main() {//clase principal
    /*
    std::cout<<"Hola\n"<<std::endl;// imprimir cosas y salto de linea
    std::cout<<"arroz"<<'\n';
    std::cout<<"rico"; //otra forma de salto de linea

    */




    // variables
     
    int algo;// se declara la variable con el tipo
    algo = 451;// se le da valor a la variable

    //pasos juntos

    int cosa = 39;

    std::cout<<algo;

    int decimal = 12.5; //si en una variable int se almacena un float entonces solo se tomara la parte entera del float


    double decimaltr = 14.8; //decimal hasta 15 decimales 64 bits
    float decimalvr = 14.89; //decimal hasta 7 decimales 32 bist

    char caracter = 'b'; //solo un caracter, se tienen que usar comillas simples
    
    bool logico = true; //verdadero o falso


    //string

    std::string frase = "esto es un string";
    
    //concatenar en strings con variables

    std::cout<<"hola, "<<frase;
    return 0;
}