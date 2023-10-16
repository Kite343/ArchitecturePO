from abc import ABC, abstractmethod
import datetime
from ticket import Ticket

class ITicketRepo(ABC):
    @abstractmethod
    def create(self, price: int, 
                  place: int, is_valid: bool = False,
                  dateTime=datetime.date.today()):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_by_id(self, id: int):
        pass

    @abstractmethod
    def update(self, ticket_id, price: int, 
                  place: int, is_valid: bool = False,
                  dateTime=datetime.date.today()):
        pass

    @abstractmethod
    def delete(self, ticket: Ticket):
        pass