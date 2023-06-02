print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
        bill += 5
    elif age <= 18:
        print("Please pay $7")
        bill += 7
    else:
        print("Please pay $12")
        bill += 12

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        print("You spent $3")
        bill += 3

    print(f"You have spent ${bill} dollars.")
    
else:
    print("You can't ride the rollercoaster!")