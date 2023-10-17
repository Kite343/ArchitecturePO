from carrier_repository import CarrierRepository

class CarrierProvider:
    _carrier_provider: CarrierRepository

    def __init__(self, carrier_provider: CarrierRepository=CarrierRepository()) -> None:
        self._carrier_provider = carrier_provider

    def add_carrier(self, placec: int, card_number: int,
                  name: str):
        self._carrier_provider.create(placec, card_number, name)

    def read_by_id(self, id: int):
        return self._carrier_provider.read_by_id(id)
    
    def read_all(self):
        return self._carrier_provider.read_all()
    
    def update(self, carrier_id, placec: int, card_number: int,
                  name: str):
        self._carrier_provider.update(carrier_id, placec, card_number, name)

    def delete(self, id: int):
        carrier = self.read_by_id(id)
        self._carrier_provider.delete(carrier)