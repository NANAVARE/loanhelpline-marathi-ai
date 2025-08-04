import csv
import os
from datetime import date

class BankDataAgent:
    def __init__(self):
        self.output_path = "data/loan_rates.csv"
        os.makedirs("data", exist_ok=True)

    def fetch_sbi_rates(self):
        return {
            "बँक": "SBI",
            "कर्ज प्रकार": "गृहकर्ज",
            "व्याजदर": "8.50%",  # ✅ Static manual value
            "तारीख": str(date.today())
        }

    def fetch_hdfc_rates(self):
        return {
            "बँक": "HDFC",
            "कर्ज प्रकार": "गृहकर्ज",
            "व्याजदर": "8.75%",  # ✅ Static manual value
            "तारीख": str(date.today())
        }

    def fetch_icici_rates(self):
        return {
            "बँक": "ICICI",
            "कर्ज प्रकार": "गृहकर्ज",
            "व्याजदर": "8.60%",  # ✅ Static manual value
            "तारीख": str(date.today())
        }

    def fetch_axis_rates(self):
        return {
            "बँक": "Axis Bank",
            "कर्ज प्रकार": "गृहकर्ज",
            "व्याजदर": "8.65%",  # ✅ Static manual value
            "तारीख": str(date.today())
        }

    def update_csv(self, data_list):
        with open(self.output_path, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["बँक", "कर्ज प्रकार", "व्याजदर", "तारीख"])
            writer.writeheader()
            writer.writerows(data_list)
        print(f"✅ CSV अपडेट झाला: {self.output_path}")

    def run(self):
        print("🚀 Bank Loan Rate Agent सुरू झाला...")

        all_data = [
            self.fetch_sbi_rates(),
            self.fetch_hdfc_rates(),
            self.fetch_icici_rates(),
            self.fetch_axis_rates()
        ]

        self.update_csv(all_data)

        print("🏁 Agent पूर्ण झाला ✅")
