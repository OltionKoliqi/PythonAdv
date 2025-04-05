class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi, I'm", self.name)

p1 = Person("Oltion")
p1.greet()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)

r = Rectangle(5,5)
r.area()


class Pet:
    def __int__(self, name, age, species, breed, color):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.color = color
def make_sounds(self):
    if self.species() == "dog":
        return "Woof Woof"
    elif self.species() == "cat":
        return "Meow"
    else:
        return "Unknown sound"

def sleep(self):
    print(f"{self.species()} is sleeping")
def eat(self):
    print(f"{self.species} is eating")





