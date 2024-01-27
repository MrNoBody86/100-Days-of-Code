import datetime as dt
import smtplib
import random

EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

now = dt.datetime.now()

day_of_week = now.weekday()

if day_of_week == 0 :
    with open(file="Day-30to39\\Day-32\\quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list).strip()

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject :Monday Motivation \n\n {quote}"
        )





# import smtplib


# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=EMAIL,password=PASSWORD)
#     connection.sendmail(
#         from_addr=EMAIL,
#         to_addrs="mrnobody10307@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of the email."
#     )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=2003,month=9,day=16,hour=3)
# print(date_of_birth)
