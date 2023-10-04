import zope.interface

from ..ModelElements.Flash import Flash
from ..ModelElements.Scene import Scene
from ..ModelElements.Camera import Camera
from ..ModelElements.PoligonalModel import PoligonalModel
from IModelChanger import IModelChanger
from IModelChangedObserver import IModelChangedObserver

class ModelSrore:
    zope.interface.implements( IModelChanger)
    models = list[PoligonalModel]
    scenes = list[Scene]
    flashes = list[Flash]
    cameras = list[Camera]
    _change_oservers = IModelChangedObserver

    def __init__(self, n_models: int=1, n_scences: int=1, n_flashes: int=1, n_cameras: int=1 ):
        self.models = [PoligonalModel() for _ in n_models]
        self.scenes = [Scene() for _ in n_scences]
        self.flashes = [Flash() for _ in n_flashes]
        self.cameras = [Camera() for _ in n_cameras]

    def get_scena(self, num: int) -> Scene:        
        return self.scenes[num]

    def notify_change(self, i_model_change: IModelChanger):
        pass

