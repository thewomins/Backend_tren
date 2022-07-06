from fastapi import APIRouter
from Controllers.adminController import adminController
from models.admin import Admin

admin = APIRouter() #se define la ruta admin
AC = adminController()

#endpoint get 
#retorna una lista de todos los administradores
@admin.get("/admin",response_model=list[Admin])
async def get_admin():
    return await AC.admin_list_entity()

#endpoint post 
#parametro es un objeto tipo admin 
#retorna el administrador ingresado
@admin.post("/admin/post", response_model=Admin)
async def post_admin(admin:Admin):
    return await AC.post_admin(admin)

#endpoint get 
#parametro es el objeto admin actualizado y el email del admin que se quiere actualizar
#retorna el administrador actualizado
@admin.put("/admin/put-{email}",response_model=Admin)
async def put_admin(admin:Admin,email:str):
    return await AC.update_admin(admin,email)

#endpoint get 
#parametro es el email del admin a eliminar
#retorna un booleano si se realiza
@admin.delete("/admin/delete-{email}",response_model=bool)
async def delete_admin(email:str):
    return await AC.delete_admin(email)


@admin.post("/admin/auth",response_model=dict)
async def auth_admin(admin:Admin):
    return await AC.autenticar_admin(admin)