class Creature:
    def __init__(self, name, attack, defense) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self) -> str:
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier:
    def __init__(self, creature) -> None:
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print('No bonuses for you')


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f'Doubling {self.creature.name}\'s attack')
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f'Increase {self.creature.name}\'s defense')
            self.creature.defense += 2
            super().handle()
        else:
            print(
                f'{self.creature.name}\'s attack too strong.',
                'Skipping defense upgrade'
            )


if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)

    # root.add_modifier(NoBonusesModifier(goblin))

    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))

    root.handle()

    print(goblin)
