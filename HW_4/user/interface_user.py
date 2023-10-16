from abc import ABC, abstractmethod

from user import User

class IUserRepo(ABC):
    @abstractmethod
    def add_user(self, name: str, hash_password: int, card_number: int):
        pass

    @abstractmethod
    def read_by_id(self, id: int):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self, user_id: int, 
               name: str, hash_password: int, card_number: int):
        pass

    @abstractmethod
    def delete(self, user: User):
        pass


