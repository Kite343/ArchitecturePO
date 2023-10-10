from abc import ABC, abstractmethod

class DrawShape(ABC):
    @abstractmethod
    def draw(self):
        pass