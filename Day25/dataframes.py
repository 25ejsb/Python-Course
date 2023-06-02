import pandas
data = pandas.read_csv("Day25/weather.csv")
print(type(data["temp"]))

# turns to dictonary
data_dict = data.to_dict()
print(data_dict)

# turns to list
temp_list = data["temp"].to_list()
print(len(temp_list))

# dont do this
number = sum(temp_list) / len(data["temp"])
print(number)
# do this
print(data["temp"].mean())

# gets highest temperature
print(data["temp"].max())

# Get Data in Columns
print(data.condition)

# Change values

def fahrenheit(num):
    return (num * (9/5)) + 32

monday = data[data.day == "Monday"]
data[monday.temp] = fahrenheit(monday.temp)

# Get Data in Row
print(data[data.day == "Monday"])

# Get the max row
print(data[data.temp == data.temp.max()])

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

# turn the data to csv

data.to_csv("Day25/new_data.csv")