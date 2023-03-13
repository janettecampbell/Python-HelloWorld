# Classes

class Person:
    def __init__(self, name):
        self.name = name

    def talk (self):
        print(f"Hi! I am {self.name}.")


jane = Person("Jane")
print(jane.name)
jane.talk()

bob = Person("Bob")
print(bob.name)
bob.talk()