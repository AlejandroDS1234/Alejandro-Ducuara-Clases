
/* 
public class helloWorld{
    public static void main(String[] args) { // es una funcion que se llama args
        System.out.println(1+1);//imprimir 1+1
        System.out.println("Hola\nmundo"); // imprimir hola mundoaa
    }
}

*/

// Variables

public class Aprendiendo_java {//La clase publica debe llamarse igual que el archivo

    public static void main(String[] args) {
        /* 
        String name = "Alejandro";  //definir de que tipo es la variable, se define nombre, valor
        
        System.out.println(name);

        name="Ducuara"; //re asignar el valor

        //int name = 3; no deja poner otro valor que no sea el tipo que se le definio


        int num = 12; //numero
        System.out.println(num);
        System.out.println(name);



        // Constantes (Que no varie)

        final String CORREO = "Alejandor@gmail.com";
        System.out.println(CORREO);
        // crear vaariable

        var email = "Hola"; // java detecta de que tipo es la variable automaticamente
        System.out.println(email);



        double decimal=3.14; //double es para decimales
        System.out.println(decimal);

        // float, long, byte
        
        char caracter = 'a'; // char es para 1 solo caracter, se usa con comillas simples
        System.out.println(caracter);


        boolean logico = true; //para un dato de tipo logico verdadero o falso
        System.out.println(logico);


        // conocer el tipo de dato  // se pueden conocer cuando el tipo de dato es una clase
        System.out.println(name.getClass().getSimpleName()); //getClass: obtiene los datos de la clase     //getSimpleName: obtiene el nombre simple

        */

























        //Operadores aritmeticos
        /* 
        double a =4;
        var b =3;
        double c= a/b;

        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
        System.out.println(c); //si los numeros de la variable donde se origina son int entoces su re4sultado tambien va a ser int



        // Operadores de asignacion

        a = b * 2;
        a+=1;
        System.out.println(a);



        // Operadores de coparacion

        System.out.println(a==b);
        System.out.println(a>=b);
        System.out.println(a<=b);
        System.out.println(a!=b);





        //Operadores logicos combinaciones

        // and

        System.out.println(true && true);// verdadero * verdadero y asi
        System.out.println(false && true);
        System.out.println(true && false);
        System.out.println(false && false); 



        // or

        System.out.println(true || true); // verdadero o verdadero y asi
        System.out.println(false || true);
        System.out.println(true || false);
        System.out.println(false || false); 




        // not
        System.out.println(!true); // verdadero o verdadero y asi
        System.out.println(!false);
        System.out.println(!true);
        System.out.println(!false); 

        //Unarios (negativos y positivos)

        var w = 45;
        System.out.println(-w);


        */


















/* 

        // Cadenas de texto

        String caracoles = "Jose";
        var papaletas = "Mario";


        //concatenacion
        System.out.println(caracoles+" "+papaletas);

        //Longitud del texto
        System.out.println(papaletas.length());//Para tener la longitud del str

        //Extraccion 1 caracter
        System.out.println(caracoles.charAt(caracoles.length()-1));

        //Extraer frase

        var frase = "L sabias que al dios de la muerte le encantas las manzanas";
        System.out.println(frase.substring(2,8));


        // Mayusculas y minusculas

        System.out.println(papaletas.toLowerCase()); //minusculas
        System.out.println(papaletas.toUpperCase()); //mayusculas


        // Saber si contiene algo

        System.out.println(caracoles.contains("churro")); 


        // Comparar strings

        System.out.println(caracoles.equals(papaletas));
        System.out.println(caracoles.equalsIgnoreCase("Jose")); //Para comparar sin tener en cuenta las mayusculas o minusculas


        // Borrar o remplazar


        //Eliminar espacios al inicio y al final
        System.out.println(" Hola mucho gusto       ".trim());//Elimina el espacio al inicio y al final

        // Remplazar
        System.out.println(" Hola mucho gusto       ".replace(" ", "_"));//caracter antiguao y caracter nuevo


        //format -- interpolacion


        var edad = 56;
        var pacheco = "Nombre";
        System.out.println(String.format("Hola, %s, tengo %d ",pacheco,edad)); // remplaza los simbolos por las variables que se le den %s para strings, %d enteros, %f para decimales



*/





















/* 
        //Condicionales

        // if

        var num1 = 14;
        var num2 = 18;

        if (num1>num2) {
            System.out.println(String.format("El numero %d es mayor que el %d", num1, num2));
        } else if (num1<num2) {// elif
            System.out.println(String.format("El numero %d es mayor que el %d", num2, num1));
        } else {
            System.out.println("Los numeros son iguales");
        }



        // switch condicon -- revisar el valor de una variable -- Sigue revisando casos logicos aunque se cumpla el primero



        var mes = 1;

        switch (mes) {
            case 1:
                System.out.println("Enero");
                break; // para romper con la revision de las demas condiciones
            case 2:
                System.out.println("Febrero");
                break;
            default:
                System.out.println("Me dio pereza poner los demas meses");

        }


*/
















/* 

        // Estructuras de datos -- listas -- arrays -- sets -- maps
        

        //Arrays --almacena multiples valores del mismo tipo indexados -- Tiene una longitud especificada

        int[] Numeros = new int[3];//Solo tiene espacio para 3 valores
        System.out.println(Numeros);


        //acceder a los datos

        String[] Nombres = {"Jose", "Antonio", "Josefo"};
        System.out.println(Nombres[0]);

        //meter datos
        Numeros[0] = 1;
        System.out.println(Numeros[0]);

        // En los arrays no se pueden eliminar datos




        //LIstas

        ArrayList<String> frutas = new ArrayList<>();


        System.out.println(frutas);

        //listas de numeros enteros --

        var cantidad = new ArrayList<Integer>(); //Intenger para definir una lista de numeros enteros
        
        System.out.println(cantidad.size()); //size para ver la cantidad de elementos en una lista


        //Añadir elemntos

        frutas.add("Fresa"); //añadir elementos
        frutas.add("Guayaba");
        System.out.println(frutas.get(frutas.size()-1)); //.get() acceder a un elemento


        //MOdificar elementos

        frutas.set(0, "Agria");
        System.out.println(frutas);

        //Eliminar elementos

        frutas.remove(1);
        System.out.println(frutas);

        // Buscar elemento

        frutas.add("gato");
        System.out.println(frutas.contains("gato"));


        //Limpiar lista
        cantidad.add(2);

        cantidad.clear();
        System.out.println(cantidad);









        // Sets almacena datos unicos

        HashSet<String> animales = new HashSet<>();
        
        //tamaño
        System.out.println(animales.size());

        //añadir elementos
        animales.add("Pinguino");
        animales.add("foca");
        animales.add("Pinguino");

        //En los sets no se pueden acceder a los elementos ya que no tiene orden

        // se pueden usar las mismas funciones que en la lista con las excepciones

        System.out.println(animales);








        // Maps -- Diccionario

        HashMap<String, Integer> frutasCantidad= new HashMap<>();

        //tamaño
        System.out.println(frutasCantidad.size());

        //Añadir elementos

        frutasCantidad.put("Fresa", 20);
        frutasCantidad.put("Guayaba", 3);
        frutasCantidad.put("sandia", 1);
        frutasCantidad.put("Melon", 2);
        System.out.println(frutasCantidad);

        //acceder elementos

        System.out.println(frutasCantidad.get("Fresa"));
        //System.out.println(frutasCantidad.get());

        //verificar si contiene elementos

        System.out.println(frutasCantidad.containsKey("Melon"));//clave
        System.out.println(frutasCantidad.containsValue(2));//valor

        //eliminar

        frutasCantidad.remove("Guayaba");
        System.out.println(frutasCantidad);

        //Modificar

        frutasCantidad.put("sandia", 5);//al hacer un put con un valor ya existente lo que hace es reemplazar la informacion

        System.out.println(frutasCantidad);


        //modificar solo si existe
        frutasCantidad.replace("Melon", 40);//Para remplazar solo si el valor existe

        System.out.println(frutasCantidad);


        //añadir solo si no existe
        frutasCantidad.putIfAbsent("Maracuya", 9);
        System.out.println(frutasCantidad);

*/




















/* 

        //Bucles

        //for

        for (int i = 0; i<5; i+=1 ) { //se indica un contador, desde donde comienza y hasta cuando se termina, y que pasa cuando cambie (el ++ es para sumar de a 1)
            System.out.println(":(");

        }

        var algo =new ArrayList<String>();
        algo.add("mesa");
        algo.add("silla");
        algo.add("plato");
        algo.add("cuchara");
        System.out.println(algo.size());
        for (int o=0; o<algo.size(); o+=1) {
            //System.out.println(o);
            System.out.println(algo.get(o));


        }



        //forEach -- para recorrer un iterable

        for (String cosa: algo) {

            System.out.println(cosa);
        }




        // while / do while

        var dia = 0;

        while (dia<5) {

            System.out.println(dia+1);
            dia+=1;
        }

        // do while -- para ejecutar si o si la primera vez y el resto si cumple la condicion
        var p = 5;
        do { 
            System.out.println("Hola");
            p-=1;
            
        } while (p > 0);


        // control de bucles
        //break

        for (String cosa: algo) {

            System.out.println(cosa);
            if (cosa.equals("silla")) {
                System.out.println("Sentado");
                break;
            }
        }

        //continue
        for (String cosa: algo) {

           
            if (cosa.equals("silla")) {
                System.out.println("Sentado");
                continue;
            }
             System.out.println(cosa);
        }





*/







        //funciones

        // funciones sin parametro ni retorno



        for (int q=0; q<5; q+=1) {
            AlgoFuncion();
        }

        AlgoFuncion();
        AlgoFuncionParametro("Pepito");
        AlgoFuncionParametro("Pepito", "si");
        System.out.println(DosMasDos());

        System.out.println(3+DosMasDos());

    }

    //como definir
    //modificador: publica o privada o clase  //publica: que se puede acceder desde cualquier parte del codigo
    //que nos quiere retornar la funcion: si o va a retornar nada se le pone void

    //funcion sin parametro ni retorno
    public static void AlgoFuncion() { //no se pueden llamar funciones dentro de una funcion static como la del inicio, para hacerlo la funcion tambien debe ser static
        System.out.println("Algo");
        
    }//linea 574

    //Funciones con parametro sobrecarga

    public static void AlgoFuncionParametro(String persona) {

        System.out.println(String.format("Hola %s", persona));
    }//linea 575

    //sobrecarga

    public static void AlgoFuncionParametro(String persona, String gusto) { //se pueden poner 2 funciones con el mismo nombre pero con la cantidad de requerimientos diferente y asi se le puede poner de a 1 requerimiento

        System.out.println(String.format("Hola %s que %s gusta la piña", persona, gusto));
    }//linea 576




    //funciones con retorno

    public static Integer DosMasDos() {    //la sobrecarga de funciones no funciona si se cambia el retorno

        var ala=2+2;

        return ala;// los return van al final
    } //577


    
}
