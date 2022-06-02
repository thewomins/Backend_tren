from models.recorrido import Recorrido
from config.singleton import SingletonMeta
from config.database import get_database

collection = get_database().recorridos

class recorridosController(metaclass=SingletonMeta):

    #devuelve 1 entidad con sus atributos
    async def recorrido_entity(email) -> dict:
        cursor = collection.find_one({"email":email})
        #print(cursor)
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

    async def update_recorrido(recorrido:Recorrido,email:str) -> dict:
        collection.update_one({"email":email},{"$set":recorrido.dict()})
        return await collection.find_one({"email":recorrido.email})

    async def delete_recorrido(email:str) -> bool:
        collection.delete_one({"email":email})
        return True