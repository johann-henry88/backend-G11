const { restar, sumar, secreto } = require("./funciones.cjs");

console.log('Hola Mundo');
const nombre = "Johann";

function saludar() {
    console.log("Buenas noches");
}

saludar();

const resultado = restar(10, 5);
console.log(resultado)