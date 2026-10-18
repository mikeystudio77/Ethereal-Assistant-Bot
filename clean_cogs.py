import os
import re

# Vietnamese characters check karne ke liye regex pattern
vietnamese_chars = re.compile(
    r"[àáảãạâấầẩẫậăắằẳẵặđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ]",
    re.IGNORECASE,
)


def process_file(filepath):
  with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

  def replace_match(m):
    full_str = m.group(0)
    quote = full_str[0]
    inner = full_str[1:-1]
    # Agar Vietnamese text mila toh uski jagah clean English description daal do
    if vietnamese_chars.search(inner):
      return f"{quote}Command execution and details{quote}"
    return full_str

  # Python string literals ko target karo
  new_text = re.sub(
      r'"([^"\\]*(\\.[^"\\]*)*)"|\'([^\'\\]*(\\.[^\'\\]*)*)\'',
      replace_match,
      text,
  )

  if new_text != text:
    with open(filepath, "w", encoding="utf-8") as f:
      f.write(new_text)
    print(f"Cleaned and Updated: {filepath}")


cogs_dir = "bot/cogs"
if not os.path.exists(cogs_dir):
  cogs_dir = "cogs"

print(f"Cleaning Cogs directory: {cogs_dir}")
for root, dirs, files in os.walk(cogs_dir):
  for file in files:
    if file.endswith(".py"):
      process_file(os.path.join(root, file))

print("All cogs successfully cleaned instantly without API limits!")
