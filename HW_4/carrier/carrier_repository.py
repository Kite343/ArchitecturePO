from carrier import Carrier
from interface_carrier import ICarrierRepo

class CarrierRepository(ICarrierRepo):
    _all_carrier: list[Carrier]

    def __init__(self, all_carrier: list[Carrier]=[]) -> None:
        self._all_carrier = all_carrier

    def create(self, placec: int, card_number: int,
                  name: str):
        id = self._all_carrier[-1].get_id() + 1
        carrier = Carrier(id, placec, card_number, name)
        self._all_carrier.append(carrier)

    def read_all(self):
        return self._all_carrier

    def read_by_id(self, id: int):
        for carrier in self._all_carrier:
            if carrier.get_id() == id:
                return carrier

    def update(self, carrier_id, placec: int, card_number: int,
                  name: str):
        for i in range(len(self._all_carrier)):
            if self._all_carrier[i] == carrier_id:
                self._all_carrier[i].card_number = card_number
                self._all_carrier[i]._placec = placec
                self._all_carrier[i].name = name

    def delete(self, carrier: Carrier):
        self._all_carrier.remove(carrier)