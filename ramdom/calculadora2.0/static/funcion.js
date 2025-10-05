let texto=""
let operacion=""

function nuevo(num) {
    if ((texto[texto.length-1]=="+" || texto[texto.length-1]=="-" || texto[texto.length-1]=="x" || texto[texto.length-1]=="÷" || texto[texto.length-1]==".")) {
        if (typeof num == 'number') {
            texto+=num
            document.getElementById("operacion").innerText=texto
            operacion+=num
        }

    } else {
        texto+=num
        document.getElementById("operacion").innerText=texto
        switch(num) {
            case "x":
                operacion+="*"
                break
            case "÷":
                operacion+="/"
                break
            default:
                operacion+=num
        }
    }
    resultado(0)

}
function borrar() {
    document.getElementById("resul").innerText=""
    texto=""
    operacion=""
    document.getElementById("operacion").innerText=texto
}

function eliminar() {
    let borrando=texto.split("")
    borrando.pop()
    let resultadoo=borrando.join("")
    texto=resultadoo
    document.getElementById("operacion").innerText=texto
    
    borrando=operacion.split("")
    borrando.pop()
    borrando=borrando.join("")
    operacion=borrando
    resultado(0)

}
function resultado(num) {
    console.log(operacion)
    if (texto=="") {
        document.getElementById("resul").innerText=" "
        return
    }
    if (num==1) {

    
        if ((texto[texto.length-1]=="+" || texto[texto.length-1]=="-" || texto[texto.length-1]=="x" || texto[texto.length-1]=="÷" || texto[texto.length-1]==".")) {
            eliminar()
        } 
        let resul=eval(operacion)
        document.getElementById("resul").innerText=""
        document.getElementById("resul").innerText+=resul
    } else {
        if ((texto[texto.length-1]=="+" || texto[texto.length-1]=="-" || texto[texto.length-1]=="x" || texto[texto.length-1]=="÷" || texto[texto.length-1]==".")) {
            let eliminado=operacion.slice(0, operacion.length-1)
            console.log(operacion.slice(0, operacion.length-1))
            pp=eval(eliminado)
            document.getElementById("resul").innerText=""
            document.getElementById("resul").innerText=pp
            return
        } 
        let eliminado=eval(operacion)
        document.getElementById("resul").innerText=""
        document.getElementById("resul").innerText=eliminado
    }


}

let op= eval("1+1")
console.log(op)