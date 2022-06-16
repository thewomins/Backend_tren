from pydantic import BaseModel

class Estaciones(BaseModel):
    nombre:str
    ciudad:str