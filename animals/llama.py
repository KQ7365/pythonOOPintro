from animals.animal import Animal
from datetime import date


class Llama(Animal):
    def __init__(self, name, species, shift, food, chip_num) -> None:
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def feed(self):
        print(
            f'on {date.today()}, {self.name} had a melody sung to it so it would eat its {self.food}')
