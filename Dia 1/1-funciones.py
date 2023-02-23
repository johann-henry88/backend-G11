def dividir(dividiendo, divisor):
    # si la division da un error entonces retornar un mensaje que diga 'division incorrecta'
    try:
        resultado = dividiendo / divisor
        return resultado
    except ZeroDivisionError:
        # aqui ingresara cuando la division sea entre 0
        return 'No puede haber division entre 0'

    except TypeError:
        # ingresara si la division tiene algun caracter 
        return 'Las divisiones solamente pueden ser entre numeros'

    except:
        # ingresara si no es ninguno de los errores anteriores
        return 'Error desconocido'

valor = dividir(10, 5)
print(valor)

valor = dividir(10, 0)
print(valor)

valor = dividir('a', 'h')
print(valor)

try:
   valor = dividir(5,)
   print(valor)
except TypeError:
    print('Estuvo mal llamada la funcion') 
