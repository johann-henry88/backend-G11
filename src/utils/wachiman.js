import jwt from "jsonwebtoken";
import { Prisma } from "../prisma.js";

// next > si todo esta correcto al momento de llamar al next este hara la invocacion al otro controlador, este puede ser el controlador final u otro middelware

export const validarToken = async (req, res, next) => {
    // valido que tenga el header de authorization
    if (!req.headers.authorization) {
        return res.status(401).json({
            message: "Se necesita una token para realizar esta peticion",
        });
    }
    // Bearer xxxxx.xxxxxx.xxxxx
    // ahora divido el texto mediante un spacio para separar la palabra Bearer y la token
  const token = req.headers.authorization.split(" ")[1];

  // si la token no existe, retorno un error
  if (!token) {
    return res.status(401).json({
      message: "El formato debe ser Bearer YOUR_TOKEN",
    });
  }

  try {
    // verifico la autenticidad de la token, que tenga tiempo de vida, que sea una token valida
    const payload = jwt.verify(token, process.env.JWT_SECRET);

    // findUniqueOrThrow > emitira un error de not found si el usuario no existe
    const usuarioEncontrado = await Prisma.usuario.findUniqueOrThrow({
      where: { id: payload.jti },
    });

    // pasar al siguiente middleware o controlador
    next();
  } catch (error) {
    // si la token es incorrecta ingresara al catch y/o si el usuario no existe
    return res.status(400).json({
      message: "Error",
      content: error.message,
    });
  }
};