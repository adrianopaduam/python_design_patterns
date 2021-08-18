from random import choice
from string import ascii_lowercase


class User:
    def __init__(self, name: str) -> None:
        self.name = name


# Insetad of storing the name for each individual,
# each individual carries it`s names indexes, saving huge memory
class UserFlyweight:
    strings = list()

    def __init__(self, name: str) -> None:
        def get_or_add(string):
            if string not in self.strings:
                self.strings.append(string)
            return self.strings.index(string)

        self.names = [get_or_add(word) for word in name.split(' ')]

    def __str__(self) -> str:
        return ' '.join([self.strings[name_idx] for name_idx in self.names])


def random_string():
    return ''.join([choice(ascii_lowercase) for _ in range(8)])


if __name__ == '__main__':

    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    users = [
        UserFlyweight(f'{first_name} {last_name}')
        for first_name in first_names
        for last_name in last_names
    ]

    print(users[0])
