from datetime import datetime
import requests

MY_LAT = 18.520430
MY_LNG = 73.856743
MY_TZID = "Asia/Kolkata"

# response = requests.get( url="http://api.open-notify.org/iss-now.json", timeout=69)
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude,latitude)

# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted" : 0,
    "tzid" : MY_TZID
}

response = requests.get("https://api.sunrise-sunset.org/json", timeout= 69 , params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


time_now = datetime.now()


