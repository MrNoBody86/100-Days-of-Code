from datetime import datetime
import requests

USERNAME = "mrnobody"
TOKEN = "c8q94yt8ikial,krukrlq0"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params,timeout=None)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name":"Reading Graph",
    "unit" : "minutes",
    "type":"int",
    "color": "ajisai",
    "timezone": "Asia/Kolkata",
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers,timeout=None)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you read?: "),
}

response = requests.post(url=pixel_endpoint,json=pixel_data,headers=headers,timeout=None)
print(response.text)

pixel_update = {
    "quantity" : "15"
}

# response = requests.put(url=f"{pixel_endpoint}/{today.strftime('%Y%m%d')}",
#                         json=pixel_update,
#                         headers=headers,
#                         timeout=None)
# print(response.text)


# response = requests.delete(url=f"{pixel_endpoint}/20240206",
#                         headers=headers,
#                         timeout=None)
# print(response)
