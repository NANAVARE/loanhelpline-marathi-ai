# agents/site_builder_ai_agent.py

import os
from datetime import datetime
from utils.helpers import translate_to_marathi, slugify_text

class SiteBuilderAIAgent:
    def __init__(self):
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_home_page(self):
        content = """
        <h1>LoanHelpline.co वर स्वागत आहे</h1>
        <p>ही वेबसाईट आपल्याला गृहकर्ज, वैयक्तिक कर्ज, क्रेडिट कार्ड्स, विमा यासारख्या आर्थिक सेवा मराठीत समजावून सांगते.</p>
        <ul>
            <li><a href='/loans'>🏠 कर्जे</a></li>
            <li><a href='/credit-cards'>💳 क्रेडिट कार्ड्स</a></li>
            <li><a href='/insurance'>🛡️ विमा</a></li>
            <li><a href='/tools'>🧮 तुलना साधने</a></li>
            <li><a href='/guides'>📘 आर्थिक मार्गदर्शक</a></li>
        </ul>
        """
        with open(os.path.join(self.output_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(content)
        print("🏠 मुख्यपृष्ठ तयार झाले")

    def auto_generate_site_structure(self):
        pages = [
            ("loans.html", "🏠 कर्जे", ["गृहकर्ज", "वैयक्तिक कर्ज", "वाहन कर्ज", "शिक्षण कर्ज"]),
            ("credit_cards.html", "💳 क्रेडिट कार्ड्स", ["वेतनदार", "स्वयंरोजगार", "रिवॉर्ड कार्ड्स"]),
            ("insurance.html", "🛡️ विमा", ["जीवन विमा", "आरोग्य विमा", "वाहन विमा"]),
            ("guides.html", "📘 मार्गदर्शक", ["EMI गणना", "क्रेडिट स्कोअर टिप्स", "गुंतवणूक शिका"]),
            ("tools.html", "🧮 साधने", ["EMI कॅल्क्युलेटर", "दर तुलना", "स्कोअर तपासणी"])
        ]

        for file_name, heading, topics in pages:
            html = f"<h2>{heading}</h2><ul>"
            for topic in topics:
                slug = slugify_text(topic)
                html += f"<li><a href='/{slug}'>{topic}</a></li>"
            html += "</ul>"

            with open(os.path.join(self.output_dir, file_name), "w", encoding="utf-8") as f:
                f.write(html)
            print(f"📄 {file_name} तयार झाला")
