from fastapi import APIRouter
from Controllers.lineaController import lineaController
from models.linea import Linea

linea = APIRouter()
lc = lineaController()

@linea.get("/linea",response_model=list[Linea])
async def get_linea():
    return await lc.linea_list_entity()

@linea.get("/linea/where-estacion-{estacion}",response_model=list)
async def get_linea(estacion):
    return await lc.linea_list_by_estacion(estacion)

@linea.post("/linea/post", response_model=Linea)
async def post_linea(linea:Linea):
    return await lc.post_linea(linea)
    
@linea.put("/linea/put-{nombre_linea}",response_model=Linea)
async def put_linea(linea:Linea,nombre_linea:str):
    return await lc.put_linea(linea, nombre_linea)

@linea.delete("/linea/delete-{id}")
async def delete_linea(id:str):
    return await lc.delete_linea(id)