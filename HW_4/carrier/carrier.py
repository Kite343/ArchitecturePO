class Carrier:
    _id: int
    _placec: int
    _card_number: int
    _name: str

    def __init__(self, id: int, placec: int, card_number: int,
                  name: str) -> None:
        self._id = id
        self._placec = placec
        self._card_number = card_number
        self._name = name

    def get_id(self):
        return self._id
    
    @property
    def card_number(self):
        return self._card_number
    
    @card_number.setter
    def card_number(self, new_card_number):
        self._card_number = new_card_number

    def get_placec(self):
        return self._placec
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
