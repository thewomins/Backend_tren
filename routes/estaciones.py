from fastapi import APIRouter, Depends
from Controllers.estacionesController import estacionesController
from models.estaciones import Estaciones
from config.database import get_database
from models.auth import Hasher

hasher = Hasher()

estaciones = APIRouter()
collection = get_database().estaciones

@estaciones.get("/estaciones",response_model=list[Estaciones])
async def get_estaciones():
    return await estacionesController.estaciones_list_entity()

@estaciones.get("/estaciones-by-city-{city}",response_model=Estaciones)
async def get_estaciones(city):
    return await estacionesController.estaciones_entity_by_city(city)

@estaciones.post("/estaciones/post", response_model=Estaciones ,dependencies=[Depends(hasher.auth_wrapper)])
async def post_estaciones(estaciones:Estaciones):
    return await estacionesController.post_estaciones(estaciones)
    
#cambiar para actualizar demas elementos
@estaciones.put("/estaciones/put-{id}",response_model=Estaciones ,dependencies=[Depends(hasher.auth_wrapper)])
async def put_estaciones(estaciones:Estaciones,id:str):
    return await estacionesController.put_estaciones(estaciones,id)

@estaciones.delete("/estaciones/delete-{id}",response_model=bool ,dependencies=[Depends(hasher.auth_wrapper)])
async def delete_estaciones(id:str):
    return await estacionesController.delete_estaciones(id)