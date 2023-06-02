finalAge = 90
days = 365
weeks = 52
months = 12
age = int(input("What is your age? "))

finalDays = days * (finalAge-age)
finalWeeks = weeks * (finalAge-age)
finalMonths = months * (finalAge-age)

print(f"You have {finalDays} days, {finalWeeks} weeks, and {finalMonths} months")