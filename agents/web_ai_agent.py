import os

class WebAIAgent:
    def generate_loan_rates(self):
        content = "<h2>सर्व बँकांचे नवीनतम गृहकर्ज दर</h2><ul><li>HDFC: 8.25%</li><li>SBI: 8.15%</li></ul>"
        os.makedirs("output", exist_ok=True)
        with open("output/loan_rates.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("📄 loan_rates.html तयार झाला.")

    def generate_lead_form(self):
        with open("templates/lead_form_template.html", "r", encoding="utf-8") as f:
            content = f.read()
        os.makedirs("output", exist_ok=True)
        with open("output/lead_form.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("📄 lead_form.html तयार झाला.")

    def generate_loan_pages(self):
        # ✅ एकाच कॉल मध्ये दोन्ही तयार करा
        self.generate_loan_rates()
        self.generate_lead_form()
