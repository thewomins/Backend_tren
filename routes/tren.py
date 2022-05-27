from typing import Collection
from fastapi import APIRouter
from Controllers.trenController import trenController
from models.tren import Tren
from config.database import get_database

tren = APIRouter()
collection = get_database().tren

@tren.get("/tren",response_model=list[Tren])
async def get_tren():
    return trenController.tren_list_entity()

#get 1
@tren.get("/tren-{numero_serie}",response_model=Tren)
async def get_tren(numero_serie:str):
    return trenController.tren_entity(numero_serie)

@tren.post("/tren/post", response_model=Tren)
async def post_tren(tren:Tren):
    return trenController.post_tren(tren)
    
#cambiar para no actualizar id y demas elementos
@tren.put("/tren/put-{id}",response_model=Tren)
async def put_tren(tren:Tren,id:str):
    return trenController.put_tren(tren,id)

@tren.delete("/tren/delete-{id}",response_model=bool)
async def delete_tren(id:str):
    return trenController.delete_tren(id)