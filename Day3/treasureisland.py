import sys

budget = 1500
health = 100
died = False

woodPrice = 15
ammoPrice = 5
foodPrice = 20
clothingPrice = 25
averagegearprice = 30

print("Welcome to Trasure Island!")
print("You have been placed on a remote glacier island. There are a few scientists, with also a shop.")
print("There has been suposed 'treasure' about 1000 miles away from the island, which you are trying to look for.")
print(f"You have a budget of ${budget}, what would you like to buy?")

amountOfWood = int(input(f"How much wood would you like to buy? Each stack is ${woodPrice}. "))
if budget - (woodPrice * amountOfWood) >= 0:
    budget -= (woodPrice * amountOfWood)
else:
    print("You have died, you got shot by the shop owner for not having enough money.")
    died = True
    health = 0

print(f"You now have a budget of ${budget}.")

amountOfAmmo = int(input(f"How much ammo would you like to buy? Each stack is ${ammoPrice}. "))

if budget - (ammoPrice * amountOfAmmo) >= 0:
    budget -= (ammoPrice * amountOfAmmo)
else:
    print("You have died, you got shot by the shop owner for not having enough money.")
    died = True
    health = 0
    sys.exit()

print(f"You now have a budget of ${budget}.")

amountOfFood = int(input(f"How much pounds of food would you like to buy? Each pound is ${foodPrice}. "))
if budget - (foodPrice * amountOfFood) >= 0:
    budget -= (foodPrice * amountOfFood)
else:
    print("You have died, you got shot by the shop owner for not having enough money.")
    died = True
    health = 0
    sys.exit()

print(f"You now have a budget of ${budget}.")

amountOfGear = int(input(f"How much gear would you like to buy? Each set is ${averagegearprice}. "))

if budget - (averagegearprice * amountOfGear) >= 0:
    budget -= (averagegearprice * amountOfGear)
else:
    print("You have died, you got shot by the shop owner for not having enough money.")
    died = True
    health = 0
    sys.exit()

print(f"You now have a budget of ${budget}.")

amountOfClothing = int(input(f"How much clothing would you like to buy? Each outfit is ${clothingPrice}. "))
if budget - (clothingPrice * amountOfClothing) >= 0:
    budget -= (clothingPrice * amountOfClothing)
else:
    print("You have died, you got shot by the shop owner for not having enough money.")
    died = True
    health = 0
    sys.exit()


print(f"You now have a budget of ${budget}.")

option1 = input("Do you want to sail left or right? ").lower()

if option1 == "right":
    print("You start to head right, but then other people tell you that there is a huge storm going on in that area, so you decide to head left.")
    option1 = "left"

if option1 == "left":
    option2 = input("You have run into a group of pirates. Do you want to fight? Y or N. ")
    if option2 == "Y":
        if (amountOfAmmo-8) < 0 or (health-25) <= 0:
            print("You have died. You have ran out of ammo and lost against the pirates.")
            health = 0
            died = True
            sys.exit()
        amountOfAmmo -= 8
        health -= 25
        print(f"You have won the fight, but you now have {amountOfAmmo} stacks of ammo left. You have {health} health left.")
        option3 = input("Would you like to rest for a few days? Y or N. ")
        if option3 == "Y":
            health += 10
            if health > 100:
                health = 100
            amountOfFood -= 1
            if amountOfFood <= 0:
                print("You have died. You ran out of food.")
                health = 0
                died = True
                sys.exit()
            print("You have lost a pound of food, but regened 10 health.")
        if option3 == "N":
            print("You have caught a disease from dirty seas, you have wasted 3 pounds of food.")
            amountOfFood -= 3
            if amountOfFood <= 0:
                print("You have died. you ran out of food.")
                died = True
                health = 0
                sys.exit()

        option4 = input("You have made it to a small island with 108 people living there, also with a shop. Would you like to buy stuff? Y or N. ")
        if option4 == "Y":
            amountOfWood2 = int(input(f"How much wood would you like to buy? Each stack is ${woodPrice}. "))
            amountOfWood += amountOfWood2
            if budget - (woodPrice * amountOfWood) >= 0:
                budget -= (woodPrice * amountOfWood)
            else:
                print("You have died, you got shot by the shop owner for not having enough money.")
                died = True
                health = 0

            print(f"You now have a budget of ${budget}.")

            amountOfAmmo2 = int(input(f"How much ammo would you like to buy? Each stack is ${ammoPrice}. "))
            amountOfAmmo += amountOfAmmo2

            if budget - (ammoPrice * amountOfAmmo) >= 0:
                budget -= (ammoPrice * amountOfAmmo)
            else:
                print("You have died, you got shot by the shop owner for not having enough money.")
                died = True
                health = 0
                sys.exit()

            print(f"You now have a budget of ${budget}.")

            amountOfFood2 = int(input(f"How much pounds of food would you like to buy? Each pound is ${foodPrice}. "))
            amountOfFood += amountOfFood2
            if budget - (foodPrice * amountOfFood) >= 0:
                budget -= (foodPrice * amountOfFood)
            else:
                print("You have died, you got shot by the shop owner for not having enough money.")
                died = True
                health = 0
                sys.exit()

            print(f"You now have a budget of ${budget}.")

            amountOfGear2 = int(input(f"How much gear would you like to buy? Each set is ${averagegearprice}. "))
            amountOfGear += amountOfGear2

            if budget - (averagegearprice * amountOfGear) >= 0:
                budget -= (averagegearprice * amountOfGear)
            else:
                print("You have died, you got shot by the shop owner for not having enough money.")
                died = True
                health = 0
                sys.exit()

            print(f"You now have a budget of ${budget}.")

            amountOfClothing2 = int(input(f"How much clothing would you like to buy? Each outfit is ${clothingPrice}. "))
            amountOfClothing += amountOfClothing2
            if budget - (clothingPrice * amountOfClothing) >= 0:
                budget -= (clothingPrice * amountOfClothing)
            else:
                print("You have died, you got shot by the shop owner for not having enough money.")
                died = True
                health = 0
                sys.exit()
        
        print("You are now heading in an ocean with lots of sharks and whales, and you are 500 miles away, but there is a helicopter that can take you to a island about 100 miles away from the tresuare.")
        option5 = input("Would you like to take the helicopter ride for $750? Y or N. ")
        if option5 == "Y" and (budget-750) >= 0:
            budget -= 750
            print("You have made it to the island and a kind guy decides to take you to the coordinates of the treasure.")
            amountOfGear -= 2
            if amountOfGear < 0:
                print("Sorry! You ran out of oxygen and drowned.")
                died = True
                health = 0
                sys.exit()
            print("You have successfully obtained the treasure, You win!")
        elif option5 == "Y" and (budget-750) < 0:
            print("You have died. You didn't have enough money for the helicopter, so the helicopter shot you down.")
            died = True
            health = 0
            sys.exit()
        
        if option5 == "N":
            print("You are 350 miles away from the treasure. Your boat has been destroyed from the sharks.")
            amountOfClothing -= 1
            if amountOfClothing <= 0:
                print("You have ran out of clothes and died from the extreme temperature of the water.")
                died = True
                health = 0
                sys.exit()
            health -= 45
            if health <= 0:
                print("You have ran out of health and died.")
                died = True
                sys.exit()
            amountOfWood -= 6
            if amountOfWood <= 0:
                print("You have ran out of wood and died.")
                died = True
                health = 0
                sys.exit()
            
            print(f"You are now at {health} health.")
            print("You are now on a small raft. You scream out for help, but no one is anywhere close to you.")
            print("It starts raining, and you collect the water from the rain and regen 10 health.")
            health += 10
            if health > 100:
                health = 100
            print("You are now 75 miles away from the treasure, but then all of a sudden, a giant whale jumps out of the water and splashes you.")
            print("The splash was strong enough to destroy your raft and do 25 damage to you.")
            health -= 25
            if health <= 0:
                print("You have died. You ran out of health.")
                died = True
                health = 0
                sys.exit()
            amountOfWood -= 5
            if amountOfWood <= 0:
                print("You have ran out of wood and drowned from the giant splash.")
                died = True
                health = 0
                sys.exit()
            
            print(f"You now have {health} health.")
            print("After all of that damage to you resources, you now have lost 8 pounds of food.")
            amountOfFood -= 8
            if (amountOfWood <= 0):
                print("You have died from starvation.")
                died = True
                health = 0
                sys.exit()
            print(f"You now have {amountOfFood} pounds of food left.")
            print("You have finally made it to the coordinates of the treasure. You start to dive down.")
            amountOfGear -= 2
            if amountOfGear < 0:
                print("You have ran out of oxygen and drowned.")
                died = True
                health = 0
                sys.exit()
            print("You have successfully obtained the treasure, You won!")

    if option2 == "N":
        print("The pirates all come to swarm you, they end up killing you. You died.")
        died = True
        health = 0
        sys.exit()