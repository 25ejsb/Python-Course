weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")
floatEquation = float(weight) / float(height)**2
intEquation = int(floatEquation)
equation = round(intEquation, 1)


if equation < 18.5:
    print(f"Your BMI is {equation}, you are underweight")
elif equation >= 18.5 and equation < 25:
    print(f"Your BMI is {equation}, you have a normal weight")
elif equation >= 25 and equation < 30:
    print(f"Your BMI is {equation}, you are overweight")
elif equation >= 30 and equation < 35:
    print(f"Your BMI is {equation}, you are obese")
else:
    print(f"Your BMI is {equation}, you are clinically above")