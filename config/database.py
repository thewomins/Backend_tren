import motor.motor_asyncio
import asyncio
from dotenv import dotenv_values

config = dotenv_values(".env") #datos de conexion de base de datos
DATABASE_URI = config.get("DATABASE_URI") #se obtiene el dato de env que contiene la uri de la base de datos

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URI) #se crea el cliente de motor 
client.get_io_loop = asyncio.get_running_loop #obtiene el loop actual (cursor)
#nombre database
database = client.tren_app
#nombre coleccion similar a tablas
#collection = database.trenes

#retorna la conexion de base de datos del cliente
def get_database():
    return database