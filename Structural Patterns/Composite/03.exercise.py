from abc import ABC
from collections.abc import Iterable


class AdditionComposite(ABC, Iterable):
    @property
    def sum(self):
        return sum([
            value
            for object in self
            for value in object
        ])


class SingleValue(AdditionComposite):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, AdditionComposite):
    pass


if __name__ == '__main__':
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)

    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    print(all_values.sum)
