from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True

        elif (
            command.action == Command.Action.WITHDRAW and
            self.balance >= command.amount
        ):
            self.balance -= command.amount
            command.success = True
        else:
            command.success = False


if __name__ == '__main__':
    a = Account()

    cmd = Command(Command.Action.DEPOSIT, 100)
    a.process(cmd)

    assert 100 == a.balance
    assert cmd.success is True

    cmd = Command(Command.Action.WITHDRAW, 50)
    a.process(cmd)

    assert 50 == a.balance
    assert cmd.success is True

    cmd.amount = 150
    a.process(cmd)

    assert 50 == a.balance
    assert cmd.success is False
