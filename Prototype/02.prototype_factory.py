from copy import deepcopy


class Address:
    def __init__(self, street, suite, city) -> None:
        self.street = street
        self.suite = suite
        self.city = city

    def __str__(self) -> str:
        return f'{self.street}, Suite #{self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123 East Dr', 0, 'London'))
    aux_office_employee = Employee('', Address('123B East Dr', 0, 'London'))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


if __name__ == '__main__':
    john = EmployeeFactory.new_main_office_employee('John', 101)
    jane = EmployeeFactory.new_aux_office_employee('Jane', 500)

    print(john)
    print(jane)
