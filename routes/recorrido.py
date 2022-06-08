from datetime import datetime
from fastapi import APIRouter
from Controllers.recorridoController import recorridosController
from models.recorrido import Recorrido
from config.database import get_database

recorridos = APIRouter()
collection = get_database().recorridos

@recorridos.get("/recorridos",response_model=list[Recorrido])
async def get_recorrido():
    return await recorridosController.recorrido_list_entity()

@recorridos.post("/recorridos/post", response_model=Recorrido)
async def post_recorrido(recorrido:Recorrido):
    return await recorridosController.post_recorrido(recorrido)
    
#cambiar para actualizar demas elementos
@recorridos.put("/recorridos/put-{id}",response_model=Recorrido)
async def put_recorrido(recorrido:Recorrido,id:datetime):
    return await recorridosController.put_recorrido(recorrido,id)

@recorridos.delete("/recorridos/delete-{id}",response_model=bool)
async def delete_recorrido(id:datetime):
    return await recorridosController.delete_recorrido(id)