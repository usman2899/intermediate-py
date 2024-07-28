print("before")

try: 
    4/0
    # print(name)
except NameError:
    print("Name issue")
except ZeroDivisionError as e:
    print(e)

print("after")

#if this code below where exception raised: class MyError(Exception): pass
class MyError(Exception):
    pass

# def upper_case(word):
#     if len(word) == 0:
#         raise MyError("Null string")
#     return word.upper()
# print(upper_case(""))

class CustomTryCatch(Exception):
    pass

try:
    raise CustomTryCatch("My exception thrown")
except CustomTryCatch:
    print("My excetpion caught")
