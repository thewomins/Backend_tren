from tkinter import E
from fastapi import APIRouter
from Controllers.estacionesController import estacionesController
from models.estaciones import Estaciones
from config.database import get_database

estaciones = APIRouter()
collection = get_database().estaciones

@estaciones.get("/estaciones",response_model=list[Estaciones])
async def get_estaciones():
    return await estacionesController.estaciones_list_entity();

@estaciones.post("/estaciones/post", response_model=Estaciones)
async def post_estaciones(estaciones:Estaciones):
    return await estacionesController.post_estaciones(estaciones);
    
#cambiar para actualizar demas elementos
@estaciones.put("/estaciones/put-{id}",response_model=Estaciones)
async def put_estaciones(estaciones:Estaciones,id:str):
    return await estacionesController.put_estaciones(estaciones,id)

@estaciones.delete("/estaciones/delete-{id}",response_model=bool)
async def delete_estaciones(id:str):
    return await estacionesController.delete_estaciones(id)