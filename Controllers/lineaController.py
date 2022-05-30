from models.linea import Linea
from config.singleton import SingletonMeta
from config.database import get_database

collection = get_database().lineas

class lineaController(metaclass=SingletonMeta):
     #devuelve 1 entidad con sus atributos
    async def linea_entity(nombre_linea) -> dict:
        cursor = collection.find_one({"nombre_linea":nombre_linea})
        #print(cursor)
        return cursor

    #devuelve una lista de entidades en este caso admin llamando la funcion anterior
    async def linea_list_entity() -> list:
        lineas=[]
        cursor = collection.find({})
        async for document in cursor:
            lineas.append(Linea(**document))#parsea el documento al modelo ya establecido
        return await lineas

    async def post_linea(linea:Linea) -> bool:
        document = linea.dict()
        result = collection.insert_one(document)
        return await result.acknowledged

    async def put_tren(linea:Linea,nombre_linea:str) ->dict:
        collection.update_one({"nombre_linea":nombre_linea},{"$set":linea.dict()})
        return await collection.find_one({"numero_serie":id})

    async def delete_linea(id:str) ->bool:
        collection.delete_one({"nombre":id})
        return await True