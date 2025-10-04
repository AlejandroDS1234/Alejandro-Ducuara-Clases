function numero() {
    document.getElementById("operador").innerText = "  "
    document.getElementById("res").innerText = ""
    document.getElementById("res2").innerText = ""
    let num1=parseFloat(document.getElementById("num1").value)
    let num2=parseFloat(document.getElementById("num2").value)
    return {num1, num2}
}
function suma() {
    let {num1, num2}=numero()
    let tres=num1+num2
    
    if (isNaN(tres)) {
        holamundo(2)
    } else {
        document.getElementById("operador").innerText = "+"
        document.getElementById("res").innerText = `Resultado suma: ${tres}`
    }
}
function multiplicacion() {
    let {num1, num2}=numero()
    let cuatro=num1*num2
    
    if (isNaN(cuatro)) {
        holamundo()
    } else {
        document.getElementById("operador").innerText = "x"
        document.getElementById("res").innerText = `Resultado multiplicación: ${cuatro}`
    }
}
function restar() {
    let {num1, num2}=numero()
    let cinco=num1-num2
    
    if (isNaN(cinco)) {
        holamundo()
    } else {
        document.getElementById("operador").innerText = "-"
        document.getElementById("res").innerText = `Resultado resta: ${cinco}`            
    }
}
function raiz() {
    let {num1, num2}=numero()
    let raiznum1=num1**0.5
    let raiznum2=num2**0.5
    
    let a=false
    let b=false
    
    !isNaN(raiznum1) ? document.getElementById("res").innerText=`Raiz de ${num1}: ${raiznum1}` : a = true
    
    !isNaN(raiznum2) ? document.getElementById("res2").innerText=`Raiz de ${num2}: ${raiznum2}` : b = true
    
    a && b ? holamundo(2) : a=true
}

function holamundo(num) {
    if (num==1) {
        document.getElementById("res").innerText = "Hola mundo"
    } else {
        document.getElementById("res").innerText = "Ingrese un numero"
    }
}