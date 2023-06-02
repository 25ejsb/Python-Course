# Error, TypeError: '>' not supported between instances of 'str' and 'int', that means a str is being compared to an int
age = input("How old are you? ")
if age > 18:
    print(f"You can't drive at the age {age}")
else:
    print(f"You can drive at the age {age}")

# Solved
age = int(input("How old are you? "))
if age > 18:
    print(f"You can't drive at the age {age}")
else:
    print(f"You can drive at the age {age}")