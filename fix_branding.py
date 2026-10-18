import os

# Kya-kya replace karna hai
name_replacements = [
    ("Ethereal Assistant", "Ethereal Assistant"),
    ("Ethereal Assistant", "Ethereal Assistant"),
    ("ethereal-assistant", "ethereal-assistant"),
]

# Naya Discord invite link
new_invite = "https://discord.gg/Zsrp2J3Jv"

print("Updating bot branding and invite links across project...")

count = 0
for root, dirs, files in os.walk("."):
  for file in files:
    # Sabhi code aur config files check karo
    if file.endswith((".py", ".json", ".md", ".txt", ".env")):
      path = os.path.join(root, file)
      try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
          content = f.read()

        updated = False

        # Name replace karo
        for old_name, new_name in name_replacements:
          if old_name in content:
            content = content.replace(old_name, new_name)
            updated = True

        # Purane Discord invites ya placeholders ko naye invite se replace karo
        # (discord.gg/ ya discord.com/invite/ wale links ko target karega)
        import re

        invite_pattern = re.compile(r"https?://discord\.(gg|com/invite)/\w+")
        if invite_pattern.search(content):
          content = invite_pattern.sub(new_invite, content)
          updated = True

        if updated:
          with open(path, "w", encoding="utf-8") as f:
            f.write(content)
          print(f"Branding updated in: {path}")
          count += 1
      except Exception as e:
        pass

print(
    f"Successfully finished! Total files updated with Ethereal branding &"
    f" invite: {count}"
)
