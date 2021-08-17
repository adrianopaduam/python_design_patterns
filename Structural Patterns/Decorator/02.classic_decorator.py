from abc import ABC


class Shape(ABC):
    def __str__(self) -> str:
        return ''


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self) -> str:
        return f'A circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def __str__(self) -> str:
        return f'A square of side {self.side}'


class ColoredShape(Shape):
    def __init__(self, shape, color) -> None:
        self.shape = shape
        self.color = color

    def __str__(self) -> str:
        return f'{self.shape} has the color {self.color}'


class TransparentShape(Shape):
    def __init__(self, shape, transparency) -> None:
        self.shape = shape
        self.transparency = transparency

    def __str__(self) -> str:
        return f'{self.shape} has {self.transparency * 100}% transparency'


if __name__ == '__main__':
    circle = Circle(2)
    print(circle)

    # Keeping Open/Close principle intact
    red_circle = ColoredShape(circle, 'red')
    print(red_circle)

    red_half_transparent_circle = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_circle)

    # Downside - it can be applied multiple times (not always favorable)
    mixed = ColoredShape(ColoredShape(Square(3), 'red'), 'green')
    print(mixed)

    # Another Downsize - Doesn`t have the methods of concrete classes
    try:
        red_circle.resize(2)
    except Exception:
        print('Error raised on red circle resize attempt - inexistent method')
