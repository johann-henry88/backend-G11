from pprint import pprint

class Operaciones:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def suma(self):
        return self.a + self.b
    def resta(self):
        return self.a - self.b
    def multiplicacion (self):
        return self.a * self.b
    def division (self):
        return self.a / self.b

Operaciones = Operaciones(9, 3)

#print(Operaciones.suma())
#print(Operaciones.resta())
#print(Operaciones.multiplicacion())
#print(Operaciones.division())


class OperacionesMatematicas:

    def __init__(self, valor_1, valor_2):
        self.a = valor_1
        self.b = valor_2

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        return self.a / self.b

    def __redondear(self, numero):
        return round(numero, 2)

operaciones = OperacionesMatematicas(5, 3)

#print(operaciones.multiplicar())


class Usuario:

    def __init__(self, nombre, edad, dni, estatura, estado_civil) :
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.estatura = estatura
        self.estado_civil = estado_civil

    def convertirDiccionario(self):
        return {
            'nombre': self.nombre,
            'edad' : self.edad,
            'dni' : self.dni,
            'estatura' : self.estatura,
            'estado_civil': self.estado_civil
        }

Usuario = Usuario('Johann', 35, 45240027, 1.65, 'soltero')

pprint(Usuario.convertirDiccionario())
        
        



