import os
from agents.web_ai_agent import WebAIAgent
from agents.seo_agent import SEOAgent
from agents.wordpress_rest_agent import WordPressRestAgent
from agents.auto_update_agent import AutoUpdateAgent
from agents.firebase_connector import FirebaseConnector
from agents.bank_rate_ai_agent import BankRateAIAgent
from agents.site_builder_ai_agent import SiteBuilderAIAgent

# 🧠 Agent Initialization
web_ai = WebAIAgent()
seo = SEOAgent()
wp = WordPressRestAgent()
auto_update = AutoUpdateAgent()
firebase = FirebaseConnector()
bank_ai = BankRateAIAgent()
site_builder = SiteBuilderAIAgent()

# ✅ Step 1: HTML फाईल्स तयार करा
web_ai.generate_loan_rates()
web_ai.generate_lead_form()

# ✅ Step 2: SEO Metadata तयार करा
meta = seo.generate_meta("गृहकर्ज सल्ला 2025")

# ✅ Step 3: WordPress वर loan_rates पोस्ट करा
wp.publish_post_from_file(
    file_path="output/loan_rates.html",
    title="📊 लोन दर माहिती",
    meta=meta
)

# ✅ Step 4: WordPress वर lead_form पोस्ट करा
wp.publish_post_from_file(
    file_path="output/lead_form.html",
    title="💼 लोन लीड फॉर्म",
    meta=meta
)

# ✅ Step 5: CSV वरून बँक दर HTML तयार करा (जर CSV फाईल अस्तित्वात असेल)
csv_path = "data/loan_rates_data.csv"
if os.path.exists(csv_path):
    bank_ai.generate_html_from_csv(csv_path)
else:
    print(f"⚠️ CSV फाईल सापडली नाही: {csv_path}")

# ✅ Step 6: Auto Site Structure तयार करा
site_builder.generate_home_page()

# Optional: Auto Site Tree बनवायचं असल्यास uncomment करा
# site_builder.auto_generate_site_structure()

print("🎯 LoanBot Agent सर्व कार्य पूर्ण ✅")
