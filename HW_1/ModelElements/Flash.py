from Angle3D import Angle3D
from Point3D import Point3D
from Color import Color


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def rotate(self, angle_3D: Angle3D) -> None:
        pass

    def move(self, point_3D: Point3D) -> None:
        pass