# agents/wordpress_rest_agent.py

import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from utils.helpers import slugify_text

load_dotenv()

class WordPressRestAgent:
    def __init__(self):
        self.site_url = os.getenv("WORDPRESS_URL")
        self.username = os.getenv("WORDPRESS_USER")
        self.app_password = os.getenv("WORDPRESS_APP_PASS")
        self.auth = HTTPBasicAuth(self.username, self.app_password)

    def publish_post_from_file(self, file_path, title, meta=None, tags=None, categories=None):
        if not os.path.exists(file_path):
            print(f"❌ फाईल सापडली नाही: {file_path}")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        post = {
            "title": title,
            "content": content,
            "status": "publish",
            "slug": slugify_text(title),
        }

        if meta:
            post["meta"] = meta

        tag_ids = self._get_or_create_terms(tags or [], taxonomy="tags")
        cat_ids = self._get_or_create_terms(categories or [], taxonomy="categories")
        if tag_ids:
            post["tags"] = tag_ids
        if cat_ids:
            post["categories"] = cat_ids

        url = f"{self.site_url}/wp-json/wp/v2/posts"
        print(f"📌 REST API URL: {url}")
        response = requests.post(url, auth=self.auth, json=post)

        if response.status_code == 201:
            data = response.json()
            print("✅ पोस्ट यशस्वीरित्या प्रकाशित झाली.")
            print(f"🔗 Preview URL: {data.get('link')}")
        else:
            print(f"❌ त्रुटी: {response.status_code} | {response.text}")

    def _get_or_create_terms(self, names, taxonomy="tags"):
        ids = []
        for name in names:
            search_url = f"{self.site_url}/wp-json/wp/v2/{taxonomy}?search={name}"
            res = requests.get(search_url, auth=self.auth)
            data = res.json()

            if isinstance(data, list) and len(data) > 0:
                ids.append(data[0]["id"])
            else:
                create_url = f"{self.site_url}/wp-json/wp/v2/{taxonomy}"
                res = requests.post(create_url, auth=self.auth, json={"name": name})
                if res.status_code in [200, 201]:
                    ids.append(res.json()["id"])
        return ids
