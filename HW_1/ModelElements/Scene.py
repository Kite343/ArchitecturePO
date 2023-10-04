from Flash import Flash
from PoligonalModel import PoligonalModel


class Scene:
    id: int
    models: list[PoligonalModel]
    flashes: list[Flash]

    def __init__(self, lst_poligonal_model: list[PoligonalModel], flashes: list[Flash]=[]):
        self.models = lst_poligonal_model
        self.flashes = flashes

    def method1(self, obj: object):
        return obj

    def method2(self, obj_1: object, obj_2: object):
        result = object()
        return result