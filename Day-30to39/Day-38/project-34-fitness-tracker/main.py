import os
import requests
from datetime import datetime

APP_ID = os.environ.get("NL_APP_ID")
API_KEY = os.environ.get("NL_API_KEY")
NL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/407bd5b3fc8ff807ff0ce54e08b178fd/myWorkouts/workouts"
BEARER = os.environ.get("BEARER")

GENDER = "Male"
WEIGHT_KG = 85
HEIGHT_CM = 185.42
AGE = 20
TEXT = input("Tell me which exercises you did: ").title()

query = {
    "query" : TEXT ,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nl_header = {
    "Content-Type" : "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

response = requests.post(url=NL_ENDPOINT,timeout=None,json=query,headers=nl_header)
response.raise_for_status()
new_data = response.json()


today = datetime.now()

for exercise in new_data["exercises"]:
    sheet_input = {
        "workout" : {
            "date" : today.strftime("%d/%m/%Y"),
            "time" : today.strftime("%H:%M:%S"),
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }

sheety_header = {
    "Authorization" : f"Bearer {BEARER}"
}

sheety = requests.post(url=SHEETY_ENDPOINT,timeout=None,json=sheet_input,headers=sheety_header)
old_data = sheety.json()
print(old_data)