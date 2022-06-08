from datetime import datetime
from fastapi import APIRouter
from Controllers.recorridoController import recorridosController
from models.recorrido import Recorrido
from config.database import get_database

recorridos = APIRouter()
collection = get_database().recorridos

@recorridos.get("/recorridos",response_model=list[Recorrido])
async def get_estaciones():
    return await recorridosController.estaciones_list_entity()

@recorridos.post("/recorridos/post", response_model=Recorrido)
async def post_estaciones(estaciones:Recorrido):
    return await recorridosController.post_estaciones(estaciones)
    
#cambiar para actualizar demas elementos
@recorridos.put("/recorridos/put-{id}",response_model=Recorrido)
async def put_estaciones(estaciones:Recorrido,id:datetime):
    return await recorridosController.put_estaciones(estaciones,id)

@recorridos.delete("/recorridos/delete-{id}",response_model=bool)
async def delete_estaciones(id:datetime):
    return await recorridosController.delete_estaciones(id)