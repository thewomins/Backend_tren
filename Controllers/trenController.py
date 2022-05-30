from models.tren import Tren
from config.singleton import SingletonMeta
from config.database import get_database

collection = get_database().tren

class trenController(metaclass=SingletonMeta):

    #devuelve 1 entidad con sus atributos
    async def tren_entity(numero_serie:str) -> dict:
        cursor = collection.find_one({"numero_serie":numero_serie})
        #print(cursor)
        return cursor

    #devuelve una lista de entidades en este caso tren llamando la funcion anterior
    async def tren_list_entity() -> list:
        trenes=[]
        cursor = collection.find({})
        async for document in cursor:
            trenes.append(Tren(**document))#parsea el documento al modelo ya establecido
        return trenes

    async def post_tren(tren) ->dict:
        document = tren.dict()
        #print(document)
        result = collection.insert_one(document)
        return document

    async def put_tren(tren:Tren,id:str) ->dict:
        collection.update_one({"numero_serie":id},{"$set":{"velocidad":tren.velocidad,"asientos":tren.asientos}})
        return collection.find_one({"numero_serie":id})

    async def delete_tren(id:str) -> bool:
        collection.delete_one({"numero_serie":id})
        return True