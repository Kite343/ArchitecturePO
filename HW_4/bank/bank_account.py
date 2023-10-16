class BankAccount:
    _card: int
    _balance: int

    def __init__(self, card: int) -> None:
        self._card = card
        self._balance = 0

    @property
    def card(self):
        return self._card
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

