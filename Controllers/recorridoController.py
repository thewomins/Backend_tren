from models.recorrido import Recorrido
from config.singleton import SingletonMeta
from config.database import get_database

collection = get_database().recorridos

class recorridosController(metaclass=SingletonMeta):

    #devuelve 1 entidad con sus atributos
    async def recorrido_entity(id:str) ->dict:
        cursor = await collection.find_one({"id_recorrido":id})
        if(cursor):
            cursor.pop("_id")
        return cursor

    #devuelve una lista de entidades en este caso admin llamando la funcion anterior
    async def recorrido_list_entity() -> list:
        recorridos=[]
        cursor = collection.find({})
        async for document in cursor:
            recorridos.append(Recorrido(**document))#parsea el documento al modelo ya establecido
        return recorridos

    async def post_recorrido(recorrido:Recorrido) -> dict:
        document = recorrido.dict()
        result = collection.insert_one(document)
        return document

    async def put_recorrido(recorrido:Recorrido,id_recorrido:str) -> dict:
        print(recorrido.dict())
        await collection.update_one({"id_recorrido":id_recorrido},{"$set":recorrido.dict()})
        return recorrido

    async def delete_recorrido(id:str) -> bool:
        collection.delete_one({"id_recorrido":id})
        return True