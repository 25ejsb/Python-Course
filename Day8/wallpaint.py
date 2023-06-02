import math
def canAmount(width, height, coverage): 
    return f"You need {math.ceil((height * width) / coverage)} cans to cover this wall." 

print(canAmount(float(input("Enter your wall height: ")), float(input("Enter your wall width: ")), float(input("Enter your wall coverage: "))))