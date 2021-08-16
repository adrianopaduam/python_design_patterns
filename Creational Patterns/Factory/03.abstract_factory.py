from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


class HotDrinkFactory(ABC):
    def preapre(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(200)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):  # this breaks open-close principle
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            self.factories = [
                (
                    drink.name.capitalize(),
                    eval(f'{drink.name.capitalize()}Factory')()
                )
                for drink in self.AvailableDrink
            ]

    def make_drink(self):
        print('Available drinks:')
        for idx, f in enumerate(self.factories):
            print(f'{idx} - {f[0]}')

        idx = int(input(f'Please pick a drink (number): '))
        amount = int(input('Specify amount (ml): '))

        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    # entry = input('What kind of drink would you like? ')
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
