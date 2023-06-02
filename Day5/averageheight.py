student_heights = input("Enter a list of student heights: ").split(", ")
numberCount = 0
for i in range(len(student_heights)):
    student_heights[i] = int(student_heights[i])
    numberCount += student_heights[i]

numberCount /= len(student_heights)
print("Average height: " + str(round(numberCount)))