from Angle3D import Angle3D
from Point3D import Point3D

class Camera:
    location: Point3D
    angle: Angle3D

    def rotate(self, angle_3D: Angle3D) -> None:
        pass

    def move(self, point_3D: Point3D) -> None:
        pass