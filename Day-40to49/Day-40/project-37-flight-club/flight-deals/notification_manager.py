import os
import smtplib
from twilio.rest import Client

TWILIO_SID = os.environ.get("SID")
TWILIO_AUTH_TOKEN = os.environ.get("Auth_token")
TWILIO_VIRTUAL_NUMBER = YOUR TWILIO VIRTUAL NUMBER
TWILIO_VERIFIED_NUMBER = YOUR TWILIO VERIFIED NUMBER
EMAIL = YOUR EMAIL
PASSWORD = os.environ.get("email_password")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self,message,user):
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=user,
                msg= f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
            )

