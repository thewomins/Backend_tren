from fastapi import FastAPI
import uvicorn
from models import *
from routes.tren import tren


from dotenv import dotenv_values
import os

app = FastAPI(title="FastAPI & Mongo CRUD",
  description="this is a simple REST API using fastapi and mongodb",
  version="0.0.1"
)

app.include_router(tren)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)


#
#hacer que se puedan buscar estaciones intermedias en las listas de las lineas probablemente quick sort????
#añadir a base de datos los vagones
#