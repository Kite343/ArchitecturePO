from draw_shape import DrawShape
from shape import Shape

class Rectangle(Shape, DrawShape):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * (self.x + self.y)
    
    def draw(self):
        return "draw Rectangle"

    def __str__(self):
        return f'Rectangle: {self.x} x {self.y}'