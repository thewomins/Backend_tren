from datetime import datetime
from pydantic import BaseModel
from models.tren import Tren

class Recorrido(BaseModel):
    id=datetime
    id_linea=str
    partida=datetime.time
    llegada=datetime.time
    tren=Tren