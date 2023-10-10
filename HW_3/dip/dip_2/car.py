from engine import Engine

class Car:
    def __init__(self, name, engine: Engine):
        self.name = name
        self.engine = engine

    def start(self):
        self.engine.start()

    def __str__(self) -> str:
        return self.name