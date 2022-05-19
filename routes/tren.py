from typing import Collection
from fastapi import APIRouter
from schemas.tren import *
from models.tren import Tren
from config.database import get_database

tren = APIRouter()
collection = get_database().tren

@tren.get("/tren",response_model=list[Tren])
async def get_tren():
    trenes=[]
    cursor = collection.find({})
    async for document in cursor:
        trenes.append(Tren(**document))#parsea el documento al modelo ya establecido
    return trenes

#get 1
@tren.get("/tren-{numero_serie}",response_model=Tren)
async def get_tren(numero_serie:str):
    cursor = await collection.find_one({"numero_serie":numero_serie})
    return cursor

@tren.post("/tren", response_model=Tren)
async def post_tren(tren:Tren):
    document = tren.dict()
    result = await collection.insert_one(document)
    return document
    
#cambiar para no actualizar id y demas elementos
@tren.put("/tren-{id}",response_model=Tren)
async def put_tren(tren:Tren,id:str):
    await collection.update_one({"numero_serie":id},{"$set":{"velocidad":tren.velocidad,"asientos_por_vagon":tren.asientos_por_vagon, "vagones":tren.vagones}})
    return await collection.find_one({"numero_serie":id})

@tren.delete("/tren-{id}")
async def delete_tren(id:str):
    await collection.delete_one({"numero_serie":id})
    return True