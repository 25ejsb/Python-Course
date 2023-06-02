student_scores = {
    "Eitan": 100,
    "Timmy": 94,
    "Johnny": 56,
    "Noah": 72,
}

for i in student_scores:
    if student_scores[i] <= 70:
        print(i + " = Failure")
    elif student_scores[i] <= 80:
        print(i + " = Acceptable")
    elif student_scores[i] <= 90:
        print(i + " = Exceeds Expectations")
    else:
        print(i + " = Outstanding")