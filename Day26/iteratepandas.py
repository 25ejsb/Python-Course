import pandas
students_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [65, 76, 98]
}

for (key, value) in students_dict.items():
    print(value)

data_frame = pandas.DataFrame(students_dict)
print(data_frame)

for (key, value) in data_frame.items():
    print(value)

for (index, row) in data_frame.iterrows():
    print(row)