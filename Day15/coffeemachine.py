coffees = {
    "espresso": 1.5,
    "latte": 2.5,
    "cappuccino": 3
}

coffessList = ["espresso", "latte", "cappucino"]

def buyCoffee(coffee):
    money = 0
    print("Please insert coins.")
    if coffee.lower() in coffessList:
        quarters = int(input("How many quarters? "))
        for i in range(quarters):
            money += .25
        dimes = int(input("How many dimes? "))
        for i in range(dimes):
            money += .10
        nickels = int(input("How many nickels? "))
        for i in range(nickels):
            money += .05
        pennies = int(input("How many pennies? "))
        for i in range(pennies):
            money += .01
        
        if coffees[coffee] < money:
            print(f"Thanks! Here is your {coffee}.")
            print(f"Here is ${round(money-coffees[coffee], 2)} cash back.")
        elif coffees[coffee] == money:
            print(f"Thanks! Here is your {coffee}.")
        else:
            print("Not enough cash, most refunded.")

while True:
    buyCoffee(input("What would you like (espresso, latte, cappuccino)? "))