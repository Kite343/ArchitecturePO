from abc import ABC, abstractmethod

from carrier import Carrier

class ICarrierRepo(ABC):
    @abstractmethod
    def create(self, id: int, placec: int, card_number: int,
                  name: str):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def read_by_id(self, id: int):
        pass

    @abstractmethod
    def update(self, carrier_id, placec: int, card_number: int,
                  name: str):
        pass

    @abstractmethod
    def delete(self, carrier: Carrier):
        pass