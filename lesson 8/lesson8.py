class Person:
    def __init__(self, name, age):
        self.name = name
        self.age=age
    def greet(self):
        print(f"Hello i am {self.name} and i am {self.age}")


person1 = Person("Arion",24)
person2 = Person("Camavinga",23)
