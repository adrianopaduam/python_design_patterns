from typing import Any, Type, TypeVar
_T = TypeVar('_T')


class CEO:
    __shared_state = {
        'name': 'Steve',
        'age': 55
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'


class Monostate:  # Not the most indicate
    _shared_state = {}

    def __new__(cls: Type[_T], *args: Any, **kwargs: Any) -> _T:
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ''
        self.money_managed = 0

    def __str__(self) -> str:
        return f'{self.name} manages ${self.money_managed}'


if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 77
    print(ceo1)
    print(ceo2)

    print('-----')

    cfo1 = CFO()
    cfo1.name = 'Sheryl'
    cfo1.money_managed = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Ruth'
    cfo2.money_managed = 10
    print(cfo1, cfo2, sep='\n')
