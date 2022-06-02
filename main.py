from fastapi import FastAPI
import uvicorn
#se importan rutas
from routes.tren import tren
from routes.admin import admin
from routes.estaciones import estaciones
from routes.lineas import linea

#se instancia fastapi 
app = FastAPI(title="Api [nombre app]",
  description="this is a REST API using fastapi and mongodb",
  version="0.0.1"
)

#se incuyen las rutas en la instancia de fastapi
app.include_router(tren)
app.include_router(admin)
app.include_router(estaciones)
app.include_router(linea)

#se crea la pagina inicial de la app
@app.get("/")
async def read_root():
  return {"Hello": "World"}

if __name__ == "__main__":
  #se corre el servidor de fastapi utilizando uvicorn
  #se utiliza en modo local
  #0.0.0.0 se utiliza para ejecutar en publico y reload en false
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


#
#hacer que se puedan buscar estaciones intermedias en las listas de las lineas probablemente quick sort????
#añadir a base de datos los vagones
#