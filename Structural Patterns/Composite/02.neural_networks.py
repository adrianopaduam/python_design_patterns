from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return

        for self_neuron in self:
            for ohter_neuron in other:
                self_neuron.outputs.append(ohter_neuron)
                ohter_neuron.inputs.append(self_neuron)


class Neuron(Connectable):
    def __init__(self, name) -> None:
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self) -> str:
        return f'{self.name}' \
            f' {len(self.inputs)} inputs' \
            f' {len(self.outputs)} outputs'

    # Initial connection funcion - replaced by abstract class
    # def connect_to(self, other):
    #     self.outputs.append(other)
    #     other.inputs.append(self)

    # Workaround to make a single object iterable
    def __iter__(self):
        yield self


class NeuronLayer(list, Connectable):
    def __init__(self, name, count) -> None:
        super().__init__()
        self.name = name
        for idx in range(count):
            self.append(Neuron(f'{name}-{idx}'))

    def __str__(self) -> str:
        return f'{self.name} with {len(self)} neurons'


# First attempt - will not work - inserted inside abstract class
# def connect_to(self, other):
#     if self == other:
#         return

#     for s in self:
#         for o in other:
#             s.outputs.append(o)
#             o.inputs.append(s)


if __name__ == '__main__':
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 4)

    # First attempt: inserting function on classes
    # Unnecerrary after creation of base class
    # Neuron.connect_to = connect_to
    # NeuronLayer.connect_to = connect_to

    # This is the expected behavior
    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)
