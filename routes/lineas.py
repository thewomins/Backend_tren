from fastapi import APIRouter
from Controllers.lineaController import lineaController
from models.linea import Linea

linea = APIRouter()

@linea.get("/linea",response_model=list[Linea])
async def get_linea():
    return await lineaController.estaciones_list_entity()

@linea.post("/linea/post", response_model=Linea)
async def post_linea(linea:Linea):
    return await lineaController.post_linea(linea)
    
@linea.put("/linea/put-{nombre_linea}",response_model=Linea)
async def put_linea(linea:Linea,nombre_linea:str):
    return await lineaController.put_tren(linea, nombre_linea)

@linea.delete("/linea-{id}")
async def delete_linea(id:str):
    return await lineaController.delete_linea(id)