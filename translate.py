import json
from deep_translator import GoogleTranslator

# en.json file load karo
with open("locales/en.json", "r", encoding="utf-8") as f:
    data = json.load(f)

translator = GoogleTranslator(source='vi', target='en')

new_data = {}
print("Translating json keys from Vietnamese to English...")
for k, v in data.items():
    if isinstance(v, str):
        try:
            # Agar text mein format variables hain toh dhyan rakhega, baaki translate karega
            translated = translator.translate(v)
            new_data[k] = translated if translated else v
        except Exception as e:
            new_data[k] = v
    else:
        new_data[k] = v

# Wapas en.json mein save kar do
with open("locales/en.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)

print("Translation Completed Successfully!")

