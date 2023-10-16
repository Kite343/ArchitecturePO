from bank_repository import BankRepository

class BankProvider():
    _bank_repository: BankRepository

    def __init__(self, bank_repository: BankRepository) -> None:
        self._bank_repository = bank_repository

    def operation_buy(self, card_user: int, card_carrier: int, amount: int):
        client = self._bank_repository.get_client(card_user)
        carrier = self._bank_repository.get_client(card_carrier)
        self._bank_repository.crediting(carrier, amount)
        self._bank_repository.debbiting(client, amount)

    def operation_return(self, card_user: int, card_carrier: int, amount: int):
        client = self._bank_repository.get_client(card_user)
        carrier = self._bank_repository.get_client(card_carrier)
        self._bank_repository.debbiting(carrier, amount)
        self._bank_repository.crediting(client, amount)



