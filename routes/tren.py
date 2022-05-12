from typing import Collection
from fastapi import APIRouter
from schemas.tren import *
from models.tren import Tren
from config.database import get_database
from __future__ import annotations

tren = APIRouter()
collection = get_database().tren

@tren.get("/tren",response_model=list[Tren])
async def get_tren():
    trenes=[]
    cursor = collection.find({})
    async for document in cursor:
        trenes.append(Tren(**document))#parsea el documento al modelo ya establecido
    return trenes

@tren.post("/tren", response_model=Tren)
async def post_tren(tren:Tren):
    document = tren.dict()
    result = await collection.insert_one(document)
    return document
    
#cambiar para no acutializar id y demas elemntos
@tren.put("/tren{id}",response_model=list[Tren])
async def put_tren(tren:Tren,id:str):
    await collection.update_one({"numero_serie":id},{"$set":tren.dict()})
    return await collection.find_one({"numero_serie":id})

@tren.delete("/tren{id}")
async def delete_tren(id:str):
    await collection.delete_one({"numero_serie":id})
    return True