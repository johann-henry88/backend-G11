class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print('Buenos dias')

class Beneficios:

    def mostrar_beneficios(self):
        return {
            'detalle': self.detalle
        }

class Alumno(Persona):
    def __init__(self, nombre, apellido, grado):
        self.grado = grado
        super().__init__(nombre, apellido)

    def saludar(self):

        saludo_padre = super().saludar()
        print(saludo_padre + 'Yo soy un alumno')

    def dar_vueltas(self):
        print('Dando vueltas. . .')

class Docente(Persona, Beneficios):
    def __init__(self, nombre, apellido, seguro_social, detalle):
        self.seguro_social = seguro_social
        Persona.__init__(self, nombre, apellido)
        Beneficios.__init__(self, detalle)

    def evaluar(self):
        print('Evaluando. . .')

johann = Alumno('Johann', 'Mora', 'Jiménez')
paolo = Docente('paolo', 'soncco', '15982254')

johann.saludar()
print(paolo.saludar())

print(paolo.mostrar_beneficios())
print(johann.nombre)