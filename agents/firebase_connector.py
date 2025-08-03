import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

FIREBASE_URL = os.getenv("FIREBASE_URL")  # Example: https://your-project.firebaseio.com/leads.json

class FirebaseConnector:
    def __init__(self):
        self.url = FIREBASE_URL

    def push_lead(self, lead_data):
        if not self.url:
            print("❌ FIREBASE_URL .env मध्ये सेट केलेले नाही.")
            return

        response = requests.post(self.url, json=lead_data)
        if response.status_code == 200:
            print("✅ लीड Firebase मध्ये यशस्वीरित्या सेव्ह झाला.")
        else:
            print(f"❌ त्रुटी: {response.status_code} | {response.text}")