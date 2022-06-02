from datetime import date
from pydantic import BaseModel

from models.estaciones import Estaciones

class Horario(BaseModel):
    salida:date
    llegada:date
    id_tren:str

class Linea(BaseModel):
    nombre_linea:str
    estaciones:list[Estaciones]
    horarios:list[Horario]

#test caja blanca clase
m1 = Linea(nombre_linea="nombre",
    estaciones=[{'nombre':"estacion","ciudad":"cuidad",'kilometro':32}],
    horarios=[{'salida':"2022-05-23",
                'llegada':"2022-05-23",
                'id_tren':"id_tren"}]
)

print(m1.dict())