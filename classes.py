class vehiculo:
    def __init__(self, color, placa, marca) -> None:
        self.color = color
        self.placa = placa
        self.marca = marca

    def verificarEstado(self, fabricacion):
        return f'El vehiculo de color {self.color} fue fabricado en el año: {fabricacion}'

    def concatenarCaracteristicas(self):
        return f'Vehiculo con placa {self.placa}, de color {self.color} es de marca: {self.marca}'
        

vehiculo = vehiculo("rojo", "V21-543", "Honda")

#print(vehiculo.verificarEstado(1999))
#print(vehiculo.concatenarCaracteristicas())

class Alumno:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

    def mostrarNombre(self):
        return self.nombre

    def mostrarEdad(self):
        return self.edad

x = Alumno('Johann', 35)

print(x.mostrarNombre())

