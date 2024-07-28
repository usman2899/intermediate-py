class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]


student_results_simple = []
student_results_adv = []

for student in students:
    if (student.score >= 0.7):
        student_results_simple.append(f"{student.name} passed")
    else:
        student_results_simple.append(f"{student.name} failed")
print(student_results_simple)

for student in students:
    student_results_adv.append(f"{student.name} passed") if (student.score >= 0.7) else student_results_adv.append(f"{student.name} failed")
print(student_results_adv)

map_res = list(map(lambda student: f"{student.name} passed" if (student.score >= 0.7) else f"{student.name} failed", students))
print(map_res)

#Functional programming: Less lines but difficult to understand


# Challenge: Use map to mulltiply all these numbers by 2

numbers = [1,2,3,4,5]

map_mul = list(map(lambda number: number * 2, numbers))
print(map_mul)