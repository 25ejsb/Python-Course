# Problem

def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it!")

my_function()

# Solved, whats happening here is range is starting at 0, not 1, so you need to add 1

def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it!")

my_function()

# Problem

from random import randint
dice_imgs = ["🎲1", "🎲2", "🎲3", "🎲4", "🎲5", "🎲6"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# Solved, can you see the issue?

from random import randint
dice_imgs = ["🎲1", "🎲2", "🎲3", "🎲4", "🎲5", "🎲6"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])