from attractions.attraction import Attraction


class Wetland(Attraction):

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
