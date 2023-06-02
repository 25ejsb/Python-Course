sentence = input("Enter a sentence: ").split(" ")
new_dict = {letters:len(letters) for letters in sentence}
print(new_dict)