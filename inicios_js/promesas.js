// Es un objeto que representa la culminacion de exito o error de una operacion asincrona
async function ejecucion() {
  console.log("Sumar");
  console.log("Restar");

  const promesa = new Promise((resolve, reject) => {
      setTimeout(() => {
          reject(new Error("Error al guardar el registro en la base de datos"));
      }, 5000);
  });

  // then > sirve para indicar si la promesa se ejecuto exitosamente osea termino sin problemas
  // eatch > sirve para indicar si fallo la ejecucion de la promesa
  // promesa
  //   .then()

  try {
    const respuesta = await promesa;
    console.log(respuesta);
  } catch (error) {
    console.error("Error al ejecutar la promesa");
    console.error()
  }
  }

  //const respuesta = await promesa;
  //console.log(respuesta);
  //console.log("FINALIZADO!");
//}

ejecucion();