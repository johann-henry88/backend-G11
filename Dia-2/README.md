# Entorno virtuales python

## Crear un entorno virtual

```
python -m venv venv
```

## Activar el entorno virtual

```
venv\Scripts\activate
```

## Desactivar el entorno virtual

```
deactivate
```

# Flask

## Instalar Flask

```
pip install Flask
```

# Verificar que flask se haya instalado

```
pip freeze
```

## Listar las librerias en el archivo
`requirements.txt`

```
pip freeze > requirements.txt
```

## instalar las librerias que están listado en nuestro requirements.txt

```
pip install -r requirements.txt
```