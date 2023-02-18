from pprint import pprint

ciudades = [
    {
        'nombre': 'Tumbes',
        'habitantes': 500000
    },
    {
        'nombre': 'Arequipa',
        'habitantes': 800000
    },
    {
        'nombre': 'Loreto',
        'habitantes': 10000    
    }
]

def miFuncion(ciudad):
    return ciudad['habitantes']

ciudades.sort(key=miFuncion, reverse=True)
ciudades.append({'nombre': 'Cusco', 'habitantes': 20000})

index = 0
for ciudad in ciudades:
    if ciudad['nombre'] == 'Cusco':
        ciudades.remove(ciudad)
    index = index + 1
#pprint(ciudades)

lista = ['Arequipa', 'Cusco', 'Tumbes']
#lista.remove('Arequipa')

for x, y in enumerate(lista):
    print(x, y)

