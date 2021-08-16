import unittest
from typing import Any, Type, TypeVar
_T = TypeVar('_T')


class Singleton(type):
    _instances = {}

    def __call__(cls: Type[_T], *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)

        return cls._instances[cls]


# ########################################################################
# Original Implementation - Tightly coupled database class
# ########################################################################
class Database(metaclass=Singleton):
    def __init__(self) -> None:
        with open('assets/city_population_db.txt') as db_file:
            db_lines = db_file.readlines()
            self.population = {
                city.strip(): int(population.strip())
                for city, population in zip(db_lines[::2], db_lines[1::2])
            }


class SingletonRecordFinder:
    def total_population(self, cities):
        return sum([
            Database().population[city]
            for city in cities
            if city in Database().population
        ])
# ########################################################################


# ########################################################################
# Optimized Implementation - Loosely coupled database class
# ########################################################################
class ConfigurableRecordFinder:
    def __init__(self, db=Database()) -> None:
        self.db = db

    def total_population(self, cities):
        return sum([
            self.db.population[city]
            for city in cities
            if city in Database().population
        ])


class DummyDatabase:
    population = {'alpha': 1, 'beta': 2, 'gamma': 3}
# ########################################################################


class SingletonTests(unittest.TestCase):
    def test_is_sigleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    # #####################################################################
    # Original test
    # #####################################################################
    def test_singleton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(tp, 17500000 + 17400000)
    # #####################################################################

    # #####################################################################
    # Improved test
    # #####################################################################
    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(crf.total_population(['alpha', 'beta']), 3)
    # #####################################################################


if __name__ == '__main__':
    unittest.main()
