from datetime import time
from pydantic import BaseModel


class Horario(BaseModel):
    Hora_salida: str
    Hora_llegada: str
    id_tren:str

class Estaciones(BaseModel):
    nombre:str
    kilometro:int

class Linea(BaseModel):
    nombre_linea:str
    estaciones:list[Estaciones]
    horarios:list[Horario]
