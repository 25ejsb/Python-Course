from random import *
names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
student_scores = {student:randint(1, 100) for student in names}
print(student_scores)

passed_students = {student:student_scores[student] for student in student_scores if student_scores[student] > 60}
print(passed_students)