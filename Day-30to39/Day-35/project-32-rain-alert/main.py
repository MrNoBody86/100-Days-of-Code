import os
import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_id = "Your API_KEY"

account_sid = "YOUR_SID"
auth_token = "Your AUTH_TOKEN"

parameter = {
    "lat" : 30,
    "lon" :  78,
    "appid" : api_id,
    "cnt" : 4,
}

response = requests.get(url= OWM_Endpoint,
                        timeout= None,
                        params= parameter,
                        )
response.raise_for_status()
weather_data = response.json()["list"]

will_rain = False

for hour_data in weather_data :
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700 :
        will_rain = True

if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☔",
                     from_='+19254063531',
                     to='+919970106137'
                 )
    
    print(message.status)