from user_repository import UserRepository

class UserProvider:
    _user_repository: UserRepository

    def __init__(self, user_repository: UserRepository=UserRepository()) -> None:
        self._user_repository = user_repository

    def add_user(self, name: str, hash_password: int, card_number: int):
        self._user_repository.add_user(name = name, hash_password = hash_password, card_number= card_number)

    def read_by_id(self, id: int):
        return self._user_repository.read_by_id(id)

    def read_all(self):
        return self._user_repository.read_all()

    def update(self, user_id: int, 
               name: str, hash_password: int, card_number: int):
        self._user_repository.update(user_id, name, hash_password, card_number)
        
    def delete(self, id: int):
        user = self.read_by_id(id)
        self._user_repository.delete(user)

    def get_card_number(self, id: int):
        user = self.read_by_id(id)
        return self._user_repository.get_card_number(user)

