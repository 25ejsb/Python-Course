row1 = ["😎", "😎", "😎", "😎", "😎", "😎"]
row2 = ["😎", "😎", "😎", "😎", "😎", "😎"]
row3 = ["😎", "😎", "😎", "😎", "😎", "😎"]
row4 = ["😎", "😎", "😎", "😎", "😎", "😎"]
row5 = ["😎", "😎", "😎", "😎", "😎", "😎"]
row6 = ["😎", "😎", "😎", "😎", "😎", "😎"]
newmap = [row1, row2, row3, row4, row5, row6]
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}")

position = input("Where would you like to position your mark (max column 5, max row 5)? ")

newmap[int(position[1])-1][int(position[0])-1] = "X"
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}")