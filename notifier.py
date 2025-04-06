from twilio.rest import Client
import os

def notify_user(message):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("USER_PHONE_NUMBER")
    )
