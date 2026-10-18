import os

target = "Ổ Cú"  # Ya us server ka unique naam/keyword
print(f"Hunting down the owl server '{target}' in all files...")

for root, dirs, files in os.walk("."):
  for file in files:
    if file.endswith((".py", ".json", ".env", ".txt", ".md")):
      path = os.path.join(root, file)
      try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
          content = f.read()
          if target in content or "Zsrp" not in content:  # check kar rahe hain
            if target in content:
              print(f"-> Found owl server inside: {path}")
      except Exception as e:
        pass

print("Hunt completed!")
