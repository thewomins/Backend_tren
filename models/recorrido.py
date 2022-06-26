from pydantic import BaseModel
from models.tren import Tren

class Recorrido(BaseModel):
    fecha:str
    id_linea:str
    partida:str
    llegada:str
    tren:Tren
    id_recorrido:str
