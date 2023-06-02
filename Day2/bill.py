print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = input("What would you like the tip percent to be? (10, 12, 15): ")
while tip != "10" and tip != "12" and tip != "15":
    print("Your tip percent is invalid")
    tip = input("What would you like the tip percent to be? (10, 12, 15): ")
split = int(input("How many people would you like to split the bill with? "))

tipPercent = int(tip)/100

amount = round((bill+(bill*tipPercent))/split, 2)
print(f"The bill for each is: ${amount}")