import os
import requests

SHEETY_PRICES_ENDPOINT = YOUR SHEETY PRICES ENDPOINT
SHEETY_USERS_ENDPOINT = YOUR SHEETY USERS ENDPOINT

BEARER = os.environ.get("SHEETY_BEARER")
USERNAME = os.environ.get("SHEETY_USERNAME")

headers = {
                "Authorization": f"Bearer {BEARER}",
                "Content-Type": "application/json",
            }

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,timeout=None,headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                timeout=None,
                headers=headers
            )
            print(response.text)

    def get_customer_email(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT,timeout=None,headers=headers)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data
