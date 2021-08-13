""" High level modules should depend on abstractions not other modules """
from abc import abstractmethod
from enum import Enum


########################################################################
# Unwanted implementation - concrete class depends on another concrete class
class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name) -> None:
        self.name = name


class Relationships:
    def __init__(self) -> None:
        self.relations = []  # if this changes, breaks everything

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


# Unwanted dependency with lo level class example
class Research:
    def __init__(self, relationships) -> None:
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                print(f'John has a child called {r[2].name}')
########################################################################


########################################################################
# Proper implementation - interface creation
class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


# Correct Relationships class implementation
class CorrectRelationships(RelationshipBrowser):  # low level module
    def __init__(self) -> None:
        # now, if you change this, must change internal mehtod too
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class CorrectResearch:  # high level module
    def __init__(self, browser) -> None:
        for child in browser.find_all_children_of('John'):
            print(f'John has a child called {child}')
########################################################################


if __name__ == "__main__":
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    # It works, but will bring problems in the future
    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)
    Research(relationships)

    print()

    # Also works, but is modifiable and expandable
    relationships = CorrectRelationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)
    CorrectResearch(relationships)
