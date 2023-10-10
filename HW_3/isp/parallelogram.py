from shape3D import Shape3D
from draw_shape import DrawShape
from shape import Shape

class Parallelogram(Shape, DrawShape, Shape3D):
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        return 2 * (self.x * self.y + self.x * self.z + self.y * self.z)

    def perimeter(self):
        return 4 * (self.x + self.y + self.z)
    
    def draw(self):
        return "draw Parallelogram"
    
    def volume(self):
        return self.x * self.y * self.z

    def __str__(self):
        return f'Parallelogram: {self.x} x {self.y} x {self.z}'