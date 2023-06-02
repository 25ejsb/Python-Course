def prime(num):
    num = int(num)
    listOfDivs = []
    for i in range(1, num):
        if num % i == 0:
            listOfDivs.append(i)
    
    listOfDivs.append("")
    
    if listOfDivs[0] == 1 and listOfDivs[1] == "":
        return "This number is prime."
    else:
        return "This number is not prime."

print(prime(input("Enter a number: ")))