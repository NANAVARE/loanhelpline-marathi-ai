import os
from datetime import datetime
from agents.content_ai_agent import ContentAIAgent
from agents.seo_agent import SEOAgent
from agents.wordpress_rest_agent import WordPressRestAgent

class AutoUpdateAgent:
    def __init__(self):
        self.content_agent = ContentAIAgent()
        self.seo_agent = SEOAgent()
        self.wp_agent = WordPressRestAgent()

    def run(self, topic="गृहकर्ज सल्ला 2025"):
        print(f"🕒 AutoUpdateAgent सुरू होत आहे – विषय: {topic}")

        # Step 1: लेख तयार करा
        title, html_content = self.content_agent.generate_article(topic)

        # Step 2: SEO meta तयार करा
        seo_data = self.seo_agent.generate_meta(title)

        # Step 3: फाईल सेव्ह करा
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = f"output/auto_article_{timestamp}.html"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Step 4: WordPress वर पोस्ट करा
        self.wp_agent.publish_html(file_path, title, seo_data=seo_data)

        print("✅ AutoUpdateAgent काम पूर्ण झाले.")
