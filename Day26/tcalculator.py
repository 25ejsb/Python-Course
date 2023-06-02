weather_celsuis = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

fahrenheit = {temperature:((weather_celsuis[temperature]*(9/5))) + 32 for temperature in weather_celsuis}
print(fahrenheit)