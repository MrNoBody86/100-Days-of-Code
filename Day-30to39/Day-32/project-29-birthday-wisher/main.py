import random
import datetime as dt
import smtplib
import pandas as pd

PLACEHOLDER = "[NAME]"
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"


today = dt.datetime.now()
day = today.day
month = today.month

df = pd.read_csv("Day-30to39\\Day-32\\project-29-birthday-wisher\\birthdays.csv")
birthday_list = df.to_dict(orient="records")

for birthday in birthday_list :
    if birthday["day"] == day and birthday["month"] == month:
        with open(
            file=f"Day-30to39\Day-32\project-29-birthday-wisher\letter_templates\letter_{random.randint(1,3)}.txt"
        ) as letter_file :
            letter = letter_file.read()
            final_letter = letter.replace(PLACEHOLDER,birthday["name"])

        with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday! \n\n {final_letter}"
            )
