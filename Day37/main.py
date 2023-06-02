import requests
from datetime import datetime

# graph https://pixe.la/v1/users/straight/graphs/graph1

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "fs81284fudu0"
USERNAME = "straight"
GRAPHID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# add user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": user_params["token"]
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

pixel_data = {
    "date": "".join([date for date in str(datetime.today()).split(" ")[0].split("-")]),
    "quantity": "9.74"
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{pixel_data['date']}"
new_pixel_data = {
    "quantity": "4.5"
}
# response = requests.put(update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{pixel_data['date']}"

response = requests.delete(delete_endpoint, headers=headers)
print(response.text)