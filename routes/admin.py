from typing import Collection
from fastapi import APIRouter
from schemas.admin import *
from models.admin import Admin
from config.database import get_database

admin = APIRouter()
collection = get_database().admin

@admin.get("/admin",response_model=list[Admin])
async def get_admin():
    admins=[]
    cursor = collection.find({})
    async for document in cursor:
        admins.append(Admin(**document))#parsea el documento al modelo ya establecido
    return admins

@admin.post("/admin", response_model=Admin)
async def post_admin(admin:Admin):
    document = admin.dict()
    result = await collection.insert_one(document)
    return document
    
#cambiar para actulizar email y password

#@admin.put("/admin{id}",response_model=list[Admin])
#async def put_tren(admin:Admin,id:str):
#    await collection.update_one({"numero_serie":id},{"$set":admin.dict()})
#    return await collection.find_one({"numero_serie":id})


@admin.delete("/admin{id}")
async def delete_admin(id:str):
    await collection.delete_one({"email":id})
    return True