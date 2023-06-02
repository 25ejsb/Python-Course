def add(*args):
    # you can also use positional arguments
    print(args[0])
    newNum = 0
    for n in args: 
        newNum += n
    return newNum
print(add(103, 23329, 338128))

def calculate(n, **kwargs):
    # turn the kwargs into a dictonary
    print(kwargs)
    for (key, value) in kwargs.items():
        print(key, value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car():
    def __init__(self, **kw):
        # .get() is basically getting something from the dictonary, but returns nothing if it doesn't exist
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GTR", color="red", seats=3)
print(my_car.model)