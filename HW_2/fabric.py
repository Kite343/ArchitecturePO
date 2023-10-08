# ДЗ. Добавить новые предметы. Сундуки с новыми предметами.

from random import choice
from abc import ABC, abstractmethod


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class GemGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GemReward()
    
# new

class KryptoniteReward(IGameItem):
    def open(self):
        print('Kryptonite')


class KryptoniteGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return KryptoniteReward()
    
class SpicesReward(IGameItem):
    def open(self):
        print('Spices')


class SpicesGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return SpicesReward()
    
class KittenReward(IGameItem):
    def open(self):
        print('Kitten')


class KittenGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return KittenReward()


if __name__ == '__main__':
    # gold_generator = GoldGenerator()
    # gold_generator.open_reward()
    lst = [GoldGenerator(), GemGenerator(), KryptoniteGenerator(), SpicesGenerator(), KittenGenerator()]
    for i in range(20):
        choice(lst).open_reward()