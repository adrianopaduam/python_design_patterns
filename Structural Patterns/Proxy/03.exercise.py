class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    @property
    def age(self):
        return self.person.age

    @age.setter
    def age(self, value):
        self.person.age = value

    def drink(self):
        return self.person.drink() if self.age >= 18 else 'too young'

    def drive(self):
        return self.person.drive() if self.age >= 16 else 'too young'

    def drink_and_drive(self):
        return 'dead'


if __name__ == '__main__':
    p = Person(10)
    rp = ResponsiblePerson(p)

    assert 'too young' == rp.drive()
    assert 'too young' == rp.drink()
    assert 'dead' == rp.drink_and_drive()

    rp.age = 20

    assert 'driving' == rp.drive()
    assert 'drinking' == rp.drink()
    assert 'dead' == rp.drink_and_drive()
