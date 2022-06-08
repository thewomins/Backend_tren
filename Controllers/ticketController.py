from models.ticket import Ticket
from config.singleton import SingletonMeta
from config.database import get_database

collection = get_database().tickets

class ticketController(metaclass=SingletonMeta):
    #devuelve 1 entidad con sus atributos
    async def ticket_entity(id) -> dict:
        cursor = collection.find_one({"id":id})
        #print(cursor)
        return cursor

    #devuelve una lista de entidades en este caso Linea
    async def ticket_list_entity() -> list:
        lineas=[]
        cursor = collection.find({})
        async for document in cursor:
            lineas.append(Ticket(**document))#parsea el documento al modelo ya establecido
        return lineas

    async def post_ticket(ticket:Ticket) -> dict:
        document = ticket.dict()
        result = collection.insert_one(document)
        return document

    async def put_ticket(ticket:Ticket,id:str) ->dict:
        collection.update_one({"id":id},{"$set":ticket.dict()})
        return collection.find_one({"id":id})

    async def delete_ticket(id:str) ->bool:
        collection.delete_one({"id":id})
        return True