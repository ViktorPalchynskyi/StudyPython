
class Toy:

    def __init__(self, name, color):
        self.name = name
        self.color = color


class ToyAnimal(Toy):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = 'animal'


class ToyCartoon(Toy):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = 'cartoon'


class ToyToxic(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = 'toxic toy'


class ToyFactory:

    def created_toy(self, name, color, toy_type):
        self._buy_raw_materials()
        self._sewing()
        self._set_color()
        if toy_type == 'animal':
            return ToyAnimal(name, color)
        elif toy_type == 'cartoon':
            return ToyCartoon(name, color)
        else:
            return ToyToxic(name, color)

    def _buy_raw_materials(self):
        print('Have bought a materials')

    def _sewing(self):
        print('Have sewed a toy')

    def _set_color(self):
        print('Have pained a toy')



factory = ToyFactory()
toy = factory.created_toy('Barbee', 'Red', 'cartoon')



print(isinstance(toy, ToyAnimal))
print(isinstance(toy, ToyToxic))
print(isinstance(toy, ToyCartoon))

if isinstance(toy, ToyToxic):
    print('It is dangerous for children')
else:
    print('It\'s ok')
