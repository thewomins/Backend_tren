import motor.motor_asyncio
from dotenv import dotenv_values

config = dotenv_values(".env")
DATABASE_URI = config.get("DATABASE_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URI)
#nombre database
database = client.prueba
#nombre coleccion similar a tablas
#collection = database.trenes
def get_database():
    return database