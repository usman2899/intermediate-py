import random


class Dog:
    info = "a dog is"

    def __init__(self, name):
        print("Constructor run")
        self.random_num = random.randint(1,5)
        self.name = name

    def bark(self, sound):
        print(f"{self.name} makes sound: {sound}")

    def newAgePrint(self, years):
        print(f"Age after {years} years is {self.age + years}")

    def newAgeReturn(self, years):
        return self.age + years

print(Dog.info)

dog1 = Dog('Jack')
dog1.bark('Aooooo')
dog1.age = 2
dog1.newAgePrint(3)

dog1.newAge = dog1.newAgeReturn(3)
print(dog1.newAge)


#Average
class Student:
    scores = [65,75,85,95]

    def average_score(self):
        sum = 0

        for score in self.scores:
            sum += score

        count = len(self.scores)
        return sum/count

student = Student()
print(student.average_score())

https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={9d55cacb9eea4865b92a29a960e8dffc}

