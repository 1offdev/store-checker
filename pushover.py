import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

if os.getenv("PUSHOVER_ENABLED").upper() in ["YES", "ON", "TRUE", "1"]:
    PUSHOVER_ENABLED = True
else:
    PUSHOVER_ENABLED = False

TOKEN = os.getenv("PUSHOVER_TOKEN")
USER = os.getenv("PUSHOVER_USER")
URL = os.getenv("PUSHOVER_URL")


def push_notify(message):
    """Sends a message using https://pushover.net/api"""
    if PUSHOVER_ENABLED:
        payload = json.dumps({
            "token": TOKEN,
            "user": USER,
            "html": 1,
            "message": message
        })
        headers = {
            'Content-Type': 'application/json'
        }

        requests.request("POST", URL, headers=headers, data=payload)
