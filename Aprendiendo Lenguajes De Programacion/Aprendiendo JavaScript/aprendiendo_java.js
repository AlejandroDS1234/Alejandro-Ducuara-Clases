/*
//imprimir

console.log("Hola, esto se imprimirá en la consola.")
console.log(0)

//variables

var varible = "esta es mi variable :)"//definirla

varible="sigue siendo"//cambiarle el valor

//formas mejores de declarar variables (let, const)

//let

let variablelet = "variable con let"//las let solo funcionan dentro de un bloque de codigo

//const

const variableconst  = "variable con const "//no se le puede reasignar el valor







//Tipos de datos

//strings

let frase = "esta es mi frase"

//enteros

let numero=1
let numeroDecimal=2.2

//Booleanos

let verdad=true
let falso=false

// undefined

let undefinedValue //valores todavia no definidos
console.log(undefinedValue)

//null

let nullValue=null


//Symbol

let simbolo=Symbol('misimbolo') //identificadores de propiedades

//BigInt

let numeromuygrande=BigInt(98760489056098640984580990840940984096958640895409)

//mostrar tipos de datos

console.log(typeof simbolo)
console.log(typeof frase) 













//operadores

//aritmeticos
j=5
console.log(1+2)
console.log(1-2)
console.log(1*2)
console.log(1/2)
console.log(1%2)
console.log(1**2)
console.log(j++)//para sumar 1
console.log(j--)//para restar 1

//operadores de asignacion

let miasignacio ="asignar"

miasignacio+="hola"

//operadores de comparacion
a=2
b=3
console.log(a>b)
console.log(a<b)
console.log(a>=b)
console.log(a>=b)
console.log(a==b)//igualdad por valor
console.log(a=="2") //java detecta el numero en la cadena de texto
console.log(a === b) //igualdad por tipo y valor
console.log(a==="2")
console.log(a!=b)
console.log(a!==b)
console.log(0==false)//0 es falso
console.log(1==true)//1 es verdadero
console.log(0=="")

//valores falsos

    // 0
    // 0n
    // null
    // undefined
    // NaN
    // false
    // strings vacios



//and &&
console.log(1>2 && 3<9)

//or ||
console.log(1>0 || 5<1)

//not !
console.log(!(1>2))//lo contrario, lo esta negando 



//operadores ternarios (como un if pero no es)

const opcion=true

opcion ? console.log("esto es verdad") : console.log("Esto es faalso")
//variable ? opcion si es verdad : opcion si es falso

















//Strtings

//concatenar
let hola="hola"
let completo= "pepito, "+hola

//longitud
console.log(completo.length)

//extracion de caracteres

console.log(completo[2])

//Metodos comunes
console.log(completo.toLocaleUpperCase())//poner en mayuscula
console.log(completo.toLowerCase())//poner en minuscula
console.log(completo.indexOf("pi"))//mirar el indice de una frase
console.log(completo.includes("jose"))//mirar si incluye
console.log(completo.slice(2,6))//para traer una porte del texto
console.log(completo.replace("hola", "adios"))//remplazar una palabra por otra

//poner texto en dos lineas

let mensaje=`hoa
pepito, lo logramoooooos!!!! \n(alt 96 o la del debajo de esc)`
console.log(mensaje)

//fstring d
console.log(`mensaje: ${mensaje}`)













//condicionales

//if  

let numero=2

if (numero==3) {
    console.log("El numero es 3")

}else if(numero==2){
    console.log("El numero es 2")
}else {
    console.log("es otro numero")
}

//operadores ternarios

numero==3 ? cconsole.log("Es 3") : console.log("Es otro numero")

let texto = numero==3 ? "es 3" : "es otro numero" //ejemplo de asignar una variable con un if
console.log(texto)


//switch //comparar una variable en muchos casos

let num=2

switch (num) {
    case 1:
        console.log("es uno")
        break
    case 2:
        console.log("Es dos")
        break
    default:
        console.log("Otro numero")
    
}












//Estructuras de datos

//array //como una lista

let arraynuevo = [1,2,3,4,"hola"] //por corchetes //acepta diferentes tipos de datos

let otroarray= new Array("hola") //array
console.log(otroarray)
console.log(arraynuevo)

arraynuevo[0]="hola" //se puede acceder al elemento con el indice y modificarlo
console.log(arraynuevo)

//metodos comunes 

//push para agragar elementos

otroarray.push("como")
otroarray.push("estas")
otroarray.push("mi")
otroarray.push("tipo")
otroarray.push("querido")
console.log(otroarray)

//pop
otroarray.pop()//elimina el ultimo elemento que se agrego
otroarray.pop("hola") //eliminar elemento en concreto
console.log(otroarray)

//shift 
otroarray.shift()
console.log(otroarray.shift())//elimina el primer elemento
console.log(otroarray)


//unshift
otroarray.unshift("uno", "dos")//agreegar elementos al inicio
otroarray.unshift("cero")
console.log(otroarray)

//length
console.log(otroarray.length)//el largo del array

//borrar el contenido de un arrray

//      otroarray = []
//      otroarray.length = 0

//slice //otro array de unos elementos de un array

let otrooarray = otroarray.slice(0,3)
console.log(otrooarray)

//splice

otroarray.splice(0,2) //elimina ese rango de elementos
otroarray.splice(0,2, "algo") //agrega otro elemento despues de borrar (al inicio)
console.log(otroarray)

*/




//sets

let unset= new Set([1,2,3, "uno", "dos", "tres"]) //tiene que ir entre corchetes para que agarre todos los lados
console.log(unset)

//dividir el texto
let cososet= new Set("holos")
console.log(cososet)