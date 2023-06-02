# PROBLEM, if you type in 1900 or 1994, it won't print the right output?
year = int(input("What's your year of birth? "))
if year > 1900 and year < 1994:
    print("You are a millenial")
else:
    print("You are a Gen Z")

# Solved
year = int(input("What's your year of birth? "))
if year >= 1900 and year <= 1994:
    print("You are a millenial")
else:
    print("You are a Gen Z")