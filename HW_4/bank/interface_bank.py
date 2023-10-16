from abc import ABC, abstractmethod
from bank_account import BankAccount

class IBankAccount(ABC):
    # зачисление
    @abstractmethod
    def crediting(self, client: BankAccount, amount: int):
        '''зачисление денежных средств на счет'''
        pass

    # списание
    @abstractmethod
    def debbiting(self, client: BankAccount, amount: int):
        '''списание денежных средств со счета'''
        pass

    @abstractmethod
    def get_all_clients(self):
        pass

    @abstractmethod
    def add_client(self, client: BankAccount):
        pass

    @abstractmethod
    def del_client(self, client: BankAccount):
        pass

    @abstractmethod
    def get_client(self, card_number: int):
        pass