import { Prisma } from "../prisma.js";

export const crearProducto = async (req, res) => {
    const data = req.body;
// TODO:
    const categoria = await Prisma.categoria.findFirst({
        where: { id: data.categoriaId },
        select: { id: true },
    });

    if(!categoria) {
        return res.status(400).json({
            message: "Categoria no existe",
        });
    }
    try {
        const nuevoProducto = await Prisma.producto.create({
          data: {
              ...data,
              fechaVencimiento: new Date(data.fechaVencimiento),
            },    
        });
        return res.status(201).json({
          message: "Producto creado exitosamente",
          content: nuevoProducto,
        });
    } catch (error) {
        return res.status(400).json({
            message: "Error al crear el producto",
            content: error.message,
        });
    }
};

export const listarProductos = async (req,res) => {
    // TODO: agregar el listar productos
};

export const devolverProducto = async (req, res) => {
    const { id } = req.params;

    const productoEncontrado = await Prisma.producto.findFirst({
        where: { id: +id },
        include: { categoria: true },
    });

    if (!productoEncontrado) {
        return res.status(400).json({
            message: "El producto no existe",
        });
    }

    return res.json({
        content: productoEncontrado,
    });
};

export const actualizarProducto = async (req, res) => {
    
}


