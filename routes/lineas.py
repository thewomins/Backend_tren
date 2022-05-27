from typing import Collection
from fastapi import APIRouter
from Controllers.lineaController import lineaController
from models.linea import Linea
from config.database import get_database

linea = APIRouter()

@linea.get("/linea",response_model=list[Linea])
async def get_linea():
    lineas=[]
    cursor = collection.find({})
    async for document in cursor:
        lineas.append(Linea(**document))#parsea el documento al modelo ya establecido
    return lineas

@linea.post("/linea", response_model=Linea)
async def post_linea(linea:Linea):
    document = linea.dict()
    result = await collection.insert_one(document)
    return document
    
@linea.put("/linea{nombre_linea}",response_model=list[Linea])
async def put_tren(linea:Linea,nombre_linea:str):
    await collection.update_one({"nombre_linea":nombre_linea},{"$set":linea.dict()})
    return await collection.find_one({"numero_serie":id})

@linea.delete("/linea-{id}")
async def delete_linea(id:str):
    await collection.delete_one({"nombre":id})
    return True