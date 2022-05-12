from pydantic import BaseModel

class Tren(BaseModel):
    numero_serie:str
    velocidad: int
    asientos_por_vagon: int
    vagones: int
