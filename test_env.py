import os
from dotenv import load_dotenv

load_dotenv()

keys = [
    "WORDPRESS_URL",
    "WORDPRESS_USER",
    "WORDPRESS_APP_PASS",
    "OPENROUTER_API_KEY",
    "FIREBASE_CRED_PATH",
    "FIREBASE_DB_URL"
]

print("🔍 .env Environment Variable Test:")

for key in keys:
    value = os.getenv(key)
    if value:
        print(f"✅ {key} = {value}")
    else:
        print(f"❌ {key} NOT FOUND! कृपया .env फाईल तपासा.")
