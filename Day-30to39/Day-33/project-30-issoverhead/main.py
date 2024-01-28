from time import sleep
import requests
from datetime import datetime
import smtplib

MY_LAT = 18.520430 # Your Latitude
MY_LNG = 73.856743 # Your Longitude
MY_TZID = "Asia/Kolkata" # Your Time Zone
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json",timeout=69)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude in range(13,23) and iss_longitude in range(69,79):
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "tzid" : MY_TZID
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters,timeout=69)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if hour_now <= sunrise or hour_now >= sunset :
        return True

while True:
    if is_dark() and iss_overhead():
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject : LOOK UP👆! \n\n ISS OVERHEAD"
            )
    sleep(60)
# BONUS: run the code every 60 seconds.
