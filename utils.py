import json
from config import DEFAULT_LANGUAGE

def load_locale(lang=DEFAULT_LANGUAGE):
    path = f"locales/{lang}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
