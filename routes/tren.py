from fastapi import APIRouter, Depends
from Controllers.trenController import trenController
from models.tren import Tren
from config.database import get_database
from models.auth import Hasher

hasher = Hasher()

tren = APIRouter()
collection = get_database().tren

@tren.get("/tren",response_model=list[Tren])
async def get_tren():
    return await trenController.tren_list_entity()

#get 1
@tren.get("/tren-{numero_serie}",response_model=Tren)
async def get_tren(numero_serie:str):
    return await trenController.tren_entity(numero_serie)

@tren.post("/tren/post", response_model=Tren ,dependencies=[Depends(hasher.auth_wrapper)])
async def post_tren(tren:Tren):
    return await trenController.post_tren(tren)
    
#cambiar para no actualizar id y demas elementos
@tren.put("/tren/put-{id}",response_model=Tren ,dependencies=[Depends(hasher.auth_wrapper)])
async def put_tren(tren:Tren,id:str):
    return await trenController.put_tren(tren,id)

@tren.delete("/tren/delete-{id}",response_model=bool ,dependencies=[Depends(hasher.auth_wrapper)])
async def delete_tren(id:str):
    return await trenController.delete_tren(id)