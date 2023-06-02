import csv, pandas
with open("Day25/weather.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)

data = pandas.read_csv("Day25/weather.csv")
print(data["temp"])