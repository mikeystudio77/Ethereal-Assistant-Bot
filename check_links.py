import os
import re

print("Scanning all files for any discord links...")

for root, dirs, files in os.walk("."):
  for file in files:
    if file.endswith((".py", ".json", ".env", ".txt", ".md", ".yml")):
      path = os.path.join(root, file)
      try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
          content = f.read()
          # Agar file mein discord link ya invite hai
          links = re.findall(r"https?://[^\s]+", content)
          for link in links:
            if "discord" in link or "zeryn" in link:
              print(f"[{path}] -> {link}")
      except Exception as e:
        pass

print("Scan completed!")
