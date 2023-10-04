from Poligon import Poligon
from Texture import Texture


class PoligonalModel:
    poligons: list[Poligon]
    textures: list[Texture]

    def __init__(self, n_poligons: int=1, textures: list[Texture]=[]) -> None:
        self.poligons = [Poligon() for _ in n_poligons]
        self.textures = textures
