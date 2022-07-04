from models.admin import Admin
from models.auth import Hasher
from config.singleton import SingletonMeta
from config.database import get_database

#se obtine la coleccion de administrador de la base de datos
collection = get_database().admin 
hasher = Hasher()

#se crea la clase usando como metaclase singleton para convertir la clase en singleton
class adminController(metaclass=SingletonMeta):
    #devuelve 1 entidad admin con sus atributos
    async def admin_entity(self, email) -> dict:
        cursor = await collection.find_one({"email":email}) #se busca por email el admin en la base de datos
        cursor.pop("_id")
        return cursor

    #devuelve una lista de entidades en este caso admin 
    async def admin_list_entity(self) -> list:
        admins=[] #se crea lista vacia
        cursor = collection.find({}) #cursor obtiene todos lo datos contenidos en la coleccion admin
        async for document in cursor: #se recorre el cursor
            admins.append(Admin(**document))#parsea el documento al modelo ya establecido
        return admins #se retorna la lista

    #se añade un admin a la coleccion 
    #el parametro de entrada debe de ser tipo admin
    async def post_admin(self, admin:Admin) -> dict: # "->" significa que la funcion retorna un diccionario 
        admin.password=hasher.get_password_hash(admin.password)
        document = admin.dict() #el objeto admin se transforma a diccionario
        result = collection.insert_one(document) # se inserta en la coleccion
        return document # se retorna el admin como diccionario

    #se actualiza un administrador
    #los parametros de entrada son el objeto admin con los datos actualizados
    #y el email del administrador a actualizar
    #retorna el admin actualizado  
    async def update_admin(self, admin:Admin,email:str) -> dict:
        collection.update_one({"email":email},{"$set":admin.dict()})
        return await collection.find_one({"email":admin.email})

    #se borra un administrador
    #el parametro de entrada es el email del admin a eliminar
    #se retorna true si se elimina
    async def delete_admin(self, email:str) -> bool:
        collection.delete_one({"email":email})
        return True

    #asigna token en la db
    async def update_token_admin(self, token:str,email:str) -> dict:
        await collection.update_one({"email":email},{"$set":{"token":token}})
        return await collection.find_one({"email":email})

    #handle errores en autenticacion
    async def autenticar_admin(self, admin:Admin):
        admin_db = await self.admin_entity(admin.email)
        if(admin_db):
            admin_db = Admin(**admin_db)
            print(admin.email,hasher.verify_password(admin.password,admin_db.password))
            if(hasher.verify_password(admin.password,admin_db.password)):
                token = hasher.encode_token(admin.email)
                await self.update_token_admin(token,admin.email)
                print(token)
        return token

    async def close_session(self, admin:Admin):
        await self.update_token_admin("",admin.email)
        return True
    