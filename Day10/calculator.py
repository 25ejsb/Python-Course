from calculatorart import logo
print(logo)
operations = ["+", "-", "*", "/", "^"]
for i in operations: print(i)
def calculate(f1, op, f2):
    if op == "+":
        return [f"{f1} {op} {f2} = {f1+f2}", f1+f2]
    elif op == "-":
        return [f"{f1} {op} {f2} = {f1-f2}", f1-f2]
    elif op == "*":
        return [f"{f1} {op} {f2} = {f1*f2}", f1*f2]
    elif op == "/":
        return [f"{f1} {op} {f2} = {f1/f2}", f1/f2]
    elif op == "^":
        return [f"{f1} {op} {f2} = {f1**f2}", f1**f2]
equation = calculate(float(input("What the first number? ")), input("Enter the operation: "), float(input("What the second number? ")))
print(equation[0])
while True:
    continInput = input("Would you like to continue with your previous equation 'y' or stop by typing 'n'? ")
    if continInput == "y":
        equation = calculate(equation[1], input("Enter the operation: "), float(input("What the second number? ")))
        print(equation[0])
    else: break