from typing import Collection
from urllib import response
from fastapi import APIRouter
from Controllers.adminController import adminController
from models.admin import Admin
from config.database import get_database

admin = APIRouter()
collection = get_database().admin

@admin.get("/admin",response_model=list[Admin])
async def get_admin():
    return await adminController.admin_list_entity()

@admin.post("/admin/post", response_model=Admin)
async def post_admin(admin:Admin):
    return adminController.post_admin(admin)

@admin.put("/admin/put-{email}",response_model=Admin)
async def put_admin(admin:Admin,email:str):
    return adminController.update_admin(admin,email)

@admin.delete("/admin/delete-{email}",response_model=bool)
async def delete_admin(email:str):
    return adminController.delete_admin(email)