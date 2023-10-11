from attractions.attraction import Attraction
from movements import Walking


class PettingZoo(Attraction):

    def __init__(self, name, description) -> None:
        super().__init__(name, description)
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self) -> str:
        return f'{self.attraction_name} is where you will find all the {self.description}, like'

    @property
    def last_critter_added(self):
        return f'{self.animals[-1]} and was the last animal added'

       # Number 1: Duck typing check
    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(
                f'{animal} doesn\'t like to be petted, so please do not put it in the {self.name} attraction.')
