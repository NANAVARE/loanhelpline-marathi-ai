import os
import csv

class CSVLoanRateAgent:
    def __init__(self):
        self.input_file = "data/loan_rates.csv"
        self.output_file = "output/loan_rates.html"

    def generate_html_from_csv(self):
        if not os.path.exists(self.input_file):
            print(f"❌ CSV फाईल सापडली नाही: {self.input_file}")
            return

        with open(self.input_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        html = "<h2>🏦 बँकनिहाय गृहकर्ज दरांची यादी</h2><table border='1' cellspacing='0' cellpadding='8'>"
        html += "<tr><th>🏦 बँक</th><th>🔢 व्याजदर</th><th>📅 अद्ययावत तारीख</th></tr>"

        for row in rows:
            html += f"<tr><td>{row['बँक']}</td><td>{row['व्याजदर']}</td><td>{row['तारीख']}</td></tr>"

        html += "</table>"

        os.makedirs("output", exist_ok=True)
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write(html)

        print("✅ HTML टेबल तयार झाला: output/loan_rates.html")
