from typing import Collection
from fastapi import APIRouter
from schemas.linea import *
from models.linea import Linea
from config.database import get_database

linea = APIRouter()
collection = get_database().lineas

@linea.get("/linea",response_model=list[Linea])
async def get_tren():
    lineas=[]
    cursor = collection.find({})
    async for document in cursor:
        lineas.append(Linea(**document))#parsea el documento al modelo ya establecido
    return lineas

@linea.post("/linea", response_model=Linea)
async def post_tren(linea:Linea):
    document = linea.dict()
    result = await collection.insert_one(document)
    return document
    
#cambiar para no actualizar id y demas elementos
#@tren.put("/tren{id}",response_model=list[Tren])
#async def put_tren(tren:Tren,id:str):
#    await collection.update_one({"numero_serie":id},{"$set":tren.dict()})
#    return await collection.find_one({"numero_serie":id})

@linea.delete("/linea-{id}")
async def delete_linea(id:str):
    await collection.delete_one({"nombre":id})
    return True