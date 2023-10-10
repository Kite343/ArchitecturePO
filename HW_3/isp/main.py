from parallelogram import Parallelogram
from rectangle import Rectangle

if __name__ == '__main__':
    parallelogram = Parallelogram(2, 3, 4)
    rectangle = Rectangle(2, 3)

    print(parallelogram)
    print(f'area {parallelogram.area()}')
    print(f'perimeter {parallelogram.perimeter()}')
    print(parallelogram.draw())
    print(f'volume {parallelogram.volume()}')

    print()

    print(rectangle)
    print(f'area {rectangle.area()}')
    print(f'perimeter {rectangle.perimeter()}')
    print(rectangle.draw())