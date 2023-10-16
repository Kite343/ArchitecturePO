import datetime
from ticket_repository import TicketRepository

class TicketRepository:
    _ticket_repository: TicketRepository

    def __init__(self, ticket_repository: TicketRepository) -> None:
        self._ticket_repository = ticket_repository

    def add_ticket(self, price: int, 
                  place: int, is_valid: bool = False,
                  dateTime=datetime.date.today()):
        self._ticket_repository.add_ticket(price, place, is_valid, dateTime)

    def read_by_id(self, id: int):
        return self._ticket_repository.read_by_id(id)
    
    def read_all(self):
        return self._ticket_repository.read_all()\
        
    def update(self, ticket_id, price: int, 
                  place: int, is_valid: bool = False,
                  dateTime=datetime.date.today()):
        self._ticket_repository.update(ticket_id, price, place, is_valid, dateTime)

    def delete(self, id: int):
        ticket = self.read_by_id(id)
        self._ticket_repository.delete(ticket)

    def get_tickets_by_day(self, dateTime):
        pass