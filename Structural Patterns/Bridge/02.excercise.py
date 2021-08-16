# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too
from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'


class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @property
    def shape(self):
        return type(self).__name__

    def __str__(self):
        # return f'Drawing {self.shape} as {self.renderer.what_to_render_as}'

        # Using this way to be accepted on udemy portal
        return 'Drawing %s as %s' % (
            self.shape,
            self.renderer.what_to_render_as
        )


class Square(Shape):
    pass


class Triangle(Shape):
    pass


if __name__ == '__main__':

    sq = Square(VectorRenderer())
    print(sq)

    print(str(Triangle(RasterRenderer())))