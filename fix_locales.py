import json
import os

new_invite = "https://discord.gg/Zsrp2J3Jv"

print("Fixing locales and JSON files...")

# 1. JSON files ko directly update karo
for root, dirs, files in os.walk("locales"):
  for file in files:
    if file.endswith(".json"):
      path = os.path.join(root, file)
      with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)


      # Recursive function to find and replace any discord links inside json
      def update_dict(d):
        for k, v in d.items():
          if isinstance(v, dict):
            update_dict(v)
          elif isinstance(v, str) and (
              "discord.gg" in v or "discord.com" in v or "zeryn" in v
          ):
            d[k] = new_invite


      update_dict(data)

      with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
      print(f"Updated JSON locale: {path}")

# 2. Cogs and other py files mein bhi koi purana invite ho toh fix karo
for root, dirs, files in os.walk("bot/cogs"):
  for file in files:
    if file.endswith(".py"):
      path = os.path.join(root, file)
      with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

      import re

      new_content = re.sub(
          r"https?://discord\.(gg|com/invite)/\w+", new_invite, content
      )
      if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
          f.write(new_content)
        print(f"Updated python cog link: {path}")

print("Locales and links successfully patched!")
