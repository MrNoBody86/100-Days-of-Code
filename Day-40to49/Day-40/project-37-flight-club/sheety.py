import requests
import os

BEARER = os.environ.get("SHEETY_BEARER")
USERNAME = os.environ.get("SHEETY_USERNAME")

PROJECT = "flightDeals"
SHEET = "users"

BASE_URL = "https://api.sheety.co"

def post_new_row(first_name,last_name,email):
    
    endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    url = BASE_URL + endpoint_url
    new_data = {
    "user" : {
        "firstName" : first_name,
        "lastName" : last_name,
        "email" : email
    }
    }

    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }

    response = requests.post(url=url, json=new_data,timeout=None,headers=headers)
    response.raise_for_status()
    print(response.text)
