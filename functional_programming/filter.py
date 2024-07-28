class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self): #https://docs.python.org/3/library/functions.html#repr
        return f"{self.name}: {self.score}"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]

failing_students = []

for student in students:
    if student.score < 0.7:
        failing_students.append(student)
print(failing_students)

filter_list = list(filter(lambda student: student.score < 0.7, students))
print(filter_list)

# Challenge: Use filter to list all even numbers

numbers = [1,2,3,4,5]

filter_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(filter_numbers)


#Test
class Student:
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def __repr__(self): 
		return f"{self.name}: {self.score}"
	
students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63), Student("Mary", 0.55)]

def m_students():
	filter_students = list(filter(lambda student: student.name[0] == 'M', students))
	return filter_students
