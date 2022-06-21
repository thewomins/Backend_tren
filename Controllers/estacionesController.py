from models.estaciones import Estaciones
from config.singleton import SingletonMeta
from config.database import get_database

collection = get_database().estaciones

class estacionesController(metaclass=SingletonMeta):

    #devuelve 1 entidad con sus atributos
    async def estaciones_entity(nombre:str) -> dict:
        cursor = await collection.find_one({"nombre":nombre})
        return cursor

    async def estaciones_entity_by_city(ciudad:str) -> dict:
        cursor = await collection.find_one({"ciudad":ciudad})
        cursor.pop("_id")
        return cursor

    #devuelve una lista de entidades en este caso estaciones llamando la funcion anterior
    async def estaciones_list_entity() -> list:
        estaciones=[]
        cursor = collection.find({})
        async for document in cursor:
            estaciones.append(Estaciones(**document))#parsea el documento al modelo ya establecido
        return estaciones

    async def post_estaciones(estaciones:Estaciones) -> dict:
        document = estaciones.dict()
        result = collection.insert_one(document)
        return document

    #cambiar para actualizar demas elementos
    async def put_estaciones(estaciones:Estaciones,id:str) ->dict:
        collection.update_one({"nombre":id},{"$set":estaciones.dict()})
        return await collection.find_one({"nombre":id})

    async def delete_estaciones(id:str) -> bool:
        result=collection.delete_one({"nombre":id})
        return True