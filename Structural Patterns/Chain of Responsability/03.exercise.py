from abc import ABC, abstractmethod
from enum import Enum


class Attribute(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature, attribute_type, attribute_initial_value):
        self.creature = creature
        self.attribute_type = attribute_type
        self.value = attribute_initial_value


class CreatureModifier(ABC):
    def __init__(self, creature):
        self.creature = creature

    @abstractmethod
    def handle(self, sender, query):
        pass


class Creature:
    def __init__(self, game, attack, defense):
        self.game = game
        self.initial_attack = attack
        self.initial_defense = defense

        # self.game.creatures.append(self)

    def __str__(self) -> str:
        return f'{type(self).__name__} ({self.attack}/{self.defense})'

    @property
    def attack(self):
        query = Query(self, Attribute.ATTACK, self.initial_attack)

        self.game.process_query(self, query)

        return query.value

    @property
    def defense(self):
        query = Query(self, Attribute.DEFENSE, self.initial_attack)

        self.game.process_query(self, query)

        return query.value


class Goblin(Creature, CreatureModifier):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    def handle(self, sender, query):
        if sender != self and query.attribute_type == Attribute.DEFENSE:
            query.value += 1


class GoblinKing(Goblin, CreatureModifier):
    def __init__(self, game):
        super().__init__(game, attack=3, defense=3)

    def handle(self, sender, query):
        if sender != self and query.attribute_type == Attribute.ATTACK:
            query.value += 1
        super().handle(sender, query)


class Game:
    def __init__(self):
        self.creatures = []

    def process_query(self, sender, query):
        for creature in self.creatures:
            creature.handle(sender, query)


if __name__ == '__main__':
    game = Game()
    goblin = Goblin(game)
    g2 = Goblin(game)
    g3 = Goblin(game)
    game.creatures.append(goblin)
    game.creatures.append(g2)
    game.creatures.append(g3)

    print('Before king (3 goblins')
    print(goblin)
    print(g2)
    print(g3)

    print('----------')

    king = GoblinKing(game)
    game.creatures.append(king)

    print('After king')
    print(king)
    print(goblin)
    print(g2)
    print(g3)
