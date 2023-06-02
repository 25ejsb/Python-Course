class Animal():
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, exhale")

# for inheritance, get the class of choice
class Fish(Animal):
    def __init__(self):
        # This gets everything from the Animal Class and adds it to the Fish class
        super().__init__()
    
    def breathe(self):
        # gets everything from the animal breathe function
        super().breathe()
        # this adds on
        print("Doing this underwater")

    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()