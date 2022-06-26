from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
#se importan rutas
from routes.tren import tren
from routes.admin import admin
from routes.estaciones import estaciones
from routes.lineas import linea
from routes.recorrido import recorridos
from routes.ticket import ticket

from threading import Thread
from Controllers.adminController import adminController


#se instancia fastapi 
app = FastAPI(title="Api [nombre app]",
  description="this is a REST API using fastapi and mongodb",
  version="0.5.1"
)

#se incuyen las rutas en la instancia de fastapi
app.include_router(tren)
app.include_router(admin)
app.include_router(estaciones)
app.include_router(linea)
app.include_router(recorridos)
app.include_router(ticket)

#se crea la pagina inicial de la app
@app.get("/")
async def read_root():
  return {"Hello": "World"}

origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def test_singleton() -> None:
  singleton = adminController()
  print(singleton)

if __name__ == "__main__":
  #se corre el servidor de fastapi utilizando uvicorn
  #se utiliza en modo local
  #0.0.0.0 se utiliza para ejecutar en publico y reload en false
  process1 = Thread(target=test_singleton())
  process2 = Thread(target=test_singleton())
  process1.start()
  process2.start()

  print("normal")

  print(adminController())
  print(adminController())



  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


#
#hacer que se puedan buscar estaciones intermedias en las listas de las lineas probablemente quick sort????
#añadir a base de datos los vagones
#