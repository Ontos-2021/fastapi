from fastapi import FastAPI

app = FastAPI()
app.title = "Mi aplicación con FastApi"
app.version = "0.0.1"

@app.get('/', tags=['Home'])
def mensaje():
    return "Hola mundo!"
