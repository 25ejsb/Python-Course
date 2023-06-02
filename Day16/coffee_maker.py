from menu import coffees

def make_coffee(coffee, quarters, dimes, nickels, pennies):
    amount = 0
    for i in range(quarters): amount += .25
    for i in range(dimes): amount += .10
    for i in range(nickels): amount += .05
    for i in range(pennies): amount += .01
    if coffee in coffees:
        if amount > coffees[coffee]:
            return f"Here is your {coffee}!, ${round(amount-coffees[coffee], 2)} refunded"
        elif amount == coffees[coffee]:
            return f"Here is your {coffee}!"
        else:
            return "Not enough money!"