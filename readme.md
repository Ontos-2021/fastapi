# Proyecto de FastAPI con Python y uvicorn

Este proyecto es parte de mi curso de [Fast APi](https://platzi.com/cursos/fastapi/) en [Platzi](https://platzi.com/) sobre FastAPI con Python. En este curso, estoy aprendiendo a crear APIs rápidas y modernas utilizando FastAPI, un marco web de Python que facilita la creación de APIs RESTful de alto rendimiento.

## Descripción

En este proyecto, estoy explorando las características y funcionalidades de FastAPI, junto con la herramienta uvicorn para ejecutar la aplicación web. FastAPI es conocido por su velocidad y facilidad de uso, lo que lo convierte en una elección popular para el desarrollo de APIs en Python.

## Ejemplos de Código

A continuación, se presentan algunos ejemplos de código para ilustrar cómo utilizar FastAPI junto con uvicorn:

### Instalación

Puedes instalar FastAPI y uvicorn utilizando pip:

```bash
pip install fastapi uvicorn
```

### Creación de una aplicación básica

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}
```

### Ejecución de la aplicación con uvicorn

```bash
uvicorn main:app --reload
```

Esto ejecutará tu aplicación FastAPI en un servidor local y habilitará la recarga automática para facilitar el desarrollo.

### Rutas y parámetros

FastAPI hace que sea fácil definir rutas y manejar parámetros en las solicitudes. Por ejemplo:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
```

En esta ruta, `item_id` es un parámetro de ruta y `query_param` es un parámetro de consulta opcional.

## Uso

Para utilizar este proyecto, sigue estos pasos:

1. Clona este repositorio en tu máquina local.

```bash
git clone https://github.com/tu-usuario/tu-proyecto.git
```

2. Instala las dependencias necesarias utilizando pip.

```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación utilizando uvicorn.

```bash
uvicorn main:app --reload
```

4. Accede a la API en tu navegador 
