class Person:
    def __init__(self) -> None:
        # Address
        self.street_address = None
        self.postal_code = None
        self.city = None

        # Employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return ''.join([
            f'Address: {self.street_address}, {self.postal_code}, {self.city}',
            '\n',
            f'Employed at {self.company_name}',
            f' as {self.position}',
            f' earning {self.annual_income}'
        ])


class PersonBuilder:
    def __init__(self, person=Person()) -> None:
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person=person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person=person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postal_code(self, postal_code):
        self.person.postal_code = postal_code
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()

    person = pb\
        .lives\
            .at('123 London Road')\
            .in_city('London')\
            .with_postal_code('SW12BC')\
        .works\
            .at('Fabrikam')\
            .as_a('Engineer')\
            .earning(123000)\
        .build()

    print(person)
