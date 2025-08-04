from agents.bank_data_agent import BankDataAgent
from agents.csv_loan_agent import CSVLoanRateAgent
from agents.bank_rate_ai_agent import BankRateAIAgent
from agents.wordpress_rest_agent import WordPressRestAgent
from agents.seo_agent import SEOAgent
from agents.firebase_connector import FirebaseConnector
from agents.web_ai_agent import WebAIAgent

def run_full_pipeline():
    print("🚀 LoanBot Pipeline सुरू झाला...")

    # STEP 1: बँक दर गोळा करा
    print("\n📊 [Step 1] बँक दर गोळा करत आहे...")
    bank_data_agent = BankDataAgent()
    bank_data_agent.run()

    # STEP 2: CSV → HTML टेबल
    print("\n📝 [Step 2] HTML टेबल तयार करत आहे...")
    csv_agent = CSVLoanRateAgent()
    csv_agent.generate_html_from_csv()

    # STEP 3: AI आधारित पोस्ट तयार करा
    print("\n✍️ [Step 3] AI HTML पोस्ट तयार करत आहे...")
    ai_agent = BankRateAIAgent()
    ai_agent.generate_html_from_csv("data/loan_rates.csv")

    # STEP 4: SEO meta tags जोडा
    print("\n🔍 [Step 4] SEO meta data जोडत आहे...")
    seo_agent = SEOAgent()
    seo_agent.add_meta_tags("output/generated_loan_rates.html")

    # STEP 5: WordPress वर पोस्ट करा
    print("\n🌐 [Step 5] WordPress वर पोस्ट करत आहे...")
    wp_agent = WordPressRestAgent()
    wp_agent.publish_post_from_file(
        file_path="output/generated_loan_rates.html",
        title="आजचे गृहकर्ज व्याजदर - मराठीत",
        meta=None,
        tags=["गृहकर्ज", "Home Loan", "Loan Rates", "मराठी"],
        categories=["Loan Rates"]
    )

    # STEP 6: Firebase ला Lead Form टाका
    print("\n🔥 [Step 6] Firebase ला Lead Form टाकत आहे...")
    firebase = FirebaseConnector()
    firebase.push_lead_form("output/lead_form.html")

    # STEP 7: मुख्यपृष्ठ तयार करा
    print("\n🏠 [Step 7] मुख्यपृष्ठ तयार करत आहे...")
    web_builder = WebAIAgent()
    web_builder.generate_homepage()

    print("\n🎯 LoanBot Agent सर्व कार्य पूर्ण ✅")

if __name__ == "__main__":
    run_full_pipeline()
