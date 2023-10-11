from animals.animal import Animal


class Shark(Animal):
    def __init__(self, name, species, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.swimming = True
