from fastapi import APIRouter
from Controllers.ticketController import ticketController
from models.ticket import Ticket
from fastapi.responses import FileResponse

ticket = APIRouter()

@ticket.get("/ticket",response_model=list[Ticket])
async def get_ticket():
    return await ticketController.ticket_list_entity()

@ticket.get("/ticket-{id}-qr")
async def get_ticket(id:str):
    return await ticketController.create_qr(id)

@ticket.get("/ticket-id_recorrido:{recorrido}-n_asiento:{asiento}",response_model=Ticket)
async def get_ticket_by_recorrido(recorrido:str,asiento:int):
    return await ticketController.ticket_entity_by_id_recorrido_y_asiento(recorrido,asiento)

@ticket.post("/ticket/post", response_model=Ticket)
async def post_ticket(ticket:Ticket):
    return await ticketController.post_ticket(ticket)
    
@ticket.put("/ticket/put-{id}",response_model=Ticket)
async def put_ticket(ticket:Ticket,id:str):
    return await ticketController.put_ticket(ticket, id)

@ticket.delete("/ticket-{id}")
async def delete_ticket(id:str):
    return await ticketController.delete_ticket(id)