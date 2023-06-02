travel_log = [
    {
        "country": "Canada",
        "visits": 3,
        "cities": ["Toronto", "Ottowa", "Niagara Falls"]
    },
    {
        "country": "Israel",
        "visits": 2,
        "cities": ["Haifa", "Jerusalem", "Tel Aviv"]
    }
]

def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})

add_new_country("China", 5, ["Shanghai", "Bejing", "Shenzen"])
print(travel_log)