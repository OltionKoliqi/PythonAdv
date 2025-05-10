class Animal:
    def sound(self):
        print("Make a sound")

class Dog(Animal):
    def sound(self):
        print("Ham Ham")

class Cat(Animal):
    def sound(self):
        print("Meow Meow")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()