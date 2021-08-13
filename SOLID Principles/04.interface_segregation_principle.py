""" Interfaces should not have an excessive number of mehtods """
from abc import abstractmethod


##########################################################################
# Problematic interface, many responsabilities
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


# Example where problematic interface should work
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


# Example where problematic interface will fail
class OldFashinedPrinter(Machine):
    def print(self, document):
        pass  # ok

    def fax(self, document):
        pass  # no operation (problematic, because method is available)

    def scan(self, document):
        """ Not supported! """
        raise NotImplementedError('Printer cannot scan!')
##########################################################################


##########################################################################
# Interface segregation implementation
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class PhotoCopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass


# Example on how to implement the original interface using smaller ones
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner) -> None:
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)

##########################################################################
