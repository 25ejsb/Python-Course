# FileNotFound
# with open("Day30/newfile.txt") as file:
#     file.read()

# KeyError
# dictonary = {"key": "value"}
# value = dictonary["NonExist"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit_list = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:
    fruit_list = ["Apple", "Banana", "Pear"]
    fruit_list = fruit_list[3]
except IndexError as error_msg:
    print("Bro, how did you get this wrong? Thankfully, I'm here to save you.")
    print(error_msg)
else:
    print("Nice job! Now move on.")
finally:
    print("Hope my job paid off!")

try:
   text = "abc"
   print(text + "5")
except IndexError as error_msg:
    print("HOW DID YOU GET IT WRONG AGAIN??? STOP FAILING.")
    print(error_msg)
else:
    print("You did it! You got the code right!")
finally:
    print("Am I helpful?")

# If you just put except, every error will be included

try:
    with open("Day30/newfile.txt") as file:
        file.read()
except:
    print("Oops, you made a mistake, but I'm here to help!")
    with open("Day30/newfile.txt", mode="w") as file:
        file.write("Welcome to your new file! What would you like to write?")
else:
    print("Nice work! Your work paid off.")
finally:
    print("Hope my work helped!")
    raise TypeError("Never gonna give you up, never gonna let you down.")