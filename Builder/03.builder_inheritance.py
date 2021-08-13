""" This is in conformity with the open-close (never change the old)"""


class Person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return ' '.join([
            f'{self.name}, born on {self.date_of_birth},',
            f'works as {self.position}'
        ])

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    me = pb\
        .called('Adriano')\
        .works_as_a('software developer')\
        .born('07/10/1990')\
        .build()
    print(me)
