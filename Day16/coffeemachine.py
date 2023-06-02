import coffee_maker
while True:
    print(coffee_maker.make_coffee(
        input("Welcome to the coffee machine! Here is the menu: espresso, latte, cappuccino. What would you like? "), 
        int(input("How many quarters? ")),
        int(input("How many dimes? ")),
        int(input("How many nickels? ")),
        int(input("How many pennies? "))
    ))