newHeight = int(input("Enter your height: "))
newWeight = int(input("Enter your weight: "))

if (newHeight * newWeight) > 100:
    raise TypeError("Person is too fat.")