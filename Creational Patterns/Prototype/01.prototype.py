from copy import deepcopy


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} lives at {self.address}'


class Address:
    def __init__(self, street, city, country) -> None:
        self.city = city
        self.street = street
        self.country = country

    def __str__(self) -> str:
        return f'{self.street}, {self.city}, {self.country}'


if __name__ == '__main__':
    john = Person('John', Address('123 London Road', 'London', 'UK'))
    print(john)

    jane = john  # Simple object copy (reference to the same object)
    jane.name = 'Jane'
    jane.address.street = '123B London Road'
    print('---')
    print(john)
    print(jane)

    # Proper way of generating a copy
    john = Person('John', Address('123 London Road', 'London', 'UK'))
    jane = deepcopy(john)

    jane.name = 'Jane'
    jane.address.street = '124 London Road'

    print('---')
    print(john)
    print(jane)
