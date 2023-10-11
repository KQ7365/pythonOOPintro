from animals import Bass, Copperhead, Dolphin, Donkey, Goat, Goldfish, Grub, Horse, Llama, Pig, Shark, Slug, Snail, Whale, Worm, Goose
from attractions import PettingZoo, SnakePit, Wetland, PettingZoo
# from animals.animal import Animal


miss_fuzz = Llama("Miss Fuzz", "domestic Llama",
                  "morning", "Llama Chow", 12233)
miss_jane = Goat("Miss Jane", "domestic Goat", "afternoon", "goat oats", 143)
miss_suzy = Donkey("Miss Suzy", "domestic Donkey",
                   "morning", "donkey pellets", 886)
miss_fran = Horse("Miss Fran", "domestic Horse",
                  "evening", "horse treats", 992)
miss_sally = Pig("Miss Sally", "domestic Pig", "morning", "pig chips", 765)
mr_slim = Copperhead("Mr Slim", "wild Copperhead", "snake snacks", 555)
mr_bert = Slug("Mr Bert", "wild Slug", "slug treats", 324)
mr_ernie = Snail("Mr Ernie", "wild Snail", "snail cakes", 777)
mr_carter = Worm("Mr Carter", "wild Worm", "work delights", 775)
mr_john = Grub("Mr John", "wild Grub", "grub rounds", 169)
ms_vicky = Goldfish("Ms Vicky", "domestic Goldfish",
                    "goldfish crackers", 65412)
ms_monica = Bass("Ms Monica", "wild Bass", "bass hook treats", 9765432)
ms_july = Shark("Ms July", "wild Shark", "shark sticks", 34343)
ms_becky = Whale("Ms Becky", "wild Whale", "whale watcher treats", 555)
ms_summer = Dolphin("Ms Summer", "tactical Dolphin", "dolphin cakes", 3222)
bob = Goose("Bob", "Canadian goose", "watercress sandwiches", 2222222)

# instances dot notation
print(mr_slim.species)


# below is activating the feed() method
miss_fuzz.feed()
# print(llama_method)

# below is activating the string method
print(miss_fuzz)

# naming each attraction
land_village = PettingZoo("Four Legged Village",
                          "four legged friends to cuddle")
slither_pit = SnakePit("Slimy Village", "creepy crawlers to touch")
wetland_water = Wetland(
    "Water Village", "all the underwater creatures to watch")
varmint_village = PettingZoo(
    "Varmint Village", "critters that like to dig and scurry")

# added animals to an attraction using the def function
land_village.add_animal(miss_fuzz)
land_village.add_animal(miss_jane)

slither_pit.add_animal(mr_ernie)

wetland_water.add_animal(ms_july)

varmint_village.add_animal(bob)

# displaying the attraction(string complied in Class) and then looping/displaying animals per attraction
print(land_village)
for animal in land_village.animals:
    print(f'    *{animal.name} the {animal.species}')

print(slither_pit)
for animal in slither_pit.animals:
    print(f'    *{animal.name} the {animal.species}')

print(wetland_water)
for animal in wetland_water.animals:
    print(f'    *{animal.name} the {animal.species}')

# displaying the chip number from using the @property. Notice how even though we tried
# to set it to 2, it cant change because of the setter function
miss_fuzz.chip_number = 2
print(miss_fuzz.chip_number)

# test last critter added getter function
land_village.add_animal(miss_sally)
print(land_village.last_critter_added)

bob.run()
bob.swim()
bob.honk()

for animal in varmint_village.animals:
    print(animal)

varmint_village.add_animal_pythonic(miss_fran)
