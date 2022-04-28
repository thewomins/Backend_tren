from pydantic import BaseModel

class Tren(BaseModel):
    numero_serie:str
    velocidad: int
    asientos: int