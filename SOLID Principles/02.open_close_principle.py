from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:

    # First method - already in production
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    # New methods - breaks OCP - must be made by extension class
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


###################################################################
# OCP conformity - Specification implementation- Enterprise pattern
class Specification:
    def is_satisfied(self, item):
        pass

    # Extra implementation - & operator override
    def __and__(self, other):
        return AndSpecification(self, other)


class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args  # Multiple specifications informed here

    def is_satisfied(self, item):
        return all(map(  # executes every specification method
            lambda spec: spec.is_satisfied(item),
            self.args
        ))


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
###################################################################


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)
    products = [apple, tree, house]

    # Old approach - wrong
    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')
    print()

    # New approach - correct
    bf = BetterFilter()
    print('Green products (new):')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')
    print('Large products (new):')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')
    print()

    # Combination of Specifications
    print('Large and Blue (AndSpecification)')
    large_and_blue = AndSpecification(
        SizeSpecification(Size.LARGE),
        ColorSpecification(Color.BLUE)
    )
    for p in bf.filter(products, large_and_blue):
        print(f' - {p.name} is large and blue')
    print()

    # Overriding & operator
    print('Large and Blue (& Override)')
    large = SizeSpecification(Size.LARGE)
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, large & green):
        print(f' - {p.name} is large and green')
    print()
