class Kids:
    
    def __init__(self, age, height):
        self.age = age
        self.height = height

John = Kids(20, 150)

age = John.age
height = John.height

#and
if age >= 8 and height >= 150:
    print("You can ride!")

#or
if age >= 17 or height >= 150:
    print("You can do easy ride") 

#elif (else if)
if height < 120:
    print("Go home")

elif height > 120 and height < 135:
    print("Easy ride")

else:
    print("Too tall")