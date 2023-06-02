enemies = 1


def increaseEnemies():
    # this is now local
    # enemies += 1 -- This code right here uses the error refrenced before assignment
    global enemies
    enemies += 1
    # the global is dangerous because it could have been created anyone in your code, and you would be editing it
    print(f"Enemies inside function: {enemies}")

increaseEnemies()
print(f"enemies outside function: {enemies}")

# The weirdness of python
enemies = ["Skeleton", "Zombie", "Enderman"]
game_level = 3
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# how to avoid global mess ups, uppercase your vars
URL = "https://shulmanrealtor.com"
PI = 3.141592653589793235
twitter = "@eitantravels"