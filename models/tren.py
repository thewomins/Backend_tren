from pydantic import BaseModel

class Asiento(BaseModel):
    numero:int
    estado:bool

class Tren(BaseModel):
    numero_serie:str
    velocidad: int
    asientos:list[Asiento]