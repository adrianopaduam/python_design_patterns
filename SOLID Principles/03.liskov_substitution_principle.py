""" Given a base class - appending a derived class should work properly"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self) -> str:
        return f'Width: {self.width}, height: {self.height}'


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_id(rc):
    w = rc.width  # This line will break the code for squares
    rc.height = 10

    expected = int(w * 10)  # this prediction is wrong for squares
    print(f'Excpected an area of {expected}, got {rc.area}')


if __name__ == '__main__':

    # Original class example
    rc = Rectangle(2, 3)
    use_id(rc)

    # Liskov principle break example
    sq = Square(5)
    use_id(sq)
