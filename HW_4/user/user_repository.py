from user import User
from interface_user import IUserRepo


class UserRepository(IUserRepo):  
    _all_clients: list[User]

    def __init__(self, clients: list[User] = []) -> None:
        self._all_clients = clients

    def add_user(self, name: str, hash_password: int, card_number: int):
        id = self._all_clients[-1].get_id() + 1
        user = User(id=id, name = name, hash_password = hash_password, card_number= card_number)
        self._all_clients.append(user)

    def read_by_id(self, id: int):
        for user in self._all_clients:
            if user._id == id:
                return user

    def read_all(self):
        return self._all_clients

    def update(self, user_id: int, 
               name: str, hash_password: int, card_number: int):
        for i in range(len(self._all_clients)):
            if self._all_clients[i]._id == user_id:
                self._all_clients[i].name = name
                self._all_clients[i].hash_password = hash_password
                self._all_clients[i].card_number = card_number

    def delete(self, user: User):
        self._all_clients.remove(user)

    def get_card_number(self, user: User):
        return user.card_number