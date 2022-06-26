from json import JSONDecoder
from fastapi import APIRouter, HTTPException
from pydantic import Json
from Controllers.recorridoController import recorridosController
from models.recorrido import Recorrido
from config.database import get_database

recorridos = APIRouter()
collection = get_database().recorridos

@recorridos.get("/recorridos-{id}",response_model=Recorrido)
async def get_recorrido(id:str):
    response = await recorridosController.recorrido_entity(id)
    if response:
        return response
    else: 
        raise HTTPException(status_code=404, detail="Item not found")

@recorridos.get("/recorridos",response_model=list[Recorrido])
async def get_recorrido():
    return await recorridosController.recorrido_list_entity()

@recorridos.post("/recorridos/post", response_model=Recorrido)
async def post_recorrido(recorrido:Recorrido):
    print(recorrido)
    return await recorridosController.post_recorrido(recorrido)
    
#cambiar para actualizar demas elementos
@recorridos.put("/recorridos/put-{id_recorrido}",response_model=Recorrido)
async def put_recorrido(recorrido:Recorrido,id_recorrido:str):
    print(recorrido.id_recorrido)
    return await recorridosController.put_recorrido(recorrido,recorrido.id_recorrido)

@recorridos.delete("/recorridos/delete-{id}",response_model=bool)
async def delete_recorrido(id:str):
    return await recorridosController.delete_recorrido(id)