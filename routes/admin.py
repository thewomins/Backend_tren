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

@admin.put("/admin-{email}",response_model=Admin)
async def put_tren(admin:Admin,email:str):
    await collection.update_one({"email":email},{"$set":admin.dict()})
    return await collection.find_one({"email":admin.email})

@admin.delete("/admin-{email}")
async def delete_admin(email:str):
    await collection.delete_one({"email":email})
    return True