# with open basically just opens the file and then when the codes done, closes it
with open("Day24/my_file.txt") as file:
    contents = file.read()
    print(contents)
# mode w makes it writeable since its set to only readable, but then you can't read the text
# mode w+ make it writeable and readable
with open("Day24/my_file.txt", mode="w+") as file:
    file.write("New Text")
# mode a appends to the file
with open("Day24/my_file.txt", mode="a") as file:
    file.write("\nMy new line")
# You have to close the file after code