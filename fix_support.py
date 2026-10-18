import os

# Naya Discord invite link jo tujhe lagana hai
new_invite = "https://discord.gg/Zsrp2J3Jv"

print("Searching and replacing support server links...")

count = 0
for root, dirs, files in os.walk("."):
  for file in files:
    if file.endswith(".py"):
      path = os.path.join(root, file)
      try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
          content = f.read()

        updated = False

        # Agar file ke andar support server ya discord invite ka koi bhi link hai
        if "discord.gg/" in content or "discord.com/invite/" in content:
          import re

          # Sabhi discord links ko naye link se replace kar do
          new_content = re.sub(
              r"https?://discord\.(gg|com/invite)/\w+", new_invite, content
          )
          if new_content != content:
            content = new_content
            updated = True

        if updated:
          with open(path, "w", encoding="utf-8") as f:
            f.write(content)
          print(f"Fixed button link in: {path}")
          count += 1
      except Exception as e:
        pass

print(f"Done! Total files fixed: {count}")
