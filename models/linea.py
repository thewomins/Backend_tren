from pydantic import BaseModel

class Linea(BaseModel):
    nombre_linea:str
    estaciones:list[str,int,int]
    horarios:list[str,str,str]
