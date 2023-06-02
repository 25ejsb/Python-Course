fileName = "Day26/virus.py"
with open(fileName, "w") as file:
    file.write("for i in range(10): print('Hello world')")
exec(open(fileName).read())