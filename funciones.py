def suma(a, b):
    resultado = a + b

#resultado_suma = suma(2, 3)
#print(resultado_suma)

def resta (a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

opcion = input('Indicar operacion matematica: ')
print('La operacion que solicito es ' + opcion)


def calcularResultadoPorOperacion(operacion, valor_1, valor_2):
    if operacion == 'suma':
        return f'El resultado de la {operacion} es: {suma(valor_1, valor_2)}'
    elif operacion == 'resta':
        return f'El resultado de la {operacion} es: {resta(valor_1, valor_2)}'
    else:
        return 'La operacion no existe'

operacion = input('Ingrese el tipo de operacion: ')
valor_1 = int(input('Ingrese el primer número: '))
valor_2 = int(input('Ingrese el segundo número: '))

resultado = calcularResultadoPorOperacion(operacion, valor_1, valor_2)

print(resultado)





