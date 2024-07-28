import random

class Animal: 
    info = "Animal info"

    def __init__(self):
        print("Animal constructor")

#if info here uncommeneted then parent overrriden and we get "Dog info"
class Dog(Animal):
    info = "Dog info"

    def __init__(self, name):
        super().__init__()
        print("Dog constructor")
        self.name = name

    def bark(self, sound):
        print(f"{self.name} makes sound: {sound}")

class Bulldog(Dog):

    def __init__(self, name):
        super().__init__(name)
        print("Bulldog constructor")


dog1 = Bulldog('Jack')
print(Dog.info)
print(dog1.name)
