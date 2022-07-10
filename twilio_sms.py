import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

if os.getenv("TWILIO_ENABLED").upper() in ["YES", "ON", "TRUE", "1"]:
    TWILIO_ENABLED = True
else:
    TWILIO_ENABLED = False

ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TO_NUMBER = os.getenv("TWILIO_TO_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms(message):
    if TWILIO_ENABLED:
        message = client.messages \
                        .create(
                            body=message,
                            from_=FROM_NUMBER,
                            to=TO_NUMBER
                        )

        print(message.sid)
