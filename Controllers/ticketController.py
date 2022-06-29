from io import BytesIO
from models.ticket import Ticket
from config.singleton import SingletonMeta
from config.database import get_database
import uuid
import qrcode
import qrcode.image.svg
from fastapi.responses import StreamingResponse

collection = get_database().tickets

class ticketController(metaclass=SingletonMeta):
    #devuelve 1 entidad con sus atributos
    async def ticket_entity(id) -> dict:
        cursor = await collection.find_one({"id":id})
        await cursor.pop("_id")
        return cursor

    async def ticket_entity_by_id_recorrido_y_asiento(id_recorrido:str,n_asiento:int) -> dict:
        cursor = await collection.find_one({"id_recorrido":id_recorrido,"numero_asiento":n_asiento})
        await cursor.pop("_id")
        return cursor

    async def create_qr(id):
        cursor = await collection.find_one({"id":id})
        cursor.pop("_id")
        img = qrcode.make(cursor["id"],image_factory=qrcode.image.svg.SvgPathImage)
        raw = BytesIO()
        img.save(raw,"SVG")
        raw.seek(0)
        return StreamingResponse(raw, media_type="image/svg")

    #devuelve una lista de entidades en este caso Linea
    async def ticket_list_entity() -> list:
        lineas=[]
        cursor = collection.find({})
        async for document in cursor:
            lineas.append(Ticket(**document))#parsea el documento al modelo ya establecido
        return lineas

    async def post_ticket(ticket:Ticket) -> dict:
        ticket.id=str(uuid.uuid4())
        document = ticket.dict()
        result = collection.insert_one(document)
        return document

    async def put_ticket(ticket:Ticket,id:str) ->dict:
        collection.update_one({"id":id},{"$set":ticket.dict()})
        return collection.find_one({"id":id})

    async def delete_ticket(id:str) ->bool:
        collection.delete_one({"id":id})
        return True