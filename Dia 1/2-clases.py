class Persona:
    estatura = 1.65
    peso = 80
    signo_zodiacal = 'ACUARIO'

    def sumar(self, *args):

        total= 0
        for numero in args:
            total = total + numero
        return total

    def saludar(self, nombre):

        return 'Hola {}'.format(nombre)
# Cuando sacamos una 'copia' de la clase para utilizarla estamos creando una instancia
persona1 = Persona()
persona2 = Persona()

# Modifico los atributos de esa persona en particular
persona1.peso = 70
persona2.peso = 50

print(persona1.peso)
print(persona2.peso)

resultado1 = persona1.sumar(10, 5, 41, 526, 489, 63)
resultado2 = persona2.sumar(5, 8, 65, 985, 492, 520, 700)

print(resultado1)
print(resultado2)