from models.tren import Tren
from config.singleton import SingletonMeta
from config.database import get_database

collection = get_database().tren

class trenController(metaclass=SingletonMeta):

    #devuelve 1 entidad con sus atributos
    async def tren_entity(numero_serie:str) -> dict:
        cursor = await collection.find_one({"numero_serie":numero_serie})
        #print(cursor)
        return cursor

    #devuelve una lista de entidades en este caso tren llamando la funcion anterior
    async def tren_list_entity() -> list:
        trenes=[]
        cursor = collection.find({})
        async for document in cursor:
            trenes.append(Tren(**document))#parsea el documento al modelo ya establecido
        return trenes

    async def post_tren(tren:Tren) -> bool:
        document = tren.dict()
        result = await collection.insert_one(document)
        return result.acknowledged

    async def put_tren(tren:Tren,id:str) ->dict:
        await collection.update_one({"numero_serie":id},{"$set":{"velocidad":tren.velocidad,"asientos":tren.asientos}})
        return await collection.find_one({"numero_serie":id})

    async def delete_tren(id:str) -> bool:
        await collection.delete_one({"numero_serie":id})
        return True