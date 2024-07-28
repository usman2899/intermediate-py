import random


class Dog:
    info = "a dog is"

    def __init__(self, name):
        print("Constructor run")
        self.random_num = random.randint(1,5)
        self.name = name


print(Dog.info)

dog1 = Dog('Jack')
print('Old name: ' + dog1.name)

dog1.name = "Tom"

print('Old name: ' + dog1.name)