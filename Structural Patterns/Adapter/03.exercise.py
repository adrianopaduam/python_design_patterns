class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    # properties are necessary in order to store the square as reference
    # and by that be sensitive to attributes changes on the original object

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side
