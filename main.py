import requests
from datetime import datetime

USERNAME = "thomas1"
TOKEN = "evianwater"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "evianwater",
    "username": "thomas1",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2020, month=7, day=23)
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today?"),
}

update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"


response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


new_pixel_data = {
    "quantity": "15",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
