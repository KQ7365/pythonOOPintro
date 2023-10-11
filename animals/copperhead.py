from animals.animal import Animal


class Copperhead(Animal):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.slithering = True
