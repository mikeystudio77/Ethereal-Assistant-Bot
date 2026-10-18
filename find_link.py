import os

target = "https://etherealbotpanel.vercel.app/"
print(f"Searching for '{target}' in all project files...")

for root, dirs, files in os.walk("."):
  for file in files:
    if file.endswith((".py", ".json", ".env", ".md", ".txt")):
      path = os.path.join(root, file)
      try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
          content = f.read()
          if target in content:
            print(f"-> Found inside: {path}")
      except Exception as e:
        pass

print("Search completed!")
