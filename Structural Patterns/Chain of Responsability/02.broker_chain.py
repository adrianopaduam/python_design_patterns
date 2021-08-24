# command/query separation (current lesson)
# implementation of event broker (observer)
from typing import Any
from enum import Enum
from abc import ABC, abstractmethod


class EventBroker(list):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value) -> None:
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value


class Game:
    def __init__(self) -> None:
        self.broker = EventBroker()

    def perform_query(self, sender, query):
        self.broker(sender, query)


class Creature:
    def __init__(self, game, name, attack, defense) -> None:
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)

        self.game.perform_query(self, q)

        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)

        self.game.perform_query(self, q)

        return q.value

    def __str__(self) -> str:
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier(ABC):
    def __init__(self, game, creature) -> None:
        self.game = game
        self.creature = creature

        # Insertion of the modifier on the game event broker
        self.game.broker.append(self.handle)

    @abstractmethod
    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.game.broker.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if (
            sender.name == self.creature.name and
            query.what_to_query == WhatToQuery.ATTACK
        ):
            query.value *= 2


if __name__ == '__main__':
    game = Game()
    goblin = Creature(game, 'Strong Goblin', 2, 2)
    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)

    print(goblin)
