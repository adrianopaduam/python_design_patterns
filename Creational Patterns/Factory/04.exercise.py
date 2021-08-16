class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    id = 0

    def create_person(self, name):
        person = Person(self.id, name)
        self.id += 1
        return person
