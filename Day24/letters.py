with open("Day24/Names/invited_names.txt") as file:
    split = str.splitlines(str(file.read()))
    for i in split:
        with open("Day24/Letters/starting_letter.txt") as file2:
            split2 = str.split(str(file2.read()), " ")
            with open(f"Day24/Output/Letter_To_{i}.txt", "a") as file3:
                 for j in split2:
                    if j == "[name]":
                        file3.write(i + " ")
                    else:
                        file3.write(j + " ")