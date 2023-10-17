from ..carrier.carrier import Carrier
from ..bank.bank_provider import BankProvider
from ..carrier.carrier_provider import CarrierProvider
from ..ticket.ticket_provider import TicketProvider
from ..ticket.ticket import Ticket
from ..user.user_provider import UserProvider
from ..user.user import User

class Customer:
    def __init__(self, user: User) -> None:
        self.user = user
        self.user_provider = UserProvider()
        self.carrier_provider = CarrierProvider()
        self.ticket_provider = TicketProvider()
        self.bank_provider = BankProvider()
        self.tickets = []

    def get_tickets(self):
        return self.tickets
    
    def get_carriers(self):
        return self.carrier_provider.read_all()
    
    def bay_ticket(self, carrier: Carrier,  price: int, dateTime):
        ticket = self.ticket_provider.create_ticket(price, carrier.get_placec, dateTime)
        self.bank_provider.operation_buy(
            self.user.card_number, carrier.card_number, price)
        self.tickets.append(ticket)


    def return_ticket(self, ticket: Ticket, carrier: Carrier):
        self.bank_provider.operation_return(
            self.user.card_number, carrier.card_number, ticket.price)
        self.tickets.remove(ticket)