from math import cos, sin


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'X: {self.x}, Y:{self.y}'

    # If there are many factory methods, a class should be created
    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()


if __name__ == '__main__':
    p1 = Point.factory.new_cartesian_point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p1, p2)
