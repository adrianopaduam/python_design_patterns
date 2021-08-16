# ^^ you are given this
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print('.', end='')
# vv


class Line:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter:
    cache = {}  # Caching object implementatiopn

    def __init__(self, line):
        self.h = hash(line)  # Storing information with hash code
        if self.h in self.cache:
            return

        print(''.join([
            'Generating points for line ',
            f'[{line.start.x}, {line.start.y}]->'
            f'[{line.end.x}, {line.end.y}]'
        ]))

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = max(line.start.x, line.end.x)
        bottom = min(line.start.x, line.end.x)

        points = list()
        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points  # Inserting generated information on cache

    def __iter__(self):  # iterating over cached object
        return iter(self.cache[self.h])


def draw(rcs):
    print('\n\n--- Drawing some stuff ---\n')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == '__main__':
    rcs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rcs)
    draw(rcs)
