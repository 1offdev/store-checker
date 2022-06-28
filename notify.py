import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("PUSHOVER_TOKEN")
USER = os.getenv("PUSHOVER_USER")
URL = os.getenv("PUSHOVER_URL")


def pushNotify(message):
    """Sends a message using https://pushover.net/api"""
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
