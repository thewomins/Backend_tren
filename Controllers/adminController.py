from models.admin import Admin
from config.singleton import SingletonMeta
from config.database import get_database

#se obtine la coleccion de administrador de la base de datos
collection = get_database().admin 

#se crea la clase usando como metaclase singleton para convertir la clase en singleton
class adminController(metaclass=SingletonMeta):
    #devuelve 1 entidad admin con sus atributos
    async def admin_entity(email) -> dict:
        cursor = collection.find_one({"email":email}) #se busca por email el admin en la base de datos
        #print(cursor)
        return cursor

    #devuelve una lista de entidades en este caso admin 
    async def admin_list_entity() -> list:
        admins=[] #se crea lista vacia
        cursor = collection.find({}) #cursor obtiene todos lo datos contenidos en la coleccion admin
        async for document in cursor: #se recorre el cursor
            admins.append(Admin(**document))#parsea el documento al modelo ya establecido
        return admins #se retorna la lista

    #se añade un admin a la coleccion 
    #el parametro de entrada debe de ser tipo admin
    async def post_admin(admin:Admin) -> dict: # "->" significa que la funcion retorna un diccionario 
        document = admin.dict() #el objeto admin se transforma a diccionario
        result = collection.insert_one(document) # se inserta en la coleccion
        return document # se retorna el admin como diccionario

    #se actualiza un administrador
    #los parametros de entrada son el objeto admin con los datos actualizados
    #y el email del administrador a actualizar
    #retorna el admin actualizado  
    async def update_admin(admin:Admin,email:str) -> dict:
        collection.update_one({"email":email},{"$set":admin.dict()})
        return await collection.find_one({"email":admin.email})

    #se borra un administrador
    #el parametro de entrada es el email del admin a eliminar
    #se retorna true si se elimina
    async def delete_admin(email:str) -> bool:
        collection.delete_one({"email":email})
        return True