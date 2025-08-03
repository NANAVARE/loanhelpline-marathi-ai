import re
from deep_translator import GoogleTranslator

def translate_to_marathi(text, direction="mr"):
    """
    Google Translator वापरून भाषांतर करते.
    direction="mr" म्हणजे इंग्रजी → मराठी, "en" म्हणजे मराठी → इंग्रजी
    """
    if not text:
        return ""

    source_lang = "en" if direction == "mr" else "mr"
    target_lang = "mr" if direction == "mr" else "en"
    
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated
    except Exception as e:
        print(f"⚠️ भाषांतर त्रुटी: {e}")
        return text  # fallback: original text

def slugify_text(text):
    """
    दिलेल्या टेक्स्टचा स्लग बनवतो (URL साठी वापरतो)
    उदा: "गृहकर्ज मार्गदर्शन" → "gruhkarj-margdarshan"
    """
    text_en = translate_to_marathi(text, direction="en")  # URL साठी इंग्रजी slug
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', text_en.lower())
    return slug.strip('-')

def sanitize_text(text):
    """
    HTML पोस्ट साठी सुरक्षित मजकूर तयार करतो.
    """
    if not text:
        return ""
    return text.replace("<", "&lt;").replace(">", "&gt;")

def extract_tags_from_csv_row(row):
    """
    CSV मधील बँकेच्या नावावरून Tag/Category तयार करतो.
    उदा: row["बँक"] = "SBI" → ["SBI", "गृहकर्ज"]
    """
    bank = row.get("बँक", "")
    tag1 = bank.strip()
    tag2 = "गृहकर्ज"
    return [tag1, tag2]
