import motor.motor_asyncio
import asyncio
from dotenv import dotenv_values

config = dotenv_values(".env")
DATABASE_URI = config.get("DATABASE_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URI)
client.get_io_loop = asyncio.get_running_loop #get the current loop (cursor?)
#nombre database
database = client.tren_app
#nombre coleccion similar a tablas
#collection = database.trenes
def get_database():
    return database