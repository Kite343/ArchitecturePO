import datetime
from ticket import Ticket
from interface_ticket import ITicketRepo


class TicketRepository(ITicketRepo):
    _all_ticket: list[Ticket]

    def __init__(self, all_ticket: list[Ticket] = []) -> None:
        self._all_ticket= all_ticket

    def create(self, price: int, 
                  place: int, is_valid: bool = False,
                  dateTime=datetime.date.today()):
        id = self._all_ticket[-1].get_id() + 1
        ticket = Ticket(id, price, place, is_valid, dateTime)
        self._all_ticket.append(ticket)

    def read_all(self):
        return self._all_ticket

    def read_by_id(self, id: int):
        for ticket in self._all_ticket:
            if ticket.get_id() == id:
                return ticket

    def update(self, ticket_id, price: int, 
                  place: int, is_valid: bool = False,
                  dateTime=datetime.date.today()):
        for i in range(len(self._all_ticket)):
            if self._all_ticket[i] == ticket_id:
                self._all_ticket[i].price = price
                self._all_ticket[i]._place = place
                self._all_ticket[i].is_valid = is_valid
                self._all_ticket[i].dateTime = dateTime

    def delete(self, ticket: Ticket):
        self._all_ticket.remove(ticket)