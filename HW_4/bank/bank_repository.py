from bank_account import BankAccount
from interface_bank import IBankAccount


class BankRepository(IBankAccount):
    _clients: list[BankAccount]

    def __init__(self, clients: list[BankAccount] = []):
        self._clients = clients

    # зачисление
    def crediting(self, client: BankAccount, amount: int):
        '''зачисление денежных средств на счет'''
        new_balance = client.balance + amount
        client.balance = new_balance

    # списание
    def debbiting(self,client: BankAccount, amount: int):
        '''списание денежных средств со счета'''
        new_balance = client.balance - amount
        client.balance = new_balance

    def get_all_clients(self):
        return self._clients
    
    def add_client(self, client: BankAccount):
        self._clients.append(client)
    
    def del_client(self, client: BankAccount):
        self._clients.remove(client)

    def get_client(self, card_number: int):
        for client in self._clients:
            if client.card == card_number:
                return client
