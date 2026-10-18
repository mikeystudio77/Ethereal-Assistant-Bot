import os

# Purana link ya server keyword jise hatana hai
old_keyword = "zerynbot"  # ya agar koi aur purana link ho
new_invite = "https://discord.gg/Zsrp2J3Jv"

print("Searching and replacing across ALL files (.py, .json, .env, .txt)...")

count = 0
for root, dirs, files in os.walk("."):
  for file in files:
    if file.endswith((".py", ".json", ".env", ".txt", ".md", ".yml", ".yaml")):
      path = os.path.join(root, file)
      try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
          content = f.read()

        updated = False

        # Agar kisi bhi file mein discord invite link ya purana keyword mila
        if "discord.gg/" in content or "discord.com/invite/" in content:
          import re

          content = re.sub(
              r"https?://discord\.(gg|com/invite)/\w+", new_invite, content
          )
          updated = True

        # Agar config ya json mein support URL hai
        if "support" in content.lower() and "http" in content:
          # Isko bhi target kar sakte hain agar zaroorat ho
          pass

        if updated:
          with open(path, "w", encoding="utf-8") as f:
            f.write(content)
          print(f"Updated links in: {path}")
          count += 1
      except Exception as e:
        pass

print(f"Done! Total files updated: {count}")
