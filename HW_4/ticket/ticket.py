import datetime


class Ticket:
    _id: int
    _price: int
    _dateTime: datetime.date()
    _place: int
    _is_valid: bool

    def __init__(self, id: int, price: int, 
                  place: int, is_valid: bool = False,
                  dateTime=datetime.date.today(),) -> None:
        self._id = id
        self._price = price
        self._dateTime = dateTime
        self._place = place
        self._is_valid = is_valid
        
    def get_id(self):
        return self._id
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price

    @property
    def dateTime(self):
        return self._dateTime
    
    @dateTime.setter
    def dateTime(self, dateTime):
        self._dateTime = dateTime

    def get_place(self):
        return self._place
    
    @property
    def is_valid(self):
        return self._is_valid
    
    @is_valid.setter
    def is_valid(self, is_valid):
        self._is_valid = is_valid


