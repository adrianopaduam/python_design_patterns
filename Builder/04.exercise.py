""" Code builder implementation """
from unittest import TestCase


class Class:
    def __init__(self, class_name: str, indent_size: int) -> None:
        self.class_name = class_name
        self.indentation = ' ' * indent_size
        self.fields = []

    def __str__(self) -> str:
        lines = [f'class {self.class_name}:']

        if not self.fields:
            lines.append(f'{self.indentation}pass')
        else:
            lines.append(f'{self.indentation}def __init__(self):')
            lines += [
                f'{self.indentation * 2}{field}'
                for field in self.fields
            ]

        return '\n'.join(lines)


class Field:
    def __init__(self, field_name: str, field_value: str) -> None:
        self.name = field_name
        self.value = field_value

    def __str__(self) -> str:
        return f'self.{self.name} = {self.value}'


class CodeBuilder:
    def __init__(self, class_name: str, indent_size: int = 4) -> None:
        self.__class = Class(class_name, indent_size)

    def add_field(self, field_name, field_value):
        self.__class.fields.append(Field(field_name, field_value))
        return self

    def __str__(self) -> str:
        return str(self.__class)


class Evaluation(TestCase):

    @staticmethod
    def preprocess(string: str = '') -> str:
        return string.strip().replace('\r\n', '\n')

    def test_empty(self):
        cb = CodeBuilder('Empty')
        self.assertEqual(
            self.preprocess(str(cb)),
            'class Empty:\n    pass'
        )

    def test_person_class(self):
        cb = CodeBuilder('Person')\
            .add_field('name', '""')\
            .add_field('age', '0')
        self.assertEqual(
            self.preprocess(str(cb)),
            '\n'.join([
                'class Person:',
                '    def __init__(self):',
                '        self.name = ""',
                '        self.age = 0'
            ])
        )


if __name__ == '__main__':
    cb = CodeBuilder('Person')\
        .add_field('name', '""')\
        .add_field('age', '0')

    print(cb)
