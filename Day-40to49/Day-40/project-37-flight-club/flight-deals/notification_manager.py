import os
from twilio.rest import Client

TWILIO_SID = os.environ.get("SID")
TWILIO_AUTH_TOKEN = os.environ.get("Auth_token")
TWILIO_VIRTUAL_NUMBER = +19254063531
TWILIO_VERIFIED_NUMBER = +919970106137


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
