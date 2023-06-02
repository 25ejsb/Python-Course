def days_in_month(month, year):
    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    num = 0

    for i in range(len(months)):
        if month == months[i]:
            if months[i] != "February":
                num = monthdays[i]
            else:
                if year % 4 == 0 and year % 100 != 0:
                    num = 29
                    
                elif year % 4 == 0 and year % 400 == 0:
                    num = 29     
                else:
                    num = 28

    return f"There is {num} days in {month} {year}"

yearinput = int(input("Enter a year: "))
monthinput = input("Enter a month: ")
days = days_in_month(monthinput, yearinput)
print(days)