import os

print("Hunting down Vietnamese text...")

for root, dirs, files in os.walk("bot/cogs"):
  for file in files:
    if file.endswith(".py"):
      path = os.path.join(root, file)
      with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

      if "Chúc mừng" in content:
        content = content.replace("Chúc mừng", "Congratulations")
        with open(path, "w", encoding="utf-8") as f:
          f.write(content)
        print(f"Cleaned leveling/cog: {path}")

print("Done! Vietnam references eliminated.")
