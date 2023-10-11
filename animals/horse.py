from animals.animal import Animal
from movements import Walking


class Horse(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num) -> None:
        Animal.__init__(self, name, species, food, chip_num)
        # This has the speed in it. I dont need to declare anything
        Walking.__init__(self)
        self.shift = shift
