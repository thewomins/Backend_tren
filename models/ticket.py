from pydantic import BaseModel

class Ticket(BaseModel):
    id:str
    id_recorrido:str
    estacion_inicio:str
    estacion_destino:str
    numero_asiento:int
    valor:int


    