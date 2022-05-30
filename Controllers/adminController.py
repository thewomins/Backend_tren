from models.admin import Admin
from config.singleton import SingletonMeta
from config.database import get_database

collection = get_database().admin

class adminController(metaclass=SingletonMeta):

    #devuelve 1 entidad con sus atributos
    async def admin_entity(email) -> dict:
        cursor = collection.find_one({"email":email})
        #print(cursor)
        return cursor

    #devuelve una lista de entidades en este caso admin llamando la funcion anterior
    async def admin_list_entity() -> list:
        admins=[]
        cursor = collection.find({})
        async for document in cursor:
            admins.append(Admin(**document))#parsea el documento al modelo ya establecido
        return admins

    async def post_admin(admin:Admin) -> dict:
        document = admin.dict()
        result = collection.insert_one(document)
        return document

    async def update_admin(admin:Admin,email:str) -> dict:
        collection.update_one({"email":email},{"$set":admin.dict()})
        return await collection.find_one({"email":admin.email})

    async def delete_admin(email:str) -> bool:
        collection.delete_one({"email":email})
        return True