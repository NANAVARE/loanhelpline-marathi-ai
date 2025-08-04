import os
import json
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv()

class FirebaseConnector:
    def __init__(self):
        # 🔧 Absolute path resolve करा
        key_path = os.getenv("FIREBASE_CRED_PATH")
        key_path = os.path.abspath(key_path)

        db_url = os.getenv("FIREBASE_DB_URL")

        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate(key_path)
                firebase_admin.initialize_app(cred, {
                    'databaseURL': db_url
                })
                print("✅ Firebase कनेक्शन यशस्वी")
            except Exception as e:
                print(f"❌ Firebase init त्रुटी: {e}")

    def push_lead_form(self, html_file):
        if not os.path.exists(html_file):
            print(f"❌ HTML फाईल सापडली नाही: {html_file}")
            return

        with open(html_file, "r", encoding="utf-8") as f:
            form_html = f.read()

        try:
            ref = db.reference("/loan_forms/latest")
            ref.set({
                "form_html": form_html
            })
            print("✅ Lead Form Firebase वर पाठवला.")
        except Exception as e:
            print(f"❌ Firebase push त्रुटी: {e}")
