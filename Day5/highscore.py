student_scores = input("Enter your classes scores: ").split(", ")

highscore = 0
meanscore = 0
for i in range(len(student_scores)):
    student_scores[i] = int(student_scores[i])
    meanscore += student_scores[i]
    if student_scores[i] > highscore:
        highscore = student_scores[i]

meanscore /= len(student_scores)
print(f"Your highest score was {highscore}. Your average score was {round(meanscore, 0)}")