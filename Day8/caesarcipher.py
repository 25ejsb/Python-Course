import caesarart

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesarart.logo)

print("Welcome to Caesar Cipher!")

# USE alphabet.index() to find the index easier

def redo():
    answer = input("Would you like to restart (Y or N)? ")
    if answer.lower() == "y":
        main()

def caesar(text, shift, mode):
    newlist = []
    num = 0
    if mode == "encode":
        for i in range(len(alphabet)):
            if (shift+num) >= len(alphabet):
                num = 0
                shift = 0
                newlist.append(alphabet[shift+num])
            else:
                newlist.append(alphabet[shift+num])

            num += 1
    else:
        for i in range(shift):
            num = len(alphabet)-shift
            newlist.append(alphabet[num])
            num += 1
    
        num = 0

        for i in range(len(alphabet)-shift):
            newlist.append(alphabet[num])
            num += 1
    
    newText = ""
    for i in text:
        if i in alphabet:
            for j in range(len(alphabet)):
                if alphabet[j] == i:
                    newText = newText + newlist[j]
        else:
            newText = newText + i
    
    return "Your new encoded text is: " + newText


def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    print(caesar(input("Type your message: ").lower(), int(input("Type the shift number: ")), direction))
    redo()

main()