import csv
import os
from utils.helpers import sanitize_text, extract_tags_from_csv_row

class BankRateAIAgent:
    def generate_html_from_csv(self, csv_path):
        if not os.path.exists(csv_path):
            print(f"❌ CSV फाईल सापडली नाही: {csv_path}")
            return
        
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        html = "<h2>🏦 आजचे गृहकर्ज व्याजदर</h2><table border='1'><tr><th>बँक</th><th>व्याजदर</th><th>तारीख</th></tr>"
        for row in rows:
            bank = sanitize_text(row.get("बँक", ""))
            rate = sanitize_text(row.get("व्याजदर", ""))
            date = sanitize_text(row.get("तारीख", ""))
            html += f"<tr><td>{bank}</td><td>{rate}</td><td>{date}</td></tr>"
        html += "</table>"

        os.makedirs("output", exist_ok=True)
        output_file = "output/generated_loan_rates.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html)
        
        print(f"✅ HTML तयार झाला: {output_file}")
