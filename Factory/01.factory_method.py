from math import cos, sin


class Point:
    # Impossible to override this method - not usable directly
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self) -> str:
        return f'X: {self.x}, Y:{self.y}'


if __name__ == '__main__':
    p1 = Point.new_cartesian_point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p1, p2)
