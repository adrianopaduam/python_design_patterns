# Two objects: circle and square
# Two print types: vector and raster

# Non Bridge Implementation:
# VectorCircle VectorSquare RasterCircle RasterSquare

# Bridge implementation below
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing a square of side {side}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing pixels for a square of side {side}')


class Shape:
    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float) -> None:
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()

    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    # It completely breakes open/closed principle
