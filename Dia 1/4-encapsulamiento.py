class Producto:

    def __init__(self, nombre, precio, cantidad, fecha_vencimiento) :
        self.nonbre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_vencimiento = fecha_vencimiento
        self.__ganancia = 0.3

    pitahaya = Producto('pitahaya')
        