# agents/seo_agent.py

class SEOAgent:
    def generate_meta(self, title):
        """
        दिलेल्या शीर्षकावरून meta-title आणि description तयार करतो
        """
        meta_title = f"{title} - LoanHelpline.co"
        meta_description = f"{title} बद्दल मार्गदर्शन, दर, आणि अर्ज प्रक्रिया. सर्व माहिती मराठीत."
        return {
            "meta_title": meta_title,
            "meta_description": meta_description
        }
