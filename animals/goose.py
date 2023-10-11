from .animal import Animal
from movements import Walking, Swimming


class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food, chip_num):
        self.chip_number = chip_num
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def honk(self):
        print(f"{self} honks, A lot")

    def run(self):
        print(f'{self} waddles')

    def __str__(self) -> str:
        return f'{self.name} the Goose'
