from fastapi import FastAPI

app = FastAPI()
app.title = "Mi aplicación con FastApi"
app.version = "0.0.1"

from fastapi.responses import HTMLResponse

movies = [
    {
        "id": 1,
        "nombre": "El Padrino",
        "resumen": "La historia de la familia Corleone y su imperio criminal.",
        "categoria": "Drama/Crimen",
        "año": 1972,
        "rating": 9.2
    },
    {
        "id": 2,
        "nombre": "Titanic",
        "resumen": "Un romance trágico a bordo del famoso barco Titanic.",
        "categoria": "Romance/Drama",
        "año": 1997,
        "rating": 7.8
    },
    {
        "id": 3,
        "nombre": "El Señor de los Anillos: La Comunidad del Anillo",
        "resumen": "Una épica aventura en un mundo de fantasía.",
        "categoria": "Fantasía/Aventura",
        "año": 2001,
        "rating": 8.8
    },
    {
        "id": 4,
        "nombre": "Star Wars: Episodio IV - Una Nueva Esperanza",
        "resumen": "La primera entrega de la saga de Star Wars.",
        "categoria": "Ciencia Ficción/Aventura",
        "año": 1977,
        "rating": 8.6
    },
    {
        "id": 5,
        "nombre": "Forrest Gump",
        "resumen": "La vida de Forrest Gump, un hombre con un coeficiente intelectual bajo.",
        "categoria": "Drama/Comedia",
        "año": 1994,
        "rating": 8.8
    }
]

@app.get('/', tags=['Home'])
def mensaje():
    return HTMLResponse('<h1>Hello World! </h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

