from typing import Collection
from fastapi import APIRouter
from schemas.estaciones import *
from models.estaciones import Estaciones
from config.database import get_database

estaciones = APIRouter()
collection = get_database().estaciones

@estaciones.get("/estaciones",response_model=list[Estaciones])
async def get_estaciones():
    estacioneses=[]
    cursor = collection.find({})
    async for document in cursor:
        estacioneses.append(Estaciones(**document))#parsea el documento al modelo ya establecido
    return estacioneses

@estaciones.post("/estaciones", response_model=Estaciones)
async def post_estaciones(estaciones:Estaciones):
    document = estaciones.dict()
    result = await collection.insert_one(document)
    return document
    
#cambiar para actualizar demas elementos
@estaciones.put("/estaciones-{id}",response_model=list[Estaciones])
async def put_estaciones(estaciones:Estaciones,id:str):
    await collection.update_one({"nombre":id},{"$set":estaciones.dict()})
    return await collection.find_one({"nombre":id})

@estaciones.delete("/estaciones-{id}")
async def delete_estaciones(id:str):
    await collection.delete_one({"nombre":id})
    return True