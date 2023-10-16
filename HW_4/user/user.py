class User:
    _id: int
    _name: str
    _hash_password: int
    _card_number: int

    def __init__(self, id: int, name: str, hash_password: int, card_number: int) -> None:
        self._id = id
        self._name = name
        self._hash_password: hash_password
        self._card_number: card_number

    def get_id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def hash_password(self):
        return self._hash_password
    
    @hash_password.setter
    def hash_password(self, new_hash_password):
        self._hash_password = new_hash_password

    @property
    def card_number(self):
        return self._card_number
    
    @card_number.setter
    def card_number(self, new_card_number):
        self._card_number = new_card_number
